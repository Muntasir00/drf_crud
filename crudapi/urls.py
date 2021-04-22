from django.urls import path,include
from .views import GenericArticleView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('article',GenericArticleView, basename='article')
urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)), 

]