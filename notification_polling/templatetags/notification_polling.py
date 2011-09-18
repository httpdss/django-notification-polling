from django import template

register = template.Library()

class PollerNode(template.Node):        
    def render(self, context):
        t = template.loader.get_template('notification_polling/polling_js.html')
        return t.render(context)
        
@register.tag
def poller_js(parser, token):
    return PollerNode()