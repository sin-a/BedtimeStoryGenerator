from flask import Flask, render_template, request
from storygeneration.prompt_generator import Topic
from main import main
import re

app = Flask(__name__)

def clean_text(text):
    """Replaces **bold** syntax with HTML <b> tags and removes 'Story:' from the beginning."""
    # Remove 'Story:' if it exists at the beginning of the text, with or without leading/trailing spaces
    text = re.sub(r'^\s*Story:\s*', '', text, flags=re.MULTILINE)
    # Replace **bold** syntax with <b> tags
    return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

def clean_title(title):
    """Removes 'Title:' if present and cleans any **bold** markers."""
    title = re.sub(r'^Title:\s*', '', title)  # Remove 'Title:' if it exists
    return re.sub(r'\*\*(.*?)\*\*', r'\1', title)  # Remove ** markers

@app.route('/', methods=['GET', 'POST'])
def index():
    topics = [(t.name, t.value) for t in Topic]  # List of topic names and values
    selected_option = None  # Default to None if no selection

    if request.method == 'POST':
        selected_option = request.form.get('dropdown')  # Get the selected option

        # Ensure the selected option matches a valid enum value
        try:
            topic_enum = Topic[selected_option]
        except KeyError:
            return render_template(
                'index.html', topics=topics, selected_option=None, error="Invalid topic selected."
            )

        response = main(topic_enum, 2, 0)  # Generate the story

        # Process the response: first line is title, remaining lines are the story
        title, *story = response.split('\n')
        cleaned_title = clean_title(title)
        story_text = clean_text('\n'.join(story))

        return render_template(
            'index.html', 
            topics=topics, 
            selected_option=selected_option,  # Pass the selected option to the template
            title=cleaned_title, 
            story=story_text
        )

    # Render the form initially without a story
    return render_template('index.html', topics=topics, selected_option=selected_option)

if __name__ == '__main__':
    app.run(debug=False)
