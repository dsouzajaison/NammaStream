from flask import jsonify, request
from app import app, db
from app.models import Video

@app.route('/api/videos', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    return jsonify([{'title': video.title, 'url': video.url, 'id': video.id} for video in videos])

@app.route('/api/video/<int:id>', methods=['GET'])
def get_video(id):
    video = Video.query.get_or_404(id)
    return jsonify({'title': video.title, 'url': video.url, 'description': video.description})

@app.route('/api/upload', methods=['POST'])
def upload_video():
    data = request.get_json()
    title = data['title']
    url = data['url']
    description = data.get('description', '')
    
    new_video = Video(title=title, url=url, description=description)
    db.session.add(new_video)
    db.session.commit()
    
    return jsonify({"message": "Video uploaded successfully!"}), 201
