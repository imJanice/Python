import tkinter as tk
import numpy as np


def new_dot(a_x,a_y,b_x,b_y,head):
	#新正三角形底邊長
	length = (((a_x-b_x)**2+(a_y-b_y)**2)**0.5)/6
	global new
	old=x_y[head][2]
	x_y[head][2]=new       #端點指向的點改變
	for i in range(3):
		if i == 1:
			#尋找垂直於ab的向量
			#判斷向量是否正確 
			x=[vector_x,vector_y]
			y=[-vector_y,vector_x]
			z=np.cross(x, y)
			if z > 0:
				tmp=vector_x
				vector_x=-vector_y
				vector_y=tmp
			else:
				tmp=vector_x
				vector_x=vector_y
				vector_y=-tmp
			#尋找垂直於ab的單位向量
			v=float((vector_x**2+vector_y**2)**0.5)
			vector_x=float(vector_x/v)
			vector_y=float(vector_y/v)
			#求ab中點
			mid_x=a_x+(b_x-a_x)/2
			mid_y=a_y+(b_y-a_y)/2
			#求新點
			c=length*3**0.5   #l代表底的長度
			#print(new)
			x_y[new][0]=mid_x+(vector_x*c)
			x_y[new][1]=mid_y+(vector_y*c)
			x_y[new][2]=new+1
			new=new+1
		elif i == 2:
			vector_x=b_x-a_x
			vector_y=b_y-a_y
			x_y[new][0]=a_x+(vector_x/3*2)
			x_y[new][1]=a_y+(vector_y/3*2)
			x_y[new][2]=old
			new=new+1
		else:
			vector_x=b_x-a_x
			vector_y=b_y-a_y
			x_y[new][0]=a_x+(vector_x/3)
			x_y[new][1]=a_y+(vector_y/3)
			x_y[new][2]=new+1
			new=new+1

def search():
	Iteration = int(input1.get())
	run_time=3    #三個邊 每個邊劃出新的三個點
	if Iteration != 0:
		next = 0
		head=0
		for i in range(Iteration):
			for i in range(run_time):
				#傳相鄰兩點去尋找新的三個點
				new_dot(x_y[next][0],x_y[next][1],x_y[x_y[next][2]][0],x_y[x_y[next][2]][1],head) 
				next = int(x_y[new-1][2])
				head = int(x_y[new-1][2])
			#計算第n次迭代時有幾個邊
			run_time=run_time+run_time*3
	draw()

def draw():
	next=0
	while(1):
		line=canvas.create_line(x_y[next][0],x_y[next][1],x_y[x_y[next][2]][0],x_y[x_y[next][2]][1])
		next = x_y[next][2]
		if next == 0:
			break
	
def close():
	window.destroy()
def clean():
	canvas.delete("all")
	#定義初始三個點
	#點a
	x_y[0][0]=86.   #座標x
	x_y[0][1]=459.   #座標y
	x_y[0][2]=1     #下一點的位置
	#點b
	x_y[1][0]=614.   #座標x
	x_y[1][1]=459.   #座標y	
	x_y[1][2]=2     #下一點的位置
	helf=(x_y[1][0]-x_y[0][0])/2
	x_y[2][0]=(x_y[1][0]-x_y[0][0])/2+x_y[0][0]
	x_y[2][1]=x_y[0][1]-helf*3**0.5
	x_y[2][2]=0
	new=3
	
	

x_y=[[0 for i in range(3)]for j in range(100000)] #儲存x,y(座標)和下一個點的位置
#定義初始三個點
#點a
x_y[0][0]=86.   #座標x
x_y[0][1]=459.   #座標y
x_y[0][2]=1     #下一點的位置
#點b
x_y[1][0]=612.   #座標x
x_y[1][1]=459.   #座標y	
x_y[1][2]=2     #下一點的位置
helf=(x_y[1][0]-x_y[0][0])/2
x_y[2][0]=(x_y[1][0]-x_y[0][0])/2+x_y[0][0]
x_y[2][1]=x_y[0][1]-helf*3**0.5
x_y[2][2]=0
global new  #新增第幾個點
new=3
#create window
window = tk.Tk()
window.title('Demo_Koch_Snowflake')
window.geometry("700x650")

#create label
label1 =  tk.Label(window,text="迭代次數:",font=("標楷體",13))
label1.pack()
label1.place(x=3,y=4)

#create netry
input1 = tk.Entry(window)
input1.pack()
input1.place(x=90,y=7)

#create button
btn_start = tk.Button(window,text="Start",command=search)
btn_start.pack()
btn_start.place(x=350,y=4)

btn_close = tk.Button(window,text="Clean",command=clean)
btn_close.pack()
btn_close.place(x=450,y=4)

btn_clean = tk.Button(window,text="Close",command=close)
btn_clean.pack()
btn_clean.place(x=550,y=4)


#create canvas
canvas = tk.Canvas(window,width=691, height=613, bg='pink')
canvas.pack()
canvas.place(x=2.4,y=30)

tk.mainloop()
