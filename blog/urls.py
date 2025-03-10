from django.urls import path
from .views import post_detail, post_list

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),  # Remove 'views.' since we imported directly
    path('<int:pk>/', post_detail, name='post_detail')  # Remove 'views.' here too
]