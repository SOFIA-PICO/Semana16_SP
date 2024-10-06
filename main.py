# Escritura de Archivo de Texto
# Creamos un archivo nuevo llamado "my_notes.txt" y escribimos tres líneas de notas personales.

def escribir_archivo():
    # Abrimos el archivo en modo de escritura ('w' para escribir).
    with open("my_notes.txt", "a") as archivo:
        # Pedimos al usuario que ingrese tres líneas de texto.
        for i in range(1, 4):
            nota = input(f"Ingrese la línea {i} de sus notas personales: ")
            archivo.write(nota + "\n")  # Escribimos cada línea en el archivo con un salto de línea al final.
    # No es necesario cerrar manualmente el archivo porque 'with' lo hace automáticamente.


# Lectura de Archivo de Texto
# Abrimos el archivo "my_notes.txt" y leemos su contenido línea por línea.

def leer_archivo():
    # Abre el archivo en modo de lectura ('r' para leer).
    with open("my_notes.txt", "r") as archivo:
        # Leer el contenido línea por línea.
        linea = archivo.readline()  # Leer la primera línea
        while linea:
            # Mostrar en la consola cada línea leída.
            print(linea.strip())  # 'strip()' elimina los saltos de línea extra al imprimir
            linea = archivo.readline()  # Leer la siguiente línea


# Función principal para ejecutar las dos operaciones
def main():
    print("Escribiendo en el archivo 'my_notes.txt'...")
    escribir_archivo()

    print("\nLeyendo del archivo 'my_notes.txt'...")
    leer_archivo()


# Ejecutar la función principal
if __name__ == "__main__":
    main()