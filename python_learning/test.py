import mysql.connector                                                                                                          
import method
import requests as rs
import json as js


#get_data_xjllb(reportDateType,reportType,endDate,stockcode):
#按报告期 ReportDateType=0，ReportType=1
#按年度 ReportDateType=1，ReportType=1
#单季度 ReportDateType=0，ReportType=2
                                                                                                                                
stockcode=''                                                                                                                             
f = open('d:\get_test.log', 'w')                                                                                                                                
#数据库连接
conn = mysql.connector.connect(user='root', password='gsc.123', database='test')
cursor = conn.cursor()

codelist = method.get_StockCode(cursor,conn)
#获取资产负债表
for stockcode in codelist:
    zbdict = method.get_data_bfbbb_zb(stockcode[0],stockcode[1],'0',f)
    dicts = method.get_data_bfbbb_lr(stockcode[0],stockcode[1],'0',f)





