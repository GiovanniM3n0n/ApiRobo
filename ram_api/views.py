from rest_framework import generics
from .models import Dados
from .serializers import DadosSerializer
from rest_framework import generics, status
from rest_framework.response import Response

class DadosListCreate(generics.ListCreateAPIView):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

class DadosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer



class DadosResetContador(generics.GenericAPIView):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.resetar_contador()  # Chama o método resetar_contador() no objeto
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

