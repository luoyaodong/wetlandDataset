import mysqlConnector
def addPosition(wetland_id,wetland_name,position):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute("select * from wetlandGeoFeatures where wetland_id=(%s)",(wetland_id,))
    if count == 1:
        T = (position,wetland_id)
        cur.execute("update wetlandGeoFeatures set position=%s where wetland_id=(%s)",(wetland_id,))
    elif count == 0 :
        T = (wetland_id,wetland_name,position)
        cur.execute("insert into wetlandGeoFeatures(wetland_id,wetland_name,position)",T)
    cur.close
    conn.commit()
    conn.close()


def geoFeatureAdd(wetland_id, wetland_name,coordinate, position, altitude, area):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute("select * from wetlandGeoFeatures where wetland_id=(%s)",(wetland_id,))
    if count == 1:
        T = (wetland_name,position,coordinate,altitude,area,wetland_id)
        cur.execute("update wetlandGeoFeatures set wetland_name=%s,position=%s,coordinate=%s,altitude=%s,area=%s where wetland_id=%s",T)
    elif count == 0:
        T = (wetland_id,wetland_name,position,altitude,area,coordinate)
        cur.execute("insert into wetlandGeoFeatures(wetland_id,wetland_name,position,altitude,area,coordinate) values(%s,%s,%s,%s,%s,%s)",T)
    cur.close()
    conn.commit()
    conn.close()

