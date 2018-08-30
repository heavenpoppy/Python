# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 09:07:41 2018

@author: Mr6
"""

import re
import requests as rs
import mysql.connector                                                                                                          
import method

conn = mysql.connector.connect(user='root', password='gsc.123', database='test')
cursor = conn.cursor()

codelist = method.get_StockCode(cursor,conn)

for stockcode in codelist:     
    stock_CodeUrl="http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=soft&code=%s" %stockcode[0]  
    html = rs.get(stock_CodeUrl).content  
    html = html.decode('utf-8')
    s = r'<input id="hidctype" type="hidden" value="(.*?)" />'
    pat = re.compile(s)
    code = pat.findall(html)
    for item in code:
        sqlstr = "update codelist set companyType = '%s' where stockcode = '%s'" %(item[0],stockcode[0])
        try:
            cursor.execute(sqlstr)
        except Exception as e:
            print('Error:', e)
            conn.close()  
            break
    conn.commit()
cursor.close()
conn.close()


#allCodelist = urlTolist(stock_CodeUrl)

#print(allCodelist)
