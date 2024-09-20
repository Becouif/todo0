from flask import render_template, url_for,redirect,flash
from app import app, db
from app.forms import TodoForm
from app.models import Todo

@app.route('/')
@app.route('/index')
def index():
    statement = db.select(Todo)
    todos = db.session.scalars(statement).all()
    form = TodoForm()
    return render_template('index.html', title="Home", todos=todos, form=form)


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
        return redirect(url_for('index'))
# this is for get method
    return render_template('create.html', title="create", form=form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get_or_404(id)
    form = TodoForm()
    if form.validate_on_submit():
        # update d data
        todo.todo = form.todo.data
        db.session.commit()
        flash('Todo updated successfully!!!')
        return redirect(url_for('index'))

    # this will prepopulate the field with existing data
    form.todo.data = todo.todo
    return render_template('edit.html', title='Edit',form=form)



@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted')
    return redirect(url_for('index'))
