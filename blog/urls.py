from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('detail/<posts_id>', views.detail),
    path('edit/<posts_id>', views.edit),
    path('delete/<posts_id>', views.delete),
    path('update/<id>/', views.update, name='update'),
    path('post', views.post),
    path('create', views.create, name='create'),
]