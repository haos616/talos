from envparse import Env
from jinja2 import Environment, FileSystemLoader


template_env = Environment(loader=FileSystemLoader('/usr/local/docker'))
template = template_env.get_template('default.conf.j2')

env = Env()

context = {
    'NGINX_DEV': env.bool('NGINX_DEV', default=False),
    'NGINX_ENABLE_PROXY_HEADERS': env.bool('NGINX_ENABLE_PROXY_HEADERS', default=False),
}

with open("/etc/nginx/conf.d/default.conf", "wb") as fh:
    fh.write(template.render(**context))
