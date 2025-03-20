from flask import Flask, jsonify

app = Flask(__name__)

alumnos = [
    {"nombre": "Angel Chan", "matricula": "A123456"},
    {"nombre": "Valentina Ortiz", "matricula": "A123457"},
    {"nombre": "Kevin Medina", "matricula": "A123458"},
    {"nombre": "Adjany Armenta", "matricula": "A123459"}
]

profesores = [
    {"nombre": "M.C.C. Daniel Canton ", "numeroEmpleado": "P001"},
    {"nombre": "Lic. Carolina Martinez", "numeroEmpleado": "P002"},
    {"nombre": "Ing. Roberto Diaz", "numeroEmpleado": "P003"},
    {"nombre": "Lic. Patricia Perez", "numeroEmpleado": "P004"}
]

@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    return jsonify(alumnos), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/profesores', methods=['GET'])
def get_profesores():
    return jsonify(profesores), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
