import os
from datetime import datetime
dt = datetime.now()
if dt.isoweekday() == 3:
    os.startfile("wednesday.exe")
else:
    print("Sorry, today isn't Wednesday")