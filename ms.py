from flask import Flask, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta básica
@app.route('/')
def home():
    return jsonify({"message": "¡Hola! Bienvenido a tu primer microservicio."})

# Otro endpoint
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return jsonify({"saludo": f"Hola, {nombre}. ¡Bienvenido al microservicio!"})

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
  # Holaaaa


###Empezamos con este desarrollo
