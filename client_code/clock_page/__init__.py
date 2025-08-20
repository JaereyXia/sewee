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

  def Cancle_button_click(self, **event_args):#cancel the creating of the clock and go back to home page
    open_form('home_page')
    
  def time_number_hour_box_pressed_enter(self, **event_args):#If the user enter a wrong time, it will detect and tell the user
    
    self.time_number_box = ""
    Notification("Wrong number, please inter times within 12 hour").show()

  def time_bottn_am_click(self, **event_args):
    if self.time_button_am.role == 'elevated-button':
      self.time_button_am.role= 'filled-button'
    else:
      self.time_button_am.role = 'elevated-button'

  def time_pm_button_click(self, **event_args):
    if self.time_button_pm.role == 'elevated-button':
      self.time_button_pm.role= 'filled-button'
    else:
      self.time_button_pm.role = 'elevated-button'

  def days_mon_button_click(self, **event_args):
    if self.days_mon_button.role == 'elevated-button':
      self.days_mon_button.role= 'filled-button'
    else:
      self.days_mon_button.role = 'elevated-button'

  def days_tue_button_click(self, **event_args):
    if self.days_tue_button.role == 'elevated-button':
      self.days_tue_button.role= 'filled-button'
    else:
      self.days_tue_button.role = 'elevated-button'

  def days_wed_button_click(self, **event_args):
    if self.days_wed_button.role == 'elevated-button':
      self.days_wed_button.role= 'filled-button'
    else:
      self.days_wed_button.role = 'elevated-button'

  def days_thu_button_click(self, **event_args):
    if self.days_thu_button.role == 'elevated-button':
      self.days_thu_button.role= 'filled-button'
    else:
      self.days_thu_button.role = 'elevated-button'

  def days_fri_button_click(self, **event_args):
    if self.days_fri_button.role == 'elevated-button':
      self.days_fri_button.role= 'filled-button'
    else:
      self.days_fri_button.role = 'elevated-button'

  def days_sat_button_click(self, **event_args):
    if self.days_sat_button.role == 'elevated-button':
      self.days_sat_button.role= 'filled-button'
    else:
      self.days_sat_button.role = 'elevated-button'

  def days_sun_button_click(self, **event_args):
    if self.days_sun_button.role == 'elevated-button':
      self.days_sun_button.role= 'filled-button'
    else:
      self.days_sun_button.role = 'elevated-button'

  def clock_save_button_click(self, **event_args):
    time_am = self.time_bottn_am_click()
    time_

  
    
  
