from sensores import limpiar_registro_sensor, generar_resumen_sensores

if __name__ == "__main__":
    # Lote de datos crudos de prueba
    lecturas_crudas = [
        {"sensor_id": " SENSOR-001", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002 ", "temperatura": "31.2°C", "ubicacion": "   "},
        {"sensor_id": "  SENSOR-003  ", "temperatura": 28, "ubicacion": "Planta Sur "},
        {"sensor_id": "SENSOR-004", "temperatura": "85.0 F", "ubicacion": None},
        {"sensor_id": "SENSOR-005", "temperatura": "LECTURA_ERRONEA"}
    ]

    # Paso A: Sanitización de cada registro
    lecturas_limpias = [limpiar_registro_sensor(reg) for reg in lecturas_crudas]

    print("=== 1. REGISTROS NORMALIZADOS ===")
    for reg in lecturas_limpias:
        print(reg)

    # Paso B: Monitoreo y resumen estadístico
    umbral = 25.0
    sensores_en_alerta, promedio_global = generar_resumen_sensores(lecturas_limpias, umbral)

    print("\n=== 2. REPORTE CONSOLIDADO DE PLANTA ===")
    print(f"Umbral configurado       : {umbral} °C")
    print(f"Sensores en alerta (> {umbral}): {sensores_en_alerta}")
    print(f"Promedio térmico global  : {promedio_global} °C")