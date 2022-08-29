from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<str:slug>', views.BlogPosts, name='BlogPosts'),
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$',serve, {'document_root':settings.STATIC_ROOT}),
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
