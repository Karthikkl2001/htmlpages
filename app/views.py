from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request,'one.html')
def two(request):
    return render(request,'two.html')
def third(request):
    return render(request,'third.html')
def four(request):
    return render(request,'four.html')