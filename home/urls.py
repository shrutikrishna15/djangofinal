from django.conf.urls import url
from home.views import HomeView
from . import views


#from home import views

urlpatterns = [
    url(r'^$', (HomeView.as_view()), name='home'),


]