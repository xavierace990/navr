from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class FeedBack(models.Model):
    name=models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField(
    max_length=255,  # Maximum length of the email address (adjust as needed)
    unique=True,     # Ensure email addresses are unique in the database
    blank=False,     # Email is required (set to True if it's optional)
    null=False,      # Email is required (set to True if it can be null)
    help_text="Please enter a valid email address",  # Help text for the field
)
    feedback = models.TextField(null=True)

    
class Firsts(models.Model):
    namee=models.CharField(max_length=100)
    emaill = models.EmailField(
    max_length=255,  # Maximum length of the email address (adjust as needed)
    unique=True,     # Ensure email addresses are unique in the database
    blank=False,     # Email is required (set to True if it's optional)
    null=False,      # Email is required (set to True if it can be null)
    help_text="Please enter a valid email address",  # Help text for the field
)
    phonee = PhoneNumberField()
    visit_datee = models.DateField()  # Add the "date of visit" field
    how_heardd = models.CharField(max_length=100)  # Add the "how did you hear about us" field
    commentss=models.TextField()

    