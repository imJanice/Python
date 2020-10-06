#測試資料
#1
#600
#紅燒牛肉,滑蛋牛肉,烤牛排,鄉村炸牛排,味噌牛肉捲
#2
#1200
#泡菜牛肉,鄉村炸牛排,骰子牛肉,炸牛肉丸,咖喱牛筋,黑胡椒牛肚

#泡菜牛肉,鄉村炸牛排,骰子牛肉,炸牛肉丸,咖喱牛筋,黑胡椒牛肚

#紅燒牛肉,紅酒燉牛肉,泡菜牛肉,牛肉麵,香煎牛小排,滷牛腱,青椒炒牛肉,滑蛋牛肉,頂級和牛,牛肉包,清蒸牛肉,清燉牛肉湯,辣炒牛肉,牛肉乾,烤牛排,蠔油牛肉甘藍,牛肉飯,麻辣牛腩鍋,胡椒牛柳,牛肉炒麵,蔥爆牛肉,鄉村炸牛排,骰子牛肉,炸牛肉丸,咖喱牛筋,黑胡椒牛肚,牛肉烏龍麵,牛肉餡餅,牛肋條,味噌牛肉捲
#蔥爆29
#牛肉包4個
#9354
#紅燒牛肉,紅酒燉牛肉,泡菜牛肉,牛肉麵,香煎牛小排,滷牛腱,滑蛋牛肉,清蒸牛肉,清燉牛肉湯,辣炒牛肉,牛肉乾,烤牛排,蠔油牛肉甘藍,牛肉飯,麻辣牛腩鍋,胡椒牛柳,牛肉炒麵,鄉村炸牛排,骰子牛肉,炸牛肉丸,咖喱牛筋,黑胡椒牛肚,牛肉烏龍麵,牛肉餡餅,牛肋條,味噌牛肉捲

#紅燒牛肉,紅酒燉牛肉,泡菜牛肉,牛肉麵,香煎牛小排,滷牛腱,青椒炒牛肉,滑蛋牛肉,頂級和牛,牛肉包,清蒸牛肉,清燉牛肉湯,辣炒牛肉,牛肉乾,烤牛排,蠔油牛肉甘藍,牛肉飯,麻辣牛腩鍋,胡椒牛柳,牛肉炒麵,蔥爆牛肉,鄉村炸牛排,骰子牛肉,炸牛肉丸,咖喱牛筋,黑胡椒牛肚,牛肉烏龍麵,牛肉餡餅,牛肋條,味噌牛肉捲

#紅燒牛肉,紅酒燉牛肉,泡菜牛肉,牛肉麵,香煎牛小排,滷牛腱,滑蛋牛肉,清蒸牛肉,清燉牛肉湯,辣炒牛肉,牛肉乾,烤牛排,蠔油牛肉甘藍,牛肉飯,麻辣牛腩鍋,胡椒牛柳,牛肉炒麵,鄉村炸牛排,骰子牛肉,炸牛肉丸,咖喱牛筋,黑胡椒牛肚,牛肉烏龍麵,牛肉餡餅,牛肋條,味噌牛肉捲

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('Demo_Knapsack_Problem')
window.geometry("1250x800")

label_size = tk.Label(window, text="請輸入背包大小:", font=("標改體",13))
label_size.pack()
label_size.place(x=5, y=3)

input_size = tk.Entry(window)
input_size.pack()
input_size.place(x=165, y=6)

label_name = tk.Label(window, text="請輸入物品名稱:", font=("標改體",13))
label_name.pack()
label_name.place(x=5, y=33)

input_name = tk.Entry(window)
input_name.pack()
input_name.place(x=165, y=36)

#文字固定距離左邊10的地方開始
#文字換行 y軸加30

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

value=[]                        #value表示目前最佳解所得之總價
top_item=[]                         #item表示最後一個放至背包的水果

itemValue=[]                    #所考慮物品的價值
itemWeight=[]                   #所考慮物品的重量
		
item_name=['紅燒牛肉','紅酒燉牛肉','泡菜牛肉','牛肉麵','香煎牛小排','滷牛腱',
           '青椒炒牛肉','滑蛋牛肉','頂級和牛','牛肉包','清蒸牛肉','清燉牛肉湯',
		   '辣炒牛肉','牛肉乾','烤牛排','蠔油牛肉甘藍','牛肉飯','麻辣牛腩鍋',
		   '胡椒牛柳','牛肉炒麵','蔥爆牛肉','鄉村炸牛排','骰子牛肉','炸牛肉丸',
		   '咖喱牛筋','黑胡椒牛肚','牛肉烏龍麵','牛肉餡餅','牛肋條','味噌牛肉捲']
		   
#紅燒牛肉,紅酒燉牛肉,泡菜牛肉,牛肉麵,香煎牛小排,滷牛腱,青椒炒牛肉,滑蛋牛肉,頂級和牛,牛肉包,清蒸牛肉,清燉牛肉湯,辣炒牛肉,牛肉乾,烤牛排,蠔油牛肉甘藍,牛肉飯,麻辣牛腩鍋,胡椒牛柳,牛肉炒麵,蔥爆牛肉,鄉村炸牛排,骰子牛肉,炸牛肉丸,咖喱牛筋,黑胡椒牛肚,牛肉烏龍麵,牛肉餡餅,牛肋條,味噌牛肉捲

item_weight=['166','80','93','50','150','60',
             '58','183','67','13','267','262',
			 '153','50','260','156','167','248',
			 '152','200','67','151','267','300',
			 '334','280','321','51','43','67']

item_value=['330','150','200','90','274','132',
            '131','366','223','33','667','653',
			'259','107','553','282','294','506',
			'264','399','318','321','588','632',
			'832','613','648','99','67','166']
		
def close():
	window.destroy()
	
def start():
	global value
	global itemWeight
	global itemValue
	global top_item
	
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
	
	
	#初始化
	bagSize=input_size.get()
	c_item=input_name.get()
	considerItem=c_item.split(',')#['紅燒牛肉','滑蛋牛肉','烤牛排','鄉村炸牛排','味噌牛肉捲','蔥爆牛肉','咖喱牛筋']#c_item.split(',')  #所考慮的物品
	
	bagSize=int(bagSize)            #背包的大小
	itemNum=len(considerItem)       #所考慮物品的數量
	
	def findItemWeight(item_n):
		item_w=[]
		for i in range(len(item_n)):
			for j in range(len(item_name)):
				if item_n[i]==item_name[j]:
					#資料型態很重要
					#字串比大小的結果跟數字比大小的結果有可能不一樣
					item_w.append(int(item_weight[j]))
					
					break
		
		return	item_w
	def findItemValue(item_n):
		item_v=[]
		for i in range(len(item_n)):
			for j in range(len(item_name)):
				if item_n[i]==item_name[j]:
					item_v.append(int(item_value[j]))
					break
		return	item_v
	#尋找要考慮物品的價值
	itemValue=findItemValue(considerItem)
	#尋找要考慮物品的重量
	itemWeight=findItemWeight(considerItem)
	#print(len(itemWeight))
	#所考慮物品的最小重量
	#itemMinWeight=findItemMinWeight(itemWeight)
	
	#初始化value、item兩個list
	value=[0]*bagSize
	top_item=['empty']*bagSize
	def printLastLine(considerItem,itemList,current_y,bagSize):
		global value
		item_num=[]
		for i in range(len(considerItem)):
			item_num.append(0)
		for i in range(len(itemList)):
			for j in range(len(considerItem)):
				if itemList[i]==considerItem[j]:
					item_num[j]=item_num[j]+1
		
		string="當背包大小為"+str(bagSize)+"，"
		for i in range(len(item_num)):
			if item_num[i]!=0:
				string=string+"拿"+str(considerItem[i])+str(item_num[i])+"個，"
				
		string=string+"得總價值"+str(value[bagSize-1])
		
		canvas.create_text(10,current_y-50,text=string,anchor='nw',font=("標改體",13))
			
		
		
		#item_num=[0*len(considerItem)]
		#print(string)
		
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
		if len(item_print[0])==3:
			text_x=r_x1+35
		elif len(item_print[0])==4:
			text_x=r_x1+27
		elif len(item_print[0])==5:
			text_x=r_x1+19
		elif len(item_print[0])==6:
			text_x=r_x1+11
		canvas.create_text(consider_x,consider_y,text=considerStr,anchor='nw',font=("標改體",13))
		for i in range(r_num):
			canvas.create_rectangle(r_x1,r_y1,r_x2,r_y2)
			canvas.create_text(text_x,text_y,text=item_print[i],anchor='nw',font=("標改體",13))
			#canvas.pack()
			r_x1=r_x2
			r_x2=r_x1+r_length
			r_y2=r_y1+r_width
			#text_x=r_x1+11
			if i!=r_num-1:
				if len(item_print[i+1])==3:
					text_x=r_x1+35
				elif len(item_print[i+1])==4:
					text_x=r_x1+27
				elif len(item_print[i+1])==5:
					text_x=r_x1+19
				elif len(item_print[i+1])==6:
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
				if len(item_print[i+1])==3:
					text_x=r_x1+35
				elif len(item_print[i+1])==4:
					text_x=r_x1+27
				elif len(item_print[i+1])==5:
					text_x=r_x1+19
				elif len(item_print[i+1])==6:
					text_x=r_x1+11
				text_y=r_y1+5
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
		
		return r_y2
		#if considerStr==6:
		#	canvas.pack()
		
		
	def itemNeedToPrintOut(bagSize,considerItem):
		global top_item
		global itemWeight    
		list=[]
		pag_index=bagSize-1   #index 0-599 bag
		while(pag_index):
			if(top_item[pag_index]=='empty'):
				#text.insert('insert',"\n")
				break
			else:
				list.append(considerItem[top_item[pag_index]])
				#text.insert('insert',considerItem[top_item[pag_index]]+" ")
				#maxValueItem.append(considerItem[top_item[pag_index]])
				pag_index=pag_index-itemWeight[top_item[pag_index]]
				if pag_index==-1:
					pag_index=0
		#print(list)
		#print("\n")
		return list
	def combineStr(considerTo,considerItem):
		string="僅考慮"
		for i in range(considerTo+1):
			if i==considerTo:
				string=string+considerItem[i]+":"
			else:
				string=string+considerItem[i]+"、"
		return string
		#text.insert('insert',string)
		#text.insert('insert',"\n")
				
		
	def countNum(maxValueItem,considerItem):
		number=[0]*len(considerItem)
		for i in range(len(maxValueItem)):
			for j in range(len(considerItem)):
				if maxValueItem[i]==considerItem[j]:
					number[j]=number[j]+1
		return	number
		
	def renewValueAndItem(current_bag_size,newTopItem,max_value):
		#print('in')
		global value
		global top_item
		value[current_bag_size]=max_value
		top_item[current_bag_size]=newTopItem
		
	def maxValue(item_index,leftSize):      #leftSize:1-600
		global value                        #value表示目前最佳解所得之總價
		global top_item                         #item表示最後一個放至背包的水果
		global itemValue                    #所考慮物品的價值
		global itemWeight                   #所考慮物品的重量
		
		current_bag_index=leftSize-1
		current_top_item=top_item[current_bag_index]
		current_value=value[current_bag_index]
		if leftSize==0 or current_top_item=='empty':
			return 0
		else:
			current_value=itemValue[item_index]
			#print(current_value)
			leftSize=leftSize-itemWeight[item_index]
			if leftSize==0:
				item_index='end'
			else:
				item_index=top_item[leftSize-1]
			return current_value+maxValue(item_index,leftSize)
			
		
		
	
	def KnapsackProblem(bagSize,itemNum,considerItem):
		global value
		global top_item
		global itemWeight                   #所考慮物品的重量
		global itemValue
		#print(len(itemWeight))
		
		for item_index in range(itemNum):   #從第一個item開始放入背包
			#print(item_index)
			#放入第一個物品 用除法就可以計算
			if item_index==0:
				for i in range(bagSize):
					num=int((i+1)/itemWeight[item_index])
					if(num>0):
						value[i]=num*int(itemValue[item_index])
						top_item[i]=item_index
						
					
			#之後的物品用DynamicProgramming
			else:
				for bag_index in range(bagSize):    #bag_index:背包負重0-599  bagSize:600
					bag_size=bag_index+1
					#先判斷背包是否放得下
					EnoughSpace=int(bag_size/itemWeight[item_index])
					if EnoughSpace:
						max_v=maxValue(item_index,bag_size)   #singleMaxNum:全部用來放第i種水果 最多放幾顆
						current_max=value[bag_index]
						if item_index==1 and bag_index==79:
							print(current_max)
							print(max_v)
						if(max_v>current_max):
							
							#更新value、item的資訊
							renewValueAndItem(bag_index,item_index,max_v)
					else:
						continue
			#僅考慮...的那一行字
			considerStr=combineStr(item_index,considerItem)
			#將要印出的背包內容物整理成list
			item_print=itemNeedToPrintOut(bagSize,considerItem)
			current_y=printTextTable(considerStr,item_print)
			if item_index==(itemNum-1):
				printLastLine(considerItem,item_print,current_y,bagSize)
			
	KnapsackProblem(bagSize,itemNum,considerItem)
	


button_start = tk.Button(window, text="Start",command=start)
button_start.pack()
button_start.place(x=110, y=69)

button_close = tk.Button(window, text="Close", command=close)
button_close.pack()
button_close.place(x=250, y=69)


tk.mainloop()











