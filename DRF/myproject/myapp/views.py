from rest_framework import generics
from rest_framework.response import Response

from .models import ExampleModel
from .serializers import ExampleModelSerializer


class ExampleModelListCreate(generics.ListCreateAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

    def get(self, request):
        my_models = ExampleModel.objects.all()
        serializer = ExampleModelSerializer(my_models, many=True)
        return Response(serializer.data)


class ExampleModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer
