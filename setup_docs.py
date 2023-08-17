from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load
import os

# Load YAML files.
# SWAGGER_INTERNAL_YAML_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'techtalk.yaml')
SWAGGER_INTERNAL_YAML_PATH = 'techtalk.yaml'

swagger_internal_yml = load(open(SWAGGER_INTERNAL_YAML_PATH, 'r', encoding='utf-8'), Loader=Loader)

swagger_url = '/docs'

# Create documentation blueprints.
# # Internal.
swaggerui_internal_blueprint = get_swaggerui_blueprint(
    swagger_url,
    SWAGGER_INTERNAL_YAML_PATH,
    config={
        'app_name': 'BBOXX Tech Talk API',
        'spec': swagger_internal_yml,
        'defaultModelRendering': 'model'
    }
)

swaggerui_internal_blueprint.name = 'swagger_internal_api_docs'
