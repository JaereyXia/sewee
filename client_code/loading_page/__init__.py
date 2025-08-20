from ._anvil_designer import loading_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from Python import random


class loading_page(loading_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.

  def timer_1_tick(self, **event_args):
    a= random(0,5)
    self.timer_1_tick.interval(1)
    open_form('home_page')
    
  



    