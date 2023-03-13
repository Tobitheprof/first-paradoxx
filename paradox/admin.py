from django.contrib import admin
from .models import *



class SlideAdmin(admin.TabularInline):
	model = Slide

class FlashCardAdmin(admin.ModelAdmin):
	inlines = [SlideAdmin]
	list_display = ['title', 'author']

admin.site.register(Profile)
admin.site.register(FlashCard, FlashCardAdmin)


# Register your models here.
