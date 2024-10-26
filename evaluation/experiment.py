import pandas as pd
from typing import Optional
from storygeneration.prompt_generator import Topic, PromptGenerator
from storygeneration.llm_interaction import LLMManager
from goldstories.goldstories_manager import StoryManager
import os

# Get the directory where the current script (experiment.py) is located
current_dir = os.path.dirname(os.path.abspath(__file__))

class ExperimentManager:
    """A class to generate stories for a given topic using no keywords or examples."""

    def __init__(self):
        self.llm_manager = LLMManager()
        self.prompt_generator = PromptGenerator()

      
    def _generate_story(self, topic:Topic, n_examples = 0, n_keywords = 0) -> str:
            prompt = self.prompt_generator.generate_prompt(topic, n_examples, n_keywords)
            response = self.llm_manager.query_model(prompt)
            return pd.DataFrame({"Topic": [topic.value], "Prompt": [prompt], "Story": [response]})
            
    
    # Generate n stories for each topic
    def generate_stories(self, n: int, n_examples = 0, n_keywords = 0) -> pd.DataFrame:
        df = pd.DataFrame(columns=["Topic", "Prompt", "Story"])
        for topic in Topic:
            for _ in range(n):
                new_entry = self._generate_story(topic, n_examples, n_keywords)
                df = pd.concat([df, new_entry], ignore_index=True)
        return df
    
    # Generate n stories for each topic, using n_examples examples and n_keywords keywords in the prompt, and save them to a CSV file
    def run_experiment(self, n:int, filename:str, n_examples = 0, n_keywords = 0):
        print(f"Generating {n} stories per topic with {n_examples} example(s) and {n_keywords} keyword(s)")
        df = self.generate_stories(n, n_examples, n_keywords)
        # Create the path to the CSV file and save the DataFrame
        csv_path = os.path.join(current_dir, filename)
        df.to_csv(csv_path, index=False)
        print(f"Stories saved to {csv_path}")

if __name__ == "__main__":
    modelname = 'llama3.1'
    llm_manager = LLMManager(modelname)
    experiment_manager = ExperimentManager()

    experiment_manager.run_experiment(10, f"{modelname}_stories_zero_shot.csv")
    experiment_manager.run_experiment(10, f"{modelname}_stories_keyword.csv", 0, 1)
    experiment_manager.run_experiment(10, f"{modelname}_stories_one_shot.csv", 1, 0)
    experiment_manager.run_experiment(10, f"{modelname}_stories_two_shot.csv", 2, 0)
    experiment_manager.run_experiment(10, f"{modelname}_stories_two_shot_keyword.csv", 2, 1)






