from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def home_page():
    """Render home page"""
    return render_template('home.html', words=story.prompts)

@app.route('/story')
def your_story():
    """Render your story"""
    your_story = story.generate(request.args)
    return render_template('story.html', your_story=your_story)
