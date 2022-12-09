from datetime import datetime, timedelta

print(datetime.now() < datetime.now() + timedelta(minutes=1))