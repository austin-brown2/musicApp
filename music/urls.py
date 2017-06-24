from django.conf.urls import url
from . import views

# ^ beginning
# $ end

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/(albumid)
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]