from ._anvil_designer import SignupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Invalid_Login import Invalid_Login
from ..username_In_Use import username_In_Use
class Signup(SignupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.added_warning=False
    # Any code you write here will run when the form opens.

  def signup_btn_click(self, **event_args):
    data = anvil.server.call("signup",username=self.username_input.text,password=self.password_input.text)
    if not data:
      if not self.added_warning:
        self.add_component(username_In_Use())
        self.added_warning=True
    else:
      self.content_panel.clear()
      from ..Login import Login
      self.content_panel.add_component(Login())

