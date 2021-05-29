from django.shortcuts import render
from . import forms
from .forms import User

# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def User(request):
    form = forms.User()
    if request.method == 'POST':
        form = forms.User(request.POST)

        if form.is_valid():
            form.save()
    return render(request, 'first/form.html', {'form': form}) 