import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

#Store feedback data using a server function
@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name=name, 
    email=email, 
    feedback=feedback, 
    created=datetime.now()
  )
  # Send an email each time the feedback is submitted
  anvil.email.send(#to="jaerey1016@gmail.com", own gmail address
    subject=f"Feedback from {name}",
    text=f"""
  A new person has filled out the feedback form!

  Name: {name}
  Email address: {email}
  Feedback:
  {feedback}
  """)
@anvil.server.callable
def add_clock(users, time_hour, time_minute, number_cycle, number_interval, button_am, button_pm, weekend_mon, weekend_tue, weekend_wed, weekend_thu, weekend_fri, weekend_sat, weekend_sun):
  app_tables.clock.add_row(
    hour = time_hour,
    minute = time_minute,
    cycle = number_cycle,
    interval = number_interval,
    am = button_am,
    pm = button_pm,
    mom = weekend_mon,
    tue = weekend_tue,
    wed = weekend_wed,
    thu = weekend_thu,
    fri = weekend_fri,
    sat = weekend_sat, 
    sun = weekend_sun,
    user = users
  )