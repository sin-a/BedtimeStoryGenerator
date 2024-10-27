from flask import Flask, render_template, request, jsonify
from storygeneration.prompt_generator import Topic
from main import main, main_test

app = Flask(__name__)

@app.route('/')
def index():
    # Pass Topic enum options to the template
    topics = [(t.name, t.value) for t in Topic]
    return render_template('index.html', topics=topics)

@app.route('/process', methods=['POST'])
def process():
    # Get the option selected by the user
    selected_option = request.form.get('dropdown')

    # Convert the selected topic to Topic enum
    topic_enum = Topic[selected_option]

    # Call main function with the selected topic and parameters
    response = main_test(topic_enum, 5, 3)

    return jsonify(result=response)
    
if __name__ == '__main__':
    app.run(debug=False)
