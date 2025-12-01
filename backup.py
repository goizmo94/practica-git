import os
import shutil
import datetime

# 1. Definimos origen y destino
carpeta_origen = "." # El punto significa "carpeta actual"
carpeta_destino = "backup"

# 2. Creamos la carpeta backup si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)
    print(f"Carpeta '{carpeta_destino}' creada.")

# 3. Obtenemos la fecha de hoy para el nombre
fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")

print(f"--- Iniciando Backup del día {fecha_hoy} ---")

# 4. Buscamos archivos y copiamos
for archivo in os.listdir(carpeta_origen):
    # Solo queremos copiar los .txt y NO queremos copiarnos a nosotros mismos (el script)
    if archivo.endswith(".txt"):
        # Construimos el nuevo nombre: log_2025-01-01.txt
        nuevo_nombre = f"{archivo.replace('.txt', '')}_{fecha_hoy}.txt"
        
        # Definimos las rutas completas
        ruta_origen = os.path.join(carpeta_origen, archivo)
        ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
        
        # Copiamos
        shutil.copy2(ruta_origen, ruta_destino)
        print(f"[COPIADO] {archivo} -> {nuevo_nombre}")

print("--- Backup Finalizado ---")
