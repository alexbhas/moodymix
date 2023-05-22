from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from operator import itemgetter
import os
import json

#Setup server and DB
app = Flask(__name__, static_folder='svelte-app/public')

client = MongoClient('mongodb://localhost:27017/')
db = client.moodmix

# Load songs to DB
with open ('songs.json', 'r') as f:
    songs_to_add = json.load(f)

# Only add songs that do not exist yet
for song in songs_to_add:
    if db.songs.count_documents({"id": song["id"]}) == 0:
        db.songs.insert_one(song)

# Serve the static Svelte bundle
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# Get songs
@app.route('/songs', methods=['POST'])
def get_songs():
    data = request.get_json()
    emotions = data.get('emotions')

    # Find songs that match the exact user list first
    songs_with_all_emotions = list(db.songs.find(
        {'tags': {'$all': emotions}},
        {"_id": 0}))

    # Limitting the total returned song count to 10 for now, will add user slider in future
    if len(songs_with_all_emotions) >= 10:
        return jsonify(songs_with_all_emotions[:10])

    ids_with_all_emotions = [song["id"] for song in songs_with_all_emotions]

    # Then find songs that match as many of the tags as possible
    songs_with_some_emotions = list(db.songs.find(
        {'tags': {'$in': emotions}, 'id': {'$nin': ids_with_all_emotions}},
        {"_id": 0}))

    for song in songs_with_some_emotions:
        song['score'] = len(set(song['tags']) & set(emotions))

    # Sort based on tag amount
    songs_with_some_emotions.sort(key=itemgetter('score'), reverse=True)

    # Add the two lists together
    return jsonify(songs_with_all_emotions + songs_with_some_emotions[:10-len(songs_with_all_emotions)])


if __name__ == '__main__':
    app.run(debug=True, port=8000)
