from myapp.app import create_app
# en app, que esta dentro de la carpeta myapp esta la funcion create
if __name__ == "__main__":
    app = create_app() # se crea la aplicacion
    app.run(debug=True) # se ejecuta la aplicacion