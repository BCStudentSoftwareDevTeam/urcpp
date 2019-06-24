import yaml, os

# For Logging
import logging
# The path is relative to the top of the project.

def load_config (file):
  with open(file, 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
  return cfg

#cfg = load_config('api/config.yaml')
#logging.basicConfig(filename = cfg['log']['filename'],
#                    level = logging.DEBUG,
#                    )
