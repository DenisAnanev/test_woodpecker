import os

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import redis

REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
redis_client = redis.from_url(REDIS_URL)


def hello_world(request):
    count = redis_client.incr('hello-world.count')
    return {'count': count}


def healthcheck(request):
    value = redis_client.ping()
    if value:
        return {'status': 'ok'}
    else:
        request.response.status = 503
        return {'status': 'error'}

def version(request):
    ver = os.environ.get("VERSION", "Not provided")
    return {'version': ver}

def secret(request):
    sec = os.environ.get("SECRET", "So secret value provided")
    return {'secret_value': sec}

with Configurator() as config:
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello', renderer='json')
    config.add_route('health', '/health')
    config.add_view(healthcheck, route_name='health', renderer='json')
    config.add_route('version', '/version')
    config.add_view(version, route_name='version', renderer='json')
    config.add_route('secret', '/secret')
    config.add_view(secret, route_name='secret', renderer='json')
    app = config.make_wsgi_app()


if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
