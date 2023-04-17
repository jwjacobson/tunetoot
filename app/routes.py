from app import app, db
from flask import render_template, flash, url_for, redirect
from app.forms import TuneForm, SearchForm
from app.models import Tune

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    tunes = Tune.query.all()
    form = SearchForm()
    if form.validate_on_submit():
        search_term = form.search_term.data
        # tunes = Tune.query.filter(Tune.title.ilike(f"%{search_term}%")).all()
        tunes = db.session.execute(db.select(Tune).where((Tune.id.ilike(f"%{search_term}%")) | (Tune.title.ilike(f"%{search_term}%")) | (Tune.composer.ilike(f"%{search_term}%")) | (Tune.key.ilike(f"%{search_term}%")) | (Tune.other_key.ilike(f"%{search_term}%")) | (Tune.song_form.ilike(f"%{search_term}%")) | (Tune.style.ilike(f"%{search_term}%")) | (Tune.meter.ilike(f"%{search_term}%")) | (Tune.year.ilike(f"%{search_term}%")) | (Tune.decade.ilike(f"%{search_term}%")) | (Tune.knowledge.ilike(f"%{search_term}%")))).scalars().all()
    return render_template("index.html", tunes=tunes, form=form)


@app.route('/entry', methods=['GET', 'POST'])
def entry():
    form = TuneForm()
    if form.validate_on_submit():
        print("Validated.")
        title = form.title.data
        composer = form.composer.data
        key = form.key.data
        other_key = form.other_key.data
        song_form = form.song_form.data
        style = form.style.data
        meter = form.meter.data
        year = form.year.data
        decade = form.decade.data
        knowledge = form.knowledge.data
        print(title + ' | ' + composer)
        check_tune = (
            db.session.execute(
                db.select(Tune).filter(
                    (Tune.title == title)
                )
            )
            .scalars()
            .all()
        )
        if check_tune:
            flash("Tune already exists.")
        new_tune = Tune(
            title=title,
            composer=composer,
            key=key,
            other_key=other_key,
            song_form=song_form,
            style=style,
            meter=meter,
            year=year,
            decade=decade,
            knowledge=knowledge
        )
        db.session.add(new_tune)
        db.session.commit()
        flash(f"Tune {new_tune.title} entered.", 'info')
        return redirect(url_for('entry'))
    return render_template("entry.html", form=form)