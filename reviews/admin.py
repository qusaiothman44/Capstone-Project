from django.contrib import admin
from .models import Review, ReviewImage

class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 1

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'rating', 'date_created']
    inlines = [ReviewImageInline]

admin.site.register(Review, ReviewAdmin)


