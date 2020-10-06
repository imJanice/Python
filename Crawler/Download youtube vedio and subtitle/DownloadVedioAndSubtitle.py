#download youtube video and subtitle
'''
The downloaded subtitle files 
can be converted into official subtitle format 
through this website
https://gotranscript.com/subtitle-converter
'''

import sys
sys.path.append('C:\\JaniceData\\Code\\Python\\my_models')
import mySelenium
import myOS
import time
from bs4 import BeautifulSoup
import pyautogui
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


def getSubtitlesFromYoutube():
	(driver,soup)=mySelenium.crawler_headless(youtubePath)
	#driver.maximize_window()
	time.sleep(5)
	#WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="其他動作"]')))
	try:
		driver.find_elements_by_css_selector('button[aria-label="其他動作"]')[1].click()
	except:
		time.sleep(1)
		driver.find_elements_by_css_selector('button[aria-label="其他動作"]')[0].click()
	time.sleep(2)	
	#開啟字幕紀錄
	driver.find_element_by_css_selector('yt-formatted-string.ytd-menu-service-item-renderer').click()
	#英文
	# 将滚动条移动到页面的指定位置
	js="var q=document.documentElement.scrollTop=300"  
	driver.execute_script(js)
	# target = driver.find_element_by_class_name('yt-dropdown-menu')
	# #print(len(target))
	# driver.execute_script("arguments[0].scrollIntoView();", target)
	time.sleep(3)
	driver.find_element_by_css_selector('div.paper-menu-button').click()
	item = driver.find_elements_by_css_selector('div.item.style-scope.yt-dropdown-menu')#.click()
	#print(len(a))
	time.sleep(2)
	for i in range(len(item)):
		if item[i].get_attribute('textContent') == '英文 (自動產生)':
			num = i
			break
	#time.sleep(3)
	driver.find_elements_by_css_selector('div.item.style-scope.yt-dropdown-menu')[num].click()
	time.sleep(2)
	#取得靜態資料
	page = driver.page_source
	driver.close()
	soup = BeautifulSoup(page, 'html.parser')
	subtitle = soup.find(id='body').text
	subtitles = subtitle.split('\n')
	#subtitles = list(set(subtitles))
	subtitles_sort = sorted(set(subtitles),key=subtitles.index)
	subtitles.remove('')
	#print(subtitles)
	file = open(srtFilePath+fileName,'w',encoding='utf-8')
	for i in subtitles:
		#print(i.lstrip())
		file.write(i.lstrip()+'\n')
	file.close()
	driver.quit()
	print('srt success')
	
def downloadYoutube(ytlink,destinationPath):
	downloadVideoPath = ytlink.replace('www.','ss')
	(driver,soup)=mySelenium.crawler(downloadVideoPath)
	driver.maximize_window()
	time.sleep(4)
	driver.find_element_by_class_name('drop-down-box').click()
	time.sleep(2)
	driver.find_element_by_css_selector('a[title="视频格式: 360"]').click()
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[0])
	pyautogui.moveTo(1573,1008,duration=0.65)
	pyautogui.click()
	#start download
	pyautogui.moveTo(1437,935,duration=0.35)
	pyautogui.click()
	time.sleep(4)
	myOS.checkDownloadCorrect(downloadPath)
	print('download success')
	driver.quit()
	(oldfilepath,filename) = myOS.getNewFile(downloadPath)
	newfilepath = destinationPath+'\\'+filename
	shutil.move(oldfilepath,newfilepath)
	print('move success')
	
	
	
	
#getSubtitlesFromYoutube()
#downloadSubtitles()

#yt字幕存放路徑
srtFilePath = 'C:\\JaniceData\\Project\\EnglishVideoPlayer\\'
#下載路徑
downloadPath = 'C:\\Users\\Janice\\Downloads\\'
#srt轉換link
convertPath = 'https://gotranscript.com/subtitle-converter'
#srt檔名
fileName = 'subtitle.srt'
#影片存放資料夾路徑
destinationPath = 'C:\\JaniceData\\Project\\EnglishVideoPlayer'
#要下載的youtube link
youtubePath = 'https://www.youtube.com/watch?v=KCm3IscwDiE'

getSubtitlesFromYoutube()
downloadYoutube(youtubePath,destinationPath)




