from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine


engine = create_engine(
    "mysql+pymysql://ваш_пользователь:ваш_пароль@localhost/druzja_cheloveka",
    connect_args={"charset": "utf8mb4"}
)


app = Flask(__name__)

@app.route('/')
def index():
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM AllAnimals")
        animals = result.fetchall()
    return render_template('index.html', animals=animals)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']

        with engine.connect() as conn:
            conn.execute(
                "INSERT INTO AllAnimals (name, breed, species, birth_date, gender, health_status, owner_contact, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    name,
                    breed,
                    request.form.get('species', 'Не указано'),  
                    request.form.get('birth_date', None),       
                    request.form.get('gender', 'Не указано'),   
                    request.form.get('health_status', 'Не указано'),
                    request.form.get('owner_contact', 'Не указано'),
                    'Добавлено через форму'
                )
            )
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
