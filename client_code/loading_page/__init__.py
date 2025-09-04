from ._anvil_designer import loading_pageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class loading_page(loading_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)  
    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()#user login  

  def timer_1_tick(self, **event_args):#after 5 sec, the user will open the app.
    open_form('home_page')

  def button_1_click(self, **event_args):#if the user stack on the loading screen, they can report the question to feedback form
    open_form('feedback_form')
    