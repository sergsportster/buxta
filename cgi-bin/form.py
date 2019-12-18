import cgi, cgitb, sqlite3, html
form = cgi.FieldStorage()
conn = sqlite3.connect('my.db')
c = conn.cursor()
csum = conn.cursor()

def selcat():
  out = ''
  cat = form.getfirst("frcat", "0")
  c.execute('SELECT note from category where id = '+ cat) 
  row = c.fetchone()
  out = row[0]
  return out
rcategory = selcat()

def selsum():
  out = ''
  dtst = form.getfirst("dtstart", "2017-01-01")
  dten = form.getfirst("dtend", "2099-01-01")
  cat = form.getfirst("frcat", "0")
  per = form.getfirst("frper", "0")
  if (cat == "0") and (per == "0"):  
    csum.execute('SELECT sum(price) FROM pad where note <> "Новый период" and data between "'+str(dtst)+'" and "'+str(dten)+'"')   
  elif (cat == "0") and (per != "0"):
    csum.execute('SELECT sum(price) FROM pad where note <> "Новый период" and (period = %s' % str(per) + ')')
  elif (cat != "0") and (per != "0"):
    csum.execute('SELECT sum(price) FROM pad where note <> "Новый период" and (cat_id = %s' % str(cat) + ') and (period = %s' % str(per) + ')')  
  else:
    csum.execute('SELECT sum(price) from pad where note <> "Новый период" and (cat_id = %s' % str(cat) + ') and (data between "'+str(dtst)+'" and "'+str(dten)+'")')   
  row = csum.fetchone()
  out = str(row[0])
  return out
rsum = selsum()
if rsum == 'None':
	rsum = 0
  
def selostatok():
  out = ''
  per = form.getfirst("frper", "0")
  cat = form.getfirst("frcat", "0")
  if (per == '0') or (cat != '0'): 
    csum.execute('select "-"')
  else:
    csum.execute('select price from pad where note = "Новый период" and period = ' + str(per))
  row = csum.fetchone()
  out = str(row[0])
  return out
rsumostatok = selostatok()

def selpad():
  out = ''
  dtst = form.getfirst("dtstart", "16-01-01")
  dten = form.getfirst("dtend", "2099-01-01")
  cat = form.getfirst("frcat", "0")
  per = form.getfirst("frper", "0")
  
  if (cat == "0") and (per == "0"):
	  c.execute('SELECT * FROM pad where (data between "'+str(dtst)+'" and "'+str(dten)+'")')

  elif (cat == "0") and (per != "0"):
      c.execute('SELECT * FROM pad where (period = %s' % str(per) + ') and (data between "'+str(dtst)+'" and "'+str(dten)+'")' )

  elif (cat != "0") and (per != "0"):
      c.execute('SELECT * FROM pad where (cat_id = %s' % str(cat) + ') and (period = %s' % str(per) + ')' )
	  
  else:
      c.execute('SELECT * FROM pad where (cat_id = %s' % str(cat) + ') and (data between "'+str(dtst)+'" and "'+str(dten)+'")' ) 
  row = c.fetchone()
  num=1
  while row is not None:
    if not row: break
    out = '<tr>' + out + '<td>'+str(num)+'</td>' +'<td>'+str(row[2])+'</td>' +'<td>'+str(row[3])+'</td>' +'<td>'+str(row[4])+'</td>' +'<td>'+str(row[5])+'</td>' + '</tr>'
    num = num+1
    row = c.fetchone()
  return out
rcat = selpad()                         

cat = form.getfirst("frcat", "0")
per = form.getfirst("frper", "0")
if per == "0":  
	datetitle = form.getfirst("dtstart", "2017-01-01")
	if datetitle == "2017-01-01":
		datetitle = " за всё время"
	else:
		datetitle = '(' + form.getfirst("dtstart", "2017-01-01") + ' - ' + form.getfirst("dtend", "2099-01-01")+ ')'
else:
	datetitle = "за период " + str(per)
  
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <title>Data</title>
        </head>
        <body>""")
title = '<h3>Report category: '+ rcategory+' '+ datetitle + '</h3>'

if rsumostatok == '-':
	rsumostatok = rsumostatok
else:
	rsumostatok = int(rsumostatok) - int(rsum)
print(title)
print("""<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">""")
print("""
        <td align="left" bgcolor="#888888">№</td>
        <td align="left" bgcolor="#888888">Naim</td>
        <td align="left" bgcolor="#cccccc">Count</td>
        <td align="left" bgcolor="#cccccc">Price</td>
        <td align="left" bgcolor="#cccccc">Date</td>
        """)
print('%s'%rcat)
print("""</table>""")
print("<br>")
print("<b> Итого: " + str(rsum) + "</b>")
print("<br>")
print("<b> Остаток: " + str(rsumostatok) + "</b>")
print("""</body>""")
print("""</html>""")
c.close()
conn.close()
