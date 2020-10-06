#test
#A B 7,B C 10
#A

#A C 10,A E 30,A F 100,B C 5,C D 50,D F 10,E F 60,E D 20
#A

import tkinter as tk
from tkinter import *
import random

window = tk.Tk()
window.title('Demo_2_Dijkstra’s Algorithm')
window.geometry("1500x600")

r_x1=10
r_y1=40
#用來控制換行
old_r_x1=r_x1
old_r_y1=r_y1
r_x2=r_x1+120
r_y2=r_y1+30
consider_x=10
consider_y=20
text_x=0
text_y=r_y1+5



def btnClick():
	def findDotNum(dd,dot):
	#print(dd)
	#print(dot)
		for i in range(len(dot)):
			if(dd==dot[i]):
				return i
				
	def printTextTable(considerStr,item_print):
		
		count=0
		totalCount=0
		changeLine=30
		r_num=len(item_print)
		global consider_x
		global consider_y
		#印長方形的四個參數(左上角座標+右下角座標)
		global r_x1
		global r_y1
		global r_x2
		global r_y2
		#印文字的座標(用於僅考慮那一行)
		global text_x
		global text_y
		#結束一次印表格後要設定好下次印表格的起始點
		global old_r_x1
		global old_r_y1
		
		r_length=120
		r_width=30
		text_x=r_x1+35
		
		considerStr="Including"+considerStr
		
		canvas.create_text(consider_x,consider_y,text=considerStr,anchor='nw',font=("標改體",13))
		for i in range(r_num):
			canvas.create_rectangle(r_x1,r_y1,r_x2,r_y2)
			canvas.create_text(text_x,text_y,text=path[i],anchor='nw',font=("標改體",13))
			#canvas.pack()
			r_x1=r_x2
			r_x2=r_x1+r_length
			r_y2=r_y1+r_width
			text_x=r_x1+11
			
			text_y=r_y1+5
			count=count+1
			totalCount=totalCount+1
			if (count>9) and (totalCount!=r_num):
				#canvas.create_rectangle(10,40,100,100)
				r_x1=old_r_x1
				r_y1=old_r_y1+changeLine
				old_r_y1=old_r_y1+changeLine
				r_x2=r_x1+r_length
				r_y2=r_y1+30
				
				text_x=r_x1+35
				
				count=0
		consider_y=r_y2
		#印一輪表格結束後 要把起點重新歸零
		r_x1=old_r_x1
		r_y1=old_r_y1+changeLine*2
		old_r_y1=old_r_y1+changeLine*2
		r_x2=r_x1+r_length
		r_y2=r_y1+30
		text_x=r_x1+20
		text_y=r_y1+5
		consider_y=consider_y+10
		if considerStr==6:
			canvas.pack()
	#Canvas and Scrollbar
	
	canvas=tk.Canvas(window,width=10000,height=20000,bg="#FFF0F5",scrollregion=(0,0,10000,20000))
	
	#canvas=tk.Canvas(window,bg='#FFB6C1',width=10000,height=10000,scrollregion=(0,0,10000,10000))
	vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
	vbar.place(x = 1270,width=10,height=525)
	vbar.configure(command=canvas.yview)
	hbar=Scrollbar(canvas,orient=HORIZONTAL)#水平滚动条
	hbar.place(y=0,width=1280,height=10)
	hbar.configure(command=canvas.xview)
	canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set)
	canvas.pack(padx=0,pady=120,side=LEFT,expand=True,fill=BOTH)
	
	dot=[]
	
	
	start=startP.get()
	pathAndW=input1.get().split(",") #split("，")以，為刀子將字串分割放進list中
	#pathAndW=pathAndW.split(",")
	
	data=[['0']*(3)for i in range(len(pathAndW))]
	for i in range(len(pathAndW)):
		data[i]=pathAndW[i].split(" ")
		i_in=0
		j_in=0
		for j in range(len(dot)):
			if(dot[j]==data[i][0]):
				i_in=1
			if(dot[j]==data[i][1]):
				j_in=1
		if(i_in==0):
			dot.append(data[i][0])
		if(j_in==0):
			dot.append(data[i][1])
			
	for i in range(len(dot)):
		for j in range(len(dot)-1):
			if(dot[j]>dot[j+1]):
				tmp=dot[j]
				dot[j]=dot[j+1]
				dot[j+1]=tmp
	
	#print(dot)  
	
	path=[]
	
	for i in range(len(dot)):
		path.append(1000)
		
	path[0]=0
		
		
	for i in range(len(data)):
		if(data[i][0]==start):
			for j in range(len(dot)):
				if(data[i][1]==dot[j]):
					path[j]=int(data[i][2])
	#print(path)
	
	notDone=[]
	for i in range(len(dot)):
		notDone.append(i)
	
	
	
	for i in range(0,len(dot)):
		#find short
		short=notDone[0]
		popN=0
		for j in range(len(notDone)):
			if(path[short]>path[notDone[j]]): 
				short=notDone[j]
				popN=j
		
		print(dot[short])		
		notDone.pop(popN)
		print(notDone)
		#short=findDotNum(data[j][1],dot)
		
		for j in range(len(data)):
			if(dot[short]==data[j][0]):
				dotN=findDotNum(data[j][1],dot)
				dot_path=int(data[j][2])
				
				if(path[short]+dot_path<path[dotN]):
					path[dotN]=path[short]+dot_path
					#print("in")
				
		for j in range(len(data)):
			if(dot[short]==data[j][1]):
				dotN=findDotNum(data[j][0],dot)
				dot_path=int(data[j][2])
				
				if(path[short]+dot_path<path[dotN]):
					path[dotN]=path[short]+int(dot_path)
					#print("in")
		
		printTextTable(dot[short],path)		
		print(path)
		

				
				

	
		
		
			
		
	
		
	
	
			
def close():
	window.destroy()
	
label1 = tk.Label(window, text="請輸入一組node:", font=("標楷體",13))
label1.pack()
label1.place(x=5, y=3)

input1 = tk.Entry(window)
input1.pack()
input1.place(x=165, y=6)

startP = tk.Entry(window)
startP.pack()
startP.place(x=400, y=6)

button1 = tk.Button(window, text="Start",command=btnClick)
button1.pack() 
button1.place(x=110, y=29)

btn_close = tk.Button(window,text="Close",command=close)
btn_close.pack()
btn_close.place(x=250,y=29)

tk.mainloop()