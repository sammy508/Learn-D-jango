# utils/validations.py
from django.core.validators import RegexValidator

# Pre-created validator instances (serializable)
PASSWORD_VALIDATOR = RegexValidator(
    regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
    message="Password must be at least 8 characters, include uppercase, lowercase, number, and special character."
)

NAME_VALIDATOR = RegexValidator(
    regex=r'^[A-Za-z ]{2,50}$',
    message="Name must contain only letters and spaces, 2-50 characters."
)

PHONE_VALIDATOR = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number must be 10 digits."
)

EMAIL_VALIDATOR = RegexValidator(
    regex=r'^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$',
    message="Enter a valid email address."
)

USERNAME_VALIDATOR = RegexValidator(
    regex=r'^[a-zA-Z][a-zA-Z0-9._]{2,29}$',
    message='Username must start with a letter and contain only letters, numbers, dots, or underscores. Min 3 characters.'
)
