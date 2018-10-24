from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
urlpatterns=[
    url(r'^$',views.work,name = 'home'),
    url(r'^seller/$', views.seller, name='seller'),
    url(r'^buyer/$', views.buyer, name='buyer'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)