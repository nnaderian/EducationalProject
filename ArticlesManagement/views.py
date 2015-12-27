# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import UserForm, UserProfileForm, ArticleForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Article
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def home(request):
    context = RequestContext(request)
    articles = Article.objects.all().order_by('-created_date')
    return render_to_response('home.html',{'articles': articles}, context)

@csrf_protect
def register(request):
    context = RequestContext(request)
    registered = False


    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered':registered}, context)


def user_login(request):
    context = RequestContext(request)
    errors = ''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/ArticlesManagement/')
            else:
                errors = 'حساب شما غیرفعال می باشد'
        elif username == '' or password == '':
            errors = 'همه موارد باید تکمیل شوند'
        else:
            errors = 'حسابی با این مشخصات موجود نمی باشد، دوباره تلاش کنید'

    else:
        username = ''
        password = ''


    return render_to_response('login.html',{'errors':errors}, context)

def user_logout(request):
    context = RequestContext(request)

    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/ArticlesManagement/')
    else:
        return HttpResponse("You are not login yet")


def add_article(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/ArticlesManagement/add_new_article')
    else:
        return HttpResponse("You are not login yet")


@csrf_protect
def add_new_article(request):
    context = RequestContext(request)

    if request.method == 'POST':
        article_form = ArticleForm(data=request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.created_date = timezone.now()
            article.save()
            return HttpResponseRedirect('/ArticlesManagement/')


    else:
        article_form = ArticleForm()

    return render_to_response('add_new_article.html', {'article_form' : article_form}, context)

def list_article(request):
    context = RequestContext(request)

def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return HttpResponseRedirect('/ArticlesManagement/')

