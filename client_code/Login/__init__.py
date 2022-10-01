from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Invalid_Login import Invalid_Login
app_url = "http://139.84.135.123:8000"
class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.username_input.text
    response = http.request(method="GET",url=app_url+f"/login?username:{self.username_input.text}&password:{self.password_input.text}")
    if response.status_code == 200:
      print("uwu")
    else:
      self.content_panel.add_component(Invalid_Login())


    

