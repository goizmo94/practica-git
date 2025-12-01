import requests
import datetime

# Función para escribir entradas en el archivo monitor.log
def escribir_log(mensaje, estado="INFO"):
    """Escribe el mensaje con la fecha y el estado en el log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Usamos 'a' (append) para añadir al final del archivo
    with open('monitor.log', 'a') as archivo:
        archivo.write(f"[{timestamp}] [{estado}] {mensaje}\n")

print("--- INICIANDO CHECKEO DE SITIOS WEB ---")
escribir_log("Monitor de URLs iniciado.")

# 1. Leemos el archivo urls.txt línea por línea
try:
    with open('urls.txt', 'r') as f:
        urls = [linea.strip() for linea in f if linea.strip()] # Lee las URLs, quita espacios y líneas vacías
except FileNotFoundError:
    escribir_log("ERROR: El archivo 'urls.txt' no se encuentra.", "ERROR")
    print("ERROR: Archivo de URLs no encontrado.")
    exit() # Detenemos el script

# 2. Procesamos cada URL
for url in urls:
    try:
        # Hacemos la petición HTTP GET (timeout evita que el script se cuelgue)
        response = requests.get(url, timeout=5)
        
        # 3. Lógica para escribir el resultado en el log
        if response.status_code == 200:
            escribir_log(f"URL {url} operativa. Código: 200", "OK")
            print(f"[OK] {url}")
        elif response.status_code >= 400:
            escribir_log(f"URL {url} falló. Código: {response.status_code}", "FALLO")
            print(f"[FALLO] {url}")
        
    except requests.exceptions.RequestException as e:
        # Capturamos errores de red (ej: URL no existe, no hay DNS)
        escribir_log(f"URL {url} es INACCESIBLE. Error: {e.__class__.__name__}", "CRITICO")
        print(f"[CRITICO] {url}")
        
escribir_log("Monitorización completada con éxito.")
print("--- CHECKEO FINALIZADO. VERIFIQUE monitor.log ---")
