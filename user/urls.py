from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookView

router = DefaultRouter()

router.register('user',BookView,'demo')

urlpatterns = [
    path('',include(router.urls)),
]
