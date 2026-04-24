from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm

def home(request):
    return HttpResponse("Welcome to SwiftBuy!")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

        
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")

    
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'Shop/contact.html', {'form': form})

def contact_success(request):
    return HttpResponse("Your message has been sent successfully!")
# Create your views here.
