from crypt import methods
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@notes_db:3306/notes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    note = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Notes {self.id}>' 


@app.route('/',methods=['GET'])
def index():
    print('hi')
    notes = Notes.query.all()
    notes = [note.note for note in notes]
    return render_template('index.html',notes=notes)

@app.route('/add',methods=['POST'])
def add_note():
    note_text = request.form['note']
    note = Notes(note=note_text)
    db.session.add(note)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000, host='0.0.0.0')