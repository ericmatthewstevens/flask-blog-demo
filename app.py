from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True) ##When declaring debug as True, flask will restart automatically when changes are made.