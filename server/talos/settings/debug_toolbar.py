from talos.env import env

from .common import INSTALLED_APPS, MIDDLEWARE

# Debug toolbar
ENABLE_DEBUG_TOOLBAR = env.bool('TALOS_ENABLE_DEBUG_TOOLBAR', default=False)

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar', ]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
        'SHOW_TEMPLATE_CONTEXT': True,
    }
