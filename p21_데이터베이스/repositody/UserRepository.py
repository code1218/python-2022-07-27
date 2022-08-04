from p21_데이터베이스.repositody.DBConnection import DBConnection

class UserRepository:

    dbConnection = None

    def __init__(self):
        self.dbConnection = DBConnection()

    def save(self, userDict):
        try:
            self.dbConnection.connect()
            curs = self.dbConnection.getCursor()

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

            curs.execute(sql, (
                userDict.get("username"),
                userDict.get("password"),
                userDict.get("name"),
                userDict.get("email")
            ))
            self.dbConnection.commit()
        except Exception as e:
            print(e)
        finally:
            self.dbConnection.close()

    def getUserListAll(self):
        result = None
        try:
            self.dbConnection.connect()
            curs = self.dbConnection.getCursor()

            sql = """
                select
                    um.user_code,
                    
                    um.user_id,
                    um.user_password,
                    um.user_name,
                    um.user_email,
                    
                    ud.user_address,
                    ud.user_phone,
                    ud.user_gender,
                    gm.gender_name,
                    ud.user_age
                from
                    user_mst um
                    left outer join user_dtl ud on (ud.user_code = um.user_code)
                    left outer join gender_mst gm on (gm.gender_code = ud.user_gender)
            """

            curs.execute(sql)
            result = curs.fetchall()

        except Exception as e:
            print(e)
        finally:
            self.dbConnection.close()

        return result

    def findUserbyUsername(self, username):
        try:
            self.dbConnection.connect()
            curs = self.dbConnection.getCursor()
            sql = """
                
            """
        except Exception as e:
            print(e)


if __name__ == "__main__":
    repository = UserRepository()
    repository.getUserListAll()

