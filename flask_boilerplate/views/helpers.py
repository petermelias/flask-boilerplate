from flask import redirect, request, url_for

def redirect_to_home(): pass # requires config to implement

def redirect_self(clear_args=False):
	if clear_args:
		return redirect(url_for(request.endpoint))
    return redirect(url_for(request.endpoint, **request.view_args))

redirect_to_self = redirect_self

def redirect_to_next():
    if 'next' in request.args:
        return redirect(request.args.get('next'))

    return redirect_to_home()