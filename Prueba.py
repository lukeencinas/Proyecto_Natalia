import mysql.connector

cnx = mysql.connector.connect(user='root', 
                            password='',
                            host='localhost',
                            database = 'proyectonatalia')
cursror = cnx.cursor()

cursror.execute("INSERT INTO obras(N_Registro) VALUES(1)")
cnx.commit()