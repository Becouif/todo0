from flask import render_template, url_for,redirect,flash
from app import app, db
from app.forms import TodoForm
from app.models import Todo

@app.route('/')
@app.route('/index')
def index():
    statement = db.select(Todo)
    todos = db.session.scalars(statement).all()
    return render_template('index.html', title="Home", todos=todos)


@app.route('/create', methods=['GET', 'POST'])
def create():
    # this handle the form and post
    form = TodoForm()
    if form.validate_on_submit():
        # form todo need  data or else it doesnt work
        # asdasd
        new_todo = Todo(todo=form.todo.data)
        db.session.add(new_todo)
        db.session.commit()
        flash('Todo={}'.format(form.todo.data))
        return redirect('/index')
# this is for get method
    return render_template('create.html', title="create", form=form)
