from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FB
import ftplib
from django.http import HttpResponse
 
 
def index(request):
    return render(request, "ABSOLUTE/index.html" )

def review(request): 
	return render(request, "ABSOLUTE/review.html" )

def review_insert(request):
	a = FB(email = request.POST['email_fb'], text = request.POST['text_fb'])
	a.save()
	return HttpResponseRedirect(reverse('index'))