import shutil

# 1. Obtenemos las estadísticas del disco principal
# En Windows suele ser "C:", en Linux "/"
ruta_a_verificar = "/"  # Git Bash simula Linux, así que "/" funciona
total, usado, libre = shutil.disk_usage(ruta_a_verificar)

# 2. Convertimos bytes a Gigabytes (GB) para leerlo mejor
# Dividimos por 1024 tres veces (KB -> MB -> GB)
gb_libre = libre / (1024**3)
gb_total = total / (1024**3)

# 3. Calculamos el porcentaje
porcentaje_libre = (libre / total) * 100

print("--- INSPECTOR DE DISCO ---")
print(f"Espacio Total: {gb_total:.2f} GB")
print(f"Espacio Libre: {gb_libre:.2f} GB ({porcentaje_libre:.2f}%)")

# 4. Lógica de Alerta (Umbral del 20%)
UMBRAL_ALERTA = 20

if porcentaje_libre < UMBRAL_ALERTA:
    print("⚠️  [ALERTA] Espacio en disco CRÍTICO. Libere espacio inmediatamente.")
else:
    print("✅  [OK] Espacio en disco saludable.")
