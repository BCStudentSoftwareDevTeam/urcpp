from everything import *
import os

def get_page_name (string):
  return os.path.basename(string)  

app.jinja_env.filters['get_page_name'] = get_page_name