from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post, Count
import random

# Create your views here.

def homepage(request):
    template=get_template('index.html')
    posts=Post.objects.all()
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def carpage(request):
    template=get_template('car.html')
    cars=Count.objects.all()
    years=[
        '1994',
        '2008',
        '1896'
    ]
    html=template.render({'year':(years)})
    return HttpResponse(html)