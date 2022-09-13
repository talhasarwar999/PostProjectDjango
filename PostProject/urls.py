from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from postapp import views


#API Routers urls
router = DefaultRouter()
router.register('getallposts',views.GetAllPosts, basename="post")
router.register('getpostsbycategory',views.Get_Posts_By_Category, basename="postcategory")


#Application & Admin urls
urlpatterns = [
    path('postadminpanel/', admin.site.urls),
    path('', include(router.urls)),
]
