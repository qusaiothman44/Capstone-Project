from django.urls import path
from . import views 
app_name = 'reviews'
urlpatterns = [
    path('', views.home, name='home'), 
    path('new/', views.new_review, name='new_review'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),

]

