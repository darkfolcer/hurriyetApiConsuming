from hurriyetApiConsuming.services import getPaths, getArticles, getPath,getArticle
from django.shortcuts import render
from hurriyetApiConsuming.models import userPreferences
from hurriyetApiConsuming.forms import UnknownForm
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
import re
from operator import attrgetter

def news(request):
    if(request.user.is_authenticated is False):
        return HttpResponseRedirect('login')
    _message = ""
    allPaths = []
    allArticles =[]
    allArticle = []
    _email = request.user.email
    userPaths = userPreferences.objects.all()
    userPaths= userPaths.filter(email=_email).values_list('Path')
    for x in userPaths:
        allPaths.append(getArticles(''.join(x)))

    for articles in allPaths:
        for article in articles:
            print (article.tittle)
        

    if not userPaths:
        _message="Your preferences list currently empty."

    context = {'paths': allPaths, 'userPaths': userPaths, 'request' : request, 'message' : _message}
    return render(request,'hurriyetApiConsuming/news.html', context)

def logout(request):
    logout(request)

def preferences(request):
    if(request.user.is_authenticated is False):
        return HttpResponseRedirect('login')
    _message="add/delete categories to your preferences using dropdown-list below."
    paths = getPaths()
    _email = request.user.email
    usePref = userPreferences.objects.all()
    userModel = userPreferences()
    if request.method == 'POST':
        form = UnknownForm(request.POST)
        if form.is_valid():   
            if 'add' in request.POST :
                pathId=form.cleaned_data['choices']    
                pathInfo = getPath(pathId)
                obj, created = userPreferences.objects.get_or_create(email = _email, Title = pathInfo.Tittle, categoryId = pathId, Path = pathInfo.Path)
                if created is True:
                    _message='a new category has been added to your preferences.'
                else:
                    _message='selected category already in your preferences.'
            if 'delete' in request.POST:
                pathId=form.cleaned_data['choices']
                paths =  usePref.filter(categoryId=pathId)
                if paths.count() > 0 :
                    usePref.filter(categoryId=pathId).delete()
                    _message='selected category has been deleted from your preferences.'  
                else:
                    _message='selected category is not in your preferences.'        
        context = {'preferences': usePref.filter(email=_email).values_list('Title', flat=True),'paths': getPaths, 'username': _email, 'message':_message,'request' : request}
        return render (request,'hurriyetApiConsuming/preferences.html',context )
       
    context = {'preferences': usePref.filter(email=_email).values_list('Title', flat=True), 'paths': getPaths,'username': _email, 'message':_message,'request' : request}
    return render(request,'hurriyetApiConsuming/preferences.html',context)

