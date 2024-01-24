# blog/urls.py
from django.urls import path
from .views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
]

