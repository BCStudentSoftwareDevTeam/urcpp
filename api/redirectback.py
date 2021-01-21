from everything import *

def redirect_url(default='dashboard'):
    return request.args.get('next') or request.referrer or url_for(default)
