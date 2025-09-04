from ._anvil_designer import home_pageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..clock_edit_page import clock_edit_page



class home_page(home_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    users_data = anvil.users.get_user()#Get the gmail of the user for identity check
    self.repeating_panel_1.items = app_tables.clock.search(user=users_data['email'])#use the users_data to find which user is using this app, then give them they clock


  def edit_clock(self, user, **event_args):
    #movie is the row from the Data Table
    item = dict(user)
    clock_edit = clock_edit_page(item=item)

    #if the user clicks OK on the alert
    if alert(content=clock_edit_page(), large=True):
      #pass in the Data Table row and the updated info
      anvil.server.call('update_clock', clock, item)
      #refresh the Data Grid
      self.repeating_panel_1.items = app_tables.clock.search()
  
      
  def add_clock_botton_click(self, **event_args):#open clock opage
    open_form('clock_page')
  
  def feedback_button_click(self, **event_args):#open feedback form 
    open_form('feedback_form')




