from django.shortcuts import render, HttpResponseRedirect

# Home
def home(request):
    return render(request, 'home.html')

# Foods
def food(request):
    return render(request, 'foods.html')

# Contact
def contact(request):
    return render(request, 'contact.html')

# Signup
def signup(request):
    return render(request, 'account/signup.html')

# Login
def login(request):
    return render(request, 'account/login.html')

# # About
# def about(request):
#     return render(request, 'about.html')

# # Service
# def service(request):
#     return render(request, 'service.html')

# # Menu
# def menu(request):
#     return render(request, 'menu.html')