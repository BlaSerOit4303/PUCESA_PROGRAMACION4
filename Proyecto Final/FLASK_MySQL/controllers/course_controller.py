from flask import render_template, redirect, url_for, flash
from models.course_model import Curso
from extensions import db
from datetime import datetime
from utils.helpers import formatear_fecha

def mostrar_cursos():
    cursos = Curso.query.all()
    fecha = formatear_fecha(datetime.now())
    return render_template("cursos.html", cursos=cursos, fecha=fecha)

def mostrar_formulario_edicion(id):
    curso = Curso.query.get_or_404(id)
    return render_template("editar_curso.html", curso=curso)

def editar_curso(id, form):
    curso = Curso.query.get_or_404(id)
    curso.nombre = form['nombre']
    curso.descripcion = form['descripcion']
    db.session.commit()
    flash("Curso actualizado correctamente", "success")
    return redirect(url_for('cursos.cursos'))

def eliminar_curso(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    flash("Curso eliminado", "info")
    return redirect(url_for('cursos.cursos'))