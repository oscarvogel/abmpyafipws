# coding: utf-8


import os, sys, time, sqlite3

DB = os.path.join(os.getcwdu(), 'pyfactura.db')

def main():
	creatabla()
	conn = sqlite3.connect(DB)
	cur = conn.cursor()
	# búsqueda secuencial
	t0 = time.time()
	with open("padron.txt", 'r') as fd:
		
		for linea in fd:
			# extraigo los campos del registro
			cuit = linea[0:11]
			denominacion  = linea[11:41]
			imp_g = linea[41:43]
			monotributo = linea[45:47]
			print "CUIT: ", cuit, denominacion, imp_g, monotributo
			query = """
				insert into padron
					(cuit, denominacion, imp_g, monotributo)
					values(?, ?, ?, ?)
			"""
			parametros = (cuit, denominacion.decode('utf8'), imp_g, monotributo)
			conn.execute(query, parametros)
			conn.commit()

	t1 = time.time()
	print "tiempo de búsqueda:", t1-t0, "segundos"

def creatabla():
	conn = sqlite3.connect(DB)
	cur = conn.cursor()
	
	query = """
		drop table if exists padron
	"""
	cur.execute(query)
	
	query = """
		create table padron(
			cuit char(13) PRIMARY KEY,
			denominacion char(50),
			monotributo char(2),
			imp_g char(2)
			);
	"""
	cur.execute(query)

if __name__ == "__main__":
	main()
