# -*- coding: utf-8 -*-

from pybb import defaults

__author__ = 'zeus'


def processor(request):
    context = {}
    for i in (
        'PYBB_TEMPLATE',
        'PYBB_DEFAULT_AVATAR_URL',
        'PYBB_MARKUP',
        'PYBB_DEFAULT_TITLE',
        'PYBB_ENABLE_ANONYMOUS_POST',
        'PYBB_ATTACHMENT_ENABLE'
        ):
        context[i] = getattr(defaults, i, None)
    context['PYBB_AVATAR_DIMENSIONS'] = '%sx%s' % (defaults.PYBB_AVATAR_WIDTH, defaults.PYBB_AVATAR_WIDTH)    
    return context
