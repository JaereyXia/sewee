from ._anvil_designer import home_pageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class home_page(home_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.add_clock()#load all the clock
    
  

  def add_clock(self):#this add all the clock with the information saved form data server
    clock = Label(text="Hello")#save all the infor of the clock from data.
    self.Clocks.add_component(clock, index=0)#add the clock
    
  
  def add_clock_botton_click(self, **event_args):#open clock opage
    open_form('clock_page')
  
  def feedback_button_click(self, **event_args):#open feedback form 
    open_form('feedback_form')



