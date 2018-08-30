# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:13:08 2018

@author: Mr6
"""
                                                                                                                                
import mysql.connector                                                                                                          
import method
#get_data_zcfzb(companyType,reportDateType,reportType,endDate,stockcode,f)
#按报告期 ReportDateType=0，ReportType=1
#按年度 ReportDateType=1，ReportType=1

                                                                                                                                
stockcode=''                                                                                                                 
endDate=''
endDate1=''

f = open('d:\get_zcfzb.log', 'w')                                                                                                                                
#数据库连接
conn = mysql.connector.connect(user='root', password='gsc.123', database='test')
cursor = conn.cursor()

codelist = method.get_StockCode(cursor,conn)
#获取资产负债表
for stockcode in codelist:
    #获取报告期数据
    f.write("==============开始获取  %s 的报告期数据==============\n" %stockcode[0])
    f.flush() 
    dicts = method.get_data_zcfzb(stockcode[1],'0','1','',stockcode[0],f)
    if(dicts):
        method.insert_data('0',stockcode[0],dicts,'zcfzb',cursor,conn,f)
        while(dicts and len(dicts)>5):        
            endDate = dicts[-2]['REPORTDATE']
            dicts = method.get_data_zcfzb(stockcode[1],'0','1',endDate,stockcode[0],f)
            method.insert_data('0',stockcode[0],dicts[1:6],'zcfzb',cursor,conn,f)
    #获取年度数据
    f.write("==============开始获取  %s 的年度数据  ==============\n" %stockcode[0])
    f.flush() 
    dicts1 = method.get_data_zcfzb(stockcode[1],'1','1','',stockcode[0],f)  
    if(dicts1):
        method.insert_data('1',stockcode[0],dicts1,'zcfzb',cursor,conn,f) 
        while(dicts1 and len(dicts1)>5):
            endDate1 = dicts1[-2]['REPORTDATE']
            dicts1 = method.get_data_zcfzb(stockcode[1],'1','1',endDate1,stockcode[0],f)
            method.insert_data('1',stockcode[0],dicts1[1:6],'zcfzb',cursor,conn,f)
    
f.close()  
cursor.close()
conn.close()