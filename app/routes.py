from app import app, db
from flask import render_template, flash, url_for
from app.forms import TuneForm
from app.models import Tune

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

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
        print(title, composer)
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
    return render_template("entry.html", form=form)