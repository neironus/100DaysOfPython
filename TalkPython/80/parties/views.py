from flask import Blueprint, render_template, request, redirect, url_for

from .forms import *
from models import db, Party

parties = Blueprint('parties', __name__, static_folder='static',
                    template_folder='templates', url_prefix='/parties')


@parties.route('/')
def index():
    datas = Party.query.all()
    return render_template('parties/index.html', datas=datas)


@parties.route('/create', methods=['GET', 'POST'])
def create():
    form = AddForm(request.form)

    if form.validate_on_submit():
        party = Party(name=form.name.data)
        db.session.add(party)
        db.session.commit()
        return redirect(url_for('parties.index'))

    return render_template('parties/create.html', form=form)


@parties.route('/edit/<int:id_party>', methods=['GET', 'POST'])
def edit(id_party):
    party = Party.query.filter_by(id=id_party).first_or_404()

    form = EditForm(request.form, obj=party)

    if form.validate_on_submit():
        party.name = form.name.data
        db.session.commit()
        return redirect(url_for('parties.index'))

    return render_template('parties/edit.html', form=form)


@parties.route('/delete/<int:id_party>', methods=['GET'])
def delete(id_party):
    party = Party.query.filter_by(id=id_party).first_or_404()

    db.session.delete(party)
    db.session.commit()

    return redirect(url_for('parties.index'))
