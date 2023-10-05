
class CleanerUtil:
    palabras_eliminar = ['muy', 'buenas', 'amigos', 'gusillos', 'recetas','cuando', 'aprendas',\
'estas', 'abrosas', 'recetas', 'no', 'lo', 'comerás', 'de otra', 'manera'\
'Mira', 'mira','Pero', 'si', 'tu', 'casa', 'tienes', 'tendrás', 'que', 'usarlo', 'completo.'\
'Me', 'gustaría', 'saber', 'cómo', 'conoce','mi', 'país', 'república', 'dominicana'\
'conoce', 'como','pero','asimultarte', 'un saludo', 'y un fuerte', 'abrazo', 'próximo video'\
'Reseta fácil', 'deliciosa', 'económica','muy','bien','chicos','deliciosas','Quédate','enseño',
'deliciosos','campeado','preparamos','callate', 'losico', 'quedaron', 'deliciosos','fácil','bienvenidos',\
'desayuno','ensure', 'to', 'perm' ,'managers觉ned', 'Shred', 'exciting','Bluetooth','Sun','Bluetooth',\
'deductір','urgency','trudét', 'laps', 'отп','Sesam', 'sichevél', 'bacterial','vegetal', 'ENP'\
'Gracias', 'me', 'comparten', 'preparaciones', 'Les', 'mando', 'virtual','nos', 'encontramos','vemos','.'\
'favor','cuéntenme', 'hijos', 'mis','encantar','comentarios','foto', 'Instagram','problemas','digestivos',
'niños', 'quieres','ideal','ideales','ganas','saludable','vemos','.', 'Hola,','Hola', 'Vegetable',\
'aside', 'ceilá', 'bakery', 'tbsm', 'tbs', '1.5g','Chao', 'chao,', 'cuíense.','cuídense']


    def cleanTxt(self, txt):
        # Separa el texto en palabras

        palabras = txt.split()

        # Elimina las palabras de la lista de palabras a eliminar
        palabras = [palabra for palabra in palabras if palabra.lower() not in self.palabras_eliminar]

        # Une las palabras restantes en un nuevo texto
        texto_nuevo = " ".join(palabras)

        return texto_nuevo

