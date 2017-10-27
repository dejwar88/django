from django.conf.urls import url

from guestbookapp import views

urlpatterns = [
    url (r'^$', views.index, name = 'index'),
    url (r'^delete/(?P<entry_id>\d+)/$', views.delete_entry, name = 'delete_entry'),
    url (r'^update/(?P<entry_id>\d+)/$', views.update_entry, name = 'update_entry'),
]