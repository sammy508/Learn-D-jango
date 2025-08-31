
from django.core.validators import RegexValidator


class  ValidateFields:
    @staticmethod
    def password_validator():
        password_validate = RegexValidator(
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        message="Password must be at least 8 characters, include uppercase, lowercase, number, and special character."
        )
        return password_validate
    

    @staticmethod
    def namefield_validator():
        name_validator = RegexValidator(
        regex=r'^[A-Za-z ]{2,50}$',
        message="Name must contain only letters and spaces, 2-50 characters."
            )
        return name_validator
    
    @staticmethod
    def phone_validator():
        phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits."
            )
        return phone_validator
    
    @staticmethod
    def Email_validator():
        email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$',
        message="Enter a valid email address."
         )
        
        return  email_validator
    
    @staticmethod
    def Username_validator():
       
        validators=    RegexValidator(
                regex=r'^[a-zA-Z][a-zA-Z0-9._]{2,29}$',
                message='Username must start with a letter and contain only letters, numbers, dots, or underscores. Min 3 characters.'
            )
        
        return validators