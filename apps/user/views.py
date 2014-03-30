from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings
from django.utils.translation import check_for_language
from apps.user.forms import *
from django.contrib.auth.forms import *


def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                messages.add_message(request, messages.ERROR, 'User not active')
        else:
            messages.add_message(request, messages.ERROR, 'Wrong username or password')
            return HttpResponseRedirect(reverse('lists:list', args=()))
        redirect_to = request.POST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return HttpResponseRedirect(reverse('lists:list', args=()))
    else:
        c = {}
        return render_to_response('registration/login.html', c, RequestContext(request))


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('lists:list', args=()))


def edit(request, user_id):
    if user_id == u'None':
        user_ = None
        form = UserCreationForm()
        profileForm = UserProfileForm()
    else:
        user_ = User.objects.get(pk=user_id)
        form = UserForm(instance=user_)
        profile, created = UserProfile.objects.get_or_create(user = user_)
        profileForm = UserProfileForm(instance = profile)

    return render_to_response('user/edit.html', {'form': form, 'user_': user_,'profileForm':profileForm}, RequestContext(request))


def save(request, user_id):
    if request.method == 'POST':
        if user_id == u'None':
            form = UserCreationForm(request.POST)
        else:
            user = User.objects.get(pk=user_id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.SUCCESS, 'Changes saved')
        else:
            messages.add_message(request, messages.ERROR, form.error_messages)
        return HttpResponseRedirect(reverse('lists:list', args=()))
    else:
        form = UserCreationForm
    c = {'form': form}
    return render_to_response('user/edit.html', c, RequestContext(request))