import tkinter as tk
#用來計算
import numpy as np 
#用來上色
#from PIL import Image
import matplotlib.pyplot as plt 


def print_out_picture(Mandelbrot_Set,xmin,xmax,ymin,ymax):
	plt.imshow(Mandelbrot_Set,plt.cm.inferno,extent=(xmin,xmax,ymin,ymax)) #Julia_Set要繪製的數組 #plt.cm.magma
	cb = plt.colorbar(orientation='vertical',shrink=1)  
	cb.set_label('iteration count')
	plt.savefig('MandelbrotSet.png',dpi=300)
	plt.show()
def iterate(c0_x,c0_y,z0,t):
	run=t        #迭代次數
	z_max=10.      #z的發散值 
	pixel=[ [0 for i in range(len(c0_x))] for j in range(len(c0_y)) ]
	for i in range(len(c0_y)):          #檢查z0是否發散
		for j in range(len(c0_x)):
			c0=complex(c0_x[j],c0_y[i]) #Julia Set的z值
			z=z0*z0+c0
			for k in range(run):
				z=z*z+c0
				if abs(z) > z_max:     #發散  abs()取絕對值
					break
				pixel[i][j]=int(k*255/run)
	return pixel

def start():
	t=int(Iterate.get())
	Mandelbrot_Z=complex(0,0) #complex(2,6)=2+6j 將使用者輸入的實部和虛部表示成一個複數 Julia Set的c值
	xmax,ymax=1,1    #定義複數平面x軸的範圍
	xmin,ymin=-2,-1  #定義複數平面y軸的範圍
	step=0.005
	#準備所有要測試的初始值z0
	c_x=np.arange(xmin,xmax,step) #z0的實部    
	c_y=np.arange(ymax,ymin,-step) #z0的虛部
	picture=iterate(c_x,c_y,Mandelbrot_Z,t)
	print_out_picture(picture,xmin,xmax,ymin,ymax)
	
	
			
def close():
	window.destroy()
	

window = tk.Tk()
window.title('Demo_Julia_Set') 
window.geometry("500x530")
#建立視窗

canvas = tk.Canvas(window, width=491.5, height=460, bg='black') #491.5 460
canvas.pack()
canvas.place(x=2.4,y=60) 
#建立畫布

label1 = tk.Label(window,text="Iterate:",font=("標楷體",13))
label1.pack()
label1.place(x=3,y=4)


btn_start = tk.Button(window,text="Start",command=start)
btn_start.pack()
btn_start.place(x=110,y=31)

btn_close = tk.Button(window,text="Close",command=close)
btn_close.pack()
btn_close.place(x=330,y=31)

Iterate = tk.Entry(window)
Iterate.pack()
Iterate.place(x=83,y=7)


tk.mainloop()