from django.template import RequestContext
from django.views.generic.base import View
from django.utils import simplejson
from django import http

class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return simplejson.dumps(context)

class NotificationPollingView(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        notice_unseen_count = RequestContext(request).get('notice_unseen_count')
        return self.render_to_response({'notice_unseen_count':notice_unseen_count})