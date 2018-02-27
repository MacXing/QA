import pymysql

def connMySql():

    db = pymysql.connect("192.168.160.36", "root", "gzxiaoi", "wordvec")

    cursor = db.cursor()
    # sql = "INSERT INTO word('word','vec')VALUES ('demo','demo')"
    sql = "SELECT * FROM word"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            id = row[0]
            word = row[1]
            vec=row[2]
            # 打印结果
            print("id=%s,word=%s,vec=%s" %(id, word,vec))
        db.commit()
    except:
        db.rollback()

    db.close()

if __name__ == '__main__':
    connMySql()