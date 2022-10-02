from ._anvil_designer import locationTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

class location(locationTemplate):
  def __init__(self,lat,lon,time_,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.coords={"lat":lat,"lon":lon}
    self.time__.content = time_
    # Any code you write here will run when the form opens.

  def location_click(self, **event_args):
    self.location_.add_component(GoogleMap.Marker(
  animation=GoogleMap.Animation.DROP,
  position=GoogleMap.LatLng(self.coords['lat'],self.coords['lon'])
))
