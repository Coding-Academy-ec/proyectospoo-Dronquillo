# Archivo: gestion_tareas/__main__.py
from gestion_proyectos.tareas.tarea import Tarea
from gestion_proyectos.equipos.equipo import Equipo

def main():
    # Ejemplo uno
    proyecto1 = Equipo("Diseñar interfaz de usuario", "Diseñar la interfaz de usuario para la nueva aplicación móvil", "2024-04-15", "2024-08-15", "Equipo de diseño", "drvsolutiostisa@gmail.com")
    tareas = Tarea("Lunes a viernes de 8h00 a 16h00", " 2 personas a fontend y 2 personas a backend")

    # ingresa proyecto usuario
    proyecto2 = Equipo(input("Ingrese Objetivo o nombre del proyecto: "), input("Ingrese una descripcion del proyecto a ejecutar: "), input("Ingrese fecha de inicio del proyecto: "), input("Ingrese fecha de entrega del proyecto: "), input("Ingrese el equipo encargado del desarrollo proyecto: "), input("Ingrese correo grupal del equipo: "))
    tareas2 = Tarea(input("Ingrese dias y horario de reuniones del equipo: "), input("Ingrese numero de personas y tarea de cada grupo del equipo : "))

    # Mostrar detalles de las tareas
    # print("\nEjemplo de Proyecto a ejecución:")
    # print(proyecto1)
    # print(tareas)
    
    print("\nProyecto a ejecución ingresado:")
    print(proyecto2)
    print(tareas2)

if __name__ == "__main__":
    main()
