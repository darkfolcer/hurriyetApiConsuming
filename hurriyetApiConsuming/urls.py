from django.urls import path
from .views import auth, news
from django.contrib.auth.views import logout
urlpatterns = [
    path('', auth.login, name='login'),
    path(r'login', auth.login, name='login'),
    path(r'register', auth.register, name='register'),
    path(r'news', news.news, name='news'),
    path(r'logout', logout, {'next_page': 'login'}),
    path(r'account/logout', logout, {'next_page': 'login'}),
    path(r'account/preferences', news.preferences, name='preferences'),
]
