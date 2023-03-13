from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import *
import requests
import wikipedia




"""
<_----------------------Comments in regards to debugging and maintainance of Paradox code.----------------------->
If it works don't touch it...


"""



def index(request):
	user = request.user
	if user.is_authenticated:
		return redirect('home')
	return render(request, 'index2.html')



# <==================== Auth Views Start =====================>
def login(request):
	user = request.user
	if user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		username = request.POST['username'] #Requesting Username
		password = request.POST['password'] #Requesting Password
    
		user = auth.authenticate(username=username, password=password)

		if user is not None: #Cheking If User Exists in the database
			auth.login(request, user) # Logs in User
			return redirect('home') # REdirects to home view
		else:
			messages.info(request, 'Invalid Username or Password') #Conditional Checkign if credentials are correct
			return redirect('login')#Redirects to login if invalid
	else:
		return render(request, 'login.html', {'title' : 'Login'})


def register(request):
	user = request.user
	if user.is_authenticated:
		return redirect('home')
		
	if request.method == "POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		if password == password2:
			if User.objects.filter(email=email).exists():
				messages.info(request, "This email is already in use")
				return redirect("register")
			elif User.objects.filter(username=username).exists():
				messages.info(request, "This username is alrready in use")
				return redirect("register")

			else:
				user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
				user.save()
				user_login = auth.authenticate(username=username, password=password)
				auth.login(request, user_login)

			user_model = User.objects.get(username=username)
			new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
			new_profile.save()
			return redirect("home")

		else:
			messages.info(request, "Passwords do not match")
			return redirect("register")
	else:
		return render(request, 'register.html', {'title' : 'Register'})
	

@login_required
def home(request):
	flashcard = FlashCard.objects.all().order_by('date_created')[:8]
	context = {
		'flashcard' : flashcard,
		'title' : 'Home'
	}
	return render(request, 'home.html', context)

@login_required
def science(request):
	flashcard = FlashCard.objects.filter(category="Science")
	context = {
		'flashcard' : flashcard,
		'title' : 'Science'
	}
	return render(request, 'category.html', context, {'title' : 'Flashcards on Science'})

@login_required
def art(request):
	flashcard = FlashCard.objects.filter(category="Art")
	context = {
		'flashcard' : flashcard,
		'title' : 'Art'
	}
	return render(request, 'category.html', context, {'title' : 'Flashcards on Art'})

@login_required
def history(request):
	flashcard = FlashCard.objects.filter(category="History")
	context = {
		'flashcard' : flashcard,
		'title' : 'History'
	}
	return render(request, 'category.html', context, {'title' : 'Flashcards on History'})

@login_required
def technology(request):
	flashcard = FlashCard.objects.filter(category="Technology")
	context = {
		'flashcard' : flashcard,
		'title' : 'Technology'
	}
	return render(request, 'category.html', context, {'title' : 'Technology'})

@login_required
def business(request):
	flashcard = FlashCard.objects.filter(category="Business")
	context = {
		'flashcard' : flashcard,
		'title' : 'Business'
	}
	return render(request, 'category.html', context, {'title' : 'Business'})

@login_required
def detail(request, slug):
	flashcard = FlashCard.objects.get(slug=slug)

	context = {
		'flashcard' : flashcard,
		'title' : flashcard
	}

	return render(request, 'detail.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
# <=================== Auth Views End ========================>




# Create your views here.
