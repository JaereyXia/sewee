from ._anvil_designer import loading_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class loading_page(loading_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

c = Timer(interval=1)# set a time for how long the user is gonna load for the app

def inter(self, t):# set a value if the timer match the time then send user to home page
  if t == 1:#if timer match
    open_form('home_page')#send user to home page

inter(c)

    