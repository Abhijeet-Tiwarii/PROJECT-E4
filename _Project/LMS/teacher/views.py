from django.shortcuts import render

# Create your views here.

def index(request):
	context = {}
	return render(request, 'teacher/index.html', context)
