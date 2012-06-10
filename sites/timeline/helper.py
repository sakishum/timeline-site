# -*- coding: UTF-8 -*-
from django.template import Context, Template
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

import markdown

def _html(s):
    return Template("{{s|linebreaksbr}}").render(Context({"s": s}))

def tl_markdown(md):
    return mark_safe(markdown.markdown(force_unicode(md), 
        ['nl2br'], safe_mode='escape'))


def fmt_date(d):
    #before bc, start with -
    return d[:1] + d[1:].replace('-', ',') if d else ''

def event_to_dict(e):
    return {'startDate': fmt_date(e.startdate),
            'endDate': fmt_date(e.enddate),
            'headline': _html(e.title),
            'text': tl_markdown(e.text),
            'pk': e.pk,
            "asset": {
                "media": _html(e.media),
                "credit": '',#_html(e.media_credit),
                "caption": _html(e.media_caption) }
            }

def event_to_sdict(e):
    return {'startdate': e.startdate,
            'enddate': e.enddate,
            'title': e.title,
            'text': e.text,
            '_text': tl_markdown(e.text),
            'pk': e.pk,
            'cover': e.cover,
            'media': e.media,
            'media_credit': '',#e.media_credit,
            'media_caption': e.media_caption,
            }
