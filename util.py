import mysql.connector
address = 'localhost'
username = 'root'
password = ''
db = 'streamer'
class ConnectToDB():
    
    def connect(self):
        mydb = mysql.connector.connect(
            host = address,
            user = username,
            passwd = password,
            database = db
        )
        return mydb