from Tkinter import *
import sys
import subprocess

width="1366"
height="768"
try:
    var=sys.argv[1]
    ventana = Tk()
    ventana.configure(bg='#a3d2a6')
    ventana.geometry(width+"x"+height)
    img = PhotoImage(file=var)
    widget = Label(ventana, image=img ,anchor="center").pack()
    ventana.mainloop() 
 
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
