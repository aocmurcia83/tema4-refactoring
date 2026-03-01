"""
Programa de gestión de notas de alumnos.
Autor: Andrés Ortuño Carrelón
Fecha: 28/02/2026

Este programa calcula la media de tres notas,
muestra la información del alumno y determina su calificación.
"""

def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres notas.

    Args:
        nota1 (float): Primera nota.
        nota2 (float): Segunda nota.
        nota3 (float): Tercera nota.

    Returns:
        float: Media de las tres notas.
    """
    return (nota1 + nota2 + nota3) / 3


def evaluar_aprobado(media):
    """
    Determina si la media es aprobada o suspendida.

    Args:
        media (float): Nota media del alumno.

    Returns:
        bool: True si está aprobado, False si está suspendido.
    """
    if media >= 5:
        print("aprobado")
        return True
    else:
        print("suspendido")
        return False


def obtener_calificacion(media):
    """
    Devuelve la calificación textual según la media.
    """
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"


def mostrar_alumno(nombre, nota1, nota2, nota3):
    """
    Muestra por pantalla la información completa del alumno.
    """
    print("Alumno: " + nombre)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))

    media = calcular_media(nota1, nota2, nota3)  # Se reutiliza función

    print("Media: " + str(media))
    print(obtener_calificacion(media))  # Se delega la lógica
    print("----------------------")


def main():
    """
    Función principal del programa.
    """
    mostrar_alumno("Ana García", 8, 7, 9)
    mostrar_alumno("Luis Pérez", 4, 5, 3)
    mostrar_alumno("Marta Gómez", 6, 7, 5)


if __name__ == "__main__":
    main()