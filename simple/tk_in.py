from math import *
from tkinter import *
import random

# f = input('f(x):')

root = Tk()

canv = Canvas(root, width = 500, height = 500, bg = "white")

for i in range(50):
	canv.create_line(0,i*10,500,i*10,width=1)
	canv.create_line(i*10,0,i*10,500,width=1)
	canv.create_text(5,i*10+5, text = str(50-i), fill="purple", font=("Helvectica", "5"))  

# canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
# canv.create_line(0,500,1000,500,width=2,arrow=LAST) 
x = 2

f = open('D:\python\data.csv','r')

count = 0

costs = []
for line in f:
	elements = line.split(';')
	el = elements[3].replace('.','')
	if el.isdigit():
		costs.append(float(elements[3]))

print(costs)
print(max(costs))
costs50 = []
for el in costs:
	costs50.append(int(el/168000*50))
print(costs50)

First_x = -500

prices = []
for i in range(50):
	prices.append(random.randint(1, 50))

for i in range(len(costs50)):
	print(f"{i} {costs50[i]}")
	canv.create_oval(i*10, 500-costs50[i]*10, i*10+10, 500-costs50[i]*10+10, fill = 'black')
	# canv.create_oval(x, y, x + 1, y + 1, fill = 'black')
	 
canv.pack()	
root.mainloop()