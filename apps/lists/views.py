# Create your views here.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import *
from django.core.urlresolvers import reverse
from random import randint
from models import *
from forms import *
from search_objects import *
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


def view(request, LIST_id):
    LIST = LIST.objects.get(pk=LIST_id)
    context = {'LIST': LIST}
    return render(request, 'lists/view.html', context)


def add(request):
    return edit(request, None)


def edit(request, LIST_id):
    if LIST_id:
        LIST = LIST.objects.get(pk=LIST_id)
    else:
        LIST = LIST()
    if request.method == 'POST':
        form = LISTInputForm(request.POST, instance=LIST)
        if form.is_valid():
            LIST = form.save(commit=False)
            LIST.time = int(parse_range_string(form.cleaned_data['timeString']))
            LIST.user = request.user
            LIST.save()
            return HttpResponseRedirect(reverse('lists:list', args=()))
    else:
        form = LISTInputForm(instance=LIST)
    context = {'form': form}
    return render(request, 'lists/edit.html', context)


def parse_range_string(input_string):
    d, tmp = input_string.split('d', 1)
    h, tmp = tmp.split('h', 1)
    m, tmp = tmp.split('m', 1)
    return int(d.strip()) * 1440 + int(h.strip()) * 60 + int(m.strip())


def split_range_string(range_):
    min_, max_ = range_.split('-', 1)
    return parse_range_string(min_), parse_range_string(max_)


def get_lists(search):
    if search.max_time != 1440 and search.min_time != 0:
        LIST_list = LIST.objects.filter(Q(time__lt=search.max_time), Q(time__gt=search.min_time), ~Q(
            completed=1)).filter(user__id=search.user.id).order_by(
            'name')
    elif search.min_time == 0 and search.max_time != 1440:
        LIST_list = LIST.objects.filter(Q(time__lt=search.max_time), ~Q(completed=1)).filter(
            user__id=search.user.id).order_by(
            'name')
    elif search.max_time == 1440 and search.min_time != 0:
        LIST_list = LIST.objects.filter(Q(time__gt=search.min_time), ~Q(completed=1)).filter(
            user__id=search.user.id).order_by(
            'name')
    else:
        LIST_list = LIST.objects.filter(
            ~Q(completed=1)).filter(user__id=search.user.id).order_by(
            'name')
    return LIST_list


def list_(request):
    search = LIST_search()
    search.min_time = 0
    search.max_time = 1440
        #if request.method == 'POST':
        #range_ = request.POST.get('range')
        #if range_:
        #    request.session['min_'], request.session['max_'] = split_range_string(range_)
    search.user = request.user
    LIST_list = get_lists(search)
    paginator = Paginator(LIST_list, 25) # Show 25 contacts per page
    try:
        posts = paginator.page(LIST_list)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    max_list = []
    for LIST in LIST_list:
        max_list.append(LIST.time)

    context = {'LIST_list': LIST_list, 'max_list': max_list}

    return render(request, 'lists/list.html', context)


def complete(request, LIST_id):
    LIST_to_complete = get_object_or_404(LIST, id=LIST_id)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = DeleteLISTForm(request.POST, instance=LIST_to_complete)

        if form.is_valid(): # checks CSRF
            LIST_to_complete.completed = 1
            LIST_to_complete.save()
            return HttpResponseRedirect(reverse('lists:list', args=())) # wherever to go after deleting

    else:
        form = DeleteLISTForm(instance=LIST_to_complete)

    template_vars = {'form': form}
    return render(request, 'lists/list.html', template_vars)


def delete(request, LIST_id):
    LIST_to_delete = get_object_or_404(LIST, id=LIST_id)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = DeleteLISTForm(request.POST, instance=LIST_to_delete)

        if form.is_valid(): # checks CSRF
            LIST_to_delete.delete()
            return HttpResponseRedirect(reverse('lists:list', args=())) # wherever to go after deleting

    else:
        form = DeleteLISTForm(instance=LIST_to_delete)

    template_vars = {'form': form}
    return render(request, 'lists/list.html', template_vars)


def random(request):
    search = LIST_search()
    if request.COOKIES.get('max_') and request.COOKIES.get('min_'):
        search.min_time = request.COOKIES['min_']
        search.max_time = request.COOKIES['max_']
    else:
        search.min_time = 0
        search.max_time = 1440
    search.user = request.user
    LIST_list = get_lists(search)
    if len(LIST_list) > 0:
        LIST = LIST_list[randint(0, len(LIST_list) - 1)]
        return HttpResponseRedirect(reverse('lists:view', args=(LIST.id,)))
    else:
        template_vars = {'header': "No lists found", 'body': "No lists found for the given timeframe"}
    return render(request, 'components/empty_modal.html', template_vars)


def filters(request):
    context = {}
    return render(request, 'components/filter_menu.html', context)