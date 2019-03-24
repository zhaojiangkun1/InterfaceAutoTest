import pymysql

# 获取mysql的连接
db_connection = pymysql.connect(
    host="192.168.1.35",
    user="admin",
    password="123456",
    database="python_ui",
    charset="utf8"
)
# 获取游标
cursor = db_connection.cursor()
# 书写sql
sql = "insert into goods(computer_part,computer_info)" \
      " values ('主体','主体信息')"
# 执行sql
cursor.execute(sql)
# 提交sql
db_connection.commit()
# 关闭游标
cursor.close()
# 关闭链接
db_connection.close()
