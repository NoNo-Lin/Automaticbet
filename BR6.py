from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import datetime
import os, sys
import telegram
from bs4 import BeautifulSoup

istime = time.strftime("%Y-%m-%d %H:%M", time.localtime())

bot = telegram.Bot(token='access Telegram Bot API')#Telegram Bot API寫入

client = MongoClient("MONGO的伺服器")#連線MongoDB

db = client.beijing
test1 = db.racing

jgp = input("請輸入程式帳號 : ")
jpg = input("請輸入程式密碼 : ")


cursor = test1.find_one({'_id':jgp})
#print(cursor)

if cursor != None :
	#print("有值")
	if cursor["_id"] == jpg :
		print("帳號正確")
		if cursor["password"] == jpg:
			print("密碼正確")
		else:
			print("密碼錯誤")
			os.exit(n)
	else:
		print("帳號錯誤")
		os.exit(n)
else:
	print("不正確")
	os.exit(n)

gigi = istime+" #"+jgp+" 6倍登入"
bot.sendMessage(chat_id='聊天頻道ID', text=gigi)

c=['one','two','three','four','fives','six','seven','eight','nine','ten']

oneone = "inw_1_"
twotwo = "inw_5_"
threethree ="inw_9_"
fourfour = "inw_13_"
fivesfives ="inw_17_"
sixsix ="inw_21_"
sevenseven ="inw_24_"
eighteight ="inw_27_"
ninenine ="inw_30_"
tenten ="inw_33_"

for i in range(len(c)):
	locals()[c[i]+c[i]+c[i]] = -1

urll = input("請輸入線路1或2 : ")
if urll == "1":
	uurl = "網址1"
	print("選擇線路一")
elif urll == "2":
	uurl = "網址2"
	print("選擇線路二")

numberr = input("輸入XXXX帳號:")
print("帳號")
passwordd = input("輸入XXXX密碼:")
print("密碼")

double = ["這","是","測","試","品"]
for i in range(len(c)):
    locals()[c[i]+'double' ] = double

money = input("投注金額:")
print("投注金額 = ",money)

for i in range(len(c)):
    locals()[c[i]+'money' ] = money


jperiod = 0

ranking = input("請輸入要下注的 每個數字後面請加逗點:").split(",")
rranking = len(ranking)

for rrankingg in range(0,rranking):
    if ranking[rrankingg]  == "1":
        xcc = input("請輸入要下注的冠軍的數字 每個數字後面請加逗點:").split(",")
        onedouble = double
        oneone =  ["inw_1_"+pg for pg in xcc]
        #print (oneone)
        xxcc = len(xcc)
        #print(xxcc)
        print("-"*10)
        #xcc.reverse()
    elif ranking[rrankingg]  == "2":
        #print(ranking[rrankingg])
        ruu = input("請輸入要下注的亞軍的數字 每個數字後面請加逗點:").split(",")
        tworet= [str(int(i)+16) for i in ruu]
        #print(tworet)
        twotwo = ["inw_5_"+i for i in tworet]
        #print(twotwo)
        twodouble = double
        rruu = len(ruu)
        #print(rruu)
        print("-"*10)
        #ruu.reverse()
    elif ranking[rrankingg]  == "3":
        #print(ranking[rrankingg])
        threepp = input("請輸入要下注的第三名的數字 每個數字後面請加逗點:").split(",")
        threeret= [str(int(i)+32) for i in threepp]
        #print(threeret)
        threethree = ["inw_9_"+i for i in threeret]
        #print(threethree)       
        threedouble = double
        tthreepp = len(threepp)
        #print(tthreepp) 
        print("-"*10)
        #threepp.reverse()
    elif ranking[rrankingg]  == "4":
        #print(ranking[rrankingg])
        fourpp = input("請輸入要下注的第四名的數字 每個數字後面請加逗點:").split(",")
        fourret= [str(int(i)+48) for i in fourpp]
        #print(fourret)
        fourfour = ["inw_13_"+i for i in fourret]
        #print(fourfour)       
        fourdouble = double
        ffourpp = len(fourpp)
        #print(ffourpp)  
        print("-"*10)
        #fourpp.reverse()
    elif ranking[rrankingg]  == "5":
        #print(ranking[rrankingg])
        fivespp = input("請輸入要下注的第五名的數字 每個數字後面請加逗點:").split(",")
        fivesret= [str(int(i)+64) for i in fivespp]
        #print(fivesret)
        fivesfives = ["inw_17_"+i for i in fivesret]
        #print(fivesfives)              
        fivesdouble = double
        ffivespp = len(fivespp)
        #print(ffivespp)          
        print("-"*10)
        #fivespp.reverse()
    elif ranking[rrankingg]  == "6":
        #print(ranking[rrankingg])
        sixpp = input("請輸入要下注的第六名的數字 每個數字後面請加逗點:").split(",")
        sixret= [str(int(i)+80) for i in sixpp]
        #print(sixret)
        sixsix = ["inw_21_"+i for i in sixret]   
        #print(sixsix)  
        sixdouble = double
        ssixpp = len(sixpp)
        #print(ssixpp)           
        print("-"*10)
        #ssixpp.reverse()
    elif ranking[rrankingg]  == "7":
        #print(ranking[rrankingg])
        sevenpp = input("請輸入要下注的第七名的數字 每個數字後面請加逗點:").split(",")
        sevenret= [str(int(i)+94) for i in sevenpp]
        #print(sevenret)
        sevenseven = ["inw_24_"+i for i in sevenret]   
        #print(sevenseven)          
        sevendouble = double
        ssevenpp = len(sevenpp)
        #print(ssevenpp)         
        print("-"*10)
        #sevenpp.reverse()
    elif ranking[rrankingg]  == "8":
        #print(ranking[rrankingg])
        eingtpp = input("請輸入要下注的第八名的數字 每個數字後面請加逗點:").split(",")
        eightret= [str(int(i)+108) for i in eingtpp]
        #print(eightret)
        eighteight = ["inw_27_"+i for i in eightret]   
        #print(eighteight)          
        eightdouble = double
        eeingtpp = len(eingtpp)
        #print(eeingtpp)          
        print("-"*10)
    elif ranking[rrankingg]  == "9":
        #print(ranking[rrankingg])
        ninepp = input("請輸入要下注的第九名的數字 每個數字後面請加逗點:").split(",")
        nineret= [str(int(i)+122) for i in ninepp]
        #print(nineret)
        ninenine = ["inw_30_"+i for i in nineret]   
        #print(ninenine)          
        ninedouble = double
        nninepp = len(ninepp)
        #print(nninepp)          
        print("-"*10)
    elif ranking[rrankingg]  == "10":
        #print(ranking[rrankingg])
        tenpp = input("請輸入要下注的第十名的數字 每個數字後面請加逗點:").split(",")
        tenret = [str(int(i)+136) for i in tenpp]
        #print(tenret)
        tenten = ["inw_33_"+i for i in tenret]   
        #print(tenten)          
        tendouble = double
        ttenpp = len(tenpp)
        #print(ttenpp)  
        print("-"*10)
    else:
        print("沒填強制關閉程式")
        sys.exit(0) 
def process ():
    driver.find_element_by_id("loginName").send_keys(numberr)
    print ("輸入帳號")
    print("-"*10)
    #ttxxtt.write("帳號輸入成功\n")
    driver.find_element_by_id('loginPwd').send_keys(passwordd)
    #ttxxtt.write("輸入密碼成功\n")
    print("輸入密碼")
    print("-"*10)
    driver.find_element_by_xpath('//*[@id="login_btn"]').click()
    #ttxxtt.write("點擊登入\n")
    print("點擊登入")
    print("-"*10)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="myLayer_19841012"]/tbody/tr/td/div[1]/a')))
    #print(element)

    driver.find_element_by_xpath('//*[@id="myLayer_19841012"]/tbody/tr/td/div[1]/a').click()
    print("關閉視窗")
    print("-"*10)
    #ttxxtt.write('關閉提醒視窗\n') 

    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/input[2]').click()
    print("點擊同意")
    print("-"*10)

    zgzg = 1
    while (zgzg < 2 ) :
        try :
            a = driver.find_element_by_class_name("menu")
            #print(a)
            
            driver.find_element_by_class_name("menu").click()
            
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menuList"]/li[3]/a')))
            #print(element)
            driver.find_element_by_xpath('//*[@id="menuList"]/li[3]/a').click()
            print("-"*10)
            zgzg +=1
        except:
            zozozo = 1
            print("重新選擇")
            print("-"*10)

    driver.switch_to.frame(0)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[1]/ul/li[2]/a')))
    #print(element)

 

    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/div[1]/ul/li[2]/a').click()
    print("選擇單球1-10")
    print("-"*10)

def mybet():
    for rrankingg in range(0,rranking):
        if ranking[rrankingg]  == "1":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(onemoney)    
            for oneggin in range(0,xxcc):
                #print (oneone)
                driver.find_element_by_id(oneone[oneggin]).click()
                
        elif ranking[rrankingg]  == "2":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(twomoney) 
            for twoggin in range(0,rruu):
                #print (twotwo)
                driver.find_element_by_id(twotwo[twoggin]).click()
                
        elif ranking[rrankingg]  == "3":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(threemoney)
            for threeggin in range(0,tthreepp):
                #print (threethree)
                driver.find_element_by_id(threethree[threeggin]).click()     
                
        elif ranking[rrankingg]  == "4":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(fourmoney) 
            for fourggin in range(0,ffourpp):
                driver.find_element_by_id(fourfour[fourggin]).click()     
                          
        elif ranking[rrankingg]  == "5":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(fivesmoney)  
            for fiveggin in range(0,ffivespp):
                #print (fivesfives)
                driver.find_element_by_id(fivesfives[fiveggin]).click()     
                                       
        elif ranking[rrankingg]  == "6":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(sixmoney)   
            for sixggin in range(0,ssixpp):
                #print (sixsix)
                driver.find_element_by_id(sixsix[sixggin]).click()     
                                
        elif ranking[rrankingg]  == "7":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(sevenmoney)  
            for sevenggin in range(0,ssevenpp):
                #print (sevenseven)
                driver.find_element_by_id(sevenseven[sevenggin]).click()     
                             
        elif ranking[rrankingg]  == "8":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(eightmoney)  
            for eingggin in range(0,eeingtpp):
                #print (eighteight)
                driver.find_element_by_id(eighteight[eingggin]).click()     
                              
        elif ranking[rrankingg]  == "9":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(ninemoney)   
            for nineggin in range(0,nninepp):
                #print (ninenine)
                driver.find_element_by_id(ninenine[nineggin]).click()     
                                 
        elif ranking[rrankingg]  == "10":
            driver.find_element_by_id('tool_ys_input').clear()
            driver.find_element_by_id('tool_ys_input').send_keys(tenmoney)   
            for tenggin in range(0,ttenpp):
                #print (tenten)
                driver.find_element_by_id(tenten[tenggin]).click()
                
        else:
            print("沒填強制關閉程式")
            sys.exit(0)
driver=webdriver.Chrome()
driver.get(uurl)

process()
while True:
	try:
		zozozo = 1
		while (zozozo < 2 ) :
			xc = driver.find_element_by_id('closeText').text
			#print (xc)
			zozozo = 1
			if xc == "封盤":
				zozozo = zozozo+1
				print("尚未封盤")
				print("-" * 10)
			else:
				zozozo = 1
    
		
		period = driver.find_element_by_xpath('//*[@id="NowJq"]').text
		print ("現在是第"+period+"期")
		print("-"*10)
		
		try:  
			driver.find_element_by_link_text('取消')
			baba=True  
		except:  
			baba=False 
		
		if baba==True: 
			print ("有下注視窗，已取消")		
			driver.find_element_by_link_text('取消').click()
			print("-"*10)
		elif baba==False:  
			print ("無下注視窗")
			print("-"*10)
		
		if jperiod == period:
			print("第"+jperiod+"期下過注")
			print("-"*10)
		else:
			#print("尚未下注")
			#print("-"*10)
			ht =  driver.page_source
			soup = BeautifulSoup(ht,'html5lib')
			gg = soup.find("ul","tab_item base-clear active")
			gg = gg.find('li','on')
			if gg == None:
				#print("尚未下注")
				jp = "0"
			else:
				gg = str(gg)
				gg = gg.split(" ")
				gg = gg[1]
				jp = gg[33:39]
				print(jp)
				print("-" * 10)
			if jp == period:
				print("第"+jp+"期下過注")
				print("-" * 10)
			else:
				print("尚未下注")
				print("-"*10)
				mybet()
				
				driver.find_element_by_id('gameSubmit').click()
				
				driver.find_element_by_link_text('提交').click()
				 
				try:  
					driver.find_element_by_link_text('提交')
					a=True  
				except:  
					a=False 
				if a==True:  
					print ("倍率修正") 
					driver.find_element_by_link_text('提交').click()
					print("-"*10)
					jperiod = period
					#print("j"+period )
				elif a==False:  
					print ("無倍率問題")
					print("-"*10)
					jperiod = period
					#print("j"+period )
				oohay = time.strftime("%Y-%m-%d %H:%M", time.localtime())
				igig = oohay+" #"+numberr+" 6倍下注"
				bot.sendMessage(chat_id='-1001321529693', text=igig)
		print("等待開牌")
		print("-"*10)
		xoxoxo = 1
		while (xoxoxo < 2):
			periodd = driver.find_element_by_xpath('//*[@id="newPhase"]').text
			if period == periodd:
				print("開牌了")
				print("-"*10)
				xoxoxo = xoxoxo +1
			else:
				xoxoxo = 1 
	
		for rrankingg in range(0,rranking):
			if ranking[rrankingg]  == "1":
				xone = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[1]')
				for xxone in xone:
					xxone = xxone.get_attribute('class') 
				xxone = xxone.lstrip('No_')
				oneok_list = []
				oneerror_list=[]
				for champion in xcc:
					if int(champion) == int(xxone):
						oneok_list.append(champion)
					else:
						oneerror_list.append(champion)
				print("march number",oneok_list)
				print("miss number", oneerror_list)    
			elif ranking[rrankingg]  == "2":
				xtwo = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[2]')
				for xxtwo in xtwo:
					xxtwo = xxtwo.get_attribute('class')
				xxtwo = xxtwo.lstrip('No_')

				twook_list = []
				twoerror_list=[]
				for runnerup in ruu:
					if int(runnerup) == int(xxtwo):
						twook_list.append(runnerup)
					else:
						twoerror_list.append(runnerup)
				print("march number",twook_list)
				print("miss numbe", twoerror_list)   
   
			elif ranking[rrankingg]  == "3":
				xthree = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[3]') 
				for xxthree in xthree:
					xxthree = xxthree.get_attribute('class')
				xxthree = xxthree.lstrip('No_') 
        
				threeok_list = []
				threeerror_list=[]   
				for thirdplace in threepp:
					if int(thirdplace) == int(xxthree):
						threeok_list.append(thirdplace)
					else:
						threeerror_list.append(thirdplace)
				print("march number",threeok_list)
				print("miss numbe", threeerror_list)   
        
			elif ranking[rrankingg]  == "4":
				xfour = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[4]')
				for xxfour in xfour:
					xxfour = xxfour.get_attribute('class')  
				xxfour = xxfour.lstrip('No_')
				fourok_list = []
				fourerror_list = []  
				for fourthplace in fourpp:
					if int(fourthplace) == int(xxfour):
						fourok_list.append(fourthplace)
					else:
						fourerror_list.append(fourthplace)
				print("march number",fourok_list)
				print("miss numbe", fourerror_list)  
        
			elif ranking[rrankingg]  == "5":
				xfives = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[5]')
				for xxfives in xfives:
					xxfives = xxfives.get_attribute('class') 
				xxfives = xxfives.lstrip('No_') 
				fivesok_list = []
				fiveserror_list=[]   
				for thefifthplace in fivespp:
					if int(thefifthplace) == int(xxfives):
						fivesok_list.append(thefifthplace)
					else:
						fiveserror_list.append(thefifthplace)
				print("march number",fivesok_list)
				print("miss numbe", fiveserror_list)   
          
			elif ranking[rrankingg]  == "6":
				xsix = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[6]')
				for xxsix in xsix:
					xxsix = xxsix.get_attribute('class')  
				xxsix = xxsix.lstrip('No_')
				sixok_list = []
				sixerror_list=[] 
				for sixthplace in sixpp:
					if int(sixthplace) == int(xxsix):
						sixok_list.append(sixthplace)
					else:
						sixerror_list.append(sixthplace)
				print("march number",sixok_list)
				print("miss numbe", sixerror_list)  
       
			elif ranking[rrankingg]  == "7":
				xseven = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[7]')
				for xxseven in xseven:
					xxseven = xxseven.get_attribute('class')  
				xxseven = xxseven.lstrip('No_')
				sevenok_list = []
				sevenerror_list=[]
				for seventhplace in sevenpp:
					if int(seventhplace) == int(xxseven):
						sevenok_list.append(seventhplace)
					else:
						sevenerror_list.append(seventhplace)
				print("march number",sevenok_list)
				print("miss numbe", sevenerror_list)  
          
			elif ranking[rrankingg]  == "8":
				xeight = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[8]')
				for xxeight in xeight:
					xxeight = xxeight.get_attribute('class') 
				xxeight = xxeight.lstrip('No_')
				eightok_list = []
				eighterror_list=[]  
				for eightplace in eingtpp:
					if int(eightplace) == int(xxeight):
						eightok_list.append(eightplace)
					else:
						eighterror_list.append(eightplace)
				print("march number",eightok_list)
				print("miss number", eighterror_list) 
        
			elif ranking[rrankingg]  == "9":
				xnine = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[9]')
				for xxnine in xnine:
					xxnine = xxnine.get_attribute('class') 
				xxnine = xxnine.lstrip('No_')
				nineok_list = []
				nineerror_list=[]    
				for ninthplace in ninepp:
					if int(ninthplace) == int(xxnine):
						nineok_list.append(ninthplace)
					else:
						nineerror_list.append(ninthplace)
				print("march number",nineok_list)
				print("miss number", nineerror_list)   
        
			elif ranking[rrankingg]  == "10":
				xten = driver.find_elements_by_xpath('//*[@id="prevBall"]/span[10]')  
				for xxten in xten:
					xxten = xxten.get_attribute('class') 
				xxten = xxten.lstrip('No_')
				tenok_list = []
				tenerror_list=[]              
				for tenthplace in tenpp:
					if int(tenthplace) == int(xxten):
						tenok_list.append(tenthplace)
					else:
						tenerror_list.append(tenthplace)
				print("march number",tenok_list)
				print("miss number", tenerror_list)               
			else:
				print("發生錯誤")
				sys.exit(0) 
        
       
		for rrankingg in range(0,rranking):
			if ranking[rrankingg]  == "1":
				onecount = len(oneok_list)
				if onecount == 0:
					onemoney = money
					oneoneone = -1
					#print(oneoneone)
					print ("冠軍沒中")
					print("冠軍目前金額:"+onemoney)
					print("冠軍倍率歸零")
					print("-"*10)
				else:
					onemoney = money
					print("冠軍中了%s個" % onecount)
					oneoneone = oneoneone+1
					if oneoneone >= 11:
						oneoneone = 11
					oonedouble = onedouble[oneoneone]
					#print(oodouble)
					if isinstance(oonedouble,int) :
						oonedouble = int(oonedouble)
						#print('整数')
					elif isinstance(oonedouble,float):
						oonedouble = float(oonedouble)
						#print('浮点数')
					onemoney = (int(onemoney) * oonedouble)
					if isinstance(onemoney,int) :
						onemoney = int(onemoney)
						onemoney = str(onemoney)
						#print('整数')
					elif isinstance(onemoney,float):
						onemoney = int(onemoney)
						onemoney = str(onemoney)
						#print('浮点数')
					print("冠軍目前金額:"+onemoney)
					print("冠軍目前倍率"+str(oonedouble))    
					print("-"*10)
			elif ranking[rrankingg]  == "2":
				twocount = len(twook_list)
				if twocount == 0:
					twomoney = money
					twotwotwo = -1
					#print(twotwotwo)
					print("亞軍沒中")
					print("亞軍目前金額:"+twomoney)
					print("亞軍倍率歸零")
					print("-"*10)
				else:
					twomoney = money
					print("亞軍中了%s個" % twocount)
					twotwotwo = twotwotwo+1
					if twotwotwo >= 11:
						twotwotwo = 11
					ttwodouble = twodouble[twotwotwo]
					#print(ttdouble)
					if isinstance(ttwodouble,int) :
						ttwodouble = int(ttwodouble)
						#print('整数')
					elif isinstance(ttwodouble,float):
						ttwodouble = float(ttwodouble)
						#print('浮点数') 
					twomoney = (int(twomoney) * ttwodouble)
					if isinstance(twomoney,int) :
						twomoney = int(twomoney)
						twomoney = str(twomoney)
						#print('整数')
					elif isinstance(twomoney,float):
						twomoney = int(twomoney)
						twomoney = str(twomoney)
						#print('浮点数') 
					print("亞軍目前金額:"+twomoney)
					print("亞軍目前倍率"+str(ttwodouble))
					print("-"*10)
			elif ranking[rrankingg]  == "3":
				threecount = len(threeok_list)
				if threecount == 0:
					threemoney = money
					threethreethree = -1
					#print(twotwotwo)
					print("第三名沒中")
					print("第三名目前金額:"+threemoney)
					print("第三名倍率歸零")
					print("-"*10)
				else:
					threemoney = money
					print("第三名中了%s個" % threecount)
					threethreethree = threethreethree+1
					if threethreethree >= 11:
						threethreethree = 11
					tthreedouble = threedouble[threethreethree]
					#print(ttdouble)
					if isinstance(tthreedouble,int) :
						tthreedouble = int(tthreedouble)
						#print('整数')
					elif isinstance(tthreedouble,float):
						tthreedouble = float(tthreedouble)
						#print('浮点数') 
					threemoney = (int(threemoney) * tthreedouble)
					if isinstance(threemoney,int) :
						threemoney = int(threemoney)
						threemoney = str(threemoney)
						#print('整数')
					elif isinstance(threemoney,float):
						threemoney = int(threemoney)
						threemoney = str(threemoney)
						#print('浮点数') 
					print("第三名目前金額:"+threemoney)
					print("第三名目前倍率"+str(tthreedouble)) 
					print("-"*10)
			elif ranking[rrankingg]  == "4":
				fourcount = len(fourok_list)
				if fourcount == 0:
					fourmoney = money
					fourfourfour = -1
					#print(twotwotwo)
					print("第四名沒中")
					print("第四名目前金額:"+fourmoney)
					print("第四名倍率歸零")
					print("-"*10)
				else:
					fourmoney = money
					print("第四名中了%s個" % fourcount)
					fourfourfour = fourfourfour+1
					if fourfourfour >= 11:
						fourfourfour = 11
					ffourdouble = fourdouble[fourfourfour]
					#print(ttdouble)
					if isinstance(ffourdouble,int) :
						ffourdouble = int(ffourdouble)
						#print('整数')
					elif isinstance(ffourdouble,float):
						ffourdouble = float(ffourdouble)
						#print('浮点数') 
					fourmoney = (int(fourmoney) * ffourdouble)
					if isinstance(fourmoney,int) :
						fourmoney = int(fourmoney)
						fourmoney = str(fourmoney)
						#print('整数')
					elif isinstance(fourmoney,float):
						fourmoney = int(fourmoney)
						fourmoney = str(fourmoney)
						#print('浮点数') 
					print("第四名目前金額:"+fourmoney)
					print("第四名目前倍率"+str(ffourdouble))  
					print("-"*10)
			elif ranking[rrankingg]  == "5":
				fivescount = len(fivesok_list)
				if fivescount == 0:
					fivesmoney = money
					fivesfivesfives = -1
					#print(twotwotwo)
					print("第五名沒中")
					print("第五名目前金額:"+fivesmoney)
					print("第五名倍率歸零")
					print("-"*10)
				else:
					fivesmoney = money
					print("第五名中了%s個" % fivescount)
					fivesfivesfives = fivesfivesfives+1
					if fivesfivesfives >= 11:
						fivesfivesfives = 11
					ffivesdouble = fivesdouble[fivesfivesfives]
					#print(ttdouble)
					if isinstance(ffivesdouble,int) :
						ffivesdouble = int(ffivesdouble)
						#print('整数')
					elif isinstance(ffivesdouble,float):
						ffivesdouble = float(ffivesdouble)
						#print('浮点数') 
					fivesmoney = (int(fivesmoney) * ffivesdouble)
					if isinstance(fivesmoney,int) :
						fivesmoney = int(fivesmoney)
						fivesmoney = str(fivesmoney)
						#print('整数')
					elif isinstance(fivesmoney,float):
						fivesmoney = int(fivesmoney)
						fivesmoney = str(fivesmoney)
						#print('浮点数') 
					print("第五名目前金額:"+fivesmoney)
					print("第五名目前倍率"+str(ffivesdouble))  
					print("-"*10)
			elif ranking[rrankingg]  == "6":
				sixcount = len(sixok_list)
				if sixcount == 0:
					sixmoney = money
					sixsixsix = -1
					#print(twotwotwo)
					print("第六名沒中")
					print("第六名目前金額:"+sixmoney)
					print("第六名倍率歸零")
					print("-"*10)
				else:
					sixmoney = money
					print("第六名中了%s個" % sixcount)
					sixsixsix = sixsixsix+1
					if sixsixsix >= 11:
						sixsixsix = 11
					ssixdouble = sixdouble[sixsixsix]
					#print(ttdouble)
					if isinstance(ssixdouble,int) :
						ssixdouble = int(ssixdouble)
						#print('整数')
					elif isinstance(ssixdouble,float):
						ssixdouble = float(ssixdouble)
						#print('浮点数') 
					sixmoney = (int(sixmoney) * ssixdouble)
					if isinstance(sixmoney,int) :
						sixmoney = int(sixmoney)
						sixmoney = str(sixmoney)
						#print('整数')
					elif isinstance(sixmoney,float):
						sixmoney = int(sixmoney)
						sixmoney = str(sixmoney)
						#print('浮点数') 
					print("第六名目前金額:"+sixmoney)
					print("第六名目前倍率"+str(ssixdouble)) 
					print("-"*10)
			elif ranking[rrankingg]  == "7":
				sevencount = len(sevenok_list)
				if sevencount == 0:
					sevenmoney = money
					sevensevenseven = -1
					#print(twotwotwo)
					print("第七名沒中")
					print("第七名目前金額:"+sevenmoney)
					print("第七名倍率歸零")
					print("-"*10)
				else:
					sevenmoney = money
					print("第七名中了%s個" % sevencount)
					sevensevenseven = sevensevenseven+1
					if sevensevenseven >= 11:
						sevensevenseven = 11
					ssevendouble = sevendouble[sevensevenseven]
					#print(ttdouble)
					if isinstance(ssevendouble,int) :
						ssevendouble = int(ssevendouble)
						#print('整数')
					elif isinstance(ssevendouble,float):
						ssevendouble = float(ssevendouble)
						#print('浮点数') 
					sevenmoney = (int(sevenmoney) * ssevendouble)
					if isinstance(sevenmoney,int) :
						sevenmoney = int(sevenmoney)
						sevenmoney = str(sevenmoney)
						#print('整数')
					elif isinstance(sevenmoney,float):
						sevenmoney = int(sevenmoney)
						sevenmoney = str(sevenmoney)
						#print('浮点数') 
					print("第七名目前金額:"+sevenmoney)
					print("第七名目前倍率"+str(ssevendouble)) 
					print("-"*10)
			elif ranking[rrankingg]  == "8":
				eightcount = len(eightok_list)
				if eightcount == 0:
					eightmoney = money
					eighteighteight = -1
					#print(twotwotwo)
					print("第八名沒中")
					print("第八名目前金額:"+eightmoney)
					print("第八名倍率歸零")
					print("-"*10)
				else:
					eightmoney = money
					print("第八名中了%s個" % eightcount)
					eighteighteight = eighteighteight+1
					if eighteighteight >= 11:
						eighteighteight = 11
					eeightdouble = eightdouble[eighteighteight]
					#print(ttdouble)
					if isinstance(eeightdouble,int) :
						eeightdouble = int(eeightdouble)
						#print('整数')
					elif isinstance(eeightdouble,float):
						eeightdouble = float(eeightdouble)
						#print('浮点数') 
					eightmoney = (int(eightmoney) * eeightdouble)
					if isinstance(eightmoney,int) :
						eightmoney = int(eightmoney)
						eightmoney = str(eightmoney)
						#print('整数')
					elif isinstance(eightmoney,float):
						eightmoney = int(eightmoney)
						eightmoney = str(eightmoney)
						#print('浮点数') 
					print("第八名目前金額:"+eightmoney)
					print("第八名目前倍率"+str(eeightdouble)) 
					print("-"*10)
			elif ranking[rrankingg]  == "9":
				ninecount = len(nineok_list)
				if ninecount == 0:
					ninemoney = money
					nineninenine = -1
					#print(twotwotwo)
					print("第九名沒中")
					print("第九名目前金額:"+ninemoney)
					print("第九名倍率歸零")
					print("-"*10)
				else:
					ninemoney = money
					print("第九名中了%s個" % ninecount)
					nineninenine = nineninenine+1
					if nineninenine >= 11:
						nineninenine = 11
					nninedouble = ninedouble[nineninenine]
					#print(ttdouble)
					if isinstance(nninedouble,int) :
						nninedouble = int(nninedouble)
						#print('整数')
					elif isinstance(nninedouble,float):
						nninedouble = float(nninedouble)
						#print('浮点数') 
					ninemoney = (int(ninemoney) * nninedouble)
					if isinstance(ninemoney,int) :
						ninemoney = int(ninemoney)
						ninemoney = str(ninemoney)
						#print('整数')
					elif isinstance(ninemoney,float):
						ninemoney = int(ninemoney)
						ninemoney = str(ninemoney)
						#print('浮点数') 
					print("第九名目前金額:"+ninemoney)
					print("第九名目前倍率"+str(nninedouble)) 
					print("-"*10)
			elif ranking[rrankingg]  == "10":
				tencount = len(tenok_list)
				if tencount == 0:
					tenmoney = money
					tententen = -1
					#print(twotwotwo)
					print("第十名沒中")
					print("第十名目前金額:"+tenmoney)
					print("第十名倍率歸零")
					print("-"*10)
				else:
					tenmoney = money
					print("第十名中了%s個" % tencount)
					tententen = tententen+1
					if tententen >= 11:
						tententen = 11
					ttendouble = tendouble[tententen]
					#print(ttdouble)
					if isinstance(ttendouble,int) :
						ttendouble = int(ttendouble)
						#print('整数')
					elif isinstance(ttendouble,float):
						ttendouble = float(ttendouble)
						#print('浮点数') 
					tenmoney = (int(tenmoney) * ttendouble)
					if isinstance(tenmoney,int) :
						tenmoney = int(tenmoney)
						tenmoney = str(tenmoney)
						#print('整数')
					elif isinstance(tenmoney,float):
						tenmoney = int(tenmoney)
						tenmoney = str(tenmoney)
						#print('浮点数') 
					print("第十名目前金額:"+tenmoney)
					print("第十名目前倍率"+str(ttendouble)) 
					print("-"*10)
			else:
				print("發生錯誤")
				sys.exit(0)  
	except:
		btitle = driver.title
		print(btitle)
		if "用戶登錄"== btitle:
			if urll == "1":
				urll = "2"
				uurl = "http://mem5.maoefo418.besrubber.com/"
				print("改為線路二")
			elif urll == "2":
				urll = "1"
				uurl = "http://mem1.maoefo418.cdbybj.com:88/"
				print("改為線路一")
			driver.get(uurl)
			process()
		elif "XXXX" == btitle:
			print("程式運轉錯誤")
		else:
			if urll == "1":
				urll = "2"
				uurl = "網址2"
				print("改為線路二")
			elif urll == "2":
				urll = "1"
				uurl = "網址1"
				print("改為線路一")
			driver.get(uurl)
			process()

