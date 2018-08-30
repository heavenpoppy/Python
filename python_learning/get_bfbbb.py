# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 23:02:14 2018

@author: Mr6
"""
#get_data_bfbbb_zb(stockcode,companyType,datatype,f)
#get_data_bfbbb_lr(stockcode,companyType,datatype,f)
#datatype=0 按报告期 datatype=1 按年度 datatype=2 按季度                                                                 

import mysql.connector                                                                                                          
import method

stockcode=''                                                                                                                 
f = open('d:\get_bfbbb.log', 'w')                                                                                                                                
#数据库连接
conn = mysql.connector.connect(user='root', password='gsc.123', database='test')
cursor = conn.cursor()

codelist = method.get_StockCode(cursor,conn)
#获取资产负债表
for stockcode in codelist:
    #获取报告期数据
    f.write("==============开始获取  %s 的报告期百分比报表数据==============\n" %stockcode[0])
    f.flush() 
    zbdict = method.get_data_bfbbb_zb(stockcode[0],stockcode[1],'0',f)
    if(zbdict):
        method.insert_onedata('0',stockcode[0],zbdict,'bfbbb_zb',cursor,conn,f)
    dicts = method.get_data_bfbbb_lr(stockcode[0],stockcode[1],'0',f) 
    if(dicts):      
        method.insert_data('0',stockcode[0],dicts,'bfbbb_lr',cursor,conn,f)
    
    #获取年度数据
    f.write("==============开始获取  %s 的年度百分比报表数据  ==============\n" %stockcode[0])
    f.flush() 
    zbdict1 = method.get_data_bfbbb_zb(stockcode[0],stockcode[1],'1',f)
    if(zbdict1):
        method.insert_onedata('1',stockcode[0],zbdict1,'bfbbb_zb',cursor,conn,f)
    dicts1 = method.get_data_bfbbb_lr(stockcode[0],stockcode[1],'1',f) 
    if(dicts1):      
        method.insert_data('1',stockcode[0],dicts1,'bfbbb_lr',cursor,conn,f)        
     #获取季度数据
    f.write("==============开始获取  %s 的季度百分比报表数据  ==============\n" %stockcode[0])
    f.flush() 
    zbdict2 = method.get_data_bfbbb_zb(stockcode[0],stockcode[1],'2',f)
    if(zbdict2):
        method.insert_onedata('2',stockcode[0],zbdict2,'bfbbb_zb',cursor,conn,f)
    dicts2 = method.get_data_bfbbb_lr(stockcode[0],stockcode[1],'2',f) 
    if(dicts2):      
        method.insert_data('2',stockcode[0],dicts2,'bfbbb_lr',cursor,conn,f)          
    
f.close()  
cursor.close()
conn.close()