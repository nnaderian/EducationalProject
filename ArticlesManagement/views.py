from django.shortcuts import render
from .forms import UserForm, UserProfileForm, ArticleForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Article
from django.utils import timezone

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
            print 'all is valid'
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
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered':registered}, context)


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/ArticlesManagement/')
            else:
                return HttpResponse("You account is disable")
        else:
            return HttpResponse("Invalid Login details supplied")

    else:
        return render_to_response('login.html',{}, context)

def user_logout(request):
    context = RequestContext(request)

    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/ArticlesManagement/')
    else:
        return HttpResponse("You are not login yet")


def add_article(request):
    context = RequestContext(request)
    print '!!'
    print request.user.is_authenticated()
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
            print article_form.errors

    else:
        article_form = ArticleForm()

    return render_to_response('add_new_article.html', {'article_form' : article_form}, context)

def list_article(request):
    context = RequestContext(request)

