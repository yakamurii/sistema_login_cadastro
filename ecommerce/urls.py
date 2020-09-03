from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.logar, name='login'),
    path('login/index',views.index, name='index'),
	path('cadastro/', views.cadastrar, name='cadastro')
]