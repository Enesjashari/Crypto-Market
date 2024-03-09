from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.

# @require_POST
def index(request):

    data = requests.get("https://api.coincap.io/v2/assets")
    if data.status_code == 200 :
        assets = data.json()

    context = {
        'data':assets['data'],
    }
    return render(request,'index.html',context)