from flask import Blueprint, render_template, request, redirect, url_for, abort

from .forms import *
from models import db, Subject, Recommendation

subjects = Blueprint('subjects', __name__, static_folder='static',
                     template_folder='templates', url_prefix='/subjects')


@subjects.route('/<int:id_subject>', methods=['GET'])
def view(id_subject):
    subject = Subject.query.filter_by(id=id_subject).first_or_404()

    return render_template('subjects/view.html', subject=subject)


@subjects.route('/create', methods=['GET', 'POST'])
def create():
    form = AddForm(request.form)

    if form.validate_on_submit():
        subject = Subject(name=form.name.data, day_id=form.day_id.data.id)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for('subjects.view', id_subject=subject.id))

    return render_template('subjects/create.html', form=form)


@subjects.route('/edit/<int:id_subject>', methods=['GET', 'POST'])
def edit(id_subject):
    subject = Subject.query.filter_by(id=id_subject).first_or_404()

    form = EditForm(request.form, obj=subject)

    if form.validate_on_submit():
        subject.name = form.name.data
        subject.day_id = form.day_id.data.id
        db.session.commit()

        return redirect(url_for('subjects.view', id_subject=subject.id))

    return render_template('subjects/edit.html', form=form)


@subjects.route('/delete/<int:id_subject>', methods=['GET'])
def delete(id_subject):
    subject = Subject.query.filter_by(id=id_subject).first_or_404()

    db.session.delete(subject)
    db.session.commit()

    return redirect(url_for('days.index'))


@subjects.route('/recommendations/<int:id_subject>', methods=['GET', 'POST'])
def recommendations(id_subject):
    subject = Subject.query.filter_by(id=id_subject).first_or_404()

    # recommen = subject.recommendations if subject.recommendations else []
    # print(subject.recommendations)

    form = RecommendationsForm(request.form, id=176, party_ids=[])

    if form.validate_on_submit():
        for r in form.party_ids.data:
            print(r.id)
            rc = Recommendation(
                recommendation=True, party_id=r.id, subject_id=id_subject,
            )
            db.session.add(rc)
            db.session.commit()

        return redirect(url_for('subjects.view', id_subject=id_subject))

        # print(form.recommendations.data)

    return render_template('subjects/recommendations.html', form=form)
