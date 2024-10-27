import os
import pandas as pd

class StoryManager:
    """A class to manage stories stored as plain text files and build a DataFrame."""

    TOPIC_MAP = {
        "Ani": "Animals",
        "Adv": "Friendship and Adventure",
        "Mag": "Magic and Fairy Tales",
        "Fam": "Family and Everyday Life"
    }
    # Instance attributes (set in __init__)
    story_folder: str  # Folder containing story text files
    csv_file: str      # Path to the CSV file for storing the DataFrame
    df: pd.DataFrame   # The DataFrame holding the stories

    def __init__(self, story_folder=None, csv_file=None):
        # Ensure the base path is relative to the current file (manager.py)
        base_path = os.path.dirname(__file__)

        # If no story folder is provided, use the default 'stories/' folder
        if story_folder is None:
            self.story_folder = os.path.join(base_path, 'stories/')
        else:
            self.story_folder = story_folder

        # If no CSV file path is provided, use 'goldstories.csv' by default
        if csv_file is None:
            self.csv_file = os.path.join(base_path, 'goldstories.csv')
        else:
            self.csv_file = csv_file

        # Load the DataFrame from the CSV file if it exists, otherwise create it
        if os.path.exists(self.csv_file):
            self.df = self._load_from_csv()
        else:
            self.df = self._load_stories_into_dataframe()
            self._save_to_csv()

    def _load_from_csv(self) -> pd.DataFrame:
        """Load the DataFrame from a CSV file and convert topics back to lists."""
        print(f"Loading stories from {self.csv_file}")
        df = pd.read_csv(self.csv_file)

        # Convert the topics string back to a list
        df["Topics"] = df["Topics"].apply(lambda x: x.split(", "))
        return df

    def _save_to_csv(self):
        """Save the DataFrame to a CSV file."""
        print(f"Saving stories to {self.csv_file}")

        # Convert the topics list to a comma-separated string
        self.df["Topics"] = self.df["Topics"].apply(lambda x: ", ".join(x))
        self.df.to_csv(self.csv_file, index=False)

    def _parse_story(self, content: str) -> dict:
        """Parse the content of a story file."""
        lines = content.splitlines()
        # First line is the title
        title = lines[0].strip()

        # Second line contains topic codes
        topic_codes = lines[1].strip().split(", ")
        topics = [self.TOPIC_MAP[code] for code in topic_codes]
        body = "\n".join(lines[2:])
        return {"Title": title, "Topics": topics, "Story": body}
    
    def _load_stories_into_dataframe(self) -> pd.DataFrame:
        """Load stories from text files and build a DataFrame."""
        stories = []
        for filename in os.listdir(self.story_folder):
            if filename.endswith(".txt"):
                with open(os.path.join(self.story_folder, filename), "r", encoding="utf-8") as f:
                    content = f.read()
                    story = self._parse_story(content)
                    stories.append(story)
        return pd.DataFrame(stories)

    def get_dataframe(self) -> pd.DataFrame:
        """Return the current DataFrame."""
        return self.df

    def display_stories(self):
        """Display all stories from the DataFrame."""
        for _, row in self.df.iterrows():
            print(f"\nTitle: {row['Title']}")
            print(f"Topics: {', '.join(row['Topics'])}")
            print("Story:")
            print(row['Story'])

