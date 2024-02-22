import os #para trabajar con sistemas operativos
import re #Para trabajar expresiones regulares en python

#Clase para coontar palabras en archivos de una carpeta, y en la carpeta
class ContadorPalabras:

    #Función principal para establecer los atributos del objeto
    def __init__(self, carpeta, palabra):
        self.carpeta = carpeta
        self.palabra = palabra

    #Función para contar las palabras en un archivo
    def contar_en_archivo(self, archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                palabras = re.split(r'\W+', contenido)  # Usar expresión regular para dividir palabras
                contador = palabras.count(self.palabra)
                print(f"En el archivo {archivo}: {contador} veces.")
                return contador
        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado.")
            return 0

    #Función para contar las palabras a nivel de carpeta
    def contar_en_carpeta(self):
        total = 0
        if os.path.exists(self.carpeta):
            for archivo in os.listdir(self.carpeta):
                if archivo.endswith(('.txt', '.xml', '.json', '.csv')):
                    archivo_path = os.path.join(self.carpeta, archivo)
                    total += self.contar_en_archivo(archivo_path)
                    print(f"Total en la carpeta: {total} veces.")
                else:
                    print("La carpeta no contiene un archivo de texto") 
        else:
            print(f"La carpeta {self.carpeta} no existe.")

def main():
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")
    
    contador = ContadorPalabras(carpeta, palabra)
    contador.contar_en_carpeta()

if __name__ == "__main__":
    main()
