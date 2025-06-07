
# Secure Login System with Password Salting and Hashing

This project implements a secure login system using password salting and hashing techniques to protect user credentials. The system features a modern UI with responsive design and robust security measures.

## Security Features
- Password salting using bcrypt
- Secure password hashing
- SQLite database for user storage
- Environment variable configuration
- Session management
- CSRF protection
- Secure password requirements
- Flash messages for user feedback
- Responsive design for all devices

## Project Structure
```
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── static/            # Static files (CSS, images)
└── templates/         # HTML templates
    ├── base.html      # Base template with navigation
    ├── home.html      # Home page
    ├── login.html     # Login page
    ├── register.html  # Registration page
    └── profile.html   # User profile page
```

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```
SECRET_KEY=your-secret-key-here
```

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Features
- User registration with password validation
- Secure login system
- User profile management
- Responsive navigation bar
- Flash messages for user feedback
- Session-based authentication
- Password strength requirements
- Modern UI with Bootstrap 5
- Mobile-friendly design

## Usage
- Register a new account at `/register`
- Login at `/login`
<<<<<<< HEAD
- View your profile at `/profile` (requires authentication)
- Logout at `/logout`

## Security Best Practices
- Passwords are never stored in plain text
- Each password has a unique salt
- Session management with secure cookies
- CSRF protection on all forms
- Environment variables for sensitive data
- SQLite database with proper indexing
- Input validation and sanitization

## Dependencies
- Flask: Web framework
- Flask-SQLAlchemy: Database ORM
- bcrypt: Password hashing
- python-dotenv: Environment variable management
- Flask-Login: User session management 
=======
- View your profile at `/profile` (requires authentication) 
>>>>>>> f69bfaf105f3adb9726a48b3d11600f6984cbdc1
