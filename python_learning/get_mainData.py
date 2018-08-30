                                                                                                                                
# -*- coding: utf-8 -*-                                                                                                         
"""                                                                                                                             
Created on Tue May 15 14:49:13 2018                                                                                             
                                                                                                                                
@author: Mr6                                                                                                                    
"""                                                                                                                             
import mysql.connector                                                                                                          
import method
#datatype=0 按报告期 datatype=1 按年度 datatype=2 按季度                                                                 
                                                                                                                                
stockcode=''                                                                                                                 
                                                                                                                                f = open('d:\get_lrb.log', 'w')                                                                                                                                
                                                                                                                                
#数据库连接
conn = mysql.connector.connect(user='root', password='gsc.123', database='test')
cursor = conn.cursor()

codelist = method.get_StockCode(cursor,conn)
#获取主要指标表
for stockcode in codelist:
    
    dicts = method.get_data_main('0',stockcode[0])    
    dicts1 = method.get_data_main('1',stockcode[0])
    dicts2 = method.get_data_main('2',stockcode[0])
    if(dicts):
        method.insert_data('0',stockcode,dicts,'main_financial_indicator',cursor,conn,f)
    if(dicts1):
    method.insert_data('1',stockcode,dicts1,'main_financial_indicator',cursor,conn,f)
    if(dicts2):
    method.insert_data('2',stockcode,dicts2,'main_financial_indicator',cursor,conn,f)
   
cursor.close()
conn.close()

