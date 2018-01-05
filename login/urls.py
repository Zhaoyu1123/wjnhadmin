from django.conf.urls import url, include

from views import LoginView, index


urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'', index),
]
