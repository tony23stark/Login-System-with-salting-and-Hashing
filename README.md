# Login-System-with-salting-and-Hashing
# Secure Login System with Password Salting and Hashing

This project implements a secure login system using password salting and hashing techniques to protect user credentials.

## Security Features
- Password salting using bcrypt
- Secure password hashing
- SQLite database for user storage
- Environment variable configuration
- Session management

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

## Usage
- Register a new account at `/register`
- Login at `/login`
- View your profile at `/profile` (requires authentication) 