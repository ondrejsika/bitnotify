from django.conf.urls import url


urlpatterns = (
    url(r'^$', 'bitnotify.views.home_view', name='home'),

)

