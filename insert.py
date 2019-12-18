import sqlite3
conn = sqlite3.connect('my.db')
c = conn.cursor()
import time
from datetime import datetime, timedelta, date, time as dt_time
d = datetime.today()
def selcat():
  out = ''
  c.execute('SELECT max(period) from pad') 
  row = c.fetchone()
  out = row[0]
  return out
per = selcat()
def add_prod(cat, note, amount, price, data, per):
    c.execute("INSERT INTO pad (cat_id, note, amount, price, data, period) VALUES ('%s','%s','%s','%s','%s','%s')"%(cat, note, price, amount, data, per))
    conn.commit()
def del_prod(id):
    c.execute("DELETE FROM pad WHERE id = '%s'"%(id))
    conn.commit()
while True:
	name = input("1 - Просмотр 2 - Добавить 3 - Удалить 0 - Выход\n" )
#	Просмотр данных
	if name == "1": 
		while True:			
			print("\n")
			cat = input("1 - Продукты 2 - ХозБыт 3 - Другое 4 - Все 0 - Выход\n")
			if cat == "1": 
				c.execute('''SELECT pad.id, pad.note, pad.price, pad.amount, pad.data
							  FROM pad INNER JOIN
								category ON pad.cat_id = category.id where pad.cat_id = 1''')
				row = c.fetchone()
				while row is not None:
					print("id:"+str(row[0])+" Наименование: "+str(row[1]) +" | Цена: "+str(row[2]) +" | Кол-во: "+str(row[3]) +" | Дата: "+str(row[4]))
					row = c.fetchone()
			if cat == "2": 
				c.execute('''SELECT pad.id, pad.note, pad.price, pad.amount, pad.data
							  FROM pad INNER JOIN
								category ON pad.cat_id = category.id where pad.cat_id = 2''')
				row = c.fetchone()
				while row is not None:
					print("id:"+str(row[0])+" Наименование: "+str(row[1]) +" | Цена: "+str(row[2]) +" | Кол-во: "+str(row[3]) +" | Дата: "+str(row[4]))
					row = c.fetchone()
			if cat == "3": 
				c.execute('''SELECT pad.id, pad.note, pad.price, pad.amount, pad.data
							  FROM pad INNER JOIN
								category ON pad.cat_id = category.id where pad.cat_id = 3''')
				row = c.fetchone()
				while row is not None:
					print("id:"+str(row[0])+" Наименование: "+str(row[1]) +" | Цена: "+str(row[2]) +" | Кол-во: "+str(row[3]) +" | Дата: "+str(row[4]))
					row = c.fetchone()
			if cat == "4": 
				c.execute('''SELECT pad.id, pad.note, pad.price, pad.amount, pad.data
							  FROM pad INNER JOIN
								category ON pad.cat_id = category.id''')
				row = c.fetchone()
				while row is not None:
					print("id:"+str(row[0])+" Наименование: "+str(row[1]) +" | Цена: "+str(row[2]) +" | Кол-во: "+str(row[3]) +" | Дата: "+str(row[4]))
					row = c.fetchone()					
			if cat == "0":
				break							
	
	if name == "2":
		cat = input("Категория: ")
		note = input("Наименование: ")
		price = input("Количество: ")
		amount = input("Цена: ")
		d = datetime.today()
		data = (d.strftime('%Y-%m-%d'))
		print('\n')
		add_prod(cat, note, amount, price, data, per)

	if name == "3":
		id = input("id: ")
		del_prod(id)
		print('Ok')
		
	if name == "0":
		break
c.close()
conn.close()