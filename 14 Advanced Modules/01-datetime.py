from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "")


date = datetime(2019, 12, 1)

current_time = datetime.now()


print(current_time-date)
