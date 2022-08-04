def getUserMstAll(connection):
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql = """
        select
            *
        from
            user_mst
    """

    cursor.execute(sql)

    result = cursor.fetchall()

    for user in result:
        print(user)
        print(user.get("user_code"))

def saveUser(connection):
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql = """
        insert into
            user_mst
        values(
            0,
            %s,
            %s,
            %s,
            %s,
            now(),
            now())
    """

    cursor.execute(sql, ('ccc', '1111', '김준사', 'ccc@gmail.com'))
    cursor.execute(sql, ('ddd', '1111', '김준오', 'ddd@gmail.com'))
    cursor.execute(sql, ('eee', '1111', '김준육', 'eee@gmail.com'))
    connection.commit()

def updateUserDtl(connection):
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql = """
        update
            user_dtl
        set
            user_phone = %s,
            user_address = %s,
            user_gender = %s,
            user_age = %s,
            update_date = now()
        where
            user_code = %s
    """

    cursor.execute(sql, ("010-1234-5678", "부산 동래구 온천동", 2, 30, 4))
    connection.commit()

def deleteUser(connection):
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql = """
        delete
        from
            user_mst
        where
            user_code = %s
    """

    cursor.execute(sql, 4)
    connection.commit()

import pymysql
host = '127.0.0.1'
port = 3306
user = 'root'
password = 'toor'
database = 'python_study'

connection = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

updateUserDtl(connection)
#saveUser(connection)
#getUserMstAll(connection)

connection.close()

