from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin
from torrents.views import homepage, anime_detail, fansub_detail, fansub

urlpatterns = [
    url(r"^$", homepage, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^anime/(?P<pk>\d+)/$", anime_detail, name="anime_detail"),
    url(r"^fansub/(?P<pk>\d+)/$", fansub_detail, name="fansub_detail"),
    url(r"^fansub/$", fansub, name="byfansub"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
