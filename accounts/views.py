from django.shortcuts import render, reverse

from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect

from django.views import generic

from .forms import CustomUserCreationForm


def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/login/')
	else:
		form = CustomUserCreationForm()
	
	context = {
		'form': form,
	}

	return render(request, 'registration/register.html', context)


# Create your views here.
