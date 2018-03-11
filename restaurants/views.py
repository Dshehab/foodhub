from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Restaurant, FavoriteRestaurant
from .forms import RestaurantForm
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth import logout

def user_logout(request):
	logout(request)
	return redirect("login")

def favorite_restaurant(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	favorite_obj, created = FavoriteRestaurant.objects.get_or_create(user=request.user, restaurant=restaurant_obj)
	if created:
		action = 'fav'
	else:
		action = 'notfav'
		favorite_obj.delete()
	fav_num = restaurant_obj.favoriterestaurant_set.all().count()
	response = {
		"action": action,
		"fav_num": fav_num,
	}
	return JsonResponse(response, safe=False)



# Create your views here.
def user_login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request,auth_user)
				return redirect("go_back")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)

def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			person = form.save(commit=False)
			person.set_password(person.password)
			person.save()
			login(request, person)
			return redirect("go_back")
	context = {
		"form": form
	}
	return render(request, 'register.html', context)
def list(request):
	if(request.user.is_anonymous):
		return redirect('login')
	object_list = Restaurant.objects.all()
	object_list = object_list.order_by('publish_date', 'name')
	query = request.GET.get('q')
	if query:
		object_list = object_list.filter(name__contains=query)
	context = {
		"restaurants": object_list
		}
	return render(request, 'firstone.html', context)
	# 	"cuisines": [
	# 		{
	# 			"cuisine": "Italian",
	# 			"rating": "excellent!!",
	# 			"working_days": "saturday-thursday"
	# 		},
	# 		{
	# 			"tcuisine": "Japanese",
	# 			"rating": "very good!",
	# 			"working_days": "saturday-thursday"
	# 		},
	# 		{
	# 			"cuisine": "Indian",
	# 			"rating": "good",
	# 			"working_days": "saturday-thursday"
	# 		},

	# ]
def detail(request, detail_id):
	context = {
		"restaurants": Restaurant.objects.get(id=detail_id),
		
		}
	return render(request, 'detail.html', context)
def create(request):
	if(request.user.is_anonymous):
			return redirect('login')
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect("go_back")
	context = {
	"create_form": form,
	}
	return render(request, 'create_restaurant.html', context)
def update(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	if not(request.user==restaurant_obj.owner or request.user.is_staff):
		return redirect('login')
	form = RestaurantForm(instance=restaurant_obj)
	if request.method == "POST":
		form = RestaurantForm(request.POST, instance=restaurant_obj)
		if form.is_valid():
			form.save()
			return redirect("restaurant_detail", detail_id=restaurant_obj.id)
	context = {
		"restaurant_obj": restaurant_obj,
		"update_form": form,
	}
	return render(request, 'update.html', context)

def delete(request, delete_id):
	delete_obj = Restaurant.objects.get(id=delete_id)
	if(not(request.user.is_staff) or request.user==delete_obj.owner):
		return redirect('login')
	delete_obj.delete()
	return redirect("go_back")
	

	
	
