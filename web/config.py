import yaml, os

def load_config (file):
  print(os.getcwd())
  with open(file, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
  return cfg
