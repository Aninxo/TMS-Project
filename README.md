# TMS-Project

## Description
Project Overview: I am working on a project to create an app that assists in managing taxes for clients. The app should make it easier for my uncle, who currently manages taxes on paper, and allow clients to calculate their taxes and store tax documents securely. I need detailed, step-by-step guidance to build this app from scratch using Visual Studio Code and Flask for the UI, along with a secure database for storing client information. The app should also integrate GitHub for version control and Git Bash for pushing code.

Key Features: Login Page:

Requirements: Input fields for email and password. Option to register an account with inputs for First name, Last name, Email, Password, and Repeat password. Passwords must include special characters for stronger security. Forgot password feature: Send a code to the client's email, allow input to verify and reset the password within the app. Ensure users cannot access the website (e.g., tax calculator) without logging in first. Design: Background color: White. Text input boxes: Long rectangles with curved sides on the left and right. Include a three-lined tab at the top left for users to add document files. Add a loading animation with three jumping dots when users log in (duration: 3 seconds). Tax Calculation Function:

Requirements: Allow clients and my uncle to calculate taxes based on expenses, income, and other relevant data. Provide a detailed step-by-step guide on how to implement this, including all necessary code. Database:

Requirements: Secure database for storing client information (e.g., tax documents, full name, email). Clients should be able to create new documents and choose to encrypt them with a password. My uncle should only have access to tax documents, full name, and email. Process Requirements: Begin from Scratch:

Guide me through the entire process, starting from creating the project in Visual Studio Code. Provide detailed explanations for every step, as I am a beginner and need clarity to avoid confusion. Step-by-Step Structure:

Creating the Tax Calculator: Explain how to set up the project in Visual Studio Code. Provide the exact code I need, and specify where to place it in the project. Creating the Login Page: Ask for my input on design choices (e.g., colors, layout) and update the code based on my responses. Explain where to place the code and how to connect the login page to other features. Creating the Secure Database: Guide me through setting up a secure database for client information. Provide detailed instructions and code, specifying where to place the code in the project. Explain how to connect the database to the app’s other features (e.g., login system, tax calculator). Visual Appeal:

Make the app visually appealing and guide me through any design adjustments. Request my input on visuals where necessary (e.g., background color, layout) and update the code accordingly. Combining Everything into a Fully Functioning App:

Explain how to combine all parts of the project into one functioning app. Provide guidance on pushing the code to GitHub and ensuring it can be accessed via a link by my uncle. Additional Clarifications: Ensure that the login page and secure database are properly linked to the tax calculation function. Ask for my input during key stages, especially when it comes to design decisions. Provide code for every feature and explain where it should be placed within the project. Assume that I have no prior experience with coding, so every explanation should be beginner-friendly. Key Features
Login Page:

Input fields for email and password.
Registration form with inputs for First name, Last name, Email, Password, and Repeat password.
Passwords must include special characters for added security.
Forgot password functionality: A code is sent to the client's email to verify and reset the password within the app.
Users must have an account to access the website (e.g., tax calculator).
Design: White background, text input boxes with curved sides, a three-lined tab at the top left to add document files, and a loading animation (three jumping dots) when logging in (duration: 3 seconds).
Tax Calculation Function:

Calculate taxes based on expenses, income, and other relevant data for both clients and my uncle.
Database:

Secure database for storing client information (e.g., tax documents, full name, email).
Clients can create new documents and choose to encrypt them with a password.
My uncle will have access to tax documents, full name, and email.
Process Requirements
The app is built from scratch, with step-by-step guidance provided for setup, coding, and deployment.
Step-by-Step Structure:
Creating the Tax Calculator: Detailed explanation on setting up the project and code placement.
Creating the Login Page: Design choices and code placement explained.
Creating the Secure Database: Detailed instructions for setting up the database and linking it to other features.
Visual Appeal: Guidance on design adjustments based on input.
Combining Everything into a Fully Functioning App: Instructions on integrating all parts and pushing the code to GitHub for access.

## Project Structure
TMS-Project/
│
├── __pycache__/                 # Compiled Python files
│   ├── app.cpython-312.pyc      # Compiled app.py file
│   └── model.cpython-312.pyc    # Compiled models.py file
│
├── instance/                    # Instance folder (contains the database)
│   └── site.db                  # SQLite database file
│
├── templates/                   # Directory containing HTML templates
│   ├── home.html                # Homepage template
│   ├── login.html               # Login page template
│   └── register.html            # Registration page template
│
├── venv/                        # Virtual environment directory
│
├── app.py                       # Main Flask application file
└── models.py                    # Database models file


## Setup and Installation
Instructions on how to set up and run the project.

## Usage
Register, Login, Use Tax Calculator, Add Tax Documents to folders

## Contributors
Aninxo

## License
Information about the project's license.
