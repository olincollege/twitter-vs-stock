"""
Testing snscrape library.
"""
# MAY NOT WORK AS FUNCTIONS HAVE BEEN RENAMED - CHECK NOTEBOOK FOR CURRENT
# PROCESS.
import datetime
from datetime import timedelta

x = datetime.datetime(2020, 5, 12)

buffer = timedelta(days=15)

new_x = x - buffer

print(f"The original date is {x}, the new date is {new_x}")
