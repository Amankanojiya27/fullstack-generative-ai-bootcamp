# Hiding Implementation Details

def get_input():
    print("getting User input...")
    
def validate_input():
    print("Validating the user info..")

def save_to_db():
    print("Saving in database...")
    print("Saved ✅")
    

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User is successfully registered")
    

register_user()