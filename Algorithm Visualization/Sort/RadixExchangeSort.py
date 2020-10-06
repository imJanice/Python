#橙橙橙 紅紅紅 棕棕棕 黑黑黑 棕棕棕 紅紅紅 橙橙橙
import tkinter as tk
def RadixSort(list,input):
	zero='{0:b}'.format(0)
	array=[0 for i in range(16)] #存放0-16二進位
	for i in range(16):
		array[i]='{0:b}'.format(i)
		while len(array[i]) < 4:
			array[i]=zero+array[i]
		#print(array[i])
	for i in range(4):
		for j in range(16):
			for k in range(len(list)):
				if i==0:
					if array[j]==list[k][0:4]:
						print(input[k],end=" ")
				
				#elif i==1:
					
			
				
def Binarary(list):
	#十進位轉二進位
	#並卻保二進位有八個位數
	zero='{0:b}'.format(0)  #十進位轉二進位
	color=['黑','棕','紅','橙','黃','綠','藍','紫','灰','白']
	array=[0 for i in range(len(list))] #存放二進位
	for i in range(len(list)):
		for j in range(3):
			for k in range(len(color)):
				if list[i][j]==color[k]:
					if j!=2:
						if k==0:
							if j==0:
								array[i]=zero
							else:
								array[i]=array[i]+zero
						else:
							if j==0:
								array[i]=str(k)
							else:
								array[i]=array[i]+str(k)
					else:
						if k<8:
							for r in range(k):
								array[i]=array[i]+zero
						
	for i in range(len(array)):
		array[i]='{0:b}'.format(int(array[i]))
		while len(array[i]) < 16:
			array[i]=zero+array[i]
		text.insert('insert',list[i]+"")
		text.insert('insert',array[i])
		text.insert('insert',"\n")
		print(list[i],end=" ")
		print(array[i])
	return array
def start():
	number=input1.get().split(" ") #split(",")以，為刀子將字串分割放進list中
	#number=['橙橙橙','紅紅紅','棕棕棕','黑黑黑','棕棕棕','紅紅紅','橙橙橙']
	newlist=Binarary(number)
	RadixSort(newlist,number)
def close():
	window.destroy()
window = tk.Tk()
window.title('Demo_Radix_Sort')
window.geometry("404x432")

label1 = tk.Label(window, text="請輸入一組數字:", font=("標楷體",13))
label1.pack()
label1.place(x=5, y=3)

input1 = tk.Entry(window)
input1.pack()
input1.place(x=165, y=6)

button1 = tk.Button(window, text="Start",command=start)
button1.pack() 
button1.place(x=110, y=29)

btn_close = tk.Button(window,text="Close",command=close)
btn_close.pack()
btn_close.place(x=250,y=29)

text = tk.Text(window,width=42,height=21, bg="#FFF0F5", font=("標楷體",13))
text.pack()
text.place(x=10,y=60)

tk.mainloop()