
# Libreria

import pymongo

# Conectarse a la BBDD

try:
	cliente = pymongo.MongoClient('mongodb://localhost:27017')
	print('¡Coneccion a Mongo exitosa!')	
	cliente.close()

except pymongo.errors.ConnectionFailure as ErrorConexion:
	print('Fallo al conectarse a MongoDB')