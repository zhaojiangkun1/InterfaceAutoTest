import pymysql


def save_goods_info_to_mysql(info_list):
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        for info in info_list:
            for key, value in info.items():
                sql = "insert into goods(computer_part,computer_info) " \
                      "values (\"%s\",\"%s\")" % (key, value)
                print(sql)
                cursor.execute(sql)
                db_connection.commit()
    finally:
        close_db(db_connection, cursor)


def get_connection():
    db_connction = pymysql.connect(
        host="192.168.1.35",
        user="admin",
        password="123456",
        database="python_ui",
        charset="utf8"
    )
    return db_connction


def close_db(db_connection, cursor):
    cursor.close()
    db_connection.close()