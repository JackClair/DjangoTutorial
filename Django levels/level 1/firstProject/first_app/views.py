from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # Here Key is name of django template variable and value is what to be fitted dynamically
    my_dict = {"insert_me": "Hey I m From first_app/index.html"}
    #here in 2nd parameter first_app/ is used to indicate the sub-folder in templates folder
    return render(request, 'first_app/index.html', context=my_dict)
