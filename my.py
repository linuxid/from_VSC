from datetime import datetime
now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)
delta = new_year - now
print(f"До Нового року залишилось {delta.days} днів")