from django.urls import path

from .views import ExampleModelListCreate, ExampleModelRetrieveUpdateDestroy

urlpatterns = [
    path("examples/", ExampleModelListCreate.as_view()),
    path("examples/<int:pk>/", ExampleModelRetrieveUpdateDestroy.as_view()),
]
