from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
from .form import SignUpForm
from .form import SignUp


def home(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Success!')
        return HttpResponseRedirect('/thank/')

    return render_to_response("signup.html",
                              locals(),
                              context_instance = RequestContext(request))


def login(request):
    if bool(SignUp.objects.filter(email='')):
        return HttpResponseRedirect('//')

    return render_to_response("login.html",
                              locals(), 
                              context_instance = RequestContext(request))


def thank(request):

    return render_to_response("thank.html",
                              locals(), 
                              context_instance = RequestContext(request))


def about(request):

    return render_to_response("about.html",
                              locals(), 
                              context_instance = RequestContext(request))
