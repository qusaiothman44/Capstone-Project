from django import forms
from .models import Review , comment, Profile

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rating' ,'price', 'description']
        widgets = {

            'title': forms.TextInput(attrs={'placeholder': 'Enter a catchy title', 'class':'FInput'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your experience', 'style':'width:100%;'}),
            'rating': forms.NumberInput(attrs={'placeholder': '1 to 5', 'class':'SInput'}),
            'price': forms.NumberInput(attrs={'placeholder': '0.0', 'class':'SInput'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields= ['content']
        widgets={
            'content': forms.Textarea(attrs={'row':3,'placeholder':'Write your comment here...'},)
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['bio', 'avatar']