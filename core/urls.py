from django.urls import path
from ram_api.views import DadosListCreate, DadosRetrieveUpdateDestroy, DadosResetContador

urlpatterns = [
    path('dados/', DadosListCreate.as_view(), name='dados-list-create'),
    path('dados/<int:pk>/', DadosRetrieveUpdateDestroy.as_view(), name='dados-retrieve-update-destroy'),
    path('dados/reset-contador/<int:pk>/', DadosResetContador.as_view(), name='dados-reset-contador'),
]

