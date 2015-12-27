from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register/$', views.register),
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^add_article/$', views.add_article),
    url(r'^add_new_article/$', views.add_new_article),
    url(r'^delete_article/(?P<pk>\d+)/$', views.delete_article)
]