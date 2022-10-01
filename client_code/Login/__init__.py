from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Invalid_Login import Invalid_Login
class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = anvil.server.call("login",username=self.username_input.text,password=self.password_input.text)
    if not data:
      self.add_component(Invalid_Login())
    else:
      print(anvil.server.call("get_session"))   
