from django.shortcuts import render, redirect , get_object_or_404
from .forms import ReviewForm ,CommentForm
from .models import ReviewImage ,Review,Place , comment
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView

def new_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        images = request.FILES.getlist('images')   

        if form.is_valid():
            place_name = request.POST.get('place_name')
            place, _ = Place.objects.get_or_create(name=place_name)
            review = form.save(commit=False)
            review.user = request.user 
            review.place = place
            review.save()

            for image in images:
                ReviewImage.objects.create(review=review, image=image)

            return redirect('reviews:home')
    else:
        form = ReviewForm()

    return render(request, 'reviews/new_review.html', {'form': form})

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    comments =review.comments.all().order_by('-date_created') 

    if request.method =='POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            comment =form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect('reviews:review_detail', pk=pk)
    else:
        form=CommentForm()       
    return render(request, 'reviews/review_detail.html', {'review': review ,'comments': comments, 'form': form})


def home(request):
    reviews = Review.objects.all().order_by('-date_created')
    paginator = Paginator(reviews, 5)  # 5 مراجعات لكل صفحة
    page = request.GET.get('page')
    reviews_page = paginator.get_page(page)
    return render(request, 'reviews/home.html', {'reviews': reviews_page})   

def place_reviews(request,place_id):
    place=get_object_or_404(Place,id=place_id)
    reviews=place.reviews.all()
    return render(request,'reviews/place_reviews.html',{'place':place, 'reviews':reviews})

class reviewUpdate(LoginRequiredMixin,UpdateView):
    model = Review
    form_class= ReviewForm
    template_name = 'reviews/edit_review.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')    