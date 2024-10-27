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
        "a wise owl", "a mischievous fox", "a playful monkey", "a brave lion", 
        "a curious rabbit", "a clever squirrel", "a friendly bear", 
        "an adventurous penguin", "a gentle elephant", "a loyal dog",
        "a sneaky raccoon", "a talkative parrot", "a calm turtle", 
        "a happy dolphin", "a courageous wolf", "a sleepy sloth", 
        "a helpful badger", "a patient frog", 
        "a caring deer", "a strong bison", "a determined ant", 
        "a clever crow", "a fast cheetah", "a wise snake",
        "a joyful kangaroo", "a protective mother hen", "a grumpy hedgehog", 
        "a shy panda", "a fearless cat", "a kind-hearted giraffe",
        "a singing canary", "a chatty duck", "an adventurous otter", 
        "a helpful bee", "a smiling whale", "a thoughtful giraffe", 
        "a proud peacock", "a gentle lamb", "an energetic dragonfly", 

        # Settings
        "a forest", "a quiet meadow", "a sparkling lake", 
        "a deep jungle", "a tall mountain", "a sunny beach", 
        "a lush garden", "a small village", 
        "a cozy den", "a tall treehouse", "a grassy savannah", 
        "a busy farm", "a winding river", "a rocky cliffside", 
        "a sandy desert", "a wide ocean", 
        "a colorful coral reef", "a snowy hill", "a peaceful pond", 
        "a warm campsite", "an old bridge", 
        "a bustling market", "a foggy marsh", "a crystal-clear stream", 
        "a sunny orchard", "a golden meadow", "a peaceful island", 
        "a leafy forest path", "a moonlit field", 
        "a small seaside village", "a large flower garden",
        
        # Objects 
        "a shiny shell", "a wooden raft", "a glittering stone", 
        "a small lantern", "a sturdy rope", 
        "a colorful feather", "a comfy backpack", "a silver acorn", 
        "a delicate mushroom", "a soft blanket", 
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
    Topic.ADV: [
        # Characters
        "a loyal best friend", "a brave explorer", "a curious sidekick", 
        "a wise old guide", "a daring captain", "a clever inventor", 
        "a fearless adventurer", "a mischievous prankster", 
        "a playful companion", "a determined leader", "a cheerful helper", 
        "a brave knight", "a daring pilot", "a friendly giant", 
        "a humorous fairy", "a witty trickster", "a curious storyteller", 
        "a shy creature", "a protective big sister", 
        "a kind little brother", "a curious mermaid", "an adventurous pirate", 
        "a gentle healer", "a mysterious wanderer", "a wise wizard",
        "a determined detective", "a thoughtful friend", "a cheerful jester",
        "a kind-hearted musician", "a fearless warrior", "a gentle giant",
        "an imaginative dreamer", "a loyal animal companion", "a clever fox",

        # Settings
        "a mysterious island", "a hidden treasure cave", "a foggy forest", 
        "a waterfall", "a sprawling desert",
        "a secret treehouse", "an ancient castle", "a peaceful meadow", 
        "a bustling village", "a grand library", "a pirate ship", 
        "a quiet beach", "an old mansion", "a rocky cliff", 
        "a sunny garden", "a distant kingdom", "a busy marketplace", 
        "a secret hideout", "a floating cloud city", "an icy glacier", 
        "a forgotten temple", "a tall lighthouse", "a sandy cove", 
        "a mysterious cave", "a deep jungle", "a snowy mountain peak", 
        "an open field", "a hidden valley", 
        "a peaceful harbor", "a golden beach", "a lush meadow", 
        "a cozy cabin", "an abandoned lighthouse", "a narrow canyon", 
        "a quiet lake", "a towering fortress", "a secret underground tunnel", 
        "a mystical waterfall", "a high hill", "a small fishing village", 
        "a sunlit orchard", "an open field", "a deserted island",
        
        # Objects
        "a compass", "a tattered map", "a shiny telescope", 
        "a golden coin", "a sturdy backpack", "a trusty lantern", 
        "an amulet", "a strong rope", "a tiny treasure chest", 
        "a pirate's flag", "an old journal", "a crystal ball", 
        "a pair of binoculars", "a sturdy walking stick", "a carved wooden box", 
        "a pair of boots", "a spyglass", "a glittering diamond", 
        "a small pouch of gems", "a wooden sword", "a weathered cloak", 
        "a mysterious key", "a sturdy helmet", "a shield", 
        "a colorful kite", "a glowing crystal", "a small fishing rod", 
        "a wooden raft", "a bundle of sticks", "a rainbow-colored stone", 
        "a rope ladder", "a water flask", "a glowing lantern", 
        "a fire starter", "a pocket watch", "a pirate's hat", 
        "a hand-drawn map", "a book", "a silver necklace", 
        "a floating balloon", "a mysterious potion", 
        "a cozy blanket", "a shiny coin",
    ],
    Topic.MAG: [
        # Characters
        "a wise wizard", "a mischievous fairy", "a brave knight", 
        "a magical unicorn", "a friendly dragon", "a talking owl", 
        "a helpful elf", "a curious mermaid", "a clever witch", 
        "a powerful sorceress", "a gentle giant", "a kind prince", 
        "a daring princess", "a noble queen", 
        "a clever goblin", "a playful pixie", "a mysterious genie",
        "a wise dragon", "a courageous warrior maiden", "a determined explorer", 
        "a fearless sorceress", "a gentle healer", "an enchanted rabbit", 
        "a cheerful wood nymph", "a daring sorcerer", "a friendly troll", 
        "a sparkling fairy queen", "a protective wolf", "a guardian centaur", 
        "a shape-shifting fox", "a powerful enchantress", "a resourceful heroine", 
        "a valiant shield-maiden", "a wise queen of the forest", "a kind-hearted protector", 
        "a skilled archer", "a bold captain", "a noble lady knight", 
        "a brave heroine", "a swift and clever messenger", "a warrior of the wilds", 
        "a defender of the enchanted forest",

        # Settings
        "a magical forest", "an enchanted castle",
        "a misty lake", "a sparkling waterfall", "a dark enchanted cave", 
        "a towering mountain", "a secret door",
        "a mystical river", "a grand ballroom", "a city of magical creatures"
        "a hidden village", "a crystal cave", "a sparkling fairy pond", 
        "a deep well", "a magical marketplace", 
        "a castle on a hill", "a glistening lake", 
        "a snowy mountain peak", "an enchanted clearing", "a unicorn meadow", 
        "a floating island", "a magical academy", "a grand wizard's tower", 
        "a glowing field", "a whispering forest", "a fairy circle", 
        "a starlit cave", "a garden of talking flowers", "a giant's castle", 
        "a golden meadow", "a mystical cloud city", "a hidden fairy village", 
        "a sun-dappled forest path", "a tall tree with a door", 
        "an enchanted bridge", "a meadow with dancing fireflies", 
        "a wizard’s hidden tower", "a sparkling crystal lake", 
        "a mysterious labyrinth", "a magical sky palace", "a floating crystal castle",
        "a forgotten magical land", "a mysterious island", "a school for magical beings", "a wizard's tower", 
        "a fairy tale village", "a magical library",
        "a dragon's castle", "a wizard's workshop", 

        # Objects
        "a magic wand", "an ancient spell book", "a glowing crystal", 
        "a shimmering potion", "a golden crown", "a magic mirror", 
        "a flying carpet", "a silver locket", "a pair of enchanted shoes", 
        "a tiny vial of stardust", "a powerful amulet", "a golden goblet", 
        "a dragon scale", "a glowing pearl", "a magical staff", 
        "a bottle of fairy dust", "a mysterious key", "a spell scroll", 
        "a moonstone", "a fairy ring", "a jeweled tiara", 
        "a crystal ball", "a rainbow-colored stone", "a small treasure chest", 
        "a singing harp", "a magical flute", "a golden apple", 
        "a ring of invisibility", "a potion of courage", "a shimmering cloak", 
        "a silver chalice", "a magical lantern", "a spell-bound book", 
        "a talking mirror", "a phoenix feather", "a fairy's gift", 
        "a protective charm", "a wizard's hat", "a glass slipper", 
        "a bag of enchanted seeds", "a sparkling ring", "a feather quill", 
        "a mystical hourglass", "a basket of magical herbs", "a broomstick", 
        "a pair of crystal earrings", "a golden harp", "a charm bracelet", 
        "a diamond dagger", "a potion of bravery", "a cloak of protection", 
        "a jeweled bracelet with hidden powers", "a dragon's tooth", 
        "a unicorn horn", "a fireproof shield", "a shimmering ring of truth",
    ],
    Topic.FAM: [
        # Characters
        "a hepful mom", "a loving dad", "a funny grandma", "a kind grandpa", 
        "a playful little brother", "a curious big sister", "a noisy neighbor", 
        "a nice teacher", "a lazy mail carrier", "a caring nurse", 
        "a gentle doctor", "a firefighter", "a librarian", 
        "a smiling bus driver", "a cheerful babysitter", "a forgetful baker", 
        "a fun coach", "a shopkeeper", "a brave police officer", 
        "a janitor", "a kind friend", "a cheerful chef", 
        "a gardener", "a friendly school principal",
        "a caring crossing guard", "a friendly dentist", "a fun uncle", 
        "a loving aunt", "a fun cousin", "a playful friend", 
        "a big brother", "a big sister", "a funny cousin", 

        # Settings
        "a cozy living room", "a sunny kitchen", "a warm bedroom", 
        "a backyard with swings", "a messy playroom", "a quiet reading corner", 
        "a busy grocery store", "a friendly neighbor's house", "a fun playground", 
        "a bustling school", "a peaceful garden", "a busy city street", 
        "a small doctor's office", "a local park", "a bright classroom", 
        "a library", "a bustling market", "a quiet park bench", 
        "a colorful craft room", "a cozy treehouse", "a family car", "a train"
        "a sidewalk", "a shopping mall", "a nice bakery", 
        "a small post office", "a train station", "a busy school bus",
        "a sandy beach", "a crowded bus stop", "a friendly coffee shop", 
        "a quiet museum", "a sunny front porch", 
        "a grassy backyard", "a bright doctor's waiting room",

        # Objects
        "a favorite toy", "a warm blanket", "a storybook", 
        "a pair of pajamas", "a stuffed animal", "a colorful toothbrush", 
        "a big dinner table", "a shopping cart", "a lunchbox", 
        "a backpack", "a school notebook", "a family photo", 
        "a recipe book", "a shiny key", "a pair of boots", 
        "a school bus", "a soccer ball", "a bandage", 
        "a soft pillow", "a family calendar", "a shopping bag", 
        "a list of chores", "a magic marker", "a doctor's stethoscope", 
        "a bright flashlight", "a favorite mug", "a water bottle", 
        "a comfy chair", "a snack box", "a soft towel", 
        "a pair of mittens", "a warm hat", "a teddy bear", 
        "a pencil case", "a colorful crayon", "a family game", 
        "a set of blocks", "a tasty sandwich", "a cooking apron", 
        "a shiny bicycle", "a pile of laundry", "a pair of slippers", 
        "a lost sock", "a cozy scarf", "a favorite sweater", 
        "a stack of books", "a grocery list", "a picture frame", 
        "a bottle of bubble soap", "a snack jar", "a school report card"
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
            prompt = "Write a story for children. Give the story a title and end with \"The End.\”\n" 
        else:
            prompt = f"Write a story for children about {topic.value}. Give the story a title and end with \"The End.\”\n"
        
        return prompt
    
    def _generate_prompt_from_keywords(self, topic: Topic, n_keywords) -> str:
        """Generate a prompt using the given keywords."""
        # Build the prompt
        keywords = self._sample_keywords(topic, n_keywords)
        keyword_str = " and ".join(keywords)
        if topic == Topic.ANY:
            prompt = f"Write a story for children. Include {keyword_str}. Give the story a title and end with \"The End.\"\n"
        else:
            prompt = f"Write a story for children about {topic.value}. Include {keyword_str}. Give the story a title and end with \"The End.\"\n"
        return prompt

    def _generate_prompt_from_examples(self, topic: Topic, n_examples) -> str:
        """Generate a n-shot learning prompt for the given topic."""
        samples = self._sample_stories(topic, n_examples)

        # Build the prompt
        example_stories = ""
        for _, row in samples.iterrows():
            example_stories += (
                f"Title: {row['Title']}\n"
                f"Story: {row['Story']}\n\n"
            )
        # Instruction + examples + query
        if n_examples == 1:
            prompt = (
                f"Here is an example of a story for children:\n\n"
                f"{example_stories}"
                f"Write another story in the same style. Give the story a title, introduce the setting and characters and end with \"The End.\"\n"
            )
        else:
            prompt = (
                f"Here are examples of stories for children:\n\n"
                f"{example_stories}"
                f"Write another story in the same style. Give the story a title, introduce the setting and characters and end with \"The End.\"\n"
            )
        return prompt
    
    def _generate_prompt_from_examples_and_keywords(self, topic: Topic, n_examples, n_keywords) -> str:
        """Generate a prompt using examples and keywords."""
        # Sample stories and keywords
        samples = self._sample_stories(topic, n_examples)
        keywords = self._sample_keywords(topic, n_keywords)

        # Build the prompt
        example_stories = ""
        for _, row in samples.iterrows():
            example_stories += (
                f"Title: {row['Title']}\n"
                f"Story: {row['Story']}\n\n"
            )
        keyword_str = " and ".join(keywords)
        if n_examples == 1:
            prompt = (
                f"Here is an example of a story for children:\n\n"
                f"{example_stories}"
                f"Write another story in the same style. Include {keyword_str}. Give the story a title, introduce the setting and characters and end with \"The End.\"\n"
            )
        else:
            prompt = (
                f"Here are examples of stories for children:\n\n"
                f"{example_stories}"
                f"Write another story in the same style. Include {keyword_str}. Give the story a title, introduce the setting and characters and end with \"The End.\"\n"
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
   