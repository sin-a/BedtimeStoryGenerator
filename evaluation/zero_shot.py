import pandas as pd
from storygeneration.prompt_generator import Topic
from storygeneration.llm_interaction import LLMManager

class ExperimentZero:
    """A class to generate stories for a given topic using zero-shot learning."""

    def __init__(self, llm_manager: LLMManager):

        self.llm_manager = llm_manager


    def generate_prompt(self, topic:Topic) -> str:
        if topic == Topic.ANY:
            prompt = "Write a bedtime story for children."
        else:
            prompt = f"Write a bedtime story for children about {topic.value}."
        
        return prompt
    
    def generate_story(self, topic:Topic) -> str:
        prompt = self.generate_prompt(topic)
        response = self.llm_manager.query_model(prompt)
        return response
    
    def generate_stories(self, n:int) -> pd.DataFrame:
        zeroshot_df = pd.DataFrame(columns=["Topic", "Story"])
        for topic in Topic:
            for _ in range(n):
                story = self.generate_story(topic)
                zeroshot_df = zeroshot_df.append({"Topic": topic.value, "Story": story}, ignore_index=True)

        return zeroshot_df
    
    def save_stories(self, n:int, filename:str):
        zeroshot_df = self.generate_stories(n)
        zeroshot_df.to_csv(filename, index=False)
        print(f"Stories saved to {filename}")

if __name__ == "__main__":
    llm_manager = LLMManager()
    exp = ExperimentZero(llm_manager)
    exp.save_stories(10, "zeroshot_generated.csv")






