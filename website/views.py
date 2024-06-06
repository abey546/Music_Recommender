from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from .spotify import authenticate_spotify

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    recommendations = []
    if request.method == 'POST':
        song = request.form.get('song')
        if song:
            recommendations = get_song_recommendations(song)
            if not recommendations:
                flash('No recommendations found, please try another song!', category='error')
        else:
            flash('Please enter a song!', category='error')
    return render_template("home.html", user=current_user, recommendations=recommendations)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

def get_song_recommendations(song_title):
    sp = authenticate_spotify()
    
    # Search for the song on Spotify
    results = sp.search(q=song_title, limit=1)
    if not results['tracks']['items']:
        return []

    song = results['tracks']['items'][0]
    song_id = song['id']
    artist = song['artists'][0]['name']

    # Get recommendations based on the song
    recommendations = sp.recommendations(seed_tracks=[song_id], limit=5)

    recommended_songs = []
    for track in recommendations['tracks']:
        cover_image = track['album']['images'][0]['url'] if track['album']['images'] else "default_image_url"
        recommended_songs.append({
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'image_url': cover_image
        })
    
    return recommended_songs

