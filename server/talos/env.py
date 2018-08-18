import os

import environ


BASE_DIR = os.path.realpath(os.path.dirname(__file__))

env = environ.Env()

# If exists file settings/.env.local we load settings/envs/.env.dev and this file.
# This is necessary so that the new variables for the local environment are automatically applied
local_env_file = os.path.join(BASE_DIR, 'settings', '.env.local')
if os.path.exists(local_env_file):
    # The first should be the configuration file of which are a priority
    # because django-environ use the setdefault (for os.environ)
    # for set it and the re-setting of the value will be ignored
    environ.Env.read_env(local_env_file)
    environ.Env.read_env(os.path.join(BASE_DIR, 'settings', 'envs', '.env.dev'))
else:
    environ.Env.read_env(os.path.join(BASE_DIR, 'settings', '.env'))
