#coding:utf-8
import MySQLdb

import mysqlConnector


def cutPeopleName(str):
     try:
        newlist = []
        list = str.split(' ')
        for l in list:
            if l == '':
                continue
            if l == None:
                continue
            if l.find('.')!=-1:
                return ' '.join(newlist)
            else:
                newlist.append(l)
     except ValueError:
        return str



def getPlantsSciName():
    conn=mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select Scientific_name from 中国植物志')
    print count
    results = cur.fetchall()
    name = []
    for r in results:
        for n in r:
            name.append(cutPeopleName(n))
    cur.close()
    conn.close()
    return name
def getPlantsSynonym():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select 物种名称,拉丁名_全称,别名,异名 from 中国湿地植物别名与异名')
    results = cur.fetchall()
    # print results
    return results

def getChinesePlantName():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute("select 拉丁名全称 from 中国湿地植物")
    results = cur.fetchall()
    name = []
    for r in results:
        for n in r:
            name.append(n)
    cur.close()
    conn.close()
    return name

if __name__ == '__main__':
    #getPlantsSynonym()
    print cutPeopleName("Vanilla fragrans (Salisb.) Ames")
