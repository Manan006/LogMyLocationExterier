from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Login import Login
from ..Change_Password import Change_Password
from ..Locations import Locations
from ..location import location
import json
app_url = "http://139.84.135.123:8000"
class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if anvil.server.call('get_session')!=None:
      self.login.text="Sign Out"
      self.change_password.visible=True
    self.content_panel.add_component(Home())
    # Any code you write here will run when the form opens.

  def login_click(self, **event_args):
    print(anvil.server.call('get_session'))
    if anvil.server.call('get_session')!=None:
      anvil.server.call('signout')
      self.login.text="Log in"
      self.change_password.visible=False
    self.content_panel.clear()
    self.content_panel.add_component(Login())

  def locations_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    locations=anvil.server.call('get_location')
    for item in locations[1]:
      print(item)
      item_=json.loads(item[0].replace("'",'"'))
      print(item_)
      print(str(item[1]))
      self.add_component(location(lat=item_['lat'],lon=item_['lon'],time_=str(item[1])))
    
  def change_password_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.add_component(Change_Password())




