from ._anvil_designer import clock_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class clock_page(clock_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Cancle_button_click(self, **event_args):#open home page
    open_form('home_page')
  def time_text_box_1_pressed_enter(self, **event_args):
    
'''
  def clock_save_button_click(self, **event_args):
    name = self.time_text_box_1.text # Set 'name' to the text in the 'name_box'
    email = self.email_box.text # Set 'email' to the text in the 'email_box'
    feedback = self.feedback_box.text # Call your 'add_feedback' server function
'''




