import yaml, os

# For Logging
import logging
# The path is relative to the top of the project.

def load_config (file):
  print(os.getcwd())
  with open(file, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
  return cfg

cfg = load_config('web/config.yaml')
logging.basicConfig(filename = cfg['log']['filename'],
                    level = logging.DEBUG,
                    )
