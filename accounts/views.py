from django.shortcuts import render




def LoginView(request):
    return render(request, 'accounts/login.html')


def SignupView(request):
    return render(request,'accounts/signup.html')
