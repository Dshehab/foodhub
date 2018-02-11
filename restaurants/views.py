from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list(request):
	context = {
		"cuisines": [
			{
				"cuisine": "Italian",
				"rating": "excellent!!",
				"working_days": "saturday-thursday"
			},
			{
				"tcuisine": "Japanese",
				"rating": "very good!",
				"working_days": "saturday-thursday"
			},
			{
				"cuisine": "Indian",
				"rating": "good",
				"working_days": "saturday-thursday"
			},

	]
	}
	return render(request, 'firstone.html', context)
