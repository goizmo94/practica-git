import requests
import json

# URL de prueba que simula una API de usuarios
api_url = "https://jsonplaceholder.typicode.com/users"

print(f"Consultando API: {api_url} ...")

try:
    # 1. Hacemos la petición
    respuesta = requests.get(api_url)
    
    # 2. Convertimos el JSON recibido en una lista de Python
    usuarios = respuesta.json()
    
    print(f"Se han encontrado {len(usuarios)} usuarios.")
    
    # 3. Abrimos un archivo para guardar los resultados
    with open("listado_correos.txt", "w") as archivo:
        archivo.write("--- LISTADO DE MIGRACIÓN ---\n")
        
        # 4. Recorremos la lista de usuarios
        for usuario in usuarios:
            nombre = usuario['name']
            email = usuario['email']
            company = usuario['company']['name']
            
            # Imprimimos en pantalla para ver el proceso
            print(f"Procesando: {nombre}...")
            
            # Escribimos en el archivo
            archivo.write(f"{nombre} - {email} ({company})\n")
            
    print("\n✅ Proceso terminado. Revisa el archivo 'listado_correos.txt'")

except Exception as e:
    print(f"❌ Error conectando a la API: {e}")
