import os
from modelos import DispositivoEcologico, PanelSolar, GestorInventario, StockInvalidoError

if __name__ == "__main__":
    # 1. Instanciar PanelSolar con parámetros válidos y verificar su ficha técnica polimórfica
    panel = PanelSolar(
        id_producto="PS-001",
        nombre="EcoPanel Monocristalino",
        precio=350.50,
        stock=15,
        eficiencia=22.5,
        potencia_w=450
    )
    turbina = DispositivoEcologico(
        id_producto="DE-002",
        nombre="Aerogenerador Doméstico",
        precio=820.00,
        stock=8
    )

    print("=== 1. FICHA TÉCNICA POLIMÓRFICA (PanelSolar) ===")
    print(panel.generar_ficha_tecnica())

    # 2. Bloque try-except intentando asignar un stock de -5 al objeto
    print("\n=== 2. PRUEBA DE ASIGNACIÓN DE STOCK NEGATIVO (-5) ===")
    try:
        panel.stock = -5
    except StockInvalidoError as error:
        print(f"[ADVERTENCIA CONTROLADA] {error}")
        print(f"Stock resguardado sin cambios: {panel.stock} unidades.")

    # 3. Exportación de los productos válidos a catalogo_ecotech.json
    print("\n=== 3. EXPORTACIÓN DEL CATÁLOGO A JSON ===")
    catalogo = [panel, turbina]
    ruta_json = os.path.join(os.path.dirname(__file__), "catalogo_ecotech.json")

    GestorInventario.guardar_catalogo_json(catalogo, ruta_json)
    print(f"Archivo generado exitosamente en: {ruta_json}")