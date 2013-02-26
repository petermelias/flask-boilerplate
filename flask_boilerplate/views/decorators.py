from flask import current_app, redirect, request, flash, url_for

from functools import wraps
from flask_boilerplate.models import FriendlyException

def friendly_errors(bomb_endpoint=None, xhr=False, fragment=None):
    def _decorator(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):
            if current_app.config.get('MODE') == 'testing': # this allows tests to assert the expected exception
                return f(*args, **kwargs)
            try:
                result = f(*args, **kwargs)
                return result
            except FriendlyException as e:
                if xhr:
                    return str(e)
                flash(str(e))
                redirect_endpoint = bomb_endpoint
                if not redirect_endpoint:
                    redirect_endpoint = request.endpoint
                return redirect(url_for(redirect_endpoint, _anchor=fragment, **request.view_args))
        return _wrapper
    return _decorator