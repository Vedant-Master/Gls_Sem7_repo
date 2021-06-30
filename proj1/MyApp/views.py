from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def music(request):
	return HttpResponse("<h1 bgcolor='red'>Music:</h1>Agar tum sath ho, Radha ne shyam, Pankhida ne apinjaru")

def home(request):
	return HttpResponse("<h1></h1>This is Home Page!!!")
def hobbies(request):
	return HttpResponse("<h1></h1>Coding, Music, Swimming")
def movies(request):
	return HttpResponse("<h1></h1>Scorpion, Angoor")
def books(request):
	return HttpResponse("<h1></h1>The Adventure of sherlock homes, An Unofficial guide to Ethical Hacking")
def place(request):
	return HttpResponse("<h1></h1>Maldives, Sikkim, Udaipur")
def friends(request):
	return HttpResponse("<h1></h1>Rushabh, Yashvi, Bhavya, Parth, Tanuja, Shreya")