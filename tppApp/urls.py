from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('DB', views.database, name='DB'),
    path('contact', views.contact, name='contact'),
    path('taxi', views.taxi, name='taxi'),
    path('predict', views.predict, name='predict'),
    path('result', views.result, name='result'),



]
