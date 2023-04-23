from django.shortcuts import render,redirect
from .forms import PortfolioRegistrationForm,PortfolioImageFormSet
from .models import PortfolioImage,PortfolioRegistration
from django.shortcuts import render, get_object_or_404
from django.conf import settings

def portfolio_registration_view_old(request):
    if request.method == 'POST':
        form = PortfolioRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.save()
            for image in request.FILES.getlist('portfolio_images'):
                portfolio_image = PortfolioImage(image=image)
                portfolio_image.save()
                registration.portfolio_image.add(portfolio_image)
            registration.save()
            return render(request, 'registration_success.html')
    else:
        form = PortfolioRegistrationForm()
    return render(request, 'portfolio_registration.html', {'form': form})
    
def portfolio_registration_view(request):
    if request.method == 'POST':
        form = PortfolioRegistrationForm(request.POST, request.FILES)
        formset = PortfolioImageFormSet(request.POST, request.FILES, instance=PortfolioRegistration())
        if form.is_valid() and formset.is_valid():
            registration = form.save()
            formset.instance = registration
            formset.save()
            return render(request, 'registration_success.html')
    else:
        form = PortfolioRegistrationForm()
        formset = PortfolioImageFormSet(instance=PortfolioRegistration())
    return render(request, 'portfolio_registration.html', {'form': form, 'formset': formset})

    

   
# views.py

def view_portfolio(request):
   images = PortfolioImage.objects.all()
   return render(request, 'portfolio_detail.html',{'images': images,'media_url':settings.MEDIA_URL})
   
def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(PortfolioRegistration, id=portfolio_id)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})
    
def portfolio_list_working(request):
    registrations = PortfolioRegistration.objects.all()

    return render(request, 'portfolio_list.html', {'registrations': registrations})
    
    
def portfolio_list(request):
    images = PortfolioImage.objects.select_related('registration')
    return render(request, 'image_list.html', {'images': images})

    

def registration_details(request, registration_id):
    registration = get_object_or_404(PortfolioRegistration, pk=registration_id)
    return render(request, 'registration_details-Merge.html', {'registration': registration})
    
def portfolio_image_details(request, image_id):
    # Retrieve the clicked PortfolioImage object
    image = get_object_or_404(PortfolioImage, pk=image_id)

    # Retrieve the PortfolioRegistration object(s) that contain the clicked image
    registrations = PortfolioRegistration.objects.filter(portfolio_images=image)

    # Render the retrieved PortfolioRegistration object(s) in a template
    return render(request, 'portfolio_image_details.html', {'registrations': registrations})

