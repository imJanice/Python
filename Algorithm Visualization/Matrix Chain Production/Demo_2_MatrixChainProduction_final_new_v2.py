#測試資料
#1
#['A','B','C','D','E','F']
#['4*2','2*3','3*1','1*2','2*2','2*2']
#2
#3*7,7*8,8*5,5*9,9*9,9*4,4*2,2*6

#'3*7','7*8','8*5','5*9','9*9','9*4','4*2','2*6'
#3*7,7*8,8*5,5*9,9*9,9*4,4*2,2*6

#1*2 2*3 3*4 4*5 5*6 6*7 7*8 8*9 9*10 10*10 10*5 5*1 1*4 4*7 7*15 15*7 7*11 11*12 12*13 13*14 14*15 15*16 16*17 17*18 18*19 19*20

import tkinter as tk

SegmentationPoint=[]
		
def close():
	window.destroy()
	
def start():
	
	#初始化
	allMareix=input_matrixName.get()
	matrixSize=input_matrixSize.get().split(' ')
	numOfmatrix=len(allMareix)
	#print(numOfmatrix)
	#matrix_cost save 矩陣相乘所花費的次數
	#ex A:5*6 B:6*7  AB cost 5*6*7
	matrix_cost=[[0]*numOfmatrix for i in range(numOfmatrix)] 
	#m*n為矩陣相乘後 新矩陣的大小
	#ex A:5*6 B:6*7  AB_m = 5 AB_n=7

	createCostMatrix(matrix_cost,numOfmatrix,matrixSize,allMareix)
	
def createCostMatrix(matrix_cost,numOfmatrix,matrixSize,allMareix):
	global SegmentationPoint
	SegmentationPoint=[[0]*(numOfmatrix) for i in range(numOfmatrix)]
	for i in range(1,len(matrix_cost)):
		for j in range(len(matrix_cost)-i):
			matrix_cost[j][j+i]=cost(j,j+i,matrix_cost,matrixSize)
	printOut(matrix_cost[0][numOfmatrix-1],SegmentationPoint,numOfmatrix,allMareix)
def printOut(result,SegmentationPoint,numOfmatrix,allMareix):
	printOptimalParents(0,int(numOfmatrix-1),allMareix)
	
	#print(int(numOfmatrix-1))
	text.insert('insert',"\n所需乘法次數：")
	text.insert('insert',result)
	text.insert('insert',"次\n")
	#text.insert('insert',"\n")
def printOptimalParents(i,j,allMareix):
	global SegmentationPoint
	#print(i)
	#print(j)
	#for i in range(len(s)):
	#	print(s[i])
	if i==j:
		text.insert('insert',allMareix[i])
	else:
		text.insert('insert',"(")
		printOptimalParents(i,SegmentationPoint[i][j],allMareix)
		printOptimalParents((SegmentationPoint[i][j])+1,j,allMareix)
		text.insert('insert',")")
def cost(x,y,matrix_cost,matrixSize):
	index=y
	min=2147483647
	cut=2147483647
	global SegmentationPoint
	if (y-x)==1:
		SegmentationPoint[x][y]=x
		m_1=matrixSize[x].split('*')
		m_2=matrixSize[y].split('*')
		#m_3
		return int(m_1[0])*int(m_1[1])*int(m_2[1])
	else:
		
		for i in range(y-1,x-1,-1):
			m_1=matrixSize[x].split('*')
			m_2=matrixSize[i].split('*')
			m_3=matrixSize[y].split('*')
			result=matrix_cost[x][i]+matrix_cost[index][y]+(int(m_1[0])*int(m_2[1])*int(m_3[1]))
			index=index-1
			if(result<min):
				min=result
				cut=i
		SegmentationPoint[x][y]=cut
		return min
	
			
window = tk.Tk()
window.title('Demo_Matrix_Chain_Production')
window.geometry("804x482")

label_matrixName = tk.Label(window, text="請輸入矩陣名稱:", font=("標改體",13))
label_matrixName.pack()
label_matrixName.place(x=5, y=3)

input_matrixName = tk.Entry(window)
input_matrixName.pack()
input_matrixName.place(x=165, y=6)

label_matrixSize = tk.Label(window, text="請輸入矩陣大小:", font=("標改體",13))
label_matrixSize.pack()
label_matrixSize.place(x=5, y=33)

input_matrixSize = tk.Entry(window)
input_matrixSize.pack()
input_matrixSize.place(x=165, y=36)

button_start = tk.Button(window, text="Start",command=start)
button_start.pack()
button_start.place(x=110, y=69)

button_close = tk.Button(window, text="Close", command=close)
button_close.pack()
button_close.place(x=250, y=69)

text = tk.Text(window, width=82, height=21, bg="#FFF0F5", font=("標楷體",13))
text.pack()
text.place(x=10,y=110)

tk.mainloop()


