import os
import yaml

def get_env():
    """Get ENV variable"""
    return os.getenv('ENV', 'qastaging')

def get_config(env):
    """Read config and return config dict"""
    filename = 'config.yaml'
    cf = open(os.path.dirname(os.path.abspath(__file__)) + '/' + filename)
    config = yaml.safe_load(cf)
    cf.close()
    return config
