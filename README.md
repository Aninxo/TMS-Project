

## Description
TMS-Project is an app designed to assist in managing taxes for clients. It aims to simplify tax management for the owner's uncle, who currently manages taxes on paper, and allows clients to calculate their taxes and store tax documents securely.

## Key Features
### Login Page:
- Input fields for email and password
- Registration form with inputs for First name, Last name, Email, Password, and Repeat password
- Password security: Must include special characters
- Forgot password functionality with email verification
- Access restriction: Users must log in to access the website

### Design:
- White background
- Text input boxes with curved sides
- Three-lined tab at the top left for document file addition
- Loading animation with three jumping dots (3 seconds duration) on login

### Tax Calculation Function:
- Calculates taxes based on expenses, income, and other relevant data
- Accessible to both clients and the administrator

### Database:
- Secure storage for client information (tax documents, full name, email)
- Document creation and optional password encryption for clients
- Limited access for the administrator (tax documents, full name, email only)

## Project Structure
TMS-Project/ │ ├── pycache/ │ ├── app.cpython-312.pyc │ └── model.cpython-312.pyc │ ├── instance/ │ └── site.db │ ├── templates/ │ ├── home.html │ ├── login.html │ └── register.html │ ├── venv/ │ ├── app.py └── models.py


## Setup and Installation
[Instructions on how to set up and run the project will be added here]

## Usage
1. Register an account
2. Login to the system
3. Use the Tax Calculator
4. Add and manage Tax Documents in folders

## Contributors
- Aninxo

## License
[Information about the project's license will be added here]
