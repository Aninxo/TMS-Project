from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, current_app, send_from_directory, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Document
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = 'uploads'  # Create this folder in your project directory
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx'}  # Allowed file extensions

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def home():
    return render_template('home.html', first_name=current_user.first_name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        
        if password != repeat_password:
            flash('Passwords do not match')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return render_template('register.html')
        
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/tax_calculator', methods=['GET', 'POST'])
@login_required
def tax_calculator():
    if request.method == 'POST':
        # Get input from the form
        income = float(request.form['income'])
        # Perform tax calculation
        tax = calculate_tax(income)
        return render_template('tax_result.html', tax=tax)
    return render_template('tax_calculator.html')

def calculate_tax(income):
    # Implement your tax calculation logic here
    # This is a simplified example
    if income <= 50000:
        return income * 0.1
    else:
        return 5000 + (income - 50000) * 0.2

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf', 'doc', 'docx'}

@app.route('/upload_document', methods=['POST'])
@login_required
def upload_document():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('home'))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('home'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = os.path.join(current_app.root_path, 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        
        # Create a new Document record in the database
        new_document = Document(filename=filename, user_id=current_user.id)
        db.session.add(new_document)
        db.session.commit()
        
        flash('File successfully uploaded')
        return redirect(url_for('home'))
    else:
        flash('Allowed file types are pdf, doc, docx')
        return redirect(url_for('home'))

@app.route('/get_documents')
@login_required
def get_documents():
    documents = Document.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': doc.id, 'filename': doc.filename} for doc in documents])

@app.route('/download_document/<int:doc_id>')
@login_required
def download_document(doc_id):
    document = Document.query.get_or_404(doc_id)
    if document.user_id != current_user.id:
        abort(403)  # Forbidden
    upload_folder = os.path.join(current_app.root_path, 'uploads')
    return send_from_directory(upload_folder, document.filename, as_attachment=True)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/remove_document/<int:doc_id>', methods=['POST'])
@login_required
def remove_document(doc_id):
    document = Document.query.get_or_404(doc_id)
    if document.user_id != current_user.id:
        abort(403)  # Forbidden
    db.session.delete(document)
    db.session.commit()
    flash('Document removed successfully')
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)