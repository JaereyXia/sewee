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

  def delete_clock_click(self, clock, **event_args):
    if confirm(f"Do you really want to delete the clock {clock['name']}?"):
      my_row_to_delete = app_tables.clock.get(name = 'name')
      my_row_to_delete.delete()
      

