import os
import time
import re
from selenium import webdriver
import time
from art import *
from bs4 import BeautifulSoup
import requests
#from requests_testadapter import Resp
from lxml import html
import subprocess
import config

os.system('color 9')

specter = text2art('==SPECTER==');
generate = text2art('>>GENERATE<<');
print('\n');
print(specter);
print(generate);

cputxt = "CPU:Min=  ,Max= (หน่วยเป็น %)";
ramtxt = "Memory:Min= ,Max= (หน่วยเป็น %)";
nettxt = "Network:Min= ,Max= (หน่วยเป็น KBps)";


max = []
min = []





def setCPUFuntion():

    try:
        cpucheck = 0;

        print('MonitorReport : Set CPU >> Start');


        while(cpucheck == 0):

            os.system('Royalcpu.text');

            with open('Royalcpu.text','r') as cpuset:

                cpusets = cpuset.readlines();

                if (len(cpusets)>11)or(len(cpusets)<11):

                    cpucheck = cpucheck+0;

                    print('MonitorReport : Set CPU >> Please check Value in Royalcpu.text');

                    if len(cpusets)>11:
                        print("\t\t"+"File Royalcpu.text have : {}".format(len(cpusets)).strip()+" line");
                    elif len(cpusets)<11:
                        print("\t\t"+"File Royalcpu.text have : {}".format(len(cpusets)).strip()+" line");
                        pass

                else:
                    cpucheck = cpucheck+1;

        print('MonitorReport : Set CPU >> Done');
    
        pass

    except EOFError:

        print('MonitorReport : Set CPU >> Fail');
        print("\t\tReport ERROR : "+EOFError);
        print('\n');
        pass

def setRAMFuntion():

    try:

        ramcheck = 0;

        print('MonitorReport : Set RAM >> Start');

        while(ramcheck == 0):

            os.system('Royalram.text');

            with open('Royalram.text','r') as ramset:

                ramsets = ramset.readlines();

                if (len(ramsets)>11)or(len(ramsets)<11):

                    ramcheck = ramcheck+0;

                    print('MonitorReport : Set RAM >> Please check Value in Royalram.text');

                    if len(ramsets)>11:
                        print("\t\t"+"File Royalram.text have : {}".format(len(ramsets)).strip()+" line");
                    elif len(ramsets)<11:
                        print("\t\t"+"File Royalram.text have : {}".format(len(ramsets)).strip()+" line");
                        pass

                else:
                    ramcheck = ramcheck+1;
    

        print('MonitorReport : Set RAM >> Done');
    
        pass
    except EOFError:

        print('MonitorReport : Set RAM >> Fail');
        print("\t\tReport ERROR : "+EOFError);
        print('\n');

        pass


def setNETFuntion():


    try:
    
        netcheck = 0;

        print('MonitorReport : Set NET >> Start');

        while(netcheck == 0):

            os.system('Royalnet.text');

            with open('Royalnet.text','r') as netset:

                netsets = netset.readlines();

                if (len(netsets)>11)or(len(netsets)<11):

                    netcheck = netcheck+0;

                    print('MonitorReport : Set NET >> Please check Value in Royalnet.text');

                    if len(netsets)>11:
                        print("\t\t"+"File Royalnet.text have : {}".format(len(netsets)).strip()+" line");
                    elif len(netsets)<11:
                        print("\t\t"+"File Royalnet.text have : {}".format(len(netsets)).strip()+" line");
                        pass

                else:
                    netcheck = netcheck+1;


        print('MonitorReport : Set NET >> Done');
    
        pass
    except EOFError:

        print('MonitorReport : Set NET >> Fail');
        print("\t\tReport ERROR : "+EOFError);
        print('\n');
        pass


def setShowReport():


    try:

        print('MonitorReport : Set Report >> Start');

        with open('Royal.text','w',encoding="utf-8") as setreport:

            gcpu = open('Royalcpu.text','r',encoding="utf-8");
            getcpu = gcpu.readlines();

            gram = open('Royalram.text','r',encoding="utf-8");
            getram = gram.readlines();

            gnet = open('Royalnet.text','r',encoding="utf-8");
            getnet = gnet.readlines();

            gip = open('IP.text','r',encoding="utf-8");
            getip = gip.readlines();


            count = 0;
            p=1;
            while (count < 11):

                setreport.writelines("No.{}".format(p).strip()+"\n");
                setreport.writelines("IP : : {}".format(getip[count]).strip()+"\n");
                setreport.writelines("CPU : : {}".format(getcpu[count]).strip()+"\n");
                setreport.writelines("RAM : : {}".format(getram[count]).strip()+"\n");
                setreport.writelines("NET : :{}".format(getnet[count]).strip()+"\n");
                setreport.writelines("\n");



                count = count + 1 ;
                p = p+1;

        print('MonitorReport : Set Report >> Done');

    except EOFError:

        print('MonitorReport : Set Report >> Fail');
        print("\t\tReport ERROR : "+EOFError);
        print('\n');

def setReportFile():


    try:

        print('MonitorReport : Set ReportFile >> Start');

        with open('ValueReport.text','w',encoding="utf-8") as setreport:

            gcpu = open('Royalcpu.text','r',encoding="utf-8");
            getcpu = gcpu.readlines();

            gram = open('Royalram.text','r',encoding="utf-8");
            getram = gram.readlines();

            gnet = open('Royalnet.text','r',encoding="utf-8");
            getnet = gnet.readlines();

            gip = open('IP.text','r',encoding="utf-8");
            getip = gip.readlines();


            count = 0;
            p=1;
            while (count < 11):

        
                setreport.writelines(format(getcpu[count]).strip()+"\n");
                setreport.writelines(format(getram[count]).strip()+"\n");
                setreport.writelines(format(getnet[count]).strip()+"\n");
           
                count = count + 1 ;
                p = p+1;

        print('MonitorReport : Set ReportFile >> Done');
        print('\n');

    except EOFError:

        print('MonitorReport : Set ReportFile >> Fail');
        print("\t\tReport ERROR : "+EOFError);
        print('\n');
    
    
    print('Show Report >> Start\n\n');



def setSendReport():



    try:

        print('MonitorReport : Set Input >> Start\n\n');


        #driver = webdriver.Chrome(r'C:\Users\Sutthinan.Ph\Documents\AppContronBrowser\chromedriver.exe');
        driver = webdriver.Chrome(r'.\Driver\chromedriver.exe');
        #driver = webdriver.Firefox(executable_path=r'.\Driver\geckodriver.exe');
        driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=Ocq5V3P1D0OnrA7143K1AQxyXVcUcTdAlxqG-0sfRY1URFcxSkJSV04yRjZKOTlIMDIzSDU3WVJTNC4u');
        time.sleep(5)

        #Login
        username = driver.find_element_by_name('loginfmt');
        username.send_keys(config.username);
        username = driver.find_element_by_id('idSIButton9');
        username.click()

        time.sleep(5);
        password = driver.find_element_by_name('passwd');
        password.send_keys(config.password);
        password = driver.find_element_by_id('idSIButton9');
        password.click();

        #setDate

        setd = str(time.strftime("%m/%d/%Y"));
        print(setd);
        time.sleep(5)
        setdate = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/input[1]');
        setdate.click();
        setdate.click();
        time.sleep(2);
        setdate.send_keys(setd);
        setdate = driver.find_element_by_class_name('picker__button--close');
        setdate.click();

        n = int(time.strftime("%H"));
        n = n+1;
        if(n==24):
            n=24;
            pass

        print(f'\n\nH : {n-1}\n\n');
        setdate = driver.find_element_by_xpath('//*[@id="Select_0_placeholder"]');
        setdate.click();
        setdate = driver.find_element_by_xpath('//*[@id="Select_0"]/ul/li[{}]'.format(n).strip());
        setdate.click();
        setdate = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button');
        setdate.click();

        #setStatus
        i = 2;
        while(i<=13):

            setstatus = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[{}]'.format(i).strip()+'/div[2]');
            setstatus.click();
    
            i = i+1;
            pass

        with open('ValueReport.text','r',encoding="utf-8") as setreport:
            getreport = setreport.readlines();

            np = 3;
            ng = 0;
            while(np < 36):

                setinput = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[{}]'.format(np).strip()+'/div/div[2]/div/div/input');
                setinput.click();
                setinput.send_keys(getreport[ng]);

                ng = ng+1;
                np = np+1;
                
                
                pass

            os.system('notepad Royal.text');
            notifyLine();

            
        
        print('\n\nMonitorReport : Set Input >> Done');
        print('\n');

    except EOFError:

        print('\n\nMonitorReport : Set Input >> Fail');
        print("\t\tReport ERROR : "+EOFError);
        print('\n');
    


#setcpu.writelines("CPU:Min=".format(min)+" ,Max=".format(max)+" (หน่วยเป็น %)\n");


def readHTML():

        with open('D.html','r',encoding="utf-8") as ghtml:
                gethtml = ghtml.read();

                with open('newx.txt','w',encoding="utf-8") as setnwx:

                        gfilx = gethtml.split("</b>");

                        for x in gfilx :

                                setnwx.writelines(x);

                        pass
        
        with open('newx.txt','r',encoding="utf-8") as gnewx:

                getnewx = gnewx.readlines();

                with open('newy.txt','w',encoding="utf-8") as setnwy:

                        for y in getnewx :

                                if '<b>H:' in y:
                                        setnwy.writelines(y);


        mylines = [];

        with open('newy.txt','rt',encoding="utf-8") as gnewy:

                for myline in gnewy:                   

                        mylines.append(myline.rstrip('\n'));
        


                i = 0;
                gk = [];
                #print(f'line1 : {len(mylines)}');
                gk = mylines[i].split('<b>H:');
                #print(f'line2 : {len(gk)}');

                with open('newz.txt','w',encoding="utf-8")as gnewz:

                        
                        for sgk in gk:

                                gnewz.writelines('{}\n'.format(sgk));

                                #print('fine : <b>H: >> {}'.format(sgk.find("H:")));
                                #print('fine : </span><span >> {}'.format(sgk.find("</span><span")));
                            
                                pass   


def readset():

        list_of_output = '';
        isetcount = 0;

        with open('newz.txt','r',encoding="utf-8") as setval:

                sval = setval.readlines();

                with open('V.text','w',encoding="utf-8") as setreport:

                    with open('Royalcpu.text','w',encoding="utf-8") as cpuset:

                        with open('Royalram.text','w',encoding="utf-8") as ramset:

                            with open('Royalnet.text','w',encoding="utf-8") as netset:

                                for x in sval:

                                    if isetcount != 0:

                                        for y in x:
                                
                                
                                            if '<' != y:

                                                list_of_output = list_of_output + y;
                                
                                            else:
                                                

                                                if (isetcount <= 11 ):
                                                    
                                                    cpuset.writelines(format(list_of_output).strip()+"\n");
                                                    setreport.writelines(format(list_of_output).strip()+"\n");
                                                    #print(list_of_output);
                                                    list_of_output = '';
                                                    break;

                                                if isetcount <= 22 :
                                                    
                                                    ramset.writelines(format(list_of_output).strip()+"\n");
                                                    setreport.writelines(format(list_of_output).strip()+"\n");
                                                    #print(list_of_output);
                                                    list_of_output = '';
                                                    break;

                                                if isetcount >= 22 :
                                                
                                                    netset.writelines(format(list_of_output).strip()+"\n");
                                                    setreport.writelines(format(list_of_output).strip()+"\n");
                                                    #print(list_of_output);
                                                    list_of_output = '';
                                                    break;

                                    isetcount=isetcount+1;
                                    
                                    
                                

        print('\n\ncount' ,isetcount);



def notifyLine():
	
	url = 'https://notify-api.line.me/api/notify'
	token = 'XXDGYijBwUe9OAWfnu7AshNWGbQUawhuK79dCanPnv3';
	headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

	with open('Royal.text','r') as target:
		
		downip = target.read();
		strset = (f'Royal Monitor : \n{downip}');
		r = requests.post(url, headers=headers, data = {'message':strset})
		print (r.text);
		#for target_list in downip:

		#	strset = (f'IP : {target_list.strip()} : Down \n');
		#	time.sleep(1)
		#	r = requests.post(url, headers=headers, data = {'message':strset})
		#	print (r.text);
		#	pass



readHTML();
readset();

#setCPUFuntion();
#setRAMFuntion();
#setNETFuntion();
setShowReport();
setReportFile();
setSendReport();

