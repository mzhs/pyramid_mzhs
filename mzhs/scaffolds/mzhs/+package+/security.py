from pyramid.security import (
    Allow,
    Authenticated,
    Everyone,
    )


class RootFactory:
    __acl__ = [(Allow, Authenticated, 'member'),
               (Allow, Everyone, 'everyone')]

    def __init__(self, request):
        pass

