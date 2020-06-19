from django.conf.urls import url
from django.contrib import admin
from boards import views
from accounts import views as accounts_views

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^signup/$',accounts_views.signup,name='signup'),
  url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
  url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
  url(r'^admin/', admin.site.urls),

en acoounts/views.py
from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')

###########################################################3
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # important
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



{% load static %}<!DOCTYPE html>
<html>


  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css?family=Peralta" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/app.css' %}">



   {% block stylesheet %}{% endblock %}  <!-- HERE -->
  </head>
  <body>
    {% block body %}  <!-- HERE -->


    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="{% url 'home' %}">Title Boards</a>
      </div>
    </nav>

    <div class="container">
      <ol class="breadcrumb my-4">
        {% block breadcrumb %}
        {% endblock %}
      </ol>
      {% block content %}
      {% endblock %}
    </div>

 {%endblock%}
  </body>
</html>



