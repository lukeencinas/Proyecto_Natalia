from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexión MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' #No te pongo mi password
app.config['MYSQL_DB'] = 'proyectonatalia'

conexion = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obras')
def obras():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT Titulo FROM obras'
        cursor.execute(sql)

        titulos_obras = cursor.fetchall()
        lista_titulos = list(titulos_obras)
        datos_obras = []
        for i in lista_titulos:
            datos_obras += i
        return render_template('obras.html', titulos = datos_obras)
        
    except Exception as e:
        data['Mensaje'] = 'Error...'
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)