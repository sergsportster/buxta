import cgi, cgitb, sqlite3, html
form = cgi.FieldStorage()
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
    c.execute("INSERT INTO pad (cat_id, note, amount, price, data, period) VALUES ('%s','%s','%s','%s','%s','%s')"%(cat, note, price, amount, data, per))
    conn.commit()

inscat = form.getfirst("frcat", "0")
insnt = form.getfirst("frnote", "0")
insamount = form.getfirst("framount", "0")
insprice = form.getfirst("frprice", "0")
insdate = form.getfirst("dt", data)

add_prod(inscat, insnt, insamount, insprice, insdate, per)
c.close()
conn.close()


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <title>Data</title>
			<script>history.go(-1)</script>
        </head>
        <body>""")

#webbrowser.get('Windows-Default')
#webbrowser.open("http://localhost:8080/insert.html", new=0)
