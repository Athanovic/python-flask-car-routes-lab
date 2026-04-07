from flask import Flask # type: ignore

# Initialize Flask app
app = Flask(__name__)

# Existing car models in the fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

# Dynamic route for specific car model
@app.route('/<model>')
def model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)