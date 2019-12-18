import sqlite3
conn = sqlite3.connect('my.db')
c = conn.cursor()
import time
from datetime import datetime, timedelta, date, time as dt_time
d = datetime.today()
data = (d.strftime('%Y-%m-%d'))

def selcat():
  out = ''
  c.execute('SELECT max(period) from pad') 
  row = c.fetchone()
  out = row[0]
  return out
per = selcat()
 
def add_prod(cat, note, price, amount, data, per):
    c.execute("INSERT INTO pad (cat_id, note, price, amount, data, period) VALUES ('%s','%s','%s','%s','%s','%s')"%(cat, note, price, amount, data, per))
    conn.commit()
add_prod(1, 'Новый период', 0, 0, data, per + 1)
c.close()
conn.close()
