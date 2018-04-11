from django.conf.urls import url

from . import views

urlpatterns = [
    url('^relatedness/?$', views.relatedness, name='relatedness'),
]
