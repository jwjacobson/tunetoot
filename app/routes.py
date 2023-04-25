from app import app, db
from flask import render_template, flash, url_for, redirect, request
from app.forms import TuneForm, SearchForm, RegistrationForm, LoginForm
from app.models import Tune, User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    tunes = Tune.query.all()
    form = SearchForm()
    if form.validate_on_submit():
        search_term = form.search_term.data
        # tunes = Tune.query.filter(Tune.title.ilike(f"%{search_term}%")).all()
        tunes = db.session.execute(db.select(Tune).where((Tune.id.ilike(f"%{search_term}%")) | (Tune.title.ilike(f"%{search_term}%")) | (Tune.composer.ilike(f"%{search_term}%")) | (Tune.key.ilike(f"%{search_term}%")) | (Tune.other_key.ilike(f"%{search_term}%")) | (Tune.song_form.ilike(f"%{search_term}%")) | (Tune.style.ilike(f"%{search_term}%")) | (Tune.meter.ilike(f"%{search_term}%")) | (Tune.year.ilike(f"%{search_term}%")) | (Tune.decade.ilike(f"%{search_term}%")))).scalars().all()
    return render_template("index.html", tunes=tunes, form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        if form.repertoire.data == "Ethan Iverson's 100 Standards":
            for tune in db.session.execute(db.select(Tune).where((Tune.groups.ilike("ethan100")))):
                user.repertoire.append(tune)
        db.session.commit()
        flash(f'User {user.username} registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid credentials')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/tune_entry', methods=['GET', 'POST'])
@login_required
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
        print(title + ' | ' + composer)
        check_tune = db.session.execute(db.select(Tune).filter((Tune.title == title))).scalars().all()
        if check_tune:
            flash(f'Error: A tune called {title} already exists.', "info")
            return redirect(url_for('tune_entry'))
        new_tune = Tune(
            title=title,
            composer=composer,
            key=key,
            other_key=other_key,
            song_form=song_form,
            style=style,
            meter=meter,
            year=year,
            decade=decade
        )
        db.session.add(new_tune)
        current_user.repertoire.append(new_tune)
        db.session.commit()
        flash(f"\"{new_tune.title}\" added to {current_user.username}'s repertoire as Tune {new_tune.id}.", 'info')
        return redirect(url_for('tune_entry'))
    return render_template("tune_entry.html", form=form)

@app.route("/edit_tune/<tune_id>", methods=["GET", "post"])
@login_required
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
        db.session.commit()
        flash(f'Changes saved to Tune {tune_to_edit.id}: "{tune_to_edit.title}."', 'info')
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
    return render_template("edit.html", form=form, tune=tune_to_edit)


@app.route("/delete_tune/<tune_id>")
@login_required
def delete_tune(tune_id):
    tune_to_delete = Tune.query.get_or_404(tune_id)
    current_user.repertoire.remove(tune_to_delete)
    db.session.delete(tune_to_delete)
    db.session.commit()
    flash(f'Tune {tune_to_delete.id}: "{tune_to_delete.title}" deleted from {current_user.username}\'s repertoire.', 'info')
    return redirect(url_for("index"))

@app.route("/options")
@login_required
def options():
    return render_template("options.html")

@app.route("/delete_user/<user_id>")
@login_required
def delete_user(user_id):
    user_to_delete = User.query.get_or_404(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    flash(f'User {user_to_delete.id}: "{user_to_delete.username}" deleted.', 'info')
    return redirect(url_for("index"))