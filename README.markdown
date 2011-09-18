# Django Notification polling
Simple app to get new notifications on pinax using polling techniques

## How to use
1. add _notification\_polling_ module to _INSTALLED\_APPS_
2. load the template tag into your template {% load notification_polling %}
3. call the template tag {% poller_js %} some place after jquery

## How to change favicon
1. Create a new folder: YOUR\_PROJECT/static/notification\_polling/img/
2. make 2 favicons named favicon\_active.png and favicon\_inactive.png