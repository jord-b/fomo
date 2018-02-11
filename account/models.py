from django.db import models
from django import forms
from cuser.models import AbstractCUser

class User(AbstractCUser):
    birthdate = models.DateField(blank=True, null=True)

class testForm(forms.Form):
    comment = forms.CharField(label="your comment")
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
