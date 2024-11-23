# Indic Be My Eyes: Technical Method Documentation

## Overview
Indic Be My Eyes is an AI-powered visual assistance application designed specifically for users speaking Indic languages. The application processes images through multiple AI models to provide comprehensive scene understanding and converts the results into Indic languages.

## Technical Architecture

### Input Processing
1. Image Input
   - The application accepts images through the web interface
   - Images are stored in the `/uploads` directory
   - Initial processing handled by `image_processor.py`

### Image Analysis Pipeline

#### Scene Text Recognition (BLIP)
- Implementation in `image_detection.py`
- Uses BLIP (Bootstrapping Language-Image Pre-training) model
- Capabilities:
  - Extracts text from images
  - Provides detailed scene descriptions
  - Identifies text in multiple orientations and styles

#### Object Detection (YOLO)
- Implementation in `image_detection.py`
- Uses YOLOv5n model (as indicated by `yolov5n.pt` in the repository)
- Features:
  - Real-time object detection
  - Multiple object class recognition
  - Object count and position information
  - Confidence scores for detections

### Information Processing

#### Summary Generation (LLaMA 3.2)
- Implementation in `summarizer.py`
- Combines information from both BLIP and YOLO
- Process:
  1. Aggregates scene text and object detection results
  2. Generates coherent summary using LLaMA 3.2
  3. Structures information for translation

### Language Processing

#### Translation (Sarvam API)
- Implementation in `translate.py`
- Converts English summaries to Hindi
- Features:
  - Context-aware translation
  - Preservation of technical terms
  - Handling of multiple sentence structures

#### Text-to-Speech Conversion
- Implementation in `speech.py`
- Uses Sarvam API for voice synthesis
- Output:
  - Generates MP3 files (stored as `output.mp3`)
  - Natural-sounding Indic language speech
  - Appropriate pace and pronunciation

## Implementation Flow
1. Web Interface (`templates/index.html`, `static/js/main.js`)
   - User uploads image
   - Displays processing status and results

2. Backend Processing (`routes.py`)
   - Coordinates the processing pipeline
   - Manages API calls and responses
   - Handles error cases and fallbacks

3. Results Delivery
   - Visual feedback on web interface
   - Audio output through speech synthesis
   - Option to replay or process new images

## File Structure Significance
- `/app`: Main application directory
  - `/static`: Frontend assets
  - `/templates`: HTML templates
  - `/uploads`: Temporary image storage
- Configuration files:
  - `config.py`: Application settings
  - `requirements.txt`: Dependencies
  - `run.py`: Application entry point

## Error Handling
- Image validation in `image_processor.py`
- API fallback mechanisms
- User feedback through web interface
- Error logging and monitoring

## Performance Considerations
- Asynchronous processing where possible
- Optimized image processing pipeline
- Caching of frequent translations
- Resource management for concurrent users