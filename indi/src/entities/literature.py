# -*- coding: UTF-8 -*-
import mysqlConnector

def getLiterature():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select AAID,TI,DE,ID,AB from 6W湿地文献')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def findAdress():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute("select AAID,AU,AF,BA,CA,GP,C1,RP,DI,D2 from 6W湿地文献")
    results = cur.fetchall()
    for result in results:
        if result==None:
            continue
        cur.execute("insert into 6WAddress(AAID,AU,AF,BA,CA,GP,C1,RP,DI,D2) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9]
        ))
    conn.commit()
    cur.close()
    conn.close()

if __name__=="__main__":
    findAdress()
