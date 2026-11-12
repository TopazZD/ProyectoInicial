"""
Diccionario de materiales reciclables para EcoVecinos.

Las claves principales coinciden con los filtros de la API de puntos limpios:
glass, paper, paperboard, cardboard_drink, plastic, metal, power_bank, phone

Valores de "se_recicla": "si", "no" o "depende" (varía según el punto limpio).
Son pautas generales: confirma con el punto limpio de tu comuna.
"""

import unicodedata

MATERIALES = {
    "plastic": {
        "nombre": "Plástico",
        "productos": [
            {"nombre": "Botellas de bebida y aceite (PET 1)", "se_recicla": "si", "nota": "Lavar y aplastar"},
            {"nombre": "Botellas de leche, shampoo y detergente (PEAD 2)", "se_recicla": "si", "nota": "Lavar y aplastar"},
            {"nombre": "Potes de yogur, envases de comida y tapas (PP 5)", "se_recicla": "si", "nota": "Lavar"},
            {"nombre": "Pajillas (PP 5)", "se_recicla": "depende", "nota": "Muchos puntos no las reciben por su tamaño"},
            {"nombre": "Tuberías y blísteres (PVC 3)", "se_recicla": "no", "nota": "Pocos puntos los reciben"},
            {"nombre": "Bolsas, films y envolturas (PEBD 4)", "se_recicla": "depende", "nota": "Algunos puntos los reciben, limpios y secos"},
            {"nombre": "Vasos y bandejas desechables (PS 6)", "se_recicla": "no", "nota": ""},
            {"nombre": "Plumavit (poliestireno expandido)", "se_recicla": "no", "nota": ""},
            {"nombre": "Policarbonato, mezclas y bioplásticos PLA (7)", "se_recicla": "no", "nota": ""},
            {"nombre": "Fundas plásticas de celular", "se_recicla": "depende", "nota": "Van con los plásticos, según el tipo"},
        ],
    },
    "glass": {
        "nombre": "Vidrio",
        "productos": [
            {"nombre": "Botellas y frascos transparentes", "se_recicla": "si", "nota": "Sin tapas"},
            {"nombre": "Botellas verdes (vino, cerveza, espumante)", "se_recicla": "si", "nota": "Sin tapas"},
            {"nombre": "Botellas ámbar o café y frascos de farmacia", "se_recicla": "si", "nota": "Sin tapas"},
            {"nombre": "Vidrio plano (ventanas, parabrisas)", "se_recicla": "no", "nota": "Va aparte"},
            {"nombre": "Espejos", "se_recicla": "no", "nota": ""},
            {"nombre": "Ampolletas y tubos fluorescentes, LED", "se_recicla": "no", "nota": "Son residuo especial"},
            {"nombre": "Cerámica y loza (platos, tazas, maceteros)", "se_recicla": "no", "nota": ""},
            {"nombre": "Vidrio refractario (Pyrex, fuentes de horno)", "se_recicla": "no", "nota": ""},
        ],
    },
    "paper": {
        "nombre": "Papel",
        "productos": [
            {"nombre": "Hojas de oficina y cuadernos", "se_recicla": "si", "nota": "Secos y limpios"},
            {"nombre": "Diarios y revistas", "se_recicla": "si", "nota": "Secos y limpios"},
            {"nombre": "Papel con grasa o comida (servilletas, papel sucio)", "se_recicla": "no", "nota": ""},
            {"nombre": "Papel higiénico y toallas de papel", "se_recicla": "no", "nota": ""},
        ],
    },
    "paperboard": {
        "nombre": "Cartón",
        "productos": [
            {"nombre": "Cartón corrugado (cajas de embalaje y mudanza)", "se_recicla": "si", "nota": "Plegado y seco"},
            {"nombre": "Cartulina / paperboard (cajas de cereal, galletas, pasta de dientes, remedios)", "se_recicla": "si", "nota": ""},
            {"nombre": "Cartón de huevos", "se_recicla": "si", "nota": "Limpio y seco"},
            {"nombre": "Tubos de cartón (rollos de papel higiénico y toalla)", "se_recicla": "si", "nota": ""},
            {"nombre": "Cajas de pizza o comida rápida sucias", "se_recicla": "no", "nota": ""},
            {"nombre": "Cartón encerado o plastificado", "se_recicla": "no", "nota": ""},
            {"nombre": "Cartón mojado o con moho", "se_recicla": "no", "nota": ""},
        ],
    },
    "cardboard_drink": {
        "nombre": "Tetrapak",
        "productos": [
            {"nombre": "Cajas de leche y jugo", "se_recicla": "depende", "nota": "Enjuagar y aplastar"},
            {"nombre": "Cajas de vino y bebidas", "se_recicla": "depende", "nota": "Enjuagar y aplastar"},
            {"nombre": "Cajas de salsa, sopa, crema y leche vegetal", "se_recicla": "depende", "nota": "Enjuagar y aplastar"},
            {"nombre": "Tapas plásticas de las cajas", "se_recicla": "depende", "nota": "Según el punto, van puestas o con los plásticos"},
            {"nombre": "Pajillas pegadas a la caja", "se_recicla": "no", "nota": "Sacarlas antes de entregar"},
        ],
    },
    "metal": {
        "nombre": "Metal",
        "productos": [
            {"nombre": "Latas de bebida (aluminio)", "se_recicla": "si", "nota": ""},
            {"nombre": "Papel aluminio limpio", "se_recicla": "si", "nota": ""},
            {"nombre": "Latas de conserva y tapas metálicas (hojalata)", "se_recicla": "si", "nota": ""},
            {"nombre": "Aerosoles vacíos", "se_recicla": "depende", "nota": ""},
            {"nombre": "Cobre, bronce y fierro", "se_recicla": "si", "nota": "En chatarrerías, no en puntos limpios comunes"},
        ],
    },
    "power_bank": {
        "nombre": "Baterías",
        "productos": [
            {"nombre": "Pilas alcalinas (AA, AAA, C, D, 9V)", "se_recicla": "si", "nota": "En puntos de acopio, nunca al basurero"},
            {"nombre": "Pilas de botón", "se_recicla": "si", "nota": "En puntos de acopio"},
            {"nombre": "Pilas recargables NiMH", "se_recicla": "si", "nota": "En puntos de acopio"},
            {"nombre": "Baterías de ion de litio (celulares, power banks, notebooks, vapers, parlantes)", "se_recicla": "si", "nota": "Tapar los bornes; no perforar ni aplastar"},
            {"nombre": "Baterías de auto o moto (plomo-ácido)", "se_recicla": "si", "nota": "En talleres o centros de acopio autorizados"},
            {"nombre": "Baterías hinchadas o dañadas", "se_recicla": "depende", "nota": "Llamar antes, por riesgo de incendio"},
        ],
    },
    "phone": {
        "nombre": "Teléfonos y electrónicos",
        "productos": [
            {"nombre": "Celulares", "se_recicla": "si", "nota": "Borrar datos y sacar la SIM"},
            {"nombre": "Cargadores, cables y audífonos", "se_recicla": "si", "nota": "En acopio de electrónicos"},
            {"nombre": "Tablets y relojes inteligentes", "se_recicla": "si", "nota": "En acopio de electrónicos"},
            {"nombre": "Power banks", "se_recicla": "si", "nota": "Se tratan como baterías de litio"},
            {"nombre": "Teléfonos que aún funcionan", "se_recicla": "si", "nota": "Mejor donar o reparar primero"},
        ],
    },
    "otros": {
        "nombre": "Otros residuos",
        "productos": [
            {"nombre": "Aceite de cocina usado", "se_recicla": "si", "nota": "En puntos de acopio, nunca por el desagüe"},
            {"nombre": "Textiles (ropa y zapatos)", "se_recicla": "si", "nota": "Donación o puntos de reciclaje textil"},
        ],
    },
}


def _normalizar(texto):
    """Pasa a minúsculas y quita tildes: 'Cartón' -> 'carton'."""
    texto = unicodedata.normalize("NFD", texto.lower().strip())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def filtrar_por_material(claves, solo_reciclables=False):
    """
    Devuelve los materiales cuyas claves se indican.
    Ejemplo: filtrar_por_material(["glass", "metal"])
    Si solo_reciclables=True, deja solo los productos con se_recicla == "si".
    """
    resultado = {}
    for clave in claves:
        material = MATERIALES.get(clave)
        if not material:
            continue
        productos = material["productos"]
        if solo_reciclables:
            productos = [p for p in productos if p["se_recicla"] == "si"]
        resultado[clave] = {"nombre": material["nombre"], "productos": productos}
    return resultado


def buscar_producto(texto, claves=None):
    """
    Busca un producto por texto (ignora mayúsculas y tildes).
    Si se pasa 'claves', busca solo dentro de esos materiales.
    Ejemplo: buscar_producto("botella", ["glass", "plastic"])
    """
    consulta = _normalizar(texto)
    if not consulta:
        return []

    resultados = []
    for clave, material in MATERIALES.items():
        if claves and clave not in claves:
            continue
        for producto in material["productos"]:
            if consulta in _normalizar(producto["nombre"]):
                resultados.append({
                    "material_clave": clave,
                    "material": material["nombre"],
                    **producto,
                })
    return resultados


if __name__ == "__main__":
    print(buscar_producto("botella"))
    print(filtrar_por_material(["glass"], solo_reciclables=True))
