
from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="api/contacts", view=views.api, name="api"),
    path(route="add", view=views.add, name="add"),
    path(route="update", view=views.update, name="add"),
    path(route="login", view=views.my_login, name="login"),
    path(route="api/num", view=views.num, name="num")
]
