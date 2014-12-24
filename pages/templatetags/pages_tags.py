from django import template
from django.template import loader
from pages import models
register = template.Library()


def title_url_from_streamable(streamable):
    return {'title': streamable.stream_title(), 'url': streamable.stream_url()}


def recent_updates(context):
    template = loader.get_template('pages/recent_updates.html')
    streamables = (models.Streamable.objects
                   .order_by('-last_updated_date')
                   .filter(published=True).all()[:10])
    context['recent_updates'] = map(title_url_from_streamable, streamables)
    return template.render(context)

register.simple_tag(recent_updates, takes_context=True)
