from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "jornalindo"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("login", views.LoginView.as_view(), name="login"),
    path("cadastro", views.CadastroView.as_view(), name="cadastro"),
    #path("cadastro_noticia", views.CadastroNoticiaView.as_view(), name="cadastro_noticia"),
    path('logout/', auth_views.LogoutView.as_view(next_page='jornalindo:index'), name='logout'),
    path('noticia/<slug:slug>/', views.NoticiaDetail, name="noticia_slug"),
    path("edicao/<int:id>/", views.EdicaoDetail, name="edicao"),
    path("pesquisa", views.Pesquisa, name="pesquisa"),
    ]