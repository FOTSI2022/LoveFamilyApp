from django import forms
from .models import *

"""
#Create the form to add a theme
class AddThemeForm(forms.ModelForm):
      class Meta:      
            model = discussionTheme
            fields = '__all__'

"""

class CommentsForm(forms.ModelForm):
      class Meta:      
            model = Messages
            fields = '__all__'