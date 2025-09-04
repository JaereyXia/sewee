from ._anvil_designer import clock_edit_pageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class clock_edit_page(clock_edit_pageTemplate):
  def __init__(self, item, **properties):

    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.am_key = False  # If the key is True, it means the user click the am button
    self.pm_key = False  # If the key is True, it means the user click the pm button
    self.mon_key = False  # If the key is True, it means the user click the mon button
    self.tue_key = False  # If the key is True, it means the user click the tue button
    self.wed_key = False  # If the key is True, it means the user click the wed button
    self.thu_key = False  # If the key is True, it means the user click the thu button
    self.fri_key = False  # If the key is True, it means the user click the fri button
    self.sat_key = False  # If the key is True, it means the user click the sat button
    self.sun_key = False  # If the key is True, it means the user click the sun button
    self.fill_in_key = False  # If the key is True, it means the user fill in all information of the clock. eg hour,minute...

    #load the clock to the text box, so the user know what he/she worte
    self.name_box.text = item['clock_name']#load the name
    self.time_number_hour_box.text = item['hour']#load the hour
    self.time_number_minute_box.text = item['minute']#load the minute
    self.write_cycle_number_box.text = item['cycle']#load the cycle
    self.alarm_interval_number_box.text = item['interval']#load the interval
    #if the itme value is True it will trigger if, therefore the user's clock has click on the button
    if item['am']:#if the key is True, it means the user click the am button
      self.am_key = True
      self.time_button_am.role = "filled-button"
    if item['pm']:#if the key is True, it means the user click the pm button
      self.pm_key = True
      self.time_button_pm.role = "filled-button"
    if item['mon']:#if the key is True, it means the user click the mon button
      self.days_mon_button.role = "filled-button"
      self.mon_key = True
    if item['tue']:#if the key is True, it means the user click the tue button
      self.days_tue_button.role = "filled-button"
      self.tue_key = True
    if item['wed']:#if the key is True, it means the user click the wed button
      self.days_wed_button.role = "filled-button"
      self.wed_key = True
    if item['thu']:#if the key is True, it means the user click the thu button
      self.days_thu_button.role = "filled-button"
      self.thu_key = True
    if item['fri']:#if the key is True, it means the user click the fri button
      self.days_fri_button.role = "filled-button"
      self.fri_key = True
    if item['sat']:#if the key is True, it means the user click the sat button
      self.days_sat_button.role = "filled-button"
      self.sat_key = True
    if item['sun']:#if the key is True, it means the user click the sun button
      self.days_sun_button.role = "filled-button"
      self.sun_key = True

    self.editing_clock = item['clock_name']#get the row by using the name
    self.row_to_edit = app_tables.clock.get(clock_name= self.editing_clock)

  def Cancle_button_click(    self, **event_args  ):  # cancel the creating of the clock and go back to home page
    open_form("home_page")

  def time_number_hour_box_pressed_enter(    self, **event_args  ):  # If the user enter a wrong time, it will detect and tell the user
    try:  # If the time was over 12hour or less then 1 hour, the app will send a notification telling the user
      if (
        float(int(self.time_number_hour_box.text)) > 12
        or float(int(self.time_number_hour_box.text)) < 0
      ):
        self.time_number_hour_box.text = ""
        Notification("Wrong number, please enter a time within 12 hours").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.time_number_hour_box.text = ""
  def time_number_hour_box_lost_focus(self, **event_args):
    try:  # If the time was over 12hour or less then 1 hour, the app will send a notification telling the user
      if (
        float(int(self.time_number_hour_box.text)) > 12
        or float(int(self.time_number_hour_box.text)) < 0
      ):
        self.time_number_hour_box.text = ""
        Notification("Wrong number, please enter a time within 12 hours").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.time_number_hour_box.text = ""

  def time_number_minute_box_pressed_enter(    self, **event_args  ):  # If the user enter a wrong time, it will detect and tell the user
    try:  # if the time was over 59 minute that means it's 1 hour, or if the time is less then 1 minute, the app will tell the user
      if (
        int(self.time_number_minute_box.text) > 59
        or int(self.time_number_minute_box.text) < 0
      ):
        self.time_number_minute_box.text = ""
        Notification(
          "Wrong number, please enter a value of less than 60 minutes"
        ).show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.time_number_minute_box.text = ""
  def time_number_minute_box_lost_focus(self, **event_args):
    try:  # if the time was over 59 minute that means it's 1 hour, or if the time is less then 1 minute, the app will tell the user
      if (
        int(self.time_number_minute_box.text) > 59
        or int(self.time_number_minute_box.text) < 0
      ):
        self.time_number_minute_box.text = ""
        Notification("Wrong number, please enter a value less than 60 minutes").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.time_number_minute_box.text = ""

  def write_cycle_number_box_pressed_enter(    self, **event_args  ):  # If the user enter a wrong number, it will detect and tell the user
    try:  # if the number was over the 20 maximum, or if the time is less then 1 minimum, the app will tell the user
      if (
        int(self.write_cycle_number_box.text) > 20
        or int(self.write_cycle_number_box.text) < 0
      ):
        self.write_cycle_number_box.text = ""
        Notification("Wrong number, please enter a number less than 20").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.write_cycle_number_box.text = ""
  def write_cycle_number_box_lost_focus(self, **event_args):
    try:  # if the number was over the 20 maximum, or if the time is less then 1 minimum, the app will tell the user
      if (
        int(self.write_cycle_number_box.text) > 20
        or int(self.write_cycle_number_box.text) < 0
      ):
        self.write_cycle_number_box.text = ""
        Notification("Wrong number, please enter a number less than 20").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.write_cycle_number_box.text = ""

  def alarm_interval_number_box_pressed_enter(    self, **event_args  ):  # If the user enter a wrong number, it will detect and tell the user
    try:  # if the time was over 10 minute the maximum, or if the time is less then 1 minute the mimimum, the app will tell the user
      if (
        int(self.alarm_interval_number_box.text) > 10
        or int(self.alarm_interval_number_box.text) < 0
      ):
        self.alarm_interval_number_box.text = ""
        Notification("Wrong number, please enter a number less than 10").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.alarm_interval_number_box.text = ""
  def alarm_interval_number_box_lost_focus(self, **event_args):
    try:  # if the time was over 10 minute the maximum, or if the time is less then 1 minute the mimimum, the app will tell the user
      if (
        int(self.alarm_interval_number_box.text) > 10
        or int(self.alarm_interval_number_box.text) < 0
      ):
        self.alarm_interval_number_box.text = ""
        Notification("Wrong number, please enter a number less than 10").show()
    except ValueError:
      Notification("Whoops! This wasn't a whole number").show()
      self.alarm_interval_number_box.text = ""

  
  """
  If the button is click,set the key to True, and the role to filled-button, so the color of the button will change.
  The key will tell the server if the button is clicked or not.
  If the button is clicked and then the user clicked one more time, the key will change to False, and the role to elevated-button so the user know that the button is off
  Becasue I use am and pm as the time, there can only be am or be pm, so when the user click on am, it will change the key and the role of the pm, and so on. 
  """
  
  def time_bottn_am_click(self, **event_args):  # time am
    if self.time_button_am.role == "elevated-button":
      self.time_button_am.role = "filled-button"
      self.am_key = True
      self.pm_key = False
      if self.am_key:  # if the user click on am button disable pm button
        self.time_button_pm.role = "elevated-button"
    else:
      self.time_button_am.role = "elevated-button"
      self.am_key = False
  def time_pm_button_click(self, **event_args):  # time pm
    if self.time_button_pm.role == "elevated-button":
      self.time_button_pm.role = "filled-button"
      self.pm_key = True
      self.am_key = False
      if self.pm_key:  # if the user click on pm button disable am button
        self.time_button_am.role = "elevated-button"
    else:
      self.time_button_pm.role = "elevated-button"
      self.pm_key = False

  def days_mon_button_click(self, **event_args):  # weekend
    if self.days_mon_button.role == "elevated-button":
      self.days_mon_button.role = "filled-button"
      self.mon_key = True
    else:
      self.days_mon_button.role = "elevated-button"
      self.mon_key = False
  def days_tue_button_click(self, **event_args):  # weekend
    if self.days_tue_button.role == "elevated-button":
      self.days_tue_button.role = "filled-button"
      self.tue_key = True
    else:
      self.days_tue_button.role = "elevated-button"
      self.tue_key = False
  def days_wed_button_click(self, **event_args):  # weekend
    if self.days_wed_button.role == "elevated-button":
      self.days_wed_button.role = "filled-button"
      self.wed_key = True
    else:
      self.days_wed_button.role = "elevated-button"
      self.wed_key = False
  def days_thu_button_click(self, **event_args):  # weekend
    if self.days_thu_button.role == "elevated-button":
      self.days_thu_button.role = "filled-button"
      self.thu_key = True
    else:
      self.days_thu_button.role = "elevated-button"
      self.thu_key = False
  def days_fri_button_click(self, **event_args):  # weekend
    if self.days_fri_button.role == "elevated-button":
      self.days_fri_button.role = "filled-button"
      self.fri_key = True
    else:
      self.days_fri_button.role = "elevated-button"
      self.fri_key = False
  def days_sat_button_click(self, **event_args):  # weekend
    if self.days_sat_button.role == "elevated-button":
      self.days_sat_button.role = "filled-button"
      self.sat_key = True
    else:
      self.days_sat_button.role = "elevated-button"
      self.sat_key = False
  def days_sun_button_click(self, **event_args):  # weekend
    if self.days_sun_button.role == "elevated-button":
      self.days_sun_button.role = "filled-button"
      self.sun_key = True
    else:
      self.days_sun_button.role = "elevated-button"
      self.sun_key = False
      
  def name_box_lost_focus(self, **event_args):
    if self.name_box.text == "":  # if the user didn't type in the name
      Notification(
        "please fill in the name"
      ).show()  # tell the user to fill in the name of the clock

  def clock_save_button_click(    self, **event_args  ):  # stone all the information of the clock, and send it to the server
    #check if any of those box is not filled, or if the am or pm button is not clicked
    if self.time_number_hour_box.text == "":  # if the user didn't type in the hour
      Notification("please fill in the hour").show()  # tell the user to fill in
    elif (
      self.time_number_minute_box.text == ""
    ):  # if the user didn't type in the minute
      Notification("please fill in the minute").show()  # tell the user to fill in
    elif self.write_cycle_number_box.text == "":  # if the user didn't tyep in the cycle
      Notification("please fill in the cycle").show()  # tell the user to fill in
    elif (
      self.alarm_interval_label.text == ""
    ):  # if the user didn't type in the interval
      Notification("please fill in the interval").show()  # tell the user to fill in
    else:  # if the user fill in the numbers
      self.fill_in_key = True  # allow to send the information to the server
    if self.am_key or self.pm_key:
      pass
    else:
      self.fill_in_key = False#the user need to fill in the value of the box
      Notification("please chose am or pm").show()#tell the user
    if (
      self.mon_key
      or self.tue_key
      or self.wed_key
      or self.thu_key
      or self.fri_key
      or self.sat_key
      or self.sun_key
    ):#if one of the day data is filled
      pass
    else:
      self.fill_in_key = False#the user need to click one of the day button
      Notification("please chonse the day").show()#tell the user

    if self.fill_in_key:#if the value is true, it means that the user has fill in all the text box, the am/pm button and one or more day button
      #store all the data 
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
      clock_names = str(self.name_box.text)
      #send all the data to the server
      self.row_to_edit.update(clock_name=clock_names, hour=time_hour, minute=time_minute, cycle=number_cycle, interval=number_interval, am=button_am, pm=button_pm, mon=weekend_mon, tue=weekend_tue, wed=weekend_wed, thu=weekend_thu, fri=weekend_fri, sat=weekend_sat, sun=weekend_sun)
      Notification("Alarm Clock Set").show()
      open_form("home_page")
    else:
      pass
