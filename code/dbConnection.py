from mysql.connector import connect,Error
def dbConnect():
    try:
        return connect(host='localhost',user='root',password='dorsa_soleymani78',database='shopping')
    except Error as error:
       print(error) 