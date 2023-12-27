
# Libreria

import pymongo

# Conectarse a la BBDD

cliente =  pymongo.MongoClient('mongodb://localhost:27017')
db = cliente['Escuela']
coleccion = db['Alumnos']

# Datos a buscar

datos = {'Nombre': 'Lisa'}
campos = {'Sexo': 'Femenino'}

# Buscar

for documento in coleccion.find(datos, campos):
	print(documento)

cliente.close()