class RecetaDTO:
    id = 0
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