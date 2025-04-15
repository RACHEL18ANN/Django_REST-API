from django.urls import path
from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDestroyAPIView
from django.http import JsonResponse  # Import for the new view

def secure_hello_view(request):
    return JsonResponse({"message": "Hello, secure world!"})

urlpatterns = [
    path('article', ArticleListCreateAPIView.as_view(), name='list-create-post'),
    path('article/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-delete-post'),
    path('secure-hello/', secure_hello_view, name='secure-hello'),
]
