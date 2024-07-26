import validators

email = input("What's your email address? ")

def validate(email):
    return "Valid" if validators.email(email) else "Invalid"

print(validate(email))
