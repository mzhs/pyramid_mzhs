from pyramid.view import view_config


@view_config(route_name='home', renderer='static_pages/home.jinja2')
def home(request):
    return dict()
