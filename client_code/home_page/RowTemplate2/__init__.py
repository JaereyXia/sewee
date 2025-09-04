from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def delete_clock_click(self, **event_args):
    if confirm(f'Do you want to delete this clock?'):
      # self.item refers to the current row in the repeating panel
      self.item.delete()
      # Optionally, remove the item from the repeating panel display
      self.remove_from_parent()
      #tell the user the delete is done
      Notification("clock deleted").show() 
      

