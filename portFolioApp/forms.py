from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PortfolioRegistration, PortfolioImage

class PortfolioRegistrationForm(forms.ModelForm):
    class Meta:
        model = PortfolioRegistration
        fields = ['name', 'email', 'phone_number', 'portfolio_url']

class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['image']
        labels = {'image': 'Upload your image'}

PortfolioImageFormSet = forms.inlineformset_factory(PortfolioRegistration, PortfolioImage, form=PortfolioImageForm, extra=1, can_delete=False)

class SignupForm(UserCreationForm):
    """
    A form that inherits from UserCreationForm to add additional fields for sign up.

    Attributes:
    -----------
    email : forms.EmailField
        Email field for the user's email address.
    first_name : forms.CharField
        Char field for the user's first name.
    last_name : forms.CharField
        Char field for the user's last name.
    
    Methods:
    --------
    Meta:
        Meta class to specify the model and fields for the form.
    """

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        """
        Meta class to specify the model and fields for the SignupForm.

        Attributes:
        -----------
        model : django.contrib.auth.models.User
            User model for the form.
        fields : list
            List of fields to include in the form.
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
