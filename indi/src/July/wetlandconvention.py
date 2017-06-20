#coding=utf8
import mysqlConnector

def getmessycode():
    conn = mysqlConnector.getJulyConn()
    cur = conn.cursor()
    cur.execute("select * from 湿地公约乱码")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
def getmessycode3():
    conn = mysqlConnector.getJulyConn()
    cur = conn.cursor()
    cur.execute("select * from 主表乱码3")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

class information_all():
    def getInformation_all(self):
        conn = mysqlConnector.getJulyConn()
        cur = conn.cursor()
        cur.execute("select * from information_all")
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results

    def insert(self, re):
        conn = mysqlConnector.getJulyConn()
        cur = conn.cursor()
        cur.execute("insert into 6W湿地文献错误行(AAID,Z9) values(%s,%s)",(re[0],re[1]))
        conn.commit()
        cur.close()
        conn.close()

        pass
