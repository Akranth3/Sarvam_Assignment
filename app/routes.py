import os
from flask import render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app import app
from app.image_processor import scene_understanding
from app.image_detection import detect_objects
from app.summarizer import summarize
from app.translate import translate

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Get the scene description
            description = scene_understanding(filepath)
            yolo_info = detect_objects(filepath)

            objects = [i for i in yolo_info['detections']['name']]

            objects = ', '.join(objects)
            # Return just the description string
            final_description = summarize(description, objects)

            hindi = translate(final_description)

            results = {
                'status': 'success',
                'description': hindi
            }
            
            # Clean up
            os.remove(filepath)
            return jsonify(results)
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400