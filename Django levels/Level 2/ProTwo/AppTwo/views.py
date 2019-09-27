from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.
def user(request):
    user_list = User.objects.order_by('first_name')
    my_dict = {'User':user_list}
    return render(request, 'AppTwo/help.html', context=my_dict)

def index(request):
    return render (request, 'AppTwo/index.html')
