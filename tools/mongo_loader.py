# mongo-engine packages
import mongoengine

# project resources
from app import default_config

# external packages
from types import FunctionType


def mongo(function: FunctionType) -> FunctionType:

    def load():
        mongoengine.connect(**default_config['MONGODB_SETTINGS'])
        function()
    return load