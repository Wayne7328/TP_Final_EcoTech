def limpiar_registro_sensor(registro_raw):
    # 1. Inicialización de diccionario vacío para no mutar el original
    registro_limpio = {}

    # 2. Sanitización del Identificador (sensor_id)
    id_crudo = str(registro_raw.get("sensor_id", ""))
    registro_limpio["sensor_id"] = id_crudo.strip()

    # 3. Estandarización de la Temperatura (temperatura)
    temp_cruda = registro_raw.get("temperatura")

    if isinstance(temp_cruda, (int, float)) and not isinstance(temp_cruda, bool):
        registro_limpio["temperatura"] = float(temp_cruda)
    else:
        try:
            temp_texto = (
                str(temp_cruda)
                .upper()
                .replace("C", "")
                .replace("F", "")
                .replace("°", "")
                .replace(" ", "")
                .strip()
            )
            registro_limpio["temperatura"] = float(temp_texto)
        except (ValueError, TypeError):
            registro_limpio["temperatura"] = 0.0

    # 4. Tratamiento del Atributo de Ubicación (ubicacion)
    ubicacion_cruda = registro_raw.get("ubicacion")

    if isinstance(ubicacion_cruda, str) and ubicacion_cruda.strip() != "":
        registro_limpio["ubicacion"] = ubicacion_cruda.strip()
    else:
        registro_limpio["ubicacion"] = "Área No Asignada"

    # 5. Retorno del diccionario estandarizado
    return registro_limpio


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    # Cláusula de guarda ante lista vacía
    if not lista_sensores_limpios:
        return ([], 0.0)

    sumatoria_termica = 0.0
    lista_sensores_alerta = []

    for sensor in lista_sensores_limpios:
        temp_actual = sensor["temperatura"]
        sumatoria_termica += temp_actual

        if temp_actual > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    promedio_temperatura = round(sumatoria_termica / len(lista_sensores_limpios), 2)

    return (lista_sensores_alerta, promedio_temperatura)