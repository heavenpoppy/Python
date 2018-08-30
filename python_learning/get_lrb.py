# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:16:56 2018

@author: Mr6
"""
                                                                                                                                
import mysql.connector                                                                                                          
import method


#get_data_lrb(companyType,reportDateType,reportType,endDate,stockcode,f):
#按报告期 ReportDateType=0，ReportType=1
#按年度 ReportDateType=1，ReportType=1
#单季度 ReportDateType=0，ReportType=2
                                                                                                                                
stockcode=''                                                                                                                 
endDate=''
endDate1=''
endDate2=''

f = open('d:\get_lrb.log', 'w')                                                                                                                                
#数据库连接
conn = mysql.connector.connect(user='root', password='gsc.123', database='test')
cursor = conn.cursor()

codelist = method.get_StockCode(cursor,conn)
#获取资产负债表
for stockcode in codelist:
    #获取报告期数据
    f.write("==============开始获取  %s 的报告期利润表数据==============\n" %stockcode[0])
    f.flush() 
    dicts = method.get_data_lrb(stockcode[1],'0','1','',stockcode[0],f)
    if(dicts):
        method.insert_data('0',stockcode[0],dicts,'lrb',cursor,conn,f)
        while(dicts and len(dicts)>5):        
            endDate = dicts[-2]['REPORTDATE']
            f.write("code=%s  endDate=%s \n" %(stockcode[0],endDate))
            f.flush()
            dicts = method.get_data_lrb(stockcode[1],'0','1',endDate,stockcode[0],f)
            method.insert_data('0',stockcode[0],dicts[1:6],'lrb',cursor,conn,f)
    #获取年度数据
    f.write("==============开始获取  %s 的年度利润表数据  ==============\n" %stockcode[0])
    f.flush() 
    dicts1 = method.get_data_lrb(stockcode[1],'1','1','',stockcode[0],f)
    if(dicts1):
        method.insert_data('1',stockcode[0],dicts1,'lrb',cursor,conn,f) 
        while(dicts1 and len(dicts1)>5):
            endDate1 = dicts1[-2]['REPORTDATE']
            f.write("code1=%s  endDate1=%s \n" %(stockcode[0],endDate1))
            f.flush()
            dicts1 = method.get_data_lrb(stockcode[1],'1','1',endDate1,stockcode[0],f)
            method.insert_data('1',stockcode[0],dicts1[1:6],'lrb',cursor,conn,f)
     #获取季度数据
    f.write("==============开始获取  %s 的季度利润表数据  ==============\n" %stockcode[0])
    f.flush() 
    dicts2 = method.get_data_lrb(stockcode[1],'0','2','',stockcode[0],f)  
    if(dicts2):
        method.insert_data('2',stockcode[0],dicts2,'lrb',cursor,conn,f) 
        while(dicts2 and len(dicts2)>5):
            endDate2 = dicts2[-2]['REPORTDATE']
            f.write("code2=%s  endDate2=%s \n" %(stockcode[0],endDate2))
            f.flush()
            dicts2 = method.get_data_lrb(stockcode[1],'0','2',endDate2,stockcode[0],f)
            method.insert_data('2',stockcode[0],dicts2[1:6],'lrb',cursor,conn,f)    
    
f.close()  
cursor.close()
conn.close()