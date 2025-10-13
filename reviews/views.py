from django.shortcuts import render, redirect , get_object_or_404
from .forms import ReviewForm
from .models import ReviewImage ,Review,Place
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
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
    return render(request, 'reviews/review_detail.html', {'review': review})


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


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')    