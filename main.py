import argparse
from enum import Enum
from goldstories.goldstories_manager import StoryManager
from storygeneration.prompt_generator import PromptGenerator, Topic
from storygeneration.llm_interaction import LLMManager

def check_valid_response(response: str) -> bool:
    """Check if the response ends with 'The End' or 'The End.'."""
    return response.strip().endswith(("The End", "The End."))

# Define the main function
def main(topic: Topic, n_examples: int, n_keywords: int):
    llm_manager = LLMManager()
    prompt_generator = PromptGenerator()

    prompt = prompt_generator.generate_prompt(topic, n_examples, n_keywords)

    # Retry mechanism to get a valid response
    for attempt in range(4):
        response = llm_manager.query_model(prompt)

        if check_valid_response(response):
            print(f"Prompt: {prompt}")
            print(f"Response: {response}")
            return response  # Return the valid response

        print(f"Invalid response on attempt {attempt + 1}, retrying...")

    # If no valid response after all retries, raise an error or handle it appropriately
    raise ValueError("Failed to generate a valid story after maximum retries.") 

# Helper function to convert command-line input to Topic enum
def topic_enum(value: str) -> Topic:
    try:
        return Topic[value.upper()]  # Convert input to uppercase to match the enum keys
    except KeyError:
        raise argparse.ArgumentTypeError(f"Invalid topic: {value}. Choose from {', '.join(t.name for t in Topic)}.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Generate a story prompt and query the LLM.")

    # Define expected arguments
    parser.add_argument(
        "--topic", type=topic_enum, default = Topic.ANY,
        help=f"Topic for the story prompt. Choose from: {', '.join(t.name for t in Topic)}."
    )
    parser.add_argument("--n_examples", type=int, default = 1, help="Number of examples to use.")
    parser.add_argument("--n_keywords", type=int, default = 0, help="Number of keywords to use.")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Call main with parsed arguments
    main(args.topic, args.n_examples, args.n_keywords)
