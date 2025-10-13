from django.urls import path
from . import views 
from .views import SignUpView

app_name = 'reviews'
urlpatterns = [
    path('', views.home, name='home'), 
    path('new/', views.new_review, name='new_review'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('place/<int:place_id>/', views.place_reviews, name='place_reviews'),

]

