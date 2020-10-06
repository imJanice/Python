#A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
#10,9,8,7,6,5,20,28,11,45,65,23,45,6,7,8,9,1,2,3,4,5,6,7,8,9


#['B','K','M','N','P','Q','S','T','V','X','Z']
#[7,777,500,734,1314,1,1019,328,666,999,3]
import tkinter as tk
from tkinter import *

def close():
	window.destroy()
	
def start():

	global arrayOnlyName
	global arrayOnlyFre
	global dotNmae
	global dotFrequency
	
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
	canvas.pack(padx=0,pady=100,side=LEFT,expand=True,fill=BOTH)
	
	#初始化
	start=['empty']
	dotNmae=input_dotName.get().split(',')#['A','C','D','I','M','N','Y']#input_dotName.get()
	dotFrequency=input_dotFrequency.get().split(',')#[4,2,1,3,5,2,1]#input_dotFrequency.get().split(',')
	#讓dotNmae、dotFrequency皆從index 1開始
	onlyDotName=dotNmae
	dotNmae=start+dotNmae
	dotFrequency=start+dotFrequency
	indexNum=len(dotNmae)
	#print(dotFrequency)
	#最終要印出來的陣列 儲存string
	arrayNameAndFre=[['empty']*(indexNum)for i in range(indexNum)]
	#方便計算的陣列
	arrayOnlyName=[['empty']*(indexNum)for i in range(indexNum)]
	arrayOnlyFre=[[0]*(indexNum)for i in range(indexNum)]
	#print(arrayNameAndFre)
	#print(arrayOnlyName)
	#print(arrayOnlyFre)
	def cost(i,j):
		def allFrequency(i,j):
			global dotFrequency
			total=0
			for k in range(i,j+1):
				total=total+int(dotFrequency[k])
			return int(total)
		global arrayOnlyName
		global arrayOnlyFre
		global dotNmae
		global dotFrequency
		min=2147483647
		if i==j:
			arrayOnlyFre[i][j]=0
			return 'empty'
		elif (j-i)==1:
			arrayOnlyName[i][j]=dotNmae[j]
			arrayOnlyFre[i][j]=dotFrequency[j]
			return str(dotFrequency[j])+dotNmae[j]
		else:
			#k代表誰來當root
			for k in range(i,j):
				result=int(arrayOnlyFre[i][k])+int(arrayOnlyFre[k+1][j])+allFrequency(i+1,j)
				if result<min:
					min=result
					root=dotNmae[k+1]
			arrayOnlyName[i][j]=root
			arrayOnlyFre[i][j]=min
			return str(min)+root
		
		#arrayNameAndFre是要印出來的矩陣
	for i in range(indexNum):
		for j in range(indexNum-i):
			arrayNameAndFre[j][j+i]=cost(j,j+i)
	def printOutArrayWithBlog(arrayNameAndFre,dotNmae):
		#for i in range(len(arrayNameAndFre)):
		#	print(arrayNameAndFre[i])
		#	print("\n")
		#每一行格子的起始點
		start_x=50
		start_y=50
		#長方形的常跟寬
		r_length=90
		r_width=30
		#印長方形的四個參數值
		#r_x1=start_x
		#r_y1=start_y
		#r_x2=start_x+r_length
		#r_y2=start_y+r_width
		#格子個行數
		TableNum=len(arrayNameAndFre)-1
		
		#印出表格左邊的名稱
		dot_x=start_x-20
		dot_y=start_y
		for i in range(1,len(dotNmae)):
			canvas.create_text(dot_x,dot_y+6,text=dotNmae[i],anchor='nw',font=("標改體",13))
			dot_y=dot_y+r_width
		#印出表格上方的點的名稱
		dot_x=start_x
		dot_y=start_y-20
		for i in range(1,len(dotNmae)):
			canvas.create_text(dot_x+40,dot_y,text=dotNmae[i],anchor='nw',font=("標改體",13))
			dot_x=dot_x+r_length
		
		#印出表格
		track_blog_y=start_y
		for i in range(TableNum):
			r_x1=start_x
			r_y1=track_blog_y
			r_x2=start_x+r_length
			r_y2=track_blog_y+r_width
			for j in range(TableNum):
				canvas.create_rectangle(r_x1,r_y1,r_x2,r_y2)
				r_x1=r_x1+r_length
				r_x2=r_x1+r_length
			track_blog_y=track_blog_y+r_width

		deep=r_y2
		
		#印出文字
		text_x=start_x
		text_y=start_y
		track_text_y=start_y
		
		#canvas.create_text(50,50,text=arrayNameAndFre[0][1],anchor='nw',font=("標改體",13))
		for i in range(0,len(arrayNameAndFre)-1):   #x
			text_x=start_x
			text_y=track_text_y
			for j in range(1,len(arrayNameAndFre)): #y
				if arrayNameAndFre[i][j]=='empty':
					text_x=text_x+r_length
				else:
					toRight=32-(len(arrayNameAndFre[i][j])-3)*2.6
					canvas.create_text(text_x+toRight,text_y+5.5,text=arrayNameAndFre[i][j],anchor='nw',font=("標改體",13))
					text_x=text_x+r_length
			track_text_y=track_text_y+r_width
		return deep
	
	#def drawLine()
	def drawLine(current_x,next_x,next_y):
		canvas.create_line(current_x+25, next_y-50, next_x+25, next_y)
		
	def drawCircle(circle_x,circle_y,printWord):
		circle_diameter=50
		canvas.create_oval(circle_x, circle_y, circle_x+circle_diameter, circle_y+circle_diameter)
		canvas.create_text(circle_x+20,circle_y+18,text=printWord,anchor='nw',font=("標改體",13))
	
	#回傳繪製表格的最後深度
	currentDeep=printOutArrayWithBlog(arrayNameAndFre,dotNmae)
	
	
	def claculateCircle_x_forL_LandR_R(currecntCircle_x,last_x):
		newCircle_x=currecntCircle_x+((currecntCircle_x-last_x)/2)
		return newCircle_x
	def claculateCircle_x_forL_RandR_L(currecntCircle_x,last_x):
		newCircle_x=currecntCircle_x-((currecntCircle_x-last_x)/2)
		return newCircle_x
	def claculateCircle_y(currecntCircle_y):
		deep=100
		newCircle_y=currecntCircle_y+deep
		return newCircle_y
		
	def prepareToStart(arrayOnlyName,onlyDotName,currentDeep):
		#只要找的到點就畫
		#全部有10node
		#判斷root是第幾個note
		#假設是第4個
		#接著搜尋[0~(4-1)]和[(4+1)~9]尋找新root
		#資料重新初始化
		allRoot=[[0]*(len(arrayOnlyName)-1)for i in range(len(arrayOnlyName)-1)]
		for i in range(len(arrayOnlyName)-1):
			for j in range(1,len(arrayOnlyName)):
				allRoot[i][j-1]=arrayOnlyName[i][j]
			#print(allRoot[i])
		#print(len(allRoot))
		#print(onlyDotName)
		#root是要印出來的字
		root=arrayOnlyName[0][len(allRoot)-1]
		for i in range(len(onlyDotName)):
			if onlyDotName[i]==root:
				rootNum=i
				break
		#定義root circle x and root circle y
		circle_x=800
		last_x=circle_x
		#circle_y必須在表格之下
		circle_y=currentDeep+100
		drawCircle(circle_x,circle_y,root)
		newLeft_x=circle_x-(circle_x/2)
		newRight_x=circle_x+(circle_x/2)
		new_y=claculateCircle_y(circle_y)
		
		
		
		#往右
		def searchRight(index_i,index_j,array,dotName,c_x,c_y,last_x):
			#find root
			newRoot=array[index_i][index_j]
			#find root name
			for i in range(len(dotName)):
				if dotName[i]==newRoot:
					rootNum=i
					break
					
			drawCircle(c_x,c_y,newRoot)
					
			print(c_x,end=' ')
			print(c_y,end=' ')
			print(newRoot)
			
			#往左
			if index_i<=(rootNum-1):
				newLeft_x=claculateCircle_x_forL_RandR_L(c_x,last_x)
				last_x_next=c_x
				new_y=claculateCircle_y(c_y)
				drawLine(last_x_next,newLeft_x,new_y)
				searchLeft(index_i,rootNum-1,array,dotName,newLeft_x,new_y,last_x_next)
			#往右
			if (rootNum+1)<=index_j:
				newRight_x=claculateCircle_x_forL_LandR_R(c_x,last_x)
				last_x_next=c_x
				new_y=claculateCircle_y(c_y)
				drawLine(last_x_next,newRight_x,new_y)
				searchRight(rootNum+1,index_j,array,dotName,newRight_x,new_y,last_x_next)
		#往左
		def searchLeft(index_i,index_j,array,dotName,c_x,c_y,last_x):
			#find root
			newRoot=array[index_i][index_j]
			#find root name
			for i in range(len(dotName)):
				if dotName[i]==newRoot:
					rootNum=i
					break
					
			drawCircle(c_x,c_y,newRoot)
			
			print(c_x,end=' ')
			print(c_y,end=' ')
			print(newRoot)
			
			#往左
			if index_i<=(rootNum-1):
				newLeft_x=claculateCircle_x_forL_LandR_R(c_x,last_x)
				last_x_next=c_x
				new_y=claculateCircle_y(c_y)
				drawLine(last_x_next,newLeft_x,new_y)
				searchLeft(index_i,rootNum-1,array,dotName,newLeft_x,new_y,last_x_next)
			#往右
			if (rootNum+1)<=index_j:
				newRight_x=claculateCircle_x_forL_RandR_L(c_x,last_x)
				last_x_next=c_x
				new_y=claculateCircle_y(c_y)
				drawLine(last_x_next,newRight_x,new_y)
				searchRight(rootNum+1,index_j,array,dotName,newRight_x,new_y,last_x_next)
				
				#drawLine(circle_x,newLeft_x,new_y)
				#drawLine(circle_x,newRight_x,new_y)
		#往左尋找子樹
		if 0<=rootNum-1:
			drawLine(circle_x,newLeft_x,new_y)
			searchLeft(0,rootNum-1,allRoot,onlyDotName,newLeft_x,new_y,last_x)
		#往右尋找子樹
		if rootNum+1<=len(onlyDotName)-1:
			drawLine(circle_x,newRight_x,new_y)
			searchRight(rootNum+1,len(onlyDotName)-1,allRoot,onlyDotName,newRight_x,new_y,last_x)
		#print(rootNum)
	prepareToStart(arrayOnlyName,onlyDotName,currentDeep)
	#drawTree()
	





	

		

	






window = tk.Tk()
window.title('Demo_Optimal_Binary_Search_Tree')
window.geometry("1250x800")

label_matrixName = tk.Label(window, text="請輸入點的名稱:", font=("標改體",13))
label_matrixName.pack()
label_matrixName.place(x=5, y=3)

input_dotName = tk.Entry(window)
input_dotName.pack()
input_dotName.place(x=165, y=6)

label_matrixSize = tk.Label(window, text="請輸入點的頻率:", font=("標改體",13))
label_matrixSize.pack()
label_matrixSize.place(x=5, y=33)

input_dotFrequency = tk.Entry(window)
input_dotFrequency.pack()
input_dotFrequency.place(x=165, y=36)

button_start = tk.Button(window, text="Start",command=start)
button_start.pack()
button_start.place(x=110, y=69)

button_close = tk.Button(window, text="Close", command=close)
button_close.pack()
button_close.place(x=250, y=69)



tk.mainloop()