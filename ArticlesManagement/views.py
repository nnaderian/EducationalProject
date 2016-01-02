# -*- coding: utf-8 -*-
from .forms import UserForm, UserProfileForm, ArticleForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Article
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    context = RequestContext(request)
    tmp_error = request.session.get('error', False)

    request.session['error'] = ''
    articles = Article.objects.filter(creator_id=request.user.id).order_by('-created_date')
    return render_to_response('home.html', {'articles': articles, 'errors': tmp_error}, context)


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
        if request.user.is_authenticated():
            error = 'برای ثبت نام مجدد باید از این حساب کاربری خارج شوید'
            request.session['error'] = error
            return HttpResponseRedirect('/ArticlesManagement/')
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('register.html', {'user_form': user_form, 'profile_form': profile_form,
                                                'registered': registered}, context)


def user_login(request):
    context = RequestContext(request)
    errors = ''

    if request.method == 'GET':
        username = ''
        password = ''
        if request.GET.get('next'):
            next = request.GET['next']
        else:
            next = ''


    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        next = request.POST['next']
        if user:
            if user.is_active:
                login(request, user)

                if next != '':
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect('/ArticlesManagement/')
            else:
                errors = 'حساب شما غیرفعال می باشد'
        elif username == '' or password == '':
            errors = 'همه موارد باید تکمیل شوند'
        else:
            errors = 'حسابی با این مشخصات موجود نمی باشد، دوباره تلاش کنید'

    return render_to_response('login.html', {'errors': errors, 'next': next, 'username': username,
                                             'password': password}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/ArticlesManagement/')


def add_article(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/ArticlesManagement/add_new_article')
    else:
        return HttpResponse("You are not login yet")


@login_required
def add_new_article(request):
    context = RequestContext(request)

    if request.method == 'POST':
        article_form = ArticleForm(data=request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.created_date = timezone.now()
            article.creator_id = request.user.id
            article.save()
            return HttpResponseRedirect('/ArticlesManagement/')

    else:
        article_form = ArticleForm()

    return render_to_response('add_new_article.html', {'article_form': article_form}, context)


@login_required
def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return HttpResponseRedirect('/ArticlesManagement/')
