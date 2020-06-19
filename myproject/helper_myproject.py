from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Topic(models.Model):
	name = models.CharField(max_length=30, unique=True)
	code=models.CharField(max_length=5)
    tex = models.TextField()
	
	def __str__(self):
		return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic',on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    favorite = models.BooleanField(default=False)
    published_date = models.DateTimeField( blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#the work inside the boards/models.py 

from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

	def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')






#################################3333333

#EN LA PRACTICA
from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]

#en boars/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')


from .models import Board

def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)


#pero esto lo podemos hacer con un  template

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
  </head>
  <body>
    <h1>Boards</h1>

    {% for board in boards %}
      {{ board.name }} <br>
    {% endfor %}

  </body>
</html>



#Para crear onjeto 1. instanciando el objeto pasándole los parámetros requeridos, y 2. llamar al método save() del modelo. 

comentario = comentario(comentario = “Comentario de prueba”, película
= pelicula1, usuario = usuario1)
comentario.save()

#lOS QUERYSETS Se muestra una ejemplo de un uso de get().
lista_cartelera = Cartelera.objects.get(identificador = identificador)
#Otra opción ES de limitar el número de resultados de un Queryset haciendo uso de la sintaxis de Python de rebanado de listas. 

def vista_pelicula(request, titulo):
	item_peli = get_object_or_404(Pelicula,titulo = titulo)
lista_comentarios=Comentario.objects.filter(peliculaitem_peli).order_by('-fecha_comentario')[:5]

from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})



from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home2(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


#We can improve the HTML template to use a table instead:templates/home.html

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
  </head>
  <body>
    <h1>Boards</h1>

    <table border="1">
      <thead>
        <tr>
          <th>Board</th>
          <th>Posts</th>
          <th>Topics</th>
          <th>Last Post</th>
        </tr>
      </thead>
      <tbody>
        {% for board in boards %}
          <tr>
            <td>
              {{ board.name }}<br>
              <small style="color: #888">{{ board.description }}</small>
            </td>
            <td>0</td>
            <td>0</td>
            <td></td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </body>
</html>

#patrone scon profundidad

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^about/company/$', views.about_company, name='about_company'),
    url(r'^about/author/$', views.about_author, name='about_author'),
    url(r'^about/author/vitor/$', views.about_vitor, name='about_vitor'),
    url(r'^about/author/erica/$', views.about_erica, name='about_erica'),
    url(r'^privacy/$', views.privacy_policy, name='privacy_policy'),
]
#requiere
def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})

#url mas avanzadas

from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),



#The {% static %} template tag uses the STATIC_URL configuration in the settings.py to compose the final URL. For example, if you hosted your static files in a subdomain like https://static.example.com/, we would set the STATIC_URL=https://static.example.com/

#en home.html (funciona)
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item active">Boards</li>
      </ol>
      <table class="table">
        <thead class="thead-inverse">
          <tr>
            <th>Board</th>
            <th>Posts</th>
            <th>Topics</th>
            <th>Last Post</th>
          </tr>
        </thead>
        <tbody>
          {% for board in boards %}
            <tr>
              <td>
                {{ board.name }}
                <small class="text-muted d-block">{{ board.description }}</small>
              </td>
              <td class="align-middle">0</td>
              <td class="align-middle">0</td>
              <td></td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </body>
</html>



#podemos modificar las condiciones del modelo

class Topic(models.Model):
    # other fields...
    # Add `auto_now_add=True` to the `last_updated` field
    last_updated = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    # other fields...
    # Add `null=True` to the `updated_by` field
    updated_by = models.ForeignKey(User, null=True, related_name='+')

from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^admin/', admin.site.urls),
]

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})

# en topics.html (funciona)
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ board.name }}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item">Boards</li>
        <li class="breadcrumb-item active">{{ board.name }}</li>
      </ol>
    </div>
  </body>
</html>

# para test de errores
class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)


<!-- code suppressed for brevity -->
<tbody>
  {% for board in boards %}
    <tr>
      <td>
        <a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
        <small class="text-muted d-block">{{ board.description }}</small>
      </td>
      <td class="align-middle">0</td>
      <td class="align-middle">0</td>
      <td></td>
    </tr>
  {% endfor %}
</tbody>
<!-- code suppressed for brevity -->


]


#Create a new file named base.html in the templates folder: templates/base.html

{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        {% block breadcrumb %}
        {% endblock %}
      </ol>
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>

#junto con otro que lleva a home vacio (solo board)
{% extends 'base.html' %}

{% block title %}
  {{ board.name }} - {{ block.super }}
{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item active">{{ board.name }}</li>
{% endblock %}

{% block content %}
    <!-- just leaving it empty for now. we will add core here soon. -->
{% endblock %}


# y el block topics

{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ board.name }}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item">Boards</li>
        <li class="breadcrumb-item active">{{ board.name }}</li>
      </ol>
    </div>
  </body>
</html>

#esta sera al base template/base

{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        {% block breadcrumb %}
        {% endblock %}
      </ol>
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>


#El nombre de plantilla pasado a {% extends %} es cargado usando el mismo método que get_template(). Esto es, el nombre de la plantilla es agregado a la variable TEMPLATE_DIRS.

#templates/topics.html


{% extends 'base.html' %}

{% block title %}
  {{ board.name }} - {{ block.super }}
{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item active">{{ board.name }}</li>
{% endblock %}

{% block content %}
    <!-- just leaving it empty for now. we will add core here soon. -->
{% endblock %}


#templates/base.html (pero no funcionan por staticFile)

{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="{% url 'home' %}">Django Boards</a>
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
  </body>
</html>

#el nucleo de las plantillas  donde se deber importar board.id
  {% for board in boards %}
    <tr>
      <td>
        <a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
        <small class="text-muted d-block">{{ board.description }}</small>
      </td>
      <td class="align-middle">0</td>
      <td class="align-middle">0</td>
      <td></td>
    </tr>
  {% endfor %}
</tbody>

#el nucleo de las plantillas  donde se deber importar post.id
  {% for board in boards %}
    <tr>
      <td>
        <a href="{% url 'board_topics' board.pk %}">{{ post.title }}</a>
        <small class="text-muted d-block">{{ post.message }}</small>
      </td>
      <td class="align-middle">0</td>
      <td class="align-middle">0</td>
      <td></td>
    </tr>
  {% endfor %}
</tbody>

#home ultimo
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item active">Boards</li>
      </ol>
      <table class="table">
        <thead class="thead-inverse">
          <tr>
            <th>Libros</th>
            <th>Posts</th>
            <th>Topicos</th>
            <th> ultimos  Post</th>
          </tr>
        </thead>
<tbody>
  {% for board in boards %}
    <tr>
      <td>
        <a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
        <small class="text-muted d-block">{{ board.description }}</small>
      </td>
      <td class="align-middle">0</td>
      <td class="align-middle">0</td>
      <td></td>
    </tr>
  {% endfor %}
</tbody>

      </table>
    </div>
  </body>
</html>

#topics ultimo
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ board.name }}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item"> Libro  </li>
        <li class="breadcrumb-item active">{{ board.name }}</li>
      </ol>
    </div>


    <div class="container">

  {% for post in posts %}
    <tr>
      <p>
        <a href="{ }">{{ post.title }}</a>
     <small class="text-muted d-block">{{ post.message }}</small>
      </p>
      <td class="align-middle">0</td>
      <td class="align-middle">0</td>
      <td></td>
    </tr>
  {% endfor %}
</tbody>

    </div>
  </body>
</html>

# parte 3 crear una cuenta
#crear app accounts al lado de boards
# ir a settings.py y anotar 'accounts'
# luego ir a la urls.py

from accounts import views as accounts_views
from boards import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]

###########################################################3

from django.shortcuts import render
from django.http import HttpResponse, Http404


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Board, Topic, Post



def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards} )


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'post_detail.html', {'topic': topic})


from django.conf.urls import url
from django.contrib import admin
from accounts import views as accounts_views  #para diferenciarlas
from boards import views


urlpatterns = [
    url(r'^$',views.home, name='home' ),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),

    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^admin/', admin.site.urls),


# put in archive topic.html

{% extends 'base.html' %}

{% block title %}
  {{ board.name }} - {{ block.super }}
{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item active">{{ board.name }}</li>
{% endblock %}

{% block content %}
  <table class="table">
    <thead class="thead-inverse">
      <tr>
        <th>Topic</th>
        <th>Starter</th>
        <th>Replies</th>
        <th>Views</th>
        <th>Last Update</th>
      </tr>
    </thead>
    <tbody>
{% for topic in board.topics.all %}
  <tr>
    <td><a href="{% url 'topic_posts' board.pk topic.pk %}">{{ topic.subject }}</a></td>
    <td>{{ topic.starter.username }}</td>
    <td>0</td>
    <td>0</td>
    <td>{{ topic.last_updated }}</td>
  </tr>
{% endfor %}

    </tbody>
  </table>
{% endblock %}


###############################
{% extends 'base.html' %}

{% block title %}Post a reply{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' topic.board.pk %}">{{ topic.board.name }}</a></li>
  <li class="breadcrumb-item"><a href="{% url 'topic_posts' topic.board.pk topic.pk %}">{{ topic.subject }}</a></li>
  <li class="breadcrumb-item active">Listas de Posts</li>
{% endblock %}

  {% block content %}
   {% for post in topic.posts.all %}
    <h2><a href="">{{ post.title }}</a></h2>
    <p>{{ post.message }}</p>

  
{% endfor %}

  {% endblock %}

# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Board(models.Model):
	name = models.CharField(max_length=30, unique=True)
	number=models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=50)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey('Board',on_delete=models.CASCADE) 

	def __str__(self):
		return self.subject



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=4000)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField( blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#este es un arhivo Json de nombre  secrets.json
{
    "SECRET_KEY": "N4HE:AMk:.Ader5354DR453TH8SHTQr",
    "DB_PASSWORD": "v3ry53cr3t"
}


#Y .gitignore a tu lista de ignorados ( .gitignore para git):

*.py[co]
*.sw[po]
*~
/secrets.json

#Luego agregue la siguiente función a su módulo de settings :

import json
import os
from django.core.exceptions import ImproperlyConfigured

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

#Luego llene la configuración de esta manera:

SECRET_KEY = get_secret('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres',
        'NAME': 'db_name',
        'USER': 'username',
        'PASSWORD': get_secret('DB_PASSWORD'),
    },
}

