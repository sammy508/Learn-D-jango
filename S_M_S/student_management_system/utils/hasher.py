

from django.contrib.auth.hashers import make_password, check_password

def hash_password(raw_password):
    """
    Hash a plain text password using Django's default algorithm.
    """
    return make_password(raw_password)

def verify_password(raw_password, hashed_password):
    """
    Verify a raw password against the hashed password.
    """
    return check_password(raw_password, hashed_password)


'''   'Note'
These two functions fully cover creation and verification of passwords.

Model save() calls hash_password when creating/updating a password.

For login, just call verify_password (or your model’s check_password)—no extra steps.
'''