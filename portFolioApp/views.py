from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from email_utils.email_lib import send_confirmation_email
from .forms import PortfolioRegistrationForm, PortfolioImageFormSet, SignupForm
from .models import PortfolioImage, PortfolioRegistration



def signupview(request):
    """
    Function to render the signup page of the application
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"You are successfully logged in as {username}!")
            return redirect('signin')
    elif request.method == "GET":
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
def index_view(request):
    """
    Function to render the index view page of the application
    """
    images = PortfolioImage.objects.all()
    return render(request, 'index.html', {'images': images, 'media_url':settings.MEDIA_URL})
def portfolio_registration_view(request):
    """
    Function to render the registration page of the application
    """
    if request.method == 'POST':
        form = PortfolioRegistrationForm(request.POST, request.FILES)
        formset = PortfolioImageFormSet(request.POST, request.FILES, instance=PortfolioRegistration())
        if form.is_valid() and formset.is_valid():
            registration = form.save()
            formset.instance = registration
            formset.save()
            send_confirmation_email(form.cleaned_data['email'])
            return render(request, 'registration_success.html')
    else:
        form = PortfolioRegistrationForm()
        formset = PortfolioImageFormSet(instance=PortfolioRegistration())
    return render(request, 'portfolio_registration.html', {'form': form, 'formset': formset})
def view_portfolio(request):
    """
    Function to render the view page of the application
    """
    images = PortfolioImage.objects.all()
    return render(request, 'portfolio_detail.html', {'images': images, 'media_url':settings.MEDIA_URL})
def portfolio_detail(request, portfolio_id):
    """
    Function to render the detail page of the application
    """
    portfolio = get_object_or_404(PortfolioRegistration, id=portfolio_id)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})
def portfolio_list_working(request):
    """
    Function to render the portfolio list page of the application
    """
    registrations = PortfolioRegistration.objects.all()
    
    return render(request, 'portfolio_list.html', {'registrations': registrations })
def portfolio_list(request):
    """
    Function to render the portfolio list page of the application
    """
    images = PortfolioImage.objects.select_related('registration')
    return render(request, 'image_list.html', {'images': images})
    
def registration_details(request, registration_id):
    """
    Function to render the portfolio list deatils on id click page of the application
    """
    registration = get_object_or_404(PortfolioRegistration, pk=registration_id)
    images = registration.portfolioimage_set.all()
    return render(request, 'registration_details-Merge.html', {'registration': registration,'images':images})
def about(request):
    """
    Function to render the about page of the application
    """
    return render(request, 'about.html')