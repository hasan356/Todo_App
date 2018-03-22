from . import views

from django.conf.urls import url,include
from .views import CreateTodo,DetailTodo,UpdateTodo,DeleteTodo

urlpatterns = [
    url(r'^todo/detail/(?P<title_id>[0-9]+)/$', DetailTodo.as_view(), name='detail'),
    url(r'^todo/update/(?P<title_id>[0-9]+)/$', UpdateTodo.as_view(), name='update'),
    url(r'^todo/delete/(?P<title_id>[0-9]+)/$', DeleteTodo.as_view(), name='delele'),
    url(r'^todo/' , CreateTodo.as_view()),
]
