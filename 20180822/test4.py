import datetime as dt

now = dt.datetime.now()
now = now.replace(microsecond = 0)
delta = dt.timedelta(seconds = 1)
t = now.time()
print t

print((dt.datetime.combine(dt.date(1,1,1), t) + delta).time())
