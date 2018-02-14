from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import RestaurantForm


# Create your views here.

def list(request):
	context = {
		"restaurants": Restaurant.objects.all(),
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
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("go_back")
	context = {
	"create_form": form,
	}
	return render(request, 'create_restaurant.html', context)
def update(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
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
	delete_obj.delete()
	return redirect("go_back")
	

	
	
