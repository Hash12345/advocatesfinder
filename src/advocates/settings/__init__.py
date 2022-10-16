import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'LOCAL')

if ENVIRONMENT == 'PRODUCTION':
    from .production import *
elif ENVIRONMENT == 'STAGING':
    from .staging import *
elif ENVIRONMENT == 'DEV':
    from .dev import *
else:
    from .local import *
