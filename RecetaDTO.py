class RecetaDTO:
    id = 0
    origen = ""
    nombre = ""
    imagen = ""
    costo = None
    calorias = None
    ingredientes = None
    texto = ""

    def get_receta_json(self):
        return {
            'nombre':self.nombre
        }
