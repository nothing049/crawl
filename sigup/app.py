#________SONPIPI________17-5-2023_____
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mail import *
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO,send
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import set_access_cookies
import mysql
app = Flask(__name__)

@app.route('/lovehistory/all', methods=['GET'])
def getDataLoveHistory():
    list_toan_bo_data = []
    list_thong_tin = []
    config = {
                'user': 'root',
                'password': '',
                'host': 'localhost',
                'port': 3306,
                'database': 'sqlmanga'
            }
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connected to MySQL database")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()[0]
            print(f"You are connected to database: {db_name}")
        mycursor = connection.cursor()

        mycursor.execute(f"SELECT * from saved_sukien")
        result2 = mycursor.fetchall()
        print(result2)
        index_get_data = 0
        thong_tin = {}
        for i in range(0, 6):
            thong_tin["id"] = result2[i][0]

            thong_tin["link_nam_goc"] = result2[i][1]

            thong_tin["link_nu_goc"] = result2[i][2]

            thong_tin["link_nam_chua_swap"] = result2[i][3]

            thong_tin["link_nu_chua_swap"] = result2[i][4]

            thong_tin["link_da_swap"] = result2[i][5]

            thong_tin["real_time"] = result2[i][6]

            thong_tin["ten_su_kien"] = result2[i][7]

            thong_tin["noi_dung_su_kien"] = result2[i][8]

            thong_tin["so_thu_tu_su_kien"] = result2[i][10]

            list_thong_tin.append(thong_tin)
            thong_tin = {}
            # Lưu các thay đổi vào database
        connection.commit()
        # mycursor.execute("SELECT thong_tin from skhanhphuc")
        print(mycursor.rowcount, "record inserted.")
        # mycursor1.execute("Select thong_tin from skhanhphuc")x
        # connection.commit()

    except mysql.connector.Error as error:
        print(f"Failed to connect to MySQL database: {error}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
    return list_thong_tin