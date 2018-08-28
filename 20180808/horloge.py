import threading
import time
import Tkinter as Tk
import math

class MyTimer:
    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)
        
    def start(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()

class Horloge(MyTimer, Tk.Canvas):
    def __init__(self, parent):
        MyTimer.__init__(self, 1.0, self.turn)
        Tk.Canvas.__init__(self, parent, width=200, height=200)

# Creation du cadre de l'horloge
#        self.create_oval(10,10,190,190, width = 3)
# Creation des tirets minute        
#        for i in range(60):
#            self.create_line(100 + math.cos(i*math.pi/30-math.pi/2)*(80+(i%5 != 0)*5), 100 + math.sin(i*math.pi/30-math.pi/2)*(80+(i%5 != 0)*5), 100 + math.cos(i*math.pi/30-math.pi/2)*90, 100 + math.sin(i*math.pi/30-math.pi/2)*90, width = 2)

# Creation des aiguilles
#        self._second = self.create_line(0, 0, 0, 0, fill = "red")
#        self._minute = self.create_line(0, 0, 0, 0, width = 2, fill = "blue")
#        self._hour = self.create_line(0, 0, 0, 0, width = 3, fill = "green")
 
    def turn(self):
        gmtime = datetime.now().time()
#        self.coords(self._hour, 100, 100, 100 + math.cos(gmtime[3]*math.pi/12+gmtime[4]*math.pi/360-math.pi/2)*45, 100 + math.sin(gmtime[3]*math.pi/12+gmtime[4]*math.pi/360-math.pi/2)*45)
#        self.coords(self._minute, 100, 100, 100 + math.cos(gmtime[4]*math.pi/30+gmtime[5]*math.pi/1800-math.pi/2)*70, 100 + math.sin(gmtime[4]*math.pi/30+gmtime[5]*math.pi/1800-math.pi/2)*70),
#        self.coords(self._second, 100, 100, 100 + math.cos(gmtime[5]*math.pi/30-math.pi/2)*85,  100 + math.sin(gmtime[5]*math.pi/30-math.pi/2)*85)        
        self.
        self.update() 
 
root = Tk.Tk()
root.title('Horloge')
h = Horloge(root)
h.pack()
btn = Tk.Button(root, text = 'Demarrer', command = h.start)
btn.pack()
root.mainloop()