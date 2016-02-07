from django.conf.urls import url, include
from Blog.views import anasayfa, detail, allposts, categories, category_detail

url_extra = [
    url(r'^$', categories, name='category'),
    url(r'^detail/(?P<id>\d+)/$', category_detail, name='category_detail'),
]


urlpatterns = [

    url(r'^$', anasayfa, name='anasayfa'),
    url(r'^detail/(?P<id>\d+)/$', detail, name='detail'),
    url(r'^all/$', allposts, name='all'),
    url(r'category/', include(url_extra, namespace='category')),
]