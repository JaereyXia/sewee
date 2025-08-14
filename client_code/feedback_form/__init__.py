from ._anvil_designer import feedback_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class feedback_form(feedback_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    name = self.name_box.text # Set 'name' to the text in the 'name_box'
    email = self.email_box.text # Set 'email' to the text in the 'email_box'
    feedback = self.feedback_box.text # Call your 'add_feedback' server function
    # pass in name, email and feedback as arguments
    anvil.server.call('add_feedback', name, email, feedback) # Set 'feedback' to the text in the 'feedback_box'
    Notification("Feedback submitted!").show() # Show a popup that says 'Feedback submitted!'
    self.clear_inputs() # Call your 'clear_inputs' method to clear the boxes

  def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""

  def home_button_click(self, **event_args):
    # If the users click this button, it will lead him/her back to the home page
    open_form('home_page')