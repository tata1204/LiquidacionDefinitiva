from flask import Flask, request, render_template, redirect, url_for

import sys
sys.path.append("src")

from model.calculateLogic import Worker
from controller.controller_worker import ControllerWorker

app = Flask(__name__)

# Route to show the main user menu.
@app.route('/')
def menu():
    return render_template('menu.html')

# Route to search for a worker by ID.
@app.route('/buscar_worker', methods=['GET', 'POST'])
def buscar_worker():
    if request.method == 'POST':
        id_buscado = request.form["id"]
        try:
            usuario_buscado = ControllerWorker.BuscarWorkerId(id=id_buscado)
            return render_template("worker.html", worker=usuario_buscado)
        except ValueError as e:
            error_message = str(e)  # Get the error message
            return render_template("mensaje_error_id.html", error_message=error_message)
    else:
        return render_template("buscar_worker.html", mensaje="Ingrese el ID del trabajador:")

# Route to delete a worker by ID.
@app.route('/eliminar_worker', methods=['GET', 'POST'])
def eliminar_worker():
    if request.method == 'POST':
        id_eliminar = request.form["id"]
        ControllerWorker.EliminarWorker(id=id_eliminar)
        return render_template("mensaje_eliminacion_exitosa.html", id_eliminado=id_eliminar)
    return render_template("eliminar_worker.html", mensaje="Eliminar Worker")

# Route to show the successful deletion message.
@app.route('/mensaje_eliminacion_exitosa')
def mensaje_eliminacion_exitosa():
    return render_template("mensaje_eliminacion_exitosa.html")  

# Route to modify a worker's details.
@app.route('/modificar_worker', methods=['GET', 'POST'])
def modificar_worker():
    id_modificar = None
    campo = None
    
    if request.method == 'POST':
        id_modificar = request.form.get("id")
        campo = request.form.get("campo")
        valor = request.form.get("valor")
        ControllerWorker.ModificarWorker(id=id_modificar, modificar=campo, valor=valor)
        return render_template("mensaje_modificacion_exitosa.html", id_modificado=id_modificar, campo_modificado=campo )
    
    return render_template("modificar_worker.html", mensaje="Introduce los datos para modificar al trabajador", id_modificado=id_modificar, campo_modificado=campo)

# Route to show the successful modification message.
@app.route('/mensaje_modificacion_exitosa')
def mensaje_modificacion_exitosa():
    return render_template("mensaje_modificacion_exitosa.html")  

# Route to insert a worker into the database.
@app.route('/insertar_worker', methods=['GET', 'POST'])
def insertar_worker():
    if request.method == 'POST':
        id = request.form["id"]
        salary_base = request.form["salary_base"]
        months_worked = request.form["months_worked"]
        vacation_days = request.form["vacation_days"]
        hours_extra = request.form["hours_extra"]
        hours_extra_nigth = request.form["hours_extra_nigth"]
        days_finish = request.form["days_finish"]
        
        nuevo_worker = Worker(
            id=id, 
            salary_base=salary_base, 
            months_worked=months_worked, 
            vacation_days=vacation_days, 
            hours_extra=hours_extra, 
            hours_extra_nigth=hours_extra_nigth, 
            days_finish=days_finish
        )
        ControllerWorker.InsertarWorker(nuevo_worker)
        return render_template("mensaje_insertar_exitosa.html", id_modificado=id)
    return render_template("insertar_worker.html", mensaje="Insertar Worker")

# Route to show the successful insertion message.
@app.route('/mensaje_insertar_exitosa')
def mensaje_insertar_exitosa():
    return render_template("mensaje_insertar_exitosa.html")  

# Route to calculate the severance pay for a worker.
@app.route('/calcular_liquidacion', methods=['GET', 'POST'])
def calcular_liquidacion():
    if request.method == 'POST':
        id = request.form["id"]
        try:
            liquidacion = ControllerWorker.calculate_liquidacion(worker_id=id)
            # Redirect to the worker details page with the calculated severance pay
            return redirect(url_for('detalle_worker', id=id, liquidacion=liquidacion))
        except Exception as e:
            error_message = str(e)  # Get the error message
            return render_template("mensaje_error_id.html", error_message=error_message)
    return render_template("calcular_liquidacion.html", mensaje="Calcular Liquidación")

# Route to show the details of the worker and their severance pay.
@app.route('/detalle_worker/<id>/<liquidacion>')
def detalle_worker(id, liquidacion):
    worker = ControllerWorker.BuscarWorkerId(id=id)
    return render_template("detalle_worker.html", worker=worker, liquidacion=liquidacion)

# Route to initialize the tables.
@app.route('/inicializar_tablas')
def inicializar_tablas():
    try:
        ControllerWorker.EliminarTabla()
        ControllerWorker.CrearTabla()
    except:
        ControllerWorker.CrearTabla()
    return render_template("mensaje_inicializacion_exitosa.html")

if __name__ == '__main__':
    app.run(debug=True)
