# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:43:39 2018

@author: Mr6
"""

import mysql.connector                                                                                                          
import method
import datetime

stockcode=''                                                                                                                 
inputDate =''
inputStockcode=''
f = open('d:\get_onedata.log', 'w')                                                                                                                                #数据库连接
datatype = '2'

while(len(inputStockcode)!=6 or inputStockcode[0:2] not in ('60','30','00')):
    inputStockcode = input("请输入你要获取的股票代码: ")
if(inputStockcode[0:2] == '60'): 
    stockcode = 'sh%s'%inputStockcode
elif(inputStockcode[0:2] in ('30','00')):
    stockcode = 'sz%s'%inputStockcode


year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day 
while(len(inputDate)!=8 or int(inputDate[0:4])!=year or int(inputDate[4:-2])<month or int(inputDate[6:])>31 or int(inputDate[6:])<1 ):
    inputDate= input("请重新输入你要获取的时间(YYYYMMDD格式): ")
    
year1 = inputDate[0:4]
month1 = inputDate[4:-2]
day1 = inputDate[6:]

reportDate = "%s-%s-%s"%(year1,month1,day1)
reportDate1 = r"%s/%s/%s 0:00:00" %(year1,int(month1),day1)

conn = mysql.connector.connect(user='root', password='gsc.123', database='test')
cursor = conn.cursor()

companyType = method.get_companyType(stockcode,cursor,conn)[0]

f.write("==============开始获取  %s 的 %s 的主表数据==============\n" %(stockcode,reportDate))
f.flush() 
maindicts = method.get_data_main(datatype,stockcode)
maindict = method.get_one_data(maindicts,reportDate)
if(maindict):
    method.delete_onedata(stockcode,datatype,reportDate,'main_financial_indicator',cursor,conn,f)
    method.insert_onedata(datatype,stockcode,maindict,'main_financial_indicator',cursor,conn,f)
    f.write("==============获取  %s 的 %s 的主表数据成功==========\n" %(stockcode,reportDate))
    f.flush() 
else:
    f.write("==============获取  %s 的 %s 的主表数据失败==========\n" %(stockcode,reportDate))
    f.flush()
    
f.write("==============开始获取  %s 的 %s 的资产负债表数据==============\n" %(stockcode,reportDate))
f.flush()
zcfzbdicts = method.get_data_zcfzb(companyType,'0','1','',stockcode,f)
zcfzbdict = method.get_one_data(zcfzbdicts,reportDate1)
if(zcfzbdict):
    method.delete_onedata(stockcode,'0',reportDate1,'zcfzb',cursor,conn,f)
    method.insert_onedata('0',stockcode,zcfzbdict,'zcfzb',cursor,conn,f)
    f.write("==============获取  %s 的 %s 的资产负债表数据成功==========\n" %(stockcode,reportDate))
else:
    f.write("==============获取  %s 的 %s 的资产负债表数据失败==========\n" %(stockcode,reportDate))
    f.flush()
    
f.write("==============开始获取  %s 的 %s 的利润表数据==============\n" %(stockcode,reportDate))
f.flush()
lrbdicts = method.get_data_lrb(companyType,'0','2','',stockcode,f)
lrbdict = method.get_one_data(lrbdicts,reportDate1)
if(lrbdict):
    method.delete_onedata(stockcode,datatype,reportDate1,'lrb',cursor,conn,f)
    method.insert_onedata(datatype,stockcode,lrbdict,'lrb',cursor,conn,f)
    f.write("==============获取  %s 的 %s 的利润表数据成功==========\n" %(stockcode,reportDate))
else:
    f.write("==============获取  %s 的 %s 的利润表数据失败==========\n" %(stockcode,reportDate))
    f.flush()
    
f.write("==============开始获取  %s 的 %s 的现金流量表数据==============\n" %(stockcode,reportDate))
f.flush()
xjllbdicts = method.get_data_xjllb(companyType,'0','2','',stockcode,f)
xjllbdict = method.get_one_data(xjllbdicts,reportDate1)
if(xjllbdict):
    method.delete_onedata(stockcode,datatype,reportDate1,'xjllb',cursor,conn,f)
    method.insert_onedata(datatype,stockcode,xjllbdict,'xjllb',cursor,conn,f)
    f.write("==============获取  %s 的 %s 的现金流量表数据成功==========\n" %(stockcode,reportDate))
else:
    f.write("==============获取  %s 的 %s 的现金流量表数据失败==========\n" %(stockcode,reportDate))
    f.flush()
    
f.write("==============开始获取  %s 的 %s 的百分比报表数据==============\n" %(stockcode,reportDate))
f.flush()
zbdict1 = method.get_data_bfbbb_zb(stockcode,companyType,'2',f)
if(zbdict1):
    method.delete_onedata(stockcode,datatype,reportDate,'bfbbb_zb',cursor,conn,f)
    method.insert_onedata('2',stockcode,zbdict1,'bfbbb_zb',cursor,conn,f)
    f.write("==============获取  %s 的 %s 的百分比报表zb数据成功==========\n" %(stockcode,reportDate))
else:
    f.write("==============获取  %s 的 %s 的百分比报表zb数据失败==========\n" %(stockcode,reportDate))
    f.flush()
    
bfbbbdicts=method.get_data_bfbbb_lr(stockcode,companyType,'2',f) 
bfbbbdict = method.get_one_data(bfbbbdicts,reportDate)
if(bfbbbdict):
    method.delete_onedata(stockcode,datatype,reportDate,'bfbbb_lr',cursor,conn,f)
    method.insert_onedata(datatype,stockcode,bfbbbdict,'bfbbb_lr',cursor,conn,f)
    f.write("==============获取  %s 的 %s 的百分比报表lr数据成功==========\n" %(stockcode,reportDate))
else:
    f.write("==============获取  %s 的 %s 的百分比报表lr数据失败==========\n" %(stockcode,reportDate))
    f.flush()



