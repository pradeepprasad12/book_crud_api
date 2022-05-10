
from django.urls import path,include
from book.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud',views.Userviewset,basename='User_book')


urlpatterns = [
     path('',include(router.urls)),
     path('auth/',include('rest_framework.urls',namespace='rest_framework')),


]