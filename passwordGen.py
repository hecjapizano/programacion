"""
Nombre del alumno: Héctor Jaime García Pizano
Curso: Programación
Grupo: 213032_390
Docente: Ivan Dario Bastidas Castellanos
Este programa genera contraseñas aleatorias con las siguientes espcificaciones:
1. La contraseña debe tener una longitud especificada por el usuario (mínimo 8 caracteres).  
2. Debe incluir al menos un número, una letra mayúscula, una letra minúscula y un carácter especial de la siguiente lista: ¿¡?=)(/ ̈*+-%&$#!.  
3. No se permiten datos repetidos en la contraseña.  
4. La asignación de los datos debe ser completamente aleatoria, es decir, sin un orden específico. 
"""
import random
import string

class GeneradorContrasena:          #Clase para generar contraseñas   
    def __init__(self, longitud):   #Constructor de la clase
        self.longitud = longitud    #Atributo longitud

    def generar(self):                 #Método para generar la contraseña
        #Requerimiento 2 Debe incluir al menos un número, una letra mayúscula, una letra minúscula y un carácter especial
        minusculas = string.ascii_lowercase         #Letras minúsculas
        mayusculas = string.ascii_uppercase         #Letras mayúsculas
        numeros = string.digits                     #Números
        especiales = "¿¡?=)(/ ̈*+-%&$#!"             #Caracteres especiales
        contrasena = [random.choice(minusculas),random.choice(mayusculas), random.choice(numeros), random.choice(especiales)]
        todos_los_caracteres = minusculas + mayusculas + numeros + especiales
        #Requerimiento 3 No se permiten datos repetidos en la contraseña
        caracteres_disponibles = list(set(todos_los_caracteres) - set(contrasena))  #esta linea garantiza que los caracteres no se repiten
        faltantes = self.longitud - len(contrasena)
        
        if faltantes > 0:
            if faltantes <= len(caracteres_disponibles):
                contrasena += random.sample(caracteres_disponibles, faltantes)
            else:
                contrasena += random.choices(caracteres_disponibles, k=faltantes)
        #Requerimiento 4 La asignación de los datos debe ser completamente aleatoria
        random.shuffle(contrasena)
        
        return ''.join(contrasena)

def obtener_longitud_valida():           #Función para obtener la longitud de la contraseña deja en bucle al usuario hasta que ingrese un valor valido
    while True:
        try:
            longitud_str = input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): ")
            longitud = int(longitud_str)
            if longitud < 8:
                print("Error: La longitud debe ser al menos 8 caracteres. Intente de nuevo.")
            else:
                return longitud
        except ValueError:
            print("Error: La longitud debe ser un número entero. Intente de nuevo.")

def main():
    try:                #requerimiento 1 longitud de la contraseña
        longitud = obtener_longitud_valida()
        generador = GeneradorContrasena(longitud)
        contrasena = generador.generar()
        print("Contraseña generada:", contrasena)
        while True:
            nueva_contrasena_resp = input("¿Desea generar otra contraseña? (s/n): ").strip().lower()
            if nueva_contrasena_resp == 's':
                longitud = obtener_longitud_valida()
                generador = GeneradorContrasena(longitud) 
                contrasena = generador.generar()
                print("Contraseña generada:", contrasena)
            elif nueva_contrasena_resp == 'n':
                print("Gracias por usar este generador, ¡Hasta Luego!")
                break
            else:
                print("Por favor, responda con 's' o 'n'.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    except KeyboardInterrupt:
        print("\nInterrupción del programa por el usuario.")

if __name__ == "__main__":
    main()

