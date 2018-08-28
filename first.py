#!/user/bin/env python
#coding:utf-8

import mysql.connector

# 连接
con = mysql.connector.connect(host='66.98.113.68',user='root',password='suiyi',database='database_test')

#print(con.connection_id)

cursor = con.cursor()

insert1 = ("insert into stu""(id,name,age)"" values (%s,%s,%s)")
cursor.execute(insert1,(4,'Tem',18))
rowid = cursor.lastrowid
#print("rowid=",rowid)

# update1 = "update stu set age=18 where id=2"
# cursor.execute(update1)

# delete1 = "delete from stu where id=2"
# cursor.execute(delete1)


con.commit()

cursor.close()
con.close()


# ("INSERT INTO employees "
#  "(first_name, last_name, hire_date, gender, birth_date) "
#  "VALUES (%s, %s, %s, %s, %s)")
