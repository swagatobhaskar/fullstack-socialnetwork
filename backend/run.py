from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# python -m flask --app app run --port 5000 --debug
# or, python run.py
