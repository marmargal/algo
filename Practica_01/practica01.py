'''
Created on 13 oct. 2017

@author: inmam
'''

#!/usr/bin/python

import Tkinter
import tkMessageBox
import urllib, urllib2
import sqlite3


top = Tkinter.Tk()
# Code to add widgets will go here...

def createDB():
    conn = sqlite3.connect('noticias01.db')
    print ("Opened database successfully")
    conn.execute('''CREATE TABLE NOTICIAS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         LINK            TEXT     NOT NULL,
         FECHA        TEXT    NOT NULL);''')
    print ("Table created successfully")

def db():
   
    conn = sqlite3.connect('noticias01.db')    
    cursor = conn.execute("SELECT id, name, link, fecha from NOTICIAS")
    
    conn.execute("INSERT INTO NOTICIAS (ID,NAME,LINK,FECHA) \
      VALUES (1, 'Paul', 'ASDFG', '12/10/17')")
    
    
    for row in cursor:
        print ("ID = ", row[0])
        print "NAME = ", row[1]
        print "LINK = ", row[2]
        print "FECHA = ", row[3], "\n"
    
    print "Operation done successfully";
    
    conn.commit()
    conn.close()


def Almacenar():
    #nombres, link y fecha de todas las noticias (http://www.us.es/rss/feed/portada)
    #title, link y pubDate
    try:
        f1 = urllib2.urlopen("http://www.us.es/rss/feed/portada")
        print f1.read()
        f1.close()
        
        #params = urllib
        
        tkMessageBox.showinfo( "Mensaje", "BD creada correctamente")
        
    except urllib2.HTTPError, e:
        print "Ocurrio un error"
        print e.code
    except urllib2.URLError, e:
        print "Ocurrio un error"
        print e.code
    




def Listar():
    tkMessageBox.showinfo("listar", "listar")

def Buscar():
    tkMessageBox.showinfo("buscar", "buscar")


    

A = Tkinter.Button(top, text ="Almacenar", command = Almacenar)
L = Tkinter.Button(top, text ="Listar", command = Listar)
B = Tkinter.Button(top, text ="Buscar", command = Buscar)

A.pack()
L.pack()
B.pack()

top.mainloop()