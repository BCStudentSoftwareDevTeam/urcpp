from everything import *


def redirect_url(default='main'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)