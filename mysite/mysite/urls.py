from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    # 指到polls
    url(r'^', include('blog.urls')),
    # 當首頁
]
