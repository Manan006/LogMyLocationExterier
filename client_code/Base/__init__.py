from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Login import Login
app_url = "http://139.84.135.123:8000"
class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if anvil.server.call('get_session')!=None:
      self.login.text="Sign Out"

    self.content_panel.add_component(Home())
    # Any code you write here will run when the form opens.

  def login_click(self, **event_args):
    print(anvil.server.call('get_session'))
    if anvil.server.call('get_session')!=None:
      anvil.server.call('signout')
      self.login.text="Log in"
    self.content_panel.clear()
    self.content_panel.add_component(Login())

