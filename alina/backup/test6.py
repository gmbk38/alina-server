from datetime import datetime, timedelta

clock_in_half_hour = datetime.now() + timedelta(minutes=30)
print(clock_in_half_hour)