from django.urls import path
from . import views 
from .views import SignUpView , profile_edit

app_name = 'reviews'
urlpatterns = [
    path('', views.home, name='home'), 
    path('new/', views.new_review, name='new_review'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('place/<int:place_id>/', views.place_reviews, name='place_reviews'),
    path('Iuser/<int:user_id>/', views.user_reviews, name='user_reviews'),
    path('review/<int:pk>/edit/', views.reviewUpdate.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', views.reviewDelete.as_view(), name='review_delete'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

]

