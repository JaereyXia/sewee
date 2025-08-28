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

def add_clock(time_hour, time_minute, number_cycle, number_interval, button_am, button_pm, weekend_mon, weekend_tue, weekend_wed, weekend_thu, weekend_fri, weekend_sat, weekend_sun):
  pass