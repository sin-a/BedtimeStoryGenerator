import pandas as pd
import random
from enum import Enum
from goldstories.goldstories_manager import StoryManager
from typing import Optional


class Topic(Enum):
    """An enumeration of story topics."""
    ANI = "Animals"
    ADV = "Friendship and Adventure"
    MAG = "Magic and Fairy Tales"
    FAM = "Family and Everyday Life"
    ANY = "Any Topic"

# Define the keyword dictionary with keywords for each topic
keywords = {
    Topic.ANI: [
        # Characters
        "a wise owl", "a happy fox", "a playful monkey", "a brave lion", 
        "a curious rabbit", "a clever squirrel", "a friendly bear", 
        "a brave penguin", "a gentle elephant", "a sweet dog",
        "a raccoon", "a parrot", "a calm turtle", 
        "a happy dolphin", "a wolf", "a sleepy sloth", 
        "a helpful badger", "a patient frog", 
        "a caring deer", "a strong bison", "a busy ant", 
        "a clever crow", "a fast cheetah", "a wise snake",
        "a joyful kangaroo", "a protective mother hen", "a grumpy hedgehog", 
        "a shy panda", "a cute cat", "a kind-hearted giraffe",
        "a singing canary", "a chatty duck", "an adventurous otter", 
        "a helpful bee", "a whale", "a giraffe", 
        "a peacock", "a gentle lamb", "a dragonfly", 

        # Settings
        "a forest", "a quiet meadow", "a sparkling lake", 
        "a jungle", "a mountain", "a sunny beach", 
        "a treehouse", "a grassy savannah", 
        "a busy farm", "a winding river", "a rocky cliffside", 
        "a sandy desert", "a wide ocean", 
        "a colorful coral reef", "a snowy hill",
        "a warm campsite", "an old bridge", 
        "a market", "a golden meadow", "a peaceful island", 
        "a leafy forest path", "a moonlit field", 
        "a small seaside village", "a large flower field",
        
        # Objects 
        "a shiny shell", "a wooden raft", "a glittering stone", 
        "a small lantern", "a sturdy rope", 
        "a colorful feather", "a comfy backpack", "a silver acorn", 
        "a delicate mushroom", "a soft blanket", "a yellow scarf"
        "a smooth pebble", "a big leaf", "a warm coat", 
        "a pair of boots", "a bright umbrella", "a fishing net", 
        "a large seashell", "a little basket", "a walking stick",
        "a small wooden boat", "a blue butterfly", 
        "a beautiful flower crown", "a sturdy shield", 
        "a tiny glass bottle", "a fluffy pillow", "a shiny coin", 
        "a red apple", "a musical instrument", "a patchwork quilt", 
        "a wooden staff", "a pair of binoculars", "a glowing gemstone",
        "a colorful kite", "a worn-out book", "a tiny glass jar"
    ],
    
    Topic.ADV: [  # Adventures and Exploration
        # Characters
        "a kind friend", "a brave explorer", "a happy sailor", 
        "a friendly bear", "a curious dog", "a smart parrot", 
        "a playful monkey", "a funny rabbit", "a little explorer", 
        "a singing bird", "a daring fox", "a joyful turtle", 
        "an inventor", "an adventurer", "a kind old lady", 
        "a pirate", "a playful mermaid", "a friendly giant", 
        "a curious storyteller", "a big sister", "a little brother", 
        "a gentle wizard", "a helpful traveler", "a joyful musician", 

        # Settings
        "a hidden cave", "a sunny hill", "a quiet river", 
        "a treehouse by the lake", "a busy harbor", "a small farm", 
        "a grassy field", "a pirate island", "a big forest", 
        "a quiet beach", "a glowing campfire", "a tall lighthouse", 
        "a fishing dock", "a flower meadow", "a warm cabin in the woods", 
        "a treasure island", "a foggy forest", "a tall waterfall", 
        "a sunny desert", "a lively village", "a pirate ship", 
        "a peaceful harbor", "a snowy mountain", "a calm lake", 
        "a glowing forest path", 

        # Objects
        "a red scarf", "a shiny spyglass", "a big backpack", 
        "a fishing pole", "a soft blanket", "a treasure map", 
        "a wooden boat", "a jar of fireflies", "a striped hat", 
        "a colorful kite", "a box of snacks", "a bright lantern", 
        "a pair of boots", "a map", "a compass", "a telescope", 
        "a treasure chest", "a gold coin", "a rope ladder", 
        "binoculars", "a jar of stars", "a pirate’s hat", "a key"
    ],

    Topic.MAG: [  # Magic and Fantasy
        # Characters
        "a kind wizard", "a playful fairy", "a happy dragon", 
        "a magical owl", "a dancing pixie", "a gentle unicorn", 
        "a curious mermaid", "a friendly elf", "a joyful prince", 
        "a daring princess", "a little goblin", "a singing frog", 
        "a brave knight", "a talking owl", "a clever witch", 
        "a joyful pixie", "a happy troll", "a magical wolf", 

        # Settings
        "a glowing forest", "a sparkling lake", 
        "a castle with tall towers", "a field of flowers", 
        "a hidden garden", "a meadow full of butterflies", 
        "a crystal cave", "a wizard's cozy room", 
        "a sunny clearing in the woods", "a small fairy village", 
        "an enchanted castle", "a floating island", 
        "a flower-filled field", "a glowing river", 
        "a school for wizards", 

        # Objects
        "a magic wand", "a bottle of fairy dust", "a glowing crystal", 
        "a flying broomstick", "a shiny crown", "a magic mirror", 
        "a jar of sparkles", "a silver bell", 
        "a pair of enchanted shoes", "a wizard's hat", 
        "a tiny music box", "a magic book", 
        "a sparkling ring", "a feather quill", "a talking mirror", 
        "a golden crown", "a harp"
    ],

    Topic.FAM: [  # Family and Home Life
        # Characters
        "a helpful mom", "a loving dad", "a playful grandma", 
        "a kind grandpa", "a little brother", "a big sister", 
        "a friendly neighbor", "a kind teacher", 
        "a happy mail carrier", "a cheerful coach", 
        "a gentle nurse", "a smiling bus driver", 
        "a fun cousin", 

        # Settings
        "a cozy kitchen", "a sunny living room", "a warm bedroom", 
        "a backyard with swings", "a playroom full of toys", 
        "a school playground", "a quiet library", 
        "a colorful park", "a sandy beach", 
        "a flower garden", "a treehouse", "a grocery store", 

        # Objects
        "a favorite teddy bear", "a soft blanket", 
        "a bedtime storybook", "a lunchbox with a sandwich", 
        "a bright flashlight", "a jump rope", 
        "a red soccer ball", "a pair of slippers", 
        "a school backpack", "a stuffed bunny", 
        "a colorful crayon", "a jar of bubbles", 
        "a family photo", "a pencil", "a bike", 
        "a snack jar"
    ]
}


class PromptGenerator:
    """A class to generate prompts based on a topic and number of examples and keywords."""

    def __init__(self):
        self.df = StoryManager().get_dataframe()

    def _sample_keywords(self, topic: Topic, n: int) -> list:
        """Sample a keyword for the given topic."""
        if topic == Topic.ANY:
            # Randomly pick any topic from the `keywords` dictionary
            random_topic = random.choice(list(keywords.keys()))
            topic_keywords = keywords[random_topic]
        else:
            topic_keywords = keywords[topic]
        
        # Return keyword
        return random.sample(topic_keywords, n)

    def _sample_stories(self, topic: Topic, n: int) -> pd.DataFrame:
        """Sample up to `n` stories matching the given topic."""
        if topic == Topic.ANY:
            stories = self.df
        else:
            stories = self.df[self.df["Topics"].apply(lambda x: topic.value in x)]

        n = min(n, len(stories))
        return stories.sample(n)
    
    def _generate_zeroshot_prompt(self, topic: Topic) -> str:
        if topic == Topic.ANY:
            prompt = "Write a story for children. Use simple, everyday words that children can easily understand. Give the story a title and end with \"The End.\”\n" 
        else:
            prompt = f"Write a story for children about {topic.value}. Use simple, everyday words that children can easily understand. Give the story a title and end with \"The End.\”\n"
        
        return prompt
    
    def _build_intro_examples_str(self, topic: Topic, n_examples) -> str:
        # Sample stories and keywords
        samples = self._sample_stories(topic, n_examples)

        # Build the prompt
        example_stories = ""
        for _, row in samples.iterrows():
            example_stories += (
                f"Title: {row['Title']}\n"
                f"Story: {row['Story']}\n\n"
            )

        intro = (
            "Here is an example of a story for children:\n\n"
            if n_examples == 1
            else f"Here are {n_examples} examples of stories for children:\n\n"
            )
        
        return(f"{intro}"
               f"{example_stories}")

    
    def _generate_prompt_from_keywords(self, topic: Topic, n_keywords) -> str:
        """Generate a prompt using the given keywords."""
        # Build the prompt
        keywords = self._sample_keywords(topic, n_keywords)
        keyword_str = " and ".join(keywords)
        if topic == Topic.ANY:
            prompt = f"Write a story for children. Include {keyword_str}. Use simple, everyday words that children can easily understand. Give the story a title and end with \"The End.\"\n"
        else:
            prompt = f"Write a story for children about {topic.value}. Try to include {keyword_str}. Use simple, everyday words that children can easily understand. Give the story a title and end with \"The End.\"\n"
        return prompt

    def _generate_prompt_from_examples(self, topic: Topic, n_examples) -> str:
        """Generate a n-shot learning prompt for the given topic."""

        # Instruction + examples + query
        prompt = (
            f"{self._build_intro_examples_str(topic, n_examples)}"
            f"Write another story in the same style. Use simple, everyday words that children can easily understand. Give the story a title, introduce the setting and characters and end with \"The End.\"\n"
        )

        return prompt
    
    def _generate_prompt_from_examples_and_keywords(self, topic: Topic, n_examples, n_keywords) -> str:
        """Generate a prompt using examples and keywords."""
        
        keywords = self._sample_keywords(topic, n_keywords)
        keyword_str = " and ".join(keywords)
        
        prompt = (
            f"{self._build_intro_examples_str(topic, n_examples)}"
            f"Write another story in the same style. Try to include {keyword_str}. Use simple, everyday words that children can easily understand. Give the story a title, introduce the setting and characters and end with \"The End.\"\n"
        )
        return prompt
        
    def generate_prompt(self, topic: Topic, n_examples: int = 0, n_keywords: int = 0) -> str:
        if not isinstance(topic, Topic):
            raise ValueError(f"Invalid topic: {topic}. Must be one of {list(Topic)}.")
        if n_examples < 0 or n_keywords < 0:
            raise ValueError("Number of examples and keywords must be non-negative.")
        if n_examples == 0 and n_keywords == 0:
            return self._generate_zeroshot_prompt(topic)
        elif n_examples > 0 and n_keywords == 0:
            return self._generate_prompt_from_examples(topic, n_examples)
        elif n_examples == 0 and n_keywords > 0:
            return self._generate_prompt_from_keywords(topic, n_keywords)
        else:
            return self._generate_prompt_from_examples_and_keywords(topic, n_examples, n_keywords)
   