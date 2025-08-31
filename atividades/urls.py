from django.urls import path
from . import views

urlpatterns = [
    path('', views.atividades_pendentes_list, name='atividades_pendentes'),
    path('<int:atividade_id>/concluir/', views.concluir_atividade, name='concluir_atividade'),
    path('<int:atividade_id>/excluir/', views.excluir_atividade, name='excluir_atividade'),
    path('<int:atividade_id>/adiar/', views.adiar_atividade, name='adiar_atividade'),
    path('<int:atividade_id>/editar/', views.editar_atividade, name='editar_atividade'),
    path('concluidas/', views.atividades_concluidas_list, name='atividades_concluidas'),
    path('adiadas/', views.atividades_adiadas_list, name='atividades_adiadas'),
    path('<int:atividade_id>/mover-para-lista-de-tarefas/', views.mover_para_atividades, name='mover_para_atividades'),
]