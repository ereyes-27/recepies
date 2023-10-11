class RecetaDTO:
    id = 0
    origen = ""
    nombre = ""
    imagen = ""
    costo = None
    calorias = None
    ingredientes = None

    def getRecetaJson(self):
        return {
            'nombre':self.nombre
        }
    def getRecetaFromForm(self, form):
        return {

        }