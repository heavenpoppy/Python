# -*- coding: utf-8 -*-
"""
Created on Tue May 15 15:02:31 2018

@author: Mr6
"""
import requests as rs                                                                                                           
import json as js                                                                                                               
import random

#get_data_main 获取东财的主要财务数据 
#get_data_zcfzb 获取东财的资产负债表
#get_data_lrb 获取东财的利润表
#get_data_xjllb 获取东财的现金流量表
#insert_data 将数据插入数据库

#datatype=0 按报告期 datatype=1 按年度 datatype=2 按季度 
USER_AGENTS = [
#    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
#    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
                                                                
def get_data_main(datatype,stockcode):
    url="http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/MainTargetAjax?ctype=4&type=%s&code=%s" %(datatype ,stockcode)
    return js.loads(rs.get(url).text)


#按报告期 ReportDateType=0，ReportType=1
#按年度 ReportDateType=1，ReportType=1
#单季度 ReportDateType=0，ReportType=2
    
def get_data_zcfzb(companyType,reportDateType,reportType,endDate,stockcode,f):
        
    url="http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/zcfzbAjax?companyType=%s&reportDateType=%s&reportType=%s&endDate=%s&code=%s" %(companyType,reportDateType,reportType,endDate,stockcode)
    
#    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    headers = {'User-Agent': 'User-Agent:%s' %random.sample(USER_AGENTS,1)}
    a=rs.get(url,headers=headers).text
#    a=rs.get(url).text
    vdicts={}
    try:
        vdicts=js.loads(js.loads(a))
    except Exception as e:
        f.write(str(e))
        f.write("\n")
        f.write(str(a))
        f.flush()
    return vdicts

def get_data_lrb(companyType,reportDateType,reportType,endDate,stockcode,f):
    url="http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/lrbAjax?companyType=%s&reportDateType=%s&reportType=%s&endDate=%s&code=%s" %(companyType,reportDateType,reportType,endDate,stockcode)
#    a=rs.get(url).text
    headers = {'User-Agent': 'User-Agent:%s' %random.sample(USER_AGENTS,1)}
    a=rs.get(url,headers=headers).text
    vdicts={}
    try:
        vdicts=js.loads(js.loads(a))
    except Exception as e:
        f.write(str(e))
        f.write("\n")
        f.write(str(a))
        f.flush()
    return vdicts

def get_data_xjllb(companyType,reportDateType,reportType,endDate,stockcode,f):
    url="http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/xjllbAjax?companyType=%s&reportDateType=%s&reportType=%s&endDate=%s&code=%s" %(companyType,reportDateType,reportType,endDate,stockcode)
#    a=rs.get(url).text
    headers = {'User-Agent': 'User-Agent:%s' %random.sample(USER_AGENTS,1)}
    a=rs.get(url,headers=headers).text
    vdicts={}
    try:
        vdicts=js.loads(js.loads(a))
    except Exception as e:
        f.write(str(e))
        f.write("\n")
        f.write(str(a))
        f.flush()
    return vdicts


def get_data_bfbbb_lr(stockcode,companyType,datatype,f):
    url="http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/PercentAjax?code=%s&ctype=%s&type=%s" %(stockcode,companyType,datatype)
#    a=rs.get(url).text
    headers = {'User-Agent': 'User-Agent:%s' %random.sample(USER_AGENTS,1)}
    a=rs.get(url,headers=headers).text
    vdicts={}
    dicts=[]
    i= '0' if companyType=='4' else companyType
    try:
        vdicts = js.loads(a)      
        dicts = vdicts['Result']['lr%s'%i]
    except Exception as e:
        f.write(str(e))
        f.write("\n")
        f.write(str(a))
        f.flush()
    return dicts

def get_data_bfbbb_zb(stockcode,companyType,datatype,f):
    url="http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/PercentAjax?code=%s&ctype=%s&type=%s" %(stockcode,companyType,datatype)
#    a=rs.get(url).text
    headers = {'User-Agent': 'User-Agent:%s' %random.sample(USER_AGENTS,1)}
    a=rs.get(url,headers=headers).text
    vdicts={}
    zbdicts={}
    try:
        vdicts=js.loads(a)
        zbdicts=vdicts['Result']['zb']
    except Exception as e:
        f.write(str(e))
        f.write("\n")
        f.write(str(a))
        f.flush()
    return zbdicts

def get_StockCode(cursor,conn):
    sqlstr ="select stockcode,companyType from codelist"
#    sqlstr ="select stockcode,companyType from codelist where id in (8,1451,937,28,952)"
#    sqlstr = "select stockcode,companyType from codelist where id =613"
    try:
        cursor.execute(sqlstr)
    except Exception as e:
        print('Error:', e)
        conn.close() 
    return cursor.fetchall() 
     
def insert_onedata(datatype,stockcode,dicts,tablename,cursor,conn,f):
    str1='stockcode,'
    str2="'%s'," %stockcode
    for key,num in dicts.items():
        str1+="%s," %key
        str2+="'%s'," %num
    str1+="datatype"
    str2+="'%s'" %datatype
    sqlstr="insert into %s(%s) values (%s)" %(tablename,str1,str2)
    try:
        cursor.execute(sqlstr)
    except Exception as e:
        conn.close()
        f.write("datatype = %s , stockcode = %s\n error:    %s\n" %(datatype,stockcode,str(e)))
        f.write("%s\n\n" %sqlstr)
        f.flush()
        pass            
    conn.commit()
    
def insert_data(datatype,stockcode,dicts,tablename,cursor,conn,f):
    i=0
    while i <len(dicts):                                                                                                            
        str1='stockcode,'
        str2="'%s'," %stockcode
        for key,num in dicts[i].items():
            str1+="%s," %key
            str2+="'%s'," %num
        str1+="datatype"
        str2+="'%s'" %datatype
        sqlstr="insert into %s(%s) values (%s)" %(tablename,str1,str2)
        i+=1                                                                                                                        
        try:
            cursor.execute(sqlstr)
        except Exception as e:
            conn.close()
            f.write("datatype = %s , stockcode = %s\n error:    %s\n" %(datatype,stockcode,str(e)))
            f.write("%s\n\n" %sqlstr)
            f.flush()
            pass            
    conn.commit()
    
def insert_test(datatype,stockcode,dicts,tablename,cursor,conn,f):
    for key,num in dicts[0].items():
        sqlstr="insert into vtest(stockcode,datatype,tablename,keyword)  values ('%s','%s','%s','%s')" %(stockcode,datatype,tablename,key)
        try:
            cursor.execute(sqlstr)
        except Exception as e:
                conn.close()
                f.write("datatype = %s , stockcode = %s\n error:    %s\n" %(datatype,stockcode,str(e)))
                f.write("%s\n\n" %sqlstr)
                f.flush()
                pass            
        conn.commit()

def get_one_data(dicts,reportDate):
    vdict = {}
    if(len(dicts)>0):
        if('date' in dicts[0]):
            if(dicts[0]['date'] == reportDate):
                vdict=dicts[0]
        elif('REPORTDATE' in dicts[0]):
            if(dicts[0]['REPORTDATE'] == reportDate):
                vdict=dicts[0]
    return vdict
def delete_onedata(stockcode,datatype,reportDate,tablename,cursor,conn,f):
    if(tablename == 'zcfzb' or tablename == 'lrb' or tablename == 'xjllb'):
        sqlstr="delete from %s where stockcode='%s' and datatype='%s' and reportdate='%s' " %(tablename,stockcode,datatype,reportDate)
    else:
        sqlstr="delete from %s where stockcode='%s' and datatype='%s' and date='%s' " %(tablename,stockcode,datatype,reportDate)
    try:
        cursor.execute(sqlstr)
    except Exception as e:
        conn.close()
        f.write("datatype = %s , stockcode = %s\n error:    %s\n" %(datatype,stockcode,str(e)))
        f.write("%s\n\n" %sqlstr)
        f.flush()
        pass            
    conn.commit()

def get_companyType(stockcode,cursor,conn):
    sqlstr ="select companyType from codelist where stockcode='%s'" %stockcode
    try:
        cursor.execute(sqlstr)
    except Exception as e:
        print('Error:', e)
        conn.close() 
    return cursor.fetchone() 

    