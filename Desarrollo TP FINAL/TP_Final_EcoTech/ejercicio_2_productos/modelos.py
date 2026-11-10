import json

# ==============================================================================
# Paso 2.1: Diseñar la Excepción Personalizada (StockInvalidoError)
# ==============================================================================
class StockInvalidoError(Exception):
    def __init__(self, mensaje="El stock no puede ser un valor negativo."):
        super().__init__(mensaje)


# ==============================================================================
# Paso 2.2: Diseñar la Clase Base del Catálogo (DispositivoEcologico)
# ==============================================================================
class DispositivoEcologico:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self._stock = 0
        # Regla de consistencia: invoca al setter para validar desde la creación
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(
                f"Error en '{self.nombre}': no se puede asignar un stock de {valor}. El stock no puede ser un valor negativo."
            )
        self._stock = valor

    def generar_ficha_tecnica(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": f"${self.precio:.2f}",
            "stock": self.stock
        }


# ==============================================================================
# Paso 2.3: Diseñar la Subclase Especializada (PanelSolar)
# ==============================================================================
class PanelSolar(DispositivoEcologico):
    def __init__(self, id_producto, nombre, precio, stock, eficiencia, potencia_w):
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self):
        ficha_base = super().generar_ficha_tecnica()
        ficha_base.update({
            "tipo": "Panel Solar Fotovoltaico",
            "potencia_w": f"{self.potencia_w}W",
            "eficiencia": f"{self.eficiencia}%"
        })
        return ficha_base


# ==============================================================================
# Punto B: Persistencia y Gestión del Catálogo (GestorInventario)
# ==============================================================================
class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos_serializados = [disp.generar_ficha_tecnica() for disp in lista_dispositivos]
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos_serializados, archivo, indent=4, ensure_ascii=False)