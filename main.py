
from phone_number_validator.validator import PhoneNumberValidator
import os

validator = PhoneNumberValidator(api_key= os.environ['API__KEY'])
is_valid1 = validator.validate("+15554234")
is_valid2 = validator.validate("+12069220880")
is_valid3 = validator.validate("+2069220880", country_code="US")

print(is_valid1)
print(is_valid2)
print(is_valid3)

