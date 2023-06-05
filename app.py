from flask import Flask , render_template


# Content Name

# Main
dashboard = 'index.html'
profil = 'profil.html'
news = 'news.html'
people = 'people.html'
todolist = 'todolist.html'

app = Flask(__name__)

@app.route('/')
def Dashboard():
    return render_template(dashboard)

@app.route('/profil')
def Profil() :
    return render_template(profil)

@app.route('/news')
def News() :
    return render_template(news)

@app.route('/people')
def People() :
    return render_template(people)

@app.route('/todolist')
def Todolist() :
    return render_template(todolist)


# app route berhenti disini

if __name__ == '__main__':
    app.run()
