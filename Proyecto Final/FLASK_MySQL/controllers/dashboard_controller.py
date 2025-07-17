from models.login_model import CuentaUsuario
from models.course_model import Curso  # adapta al nombre de tu modelo
from datetime import datetime

def obtener_dashboard_info(nombre, rol):
    total_usuarios = CuentaUsuario.query.count()
    total_cursos = Curso.query.count()
    fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M")

    return {
        "nombre": nombre,
        "rol": rol,
        "usuarios": total_usuarios,
        "cursos": total_cursos,
        "fecha": fecha_actual
    }