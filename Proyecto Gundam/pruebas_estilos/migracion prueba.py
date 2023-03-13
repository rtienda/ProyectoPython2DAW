import sqlite3

# Conectarse a la base de datos original
db_file_original = "gunplaDataNuevasImagenes.sqlite3"
conn_original = sqlite3.connect(db_file_original)
c_original = conn_original.cursor()

# Conectarse a la nueva base de datos
db_file_nuevo = "./instance/gunplaDataNuevasImagenes copy.sqlite3"
conn_nuevo = sqlite3.connect(db_file_nuevo)
c_nuevo = conn_nuevo.cursor()

# Leer los datos de la tabla original
c_original.execute("SELECT * FROM gunpla")
datos_originales = c_original.fetchall()

# Escribir los datos en la nueva base de datos
c_nuevo.executemany("INSERT INTO gunpla VALUES (?, ?, ?, ?, ?, ?, ?, ?)", datos_originales)

# Guardar los cambios
conn_nuevo.commit()

# Cerrar las conexiones
conn_original.close()
conn_nuevo.close()