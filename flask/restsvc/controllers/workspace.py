from flask import Blueprint

workspace = Blueprint('workspace', __name__)


@workspace.route('/', methods=['GET'])
def get_workspaces():
    return []
