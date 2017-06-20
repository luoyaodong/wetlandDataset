#coding:utf8
import metadata
import mysqlConnector
import wetlandconvention

wetconvention = wetlandconvention.information_all()

class updateLiteratureData():
    def hasABC(self,str):
        try:
            if str == None:
                return False
            int(str)
            return True
        except ValueError:
            return False

    #寻找6w湿地文献数据当中的错误的行
    def findErrorLineData(self):
        conn = mysqlConnector.getConn()
        cur = conn.cursor()
        cur.execute("select AAID,Z9 from 6W湿地文献")
        results = cur.fetchall()
        up = updateLiteratureData()
        for result in results:
            if up.hasABC(result[1]) == False:
                wetconvention.insert(result)
        cur.close()
        conn.close()



if __name__=='__main__':

    up = updateLiteratureData()
    print up.hasABC("12")
    up.findErrorLineData()
