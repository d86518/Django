from django.conf.urls import include, url
from . import views

# urlpatterns = patterns('',
#     url(r'^$', views.post_list),
# )
# urlpatterns = [
#     url(r'^$',  views.index, name='index1'),
# ]
urlpatterns = [
    url(r'^$',  views.post_list),
    # 連到post_list的html
]
# ^ in regex means "the beginning"; from this sign we can start looking for our pattern
# $ matches only "the end" of the string, which means that we will finish looking for our pattern here
