import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

# Configure and connect to Firebase
cred = firebase_admin.credentials.Certificate('testt-89c6c-firebase-adminsdk-x56rs-66e45a2131.json')
firebase_admin.initialize_app(cred)

# Login function
def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.get_user_by_email(email)
        if not user.email_verified:
            print('Email not verified')
            return
        user = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # Do something with the logged in user
    except auth.AuthError as e:
        print("Error logging in:", e)

# Signup Function with email verification
def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")

    user = auth.create_user(email=email, password=password)
    auth.send_email_verification(user.uid)
    print("Verification email sent to", email)
    ask=input("Do you want to login?[y/n]")
    if ask=='y':
        login()
# Main
ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()