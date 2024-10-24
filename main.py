from goldstories.manager import StoryManager
from storygeneration.prompt_generator import PromptGenerator, Topic

def main():
    # Create the StoryManager instance
    manager = StoryManager()

    # Get the DataFrame for use in other parts of the application
    df = manager.get_dataframe()

    # Create a PromptGenerator instance for the "Magic and Fairy Tales" topic
    generator = PromptGenerator(df, Topic.MAG)

    # Generate a prompt for the "Magic and Fairy Tales" topic
    prompt = generator.generate_prompt()

    # Print the prompt
    print(prompt)


if __name__ == "__main__":
    main()