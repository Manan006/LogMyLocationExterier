import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import http
import json
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
app_url = "https://api.lml.dotcodes.dev"

@anvil.server.callable
def login(username,password):
  url = app_url+f"/login?username={username}&password={password}"
  print(url)
  try:
    response = http.request(method="GET",url=url)
  except http.HttpErrorStatus as response:
    return False
  else:
    sessionid=json.loads(response.get_bytes().decode())["sessionid"]
    print(sessionid)
    anvil.server.cookies.local['sessionid']=sessionid
    return True

@anvil.server.callable
def get_session():
  return anvil.server.cookies.local.get("sessionid", None)
  
@anvil.server.callable
def signout():
  url = app_url+f"/signout?sessionid={anvil.server.cookies.local['sessionid']}"
  print(url)
  try:
    response = http.request(method="POST",url=url)
  except http.HttpErrorStatus as response:
    anvil.server.cookies.local.clear()
    return False
  else:
    anvil.server.cookies.local.clear()
    return True


@anvil.server.callable
def signup(username,password):
  url = app_url+f"/create_user?username={username}&password={password}"
  print(url)
  try:
    response = http.request(method="PUT",url=url)
  except http.HttpErrorStatus as response:
    print(response.status)
    return False
  else:
    return True