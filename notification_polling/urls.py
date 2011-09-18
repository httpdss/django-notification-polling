from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from notification_polling.views import NotificationPollingView

urlpatterns = patterns('',
    url(r'^$', login_required(NotificationPollingView.as_view()), name="notification_polling_count"),
)
