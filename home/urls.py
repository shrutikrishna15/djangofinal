from django.conf.urls import url
from home.views import HomeView,CommentView
from . import views
from django.contrib.auth.decorators import login_required


#from home import views


urlpatterns=[
  url(r'^$',HomeView.as_view(),name='home'),

  url(r'^comment/', (CommentView.as_view()),name='comment'),

]
