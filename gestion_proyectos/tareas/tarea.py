# Archivo: gestion_proyectos/tareas/tarea.py

class Tarea:
    def __init__(self, horario_reuniones, planificacion):
        self.horario_reuniones = horario_reuniones
        self.planificacion = planificacion

    def __str__(self):
        return f"Horario de Reuniones: {self.horario_reuniones}\nPersonal encargado: {self.planificacion}"
