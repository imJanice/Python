import tkinter as tk
def Sort(list,input):
	for i in range(len(list)):
		for j in range(len(list)-1):
			if list[j]>list[j+1]:
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp
				tmp=input[j]
				input[j]=input[j+1]
				input[j+1]=tmp
	return input
			
def printout(list):
	print(list)
	num=0
	for i in range(len(list)):
		number=1
		if list[num]==list[num+1]:
			number=number+1
			num=num+2
			text.insert('insert',number)
			text.insert('insert',"個："+"")
			text.insert('insert',list[num-1])
			text.insert('insert',"\n")
			
			print(number,end=" ")
			print("個：",end=" ")
			print(list[i])
			#i=i+1
		else:
			text.insert('insert',"1個："+"")
			text.insert('insert',list[num])
			text.insert('insert',"\n")
			num=num+1
			print("1個：",end=" ")
			print(list[num])
			
def turntonum(list):
	#十進位轉二進位
	#並卻保二進位有八個位數
	zero='{0:b}'.format(0)  #十進位轉二進位
	color=['黑','棕','紅','橙','黃','綠','藍','紫','灰','白']
	array=[0 for i in range(len(list))] #存放二進位
	for i in range(len(list)):
		for j in range(3):
			for k in range(len(color)):
				if j==0:
					if list[i][j]==color[k]:
						array[i] = k*10
				elif j==1:
					if list[i][j]==color[k]:
						array[i]=array[i]+k
				else:
					if list[i][j]==color[k]:
						num=10**k
						array[i]=array[i]*num
	#print(array)
	return array
def start():
	number=input1.get().split(" ") #split(",")以，為刀子將字串分割放進list中
	number=['棕紅黃','藍黃紅','橙黑棕','白藍藍','藍黃紅','藍綠綠','灰黑黑','黃黑棕','棕黑紅','藍綠綠']
	newlist=turntonum(number)
	output=Sort(newlist,number)
	printout(output)
	#print(output)
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