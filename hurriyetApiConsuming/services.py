import http.client
from hurriyetApiConsuming.models import Paths, userPreferences, Article,Path,Articles
import json, codecs
from django.shortcuts import render, render_to_response
import re
import requests
def getPaths():
    headers = {
    'accept': "application/json",
    'apikey': "cd6b6c96799847698d87dec9f9a731d6"
    }
    data = requests.get('https://api.hurriyet.com.tr/v1/paths', headers = headers).json()
    json.dumps(data)
    return data
    

def getArticles(filter):
    allArticles = []
    headers = {
    'accept': "application/json", 
    'apikey': "cd6b6c96799847698d87dec9f9a731d6"
    }
    data = requests.get('https://api.hurriyet.com.tr/v1/articles', headers = headers, params={"$filter":"Path eq '"+filter+"'"}).json()
    json.dumps(data)
    for x in data:
        articles = Articles()
        articles.Id = x['Id']
        articles.Path = x['Path']
        articles.description = x['Description']
        articles.url = x['Url']
        articles.tittle=x['Title']
        for imgs in x['Files']:
            articles.img = imgs['FileUrl']
            break
        allArticles.append(articles)  
    return allArticles

def getArticle(articleId):

    headers = {
    'accept': "application/json", 
    'apikey': "cd6b6c96799847698d87dec9f9a731d6"
    }
    filter = "15-temmuz-yildonumu"
    data = requests.get('https://api.hurriyet.com.tr/v1/articles/'+articleId, headers = headers).json()
    json.dumps(data) 
    article = Article()
    article.tittle = data['Title']
    article._Id = data['Id']
    article.description = data['Description']
    article.url = data['Url']
    for imgs in data['Files']:
        article.img = imgs['FileUrl']
        break
    return article

def getPath(pathId):
    conn = http.client.HTTPSConnection("api.hurriyet.com.tr")
    headers = {
    'accept': "application/json", 
    'apikey': "cd6b6c96799847698d87dec9f9a731d6"
    }
    filter = "15-temmuz-yildonumu"
    data = requests.get('https://api.hurriyet.com.tr/v1/paths/'+pathId, headers = headers).json()
    json.dumps(data) 
    myPath = Path()
    myPath.Tittle = data['Title']
    myPath._Id = data['Id']
    myPath.Path = data['Path']
    return myPath


def addToPreferences(_categoryId, _email):
    userPreferences.categoryId = _categoryId
    userPreferences.email = _email
    userPreferences.save()
    return True
