from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #send one time alerts to a template

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST) # form would represent UserCreationForm with POST data
		if form.is_valid():
			form.save() # saves user
			username = form.cleaned_data.get('username') #cleaned data is a dictionary
			messages.success(request,f'Acount created for {username}!')
			return redirect('blog-home')
	else:
		form = UserCreationForm() # blank form
	return render(request, 'users/register.html', {'form': form})

	#messages.debug
	#messages.info
	#messages.success
	#messages.warning
	#messages.error
