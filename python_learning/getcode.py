import re
import requests as rs
import mysql.connector                                                                                                          

stock_CodeUrl = 'http://quote.eastmoney.com/stocklist.html'

#获取股票代码列表

html = rs.get(stock_CodeUrl).content
    
html = html.decode('gbk')

s = r'<li><a target="_blank" href="http://quote.eastmoney.com/(.*?).html">(.*?)\(\S\S\S\S\S\S\)</a></li>'


conn = mysql.connector.connect(user='root', password='gsc.123', database='test')
cursor = conn.cursor()

pat = re.compile(s)

code = pat.findall(html)


for item in code:
    if item[0][:4]=='sh60' or item[0][:5]=='sz300' or item[0][:4]=='sz00':
        sqlstr = "insert into  codelist(stockcode,stockname) values ('%s','%s')" %(item[0],item[1])
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
