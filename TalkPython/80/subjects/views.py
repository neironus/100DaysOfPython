from flask import Blueprint, render_template, request, redirect, url_for, \
    abort

from .forms import *
from .models import Subject, db


subjects = Blueprint('subjects', __name__, static_folder='static',
                    template_folder='templates', url_prefix='/subjects')


@subjects.route('/create', methods=['GET', 'POST'])
def create():
    form = AddForm(request.form)

    if form.validate_on_submit():
        day = Subject(name=form.name.data)
        db.session.add(day)
        db.session.commit()
        return redirect(url_for('subjects.index'))

    return render_template('subjects/create.html', form=form)


@subjects.route('/edit/<int:id_day>', methods=['GET', 'POST'])
def edit(id_day):
    day = Subject.query.filter_by(id=id_day).first()

    if not day:
        abort(404)

    form = EditForm(request.form, obj=day)

    if form.validate_on_submit():
        day.name = form.name.data
        db.session.commit()

        return redirect(url_for('subjects.index'))

    return render_template('subjects/edit.html', form=form)

