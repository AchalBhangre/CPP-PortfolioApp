from django import forms
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

