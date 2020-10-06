#蒐集所有經由z=z0*z0+c迭代一定次數後還不會發散的點，這些點所形成的集合就是Julia Sets

import tkinter as tk
#用來計算
import numpy as np 
#用來上色
#from PIL import Image
import matplotlib.pyplot as plt 


def print_out_picture(Julia_Set,xmin,xmax,ymin,ymax):
	plt.imshow(Julia_Set,plt.cm.magma,extent=(xmin,xmax,ymin,ymax)) #Julia_Set要繪製的數組 #plt.cm.magma
	cb = plt.colorbar(orientation='vertical',shrink=1)  
	cb.set_label('iteration count')
	plt.savefig('JuliaSet.png',dpi=300)
	plt.show()
def iterate(z0_x,z0_y,c):
	run=300        #迭代次數
	z_max=10.      #z的發散值 
	pixel=[ [0 for i in range(len(z0_x))] for j in range(len(z0_y)) ]
	for i in range(len(z0_y)):          #檢查z0是否發散
		for j in range(len(z0_x)):
			z0=complex(z0_x[j],z0_y[i]) #Julia Set的z值
			z=z0*z0+c
			diverge=0
			for k in range(run):
				z=z*z+c
				if abs(z) > z_max:     #發散  abs()取絕對值
					break
				pixel[i][j]=int(k*255/run)
	return pixel

def start():
	real=float(input_real.get())
	c_plex=float(input_complex.get())
	
	Julia_C=complex(real,c_plex) #complex(2,6)=2+6j 將使用者輸入的實部和虛部表示成一個複數 Julia Set的c值
	xmax,ymax=2,2    #定義複數平面x軸的範圍
	xmin,ymin=-2,-2  #定義複數平面y軸的範圍
	step=0.005
	#準備所有要測試的初始值z0
	z_x=np.arange(xmin,xmax,step) #z0的實部    
	z_y=np.arange(ymax,ymin,-step) #z0的虛部
	picture=iterate(z_x,z_y,Julia_C)
	print_out_picture(picture,xmin,xmax,ymin,ymax)
	
	
			
def close():
	window.destroy()
	

window = tk.Tk()
window.title('Demo_Julia_Set') 
window.geometry("500x530")
#建立視窗

canvas = tk.Canvas(window, width=491.5, height=460, bg='black')
canvas.pack()
canvas.place(x=2.4,y=60)
#建立畫布

label1 = tk.Label(window,text="實部:",font=("標楷體",13))
label1.pack()
label1.place(x=3,y=4)

label2 = tk.Label(window,text="虛部:",font=("標楷體",13))
label2.pack()
label2.place(x=200,y=4)

btn_start = tk.Button(window,text="Start",command=start)
btn_start.pack()
btn_start.place(x=110,y=31)

btn_close = tk.Button(window,text="Close",command=close)
btn_close.pack()
btn_close.place(x=330,y=31)

input_real = tk.Entry(window)
input_real.pack()
input_real.place(x=53,y=7)

input_complex = tk.Entry(window)
input_complex.pack()
input_complex.place(x=250,y=7)

tk.mainloop()

