from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserRegistrationForm

def register(request):
    context = {}
    
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        context['form'] = form
    else:
        form = UserRegistrationForm()
        context['form'] = form
    return render(request, 'users/register.html', context)
