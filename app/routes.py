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


@app.route('/tune_entry', methods=['GET', 'POST'])
def tune_entry():
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
        flash(f"Tune {new_tune.id}, \"{new_tune.title}\", entered.", 'info')
        return redirect(url_for('entry'))
    return render_template("entry.html", form=form)

@app.route("/edit_tune/<tune_id>", methods=["GET", "post"])
def edit_tune(tune_id):
    form = TuneForm()
    tune_to_edit = Tune.query.get_or_404(tune_id)
    if form.validate_on_submit():
        tune_to_edit.title = form.title.data
        tune_to_edit.composer = form.composer.data
        tune_to_edit.key = form.key.data
        tune_to_edit.other_key = form.other_key.data
        tune_to_edit.song_form = form.song_form.data
        tune_to_edit.style = form.style.data
        tune_to_edit.meter = form.meter.data
        tune_to_edit.year = form.year.data
        tune_to_edit.decade = form.decade.data
        tune_to_edit.knowledge = form.knowledge.data
        db.session.commit()
        flash("Changes saved.", "info")
        return redirect(url_for("index"))

    form.title.data = tune_to_edit.title
    form.composer.data = tune_to_edit.composer
    form.key.data = tune_to_edit.key
    form.other_key.data = tune_to_edit.other_key
    form.song_form.data = tune_to_edit.song_form
    form.style.data = tune_to_edit.style
    form.meter.data = tune_to_edit.meter
    form.year.data = tune_to_edit.year
    form.decade.data = tune_to_edit.decade
    form.knowledge.data = tune_to_edit.knowledge
    return render_template("edit.html", form=form, tune=tune_to_edit)


@app.route("/delete/<entry_id>")
def delete_entry(entry_id):
    entry_to_delete = Entry.query.get_or_404(entry_id)
    if entry_to_delete.submitter != current_user:
        flash("You are not authorized to delete this entry.", "dark")
        return redirect(url_for("index"))

    db.session.delete(entry_to_delete)
    db.session.commit()
    flash(
        'Entry deleted.',
        "info",
    )
    return redirect(url_for("index"))
