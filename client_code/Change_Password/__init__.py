from ._anvil_designer import Change_PasswordTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Invalid_Login import Invalid_Login
from ..username_In_Use import username_In_Use
from ..Wrong_Old_Password import Wrong_Old_Password
class Change_Password(Change_PasswordTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.added_warning=False
    # Any code you write here will run when the form opens.

  def change_password(self, **event_args):
    data = anvil.server.call("change_password",old=self.old_pass.text,new=self.new_pass.text)
    if not data:
      if not self.added_warning:
        self.add_component(Wrong_Old_Password())
        self.added_warning=True
    else:
      self.content_panel.clear()
      self.add_component(Home())

  def username_input_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

