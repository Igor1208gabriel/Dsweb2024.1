from django.urls import path
from . import views

app_name = 'inketes'
urlpatterns = [
    path('', views.index, name="index"),

    path('<int:pergunta_id>/', views.detalhes, name='detalhes'),

    path('<int:pergunta_id>/votacao/', views.votacao, name='votacao'),

    path('<int:pergunta_id>/resultado/', views.resultado, name='resultado'),
]


'''

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),

    path('<int:pk>/', views.DetalhesView.as_view(), name='detalhes'),

    path('<int:pk>/resultado/', views.ResultadoView.as_view(), name='resultado'),

    path('<int:pergunta_id>/votacao/', views.votacao, name='votacao'),

]
'''