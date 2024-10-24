import pandas as pd
from enum import Enum
from goldstories.manager import StoryManager

class Topic(Enum):
    """An enumeration of story topics."""
    ANI = "Animals"
    ADV = "Friendship and Adventure"
    MAG = "Magic and Fairy Tales"
    FAM = "Family and Everyday Life"

class PromptGenerator:
    """A class to generate prompts for 2-shot learning using stories from a DataFrame."""

    def __init__(self, df: pd.DataFrame, topic: Topic):
        if not isinstance(topic, Topic):
            raise ValueError(f"Invalid topic: {topic}. Must be one of {list(Topic)}.")
        self.df = df
        self.topic = topic

    def sample_stories(self, n=2) -> pd.DataFrame:
        """Sample up to `n` stories matching the given topic."""
        topic_value = self.topic.value
        stories = self.df[self.df["Topics"].apply(lambda x: topic_value in x)]
        n = min(n, len(stories))
        return stories.sample(n)

    def generate_prompt(self) -> str:
        """Generate a 2-shot learning prompt for the given topic."""
        samples = self.sample_stories(2)

        # Build the prompt
        example_stories = ""
        for _, row in samples.iterrows():
            example_stories += (
                f"Title: {row['Title']}\n"
                f"Story: {row['Story']}\n\n\n"
            )

        # Instruction + examples + query
        prompt = (
            f"Write a bedtime story for children about {self.topic.value}.\n"
            f"Here are two example stories:\n\n"
            f"{example_stories}"
            f"Now, write your own story about {self.topic.value}:"
        )
        return prompt