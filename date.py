import datetime
import time

def get_n_days_after_date(date_format="%d %B %Y", add_days=7):
    date_n_days_after = datetime.datetime.now() + datetime.timedelta(days=add_days)
    return date_n_days_after

