from django.urls import path, include
# from . import views
from .views import BookViewSet
# from .views import Another
from rest_framework import routers

# User routers when usings serializers
router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    # path('Another', Another.as_view()),
    # path('first', views.first),
    path('', include(router.urls))
]
