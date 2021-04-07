import os
import redis

from ceos.app import create_app

app = create_app(config_name=os.environ.get("FLASK_ENV", default="production"))
cache = redis.Redis(host='redis', port=6379)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
