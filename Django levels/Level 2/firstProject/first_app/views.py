from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
# Create your views here.
def index(request):
    # Here Key is name of django template variable and value is what to be fitted dynamically
    webpage_list = AccessRecord.objects.order_by('date').reverse()
    #.reverse() is used as oder by desc
    #webpage_list = AccessRecord.objects.order_by('date').reverse()
    date_dict = {'AccessRecord': webpage_list}
    #here in 2nd parameter first_app/ is used to indicate the sub-folder in templates folder
    return render(request, 'first_app/index.html', context=date_dict)
