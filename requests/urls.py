from django.conf.urls import patterns, url

from requests.views import RequestView

urlpatterns = [
    url(r"^request/$", RequestView.as_view())
]
