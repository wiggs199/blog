from django.shortcuts import render # already imports for us 
from django.http import HttpResponse #(Django Http)
from .models import Post


# Take request argument
# Logic to handle how a user goes to our Blog(home page)
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})
