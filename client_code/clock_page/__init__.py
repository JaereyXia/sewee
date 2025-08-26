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
    try:#If the time was over 12hour or less then 1 hour, the app will send a notification telling the user
      if float(int(self.time_number_hour_box.text)) >12 or float(int(self.time_number_hour_box.text)) < 0:
          self.time_number_hour_box.text = ""
          Notification("Wrong number, please enter a time within 12 hours").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.time_number_hour_box.text = ""
    
  def time_number_minute_box_pressed_enter(self, **event_args):#If the user enter a wrong time, it will detect and tell the user
    try:#if the time was over 59 minute that means it's 1 hour, or if the time is less then 1 minute, the app will tell the user 
      if int(self.time_number_minute_box.text) >59 or int(self.time_number_minute_box.text) < 0:
        self.time_number_minute_box.text = ""
        Notification("Wrong number, please enter a value of less than 60 minutes").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.time_number_minute_box.text = ""

  def write_cycle_number_box_pressed_enter(self, **event_args):#If the user enter a wrong number, it will detect and tell the user
    try:#if the number was over the 20 maximum, or if the time is less then 1 minimum, the app will tell the user 
      if int(self.write_cycle_number_box.text) >20 or int(self.write_cycle_number_box.text) < 0:
        self.write_cycle_number_box.text = ""
        Notification("Wrong number, please enter a number less than 20").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.write_cycle_number_box.text = ""

  def alarm_interval_number_box_pressed_enter(self, **event_args):#If the user enter a wrong number, it will detect and tell the user
    try:#if the time was over 10 minute the maximum, or if the time is less then 1 minute the mimimum, the app will tell the user 
      if int(self.alarm_interval_number_box.text) >10 or int(self.alarm_interval_number_box.text) < 0:
        self.alarm_interval_number_box.text = ""
        Notification("Wrong number, please enter a number less than 10").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.alarm_interval_number_box.text = ""

  def time_bottn_am_click(self, **event_args):#time am
    if self.time_button_am.role == 'elevated-button':
      self.time_button_am.role= 'filled-button'
    else:
      self.time_button_am.role = 'elevated-button'

  def time_pm_button_click(self, **event_args):#time pm
    if self.time_button_pm.role == 'elevated-button':
      self.time_button_pm.role= 'filled-button'
    else:
      self.time_button_pm.role = 'elevated-button'

  def days_mon_button_click(self, **event_args):#weekend
    if self.days_mon_button.role == 'elevated-button':
      self.days_mon_button.role= 'filled-button'
    else:
      self.days_mon_button.role = 'elevated-button'

  def days_tue_button_click(self, **event_args):#weekend
    if self.days_tue_button.role == 'elevated-button':
      self.days_tue_button.role= 'filled-button'
    else:
      self.days_tue_button.role = 'elevated-button'

  def days_wed_button_click(self, **event_args):#weekend
    if self.days_wed_button.role == 'elevated-button':
      self.days_wed_button.role= 'filled-button'
    else:
      self.days_wed_button.role = 'elevated-button'

  def days_thu_button_click(self, **event_args):#weekend
    if self.days_thu_button.role == 'elevated-button':
      self.days_thu_button.role= 'filled-button'
    else:
      self.days_thu_button.role = 'elevated-button'

  def days_fri_button_click(self, **event_args):#weekend
    if self.days_fri_button.role == 'elevated-button':
      self.days_fri_button.role= 'filled-button'
    else:
      self.days_fri_button.role = 'elevated-button'

  def days_sat_button_click(self, **event_args):#weekend
    if self.days_sat_button.role == 'elevated-button':
      self.days_sat_button.role= 'filled-button'
    else:
      self.days_sat_button.role = 'elevated-button'

  def days_sun_button_click(self, **event_args):#weekend
    if self.days_sun_button.role == 'elevated-button':
      self.days_sun_button.role= 'filled-button'
    else:
      self.days_sun_button.role = 'elevated-button'

  def clock_save_button_click(self, **event_args):
    time_hour = self.time_number_hour_box.text
    time_minute = self.time_number_minute_box.text

  
    







    



  
    
  
