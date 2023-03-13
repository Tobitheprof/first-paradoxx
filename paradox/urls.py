from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login', views.login, name='login'),
	path('register', views.register, name='register'),
	path('home', views.home, name='home'),
	path('science', views.science, name="science"),
	path('art', views.art, name="art"),
	path('history', views.history, name="history"),
	path('technology', views.technology, name="technology"),
	path('business', views.business, name="business"),
	path('detail/<str:slug>', views.detail, name="detail"),
	path('logout', views.logout, name="logout")
]