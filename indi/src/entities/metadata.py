#coding:utf-8
import mysqlConnector

def getMetadata():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select Id,Title,Abstract,Keywords_authors,Keywords_Plus,Combined_Keywords_Phrases from 2497文献元数据')
    results = cur.fetchall()
    cur.close()
    cur.close()
    return results
def findAdress():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute("select Id,Authors_Initials,Authors_Full_Name,Authors,Author_Affiliations_Authors_Organization"
                " , Authors_1st_Full_Name, Author_Affiliations_Full,"
                " Reprint_Author , Reprint_Address_no_name from 2497文献元数据")
    results = cur.fetchall()
    for result in results:
        T=(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8])
        cur.execute("insert 2497Address(Id,Authors_Initials,Authors_Full_Name,Authors,"
                        "Author_Affiliations_Authors_Organization,"
                        "Authors_1st_Full_Name, Author_Affiliations_Full,Reprint_Author,Reprint_Address_no_name) "
                    "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",T)
    conn.commit()
    cur.close()
    conn.close()

if __name__=="__main__":
    findAdress()
