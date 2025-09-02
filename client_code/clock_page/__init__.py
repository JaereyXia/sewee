from ._anvil_designer import clock_pageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class clock_page(clock_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bi ndings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.am_key = False#If the key is True, it means the user click the am button
    self.pm_key = False#If the key is True, it means the user click the pm button
    self.mon_key = False#If the key is True, it means the user click the mon button
    self.tue_key = False#If the key is True, it means the user click the tue button
    self.wed_key = False#If the key is True, it means the user click the wed button
    self.thu_key = False#If the key is True, it means the user click the thu button
    self.fri_key = False#If the key is True, it means the user click the fri button
    self.sat_key = False#If the key is True, it means the user click the sat button
    self.sun_key = False#If the key is True, it means the user click the sun button
    self.fill_in_key = False#If the key is True, it means the user fill in all information of the clock. eg hour,minute...

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
      self.am_key = True
      self.pm_key = False
      if self.am_key :#if the user click on am button disable pm button
        self.time_button_pm.role = 'elevated-button'
    else:
      self.time_button_am.role = 'elevated-button'
      self.am_key = False

  def time_pm_button_click(self, **event_args):#time pm
    if self.time_button_pm.role == 'elevated-button':
      self.time_button_pm.role= 'filled-button'
      self.pm_key = True
      self.am_key = False
      if self.pm_key :#if the user click on pm button disable am button
        self.time_button_am.role = 'elevated-button'
    else:
      self.time_button_pm.role = 'elevated-button'
      self.pm_key = False

  def days_mon_button_click(self, **event_args):#weekend
    if self.days_mon_button.role == 'elevated-button':
      self.days_mon_button.role= 'filled-button'
      self.mon_key = True
    else:
      self.days_mon_button.role = 'elevated-button'
      self.mon_key = False

  def days_tue_button_click(self, **event_args):#weekend
    if self.days_tue_button.role == 'elevated-button':
      self.days_tue_button.role= 'filled-button'
      self.tue_key = True
    else:
      self.days_tue_button.role = 'elevated-button'
      self.tue_key = False

  def days_wed_button_click(self, **event_args):#weekend
    if self.days_wed_button.role == 'elevated-button':
      self.days_wed_button.role= 'filled-button'
      self.wed_key = True
    else:
      self.days_wed_button.role = 'elevated-button'
      self.wed_key = False

  def days_thu_button_click(self, **event_args):#weekend
    if self.days_thu_button.role == 'elevated-button':
      self.days_thu_button.role= 'filled-button'
      self.thu_key = True
    else:
      self.days_thu_button.role = 'elevated-button'
      self.thu_key = False

  def days_fri_button_click(self, **event_args):#weekend
    if self.days_fri_button.role == 'elevated-button':
      self.days_fri_button.role= 'filled-button'
      self.fri_key = True
    else:
      self.days_fri_button.role = 'elevated-button'
      self.fri_key = False

  def days_sat_button_click(self, **event_args):#weekend
    if self.days_sat_button.role == 'elevated-button':
      self.days_sat_button.role= 'filled-button'
      self.sat_key = True
    else:
      self.days_sat_button.role = 'elevated-button'
      self.sat_key = False

  def days_sun_button_click(self, **event_args):#weekend
    if self.days_sun_button.role == 'elevated-button':
      self.days_sun_button.role= 'filled-button'
      self.sun_key = True
    else:
      self.days_sun_button.role = 'elevated-button'
      self.sun_key = False

  def clock_save_button_click(self, **event_args):#stone all the information of the clock, and send it to the server
    if self.time_number_hour_box.text == "":#if the user didn't type in the hour
      Notification("please fill in the hour").show()#tell the user to fill in
    elif self.time_number_minute_box.text == "":#if the user didn't type in the minute
      Notification("please fill in the minute").show()#tell the user to fill in
    elif self.write_cycle_number_box.text == "":#if the user didn't tyep in the cycle
      Notification("please fill in the cycle").show()#tell the user to fill in
    elif self.alarm_interval_label.text == "":#if the user didn't type in the interval
      Notification("please fill in the interval").show()#tell the user to fill in
    else:#if the user fill in the numbers
      self.fill_in_key = True#allow to send the information to the server
    if self.am_key or self.pm_key:
      pass
    else:
      self.fill_in_key = False
      Notification("please chose am or pm").show()
    if self.mon_key or self.tue_key or self.wed_key or self.thu_key or self.fri_key or self.sat_key or self.sun_key:
      pass
    else:
      self.fill_in_key = False
      Notification("please chonse the day").show()

    
    if self.fill_in_key:
      users = anvil.users.get_user()
      time_hour = int(self.time_number_hour_box.text)
      time_minute = int(self.time_number_minute_box.text)
      number_cycle = int(self.write_cycle_number_box.text)
      number_interval = int(self.alarm_interval_number_box.text)
      button_am = self.am_key
      button_pm = self.pm_key
      weekend_mon = self.mon_key
      weekend_tue = self.tue_key
      weekend_wed = self.wed_key
      weekend_thu = self.thu_key
      weekend_fri = self.fri_key
      weekend_sat = self.sat_key
      weekend_sun = self.sun_key
      user = users['email']
      anvil.server.call('add_clock', user, time_hour, time_minute, number_cycle, number_interval, button_am, button_pm, weekend_mon, weekend_tue, weekend_wed, weekend_thu, weekend_fri, weekend_sat, weekend_sun)
      Notification("Alarm Clock Set").show()
      open_form('home_page')
    else:
      pass
    
    







    



  
    
  
