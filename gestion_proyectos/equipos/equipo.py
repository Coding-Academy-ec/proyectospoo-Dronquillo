from gestion_proyectos.proyectos.proyecto import Proyecto

class Equipo(Proyecto):
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, asignado_a, correo):
        super().__init__(nombre, descripcion, fecha_inicio, fecha_fin)
        self.asignado_a = asignado_a
        self.correo = correo

    def __str__(self):
        return f"Objetivo de {super().__str__()}Asignado a: {self.asignado_a}, Con correo grupal: {self.correo}"
