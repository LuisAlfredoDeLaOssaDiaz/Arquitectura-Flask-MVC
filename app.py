from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model_document = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

"""
-------------------------------------------------------------------------------------------------------
"""

@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html')

@app.route('/document_detail', methods=['POST'])
def person_detail():
    id_document = request.form['id_document']
    title = request.form['title']
    pag = request.form['pag']
    d = Document(id_document=id_document, title=title, pag=pag)
    model.append(p)
    return render_template('document_detail.html', value=d)


@app.route('/book')
def book():
    data = [(i.id_document, i.title, i.pag) for i in model_document]
    print(data)
    return render_template('book.html', value=data)


if __name__ == '__main__':
    app.run()