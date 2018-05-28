from flask import Blueprint, render_template, request, redirect, url_for

from .forms import *
from models import db, Day

days = Blueprint('days', __name__, static_folder='static',
                 template_folder='templates', url_prefix='/days')


@days.route('/')
def index():
    datas = Day.query.all()
    return render_template('days/index.html', datas=datas)


@days.route('/create', methods=['GET', 'POST'])
def create():
    form = AddForm(request.form)

    if form.validate_on_submit():
        day = Day(name=form.name.data)
        db.session.add(day)
        db.session.commit()
        return redirect(url_for('days.index'))

    return render_template('days/create.html', form=form)


@days.route('/edit/<int:id_day>', methods=['GET', 'POST'])
def edit(id_day):
    day = Day.query.filter_by(id=id_day).first_or_404()

    form = EditForm(request.form, obj=day)

    if form.validate_on_submit():
        day.name = form.name.data
        db.session.commit()
        return redirect(url_for('days.index'))

    return render_template('days/edit.html', form=form)

