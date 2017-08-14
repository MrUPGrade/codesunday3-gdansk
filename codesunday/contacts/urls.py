from django.conf.urls import url, include

from contacts.views import index, date, contact_list, contact_add, contact_add2

urlpatterns = [
    url(r'^$', index),
    url(r'^today/$', date),
    url(r'^list/$', contact_list),
    url(r'^add2/$', contact_add2),
    url(r'^add/$', contact_add),
]
