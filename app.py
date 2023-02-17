from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexión MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '20cancrilA' #No te pongo mi password
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
        sql = 'SELECT N_Registro,Titulo, archivo_jpg, autor, año, medidas_obra FROM obras'
        cursor.execute(sql)

        artwork = [{'N_Registro':row[0],'title': row[1], 'archivo_jpg': 'img/'+row[2], 'autor':row[3], 'año': row[4], 'medidas' : row[5]} for row in cursor.fetchall()]
        return render_template('obras.html', artworks = artwork)
        
    except Exception as e:
        data['Mensaje'] = 'Error...'
        return e
    



if __name__ == '__main__':
    app.run(debug=True, port=5000)