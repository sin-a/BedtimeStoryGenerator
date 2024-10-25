import ollama
from ollama import generate

class LLMManager:
    """Class to manage LLM interactions using ollama.generate()."""

    def __init__(self, model_name='llama3.2'):
        self.model_name = model_name

    def pull_model(self):
        """Pull the specified model using ollama."""
        print(f"Pulling the model: {self.model_name}")
        ollama.pull(self.model_name)
        print(f"Successfully pulled: {self.model_name}")

    def query_model(self, prompt):
        """Query the model with a prompt using ollama.generate() and return the response."""
        response = generate(self.model_name, prompt)
        return response['response']
