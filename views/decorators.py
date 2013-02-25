from flask import current_app, redirect, request

def friendly_errors(bomb_endpoint=None, va=None, xhr=False, fragment=None):
    def _decorator(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):
            if current_app.config.get('MODE') == 'testing':
                return f(*args, **kwargs)
            try:
                result = f(*args, **kwargs)
                return result
            except FriendlyException as e:
                if xhr:
                    return str(e)
                flash(str(e))
                red_ep = bomb_endpoint
                if not red_ep:
                    red_ep = request.endpoint
                return redirect(url_for(red_ep, _anchor=fragment, **request.view_args))
        return _wrapper
    return _decorator