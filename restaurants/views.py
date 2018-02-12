from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

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
	
	
