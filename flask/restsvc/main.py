from flask import Flask

from .controllers.health import health
from .controllers.workspace import workspace

api_prefix = '/rest-svc/api/v1'

app = Flask(__name__)
app.register_blueprint(health, url_prefix=f'{api_prefix}/health')
app.register_blueprint(workspace, url_prefix=f'{api_prefix}/workspace')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
