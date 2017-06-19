import serial
import time
import MySQLdb as mdb

arduino = serial.Serial('/dev/ttyUSB0')
arduino.baudrate=9600

data = arduino.readline()
time.sleep(1)
data = arduino.readline()
stukjes = data.split('\t')

temperatuur = stukjes[0]
luchtvochtigheid = stukjes[1]
regen = stukjes[2]

con = mdb.connect('localhost','root','Bjarne1021','project');

with con:

    cursor = con.cursor()
    cursor.execute('''INSERT INTO project_db VALUES ('',%s,%s,%s)''',(float (temperatuur),float(luchtvochtigheid),float(regen)))
    con.commit()
    cursor.close()


