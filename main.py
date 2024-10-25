from goldstories.manager import StoryManager
from storygeneration.prompt_generator import PromptGenerator, Topic
from storygeneration.llm_interaction import LLMManager

def main():
    # Create the StoryManager instance
    manager = StoryManager()

    # Get the DataFrame for use in other parts of the application
    df = manager.get_dataframe()

    # Create a PromptGenerator instance for the "Magic and Fairy Tales" topic
    generator = PromptGenerator(df, Topic.MAG)

    # Generate a prompt for the "Magic and Fairy Tales" topic
    prompt = generator.generate_prompt()
    print(f"Generated Prompt:\n{prompt}")

    # Create the LLMManager instance
    llm_manager = LLMManager()
    llm_manager.pull_model()  # Ensure the model is pulled

    # Query the model with the generated prompt
    response = llm_manager.query_model(prompt)
    print(f"LLM Response: {response}")

if __name__ == "__main__":
    main()