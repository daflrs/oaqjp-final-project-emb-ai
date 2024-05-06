"""This file is for server"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function.
        """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return 'Invalid input. Try again.'
    return_string_a = f"For the given statement, the system response is 'anger': {anger}, "
    return_string_b = f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
    return_string_c = f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    return return_string_a + return_string_b + return_string_c

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
