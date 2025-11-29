from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sugerencias.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de sugerencias
class Sugerencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    comentario = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

# Crear BD y tabla
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # cuando se envía el formulario
        email = request.form.get('email')
        comentario = request.form.get('text')

        nueva = Sugerencia(email=email, comentario=comentario)
        db.session.add(nueva)
        db.session.commit()

        return render_template("index.html", mensaje_enviado=True)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
