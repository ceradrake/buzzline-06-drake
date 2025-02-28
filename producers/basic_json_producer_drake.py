"""
basic_json_producer_drake

Generate some streaming news headline message json data to a file without using Kafka.

"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import json
import os
import random
import time
import pathlib

#sentiment analysis modules
from textblob import TextBlob

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

load_dotenv()

#####################################
# Getter Functions for .env Variables
#####################################

def get_message_interval() -> int:
    """Fetch message interval from environment or use default."""
    interval = int(os.getenv("BUZZ_INTERVAL_SECONDS", 1))
    logger.info(f"Message interval: {interval} seconds")
    return interval

#####################################
# Set up Paths - write to a file the consumer will monitor
#####################################

# The parent directory of this file is its folder.
# Go up one more parent level to get the project root.
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
logger.info(f"Project root: {PROJECT_ROOT}")

# Set directory where data is stored
DATA_FOLDER: pathlib.Path = PROJECT_ROOT.joinpath("data")
logger.info(f"Data folder: {DATA_FOLDER}")

# Set the name of the data file
DATA_FILE: pathlib.Path = DATA_FOLDER.joinpath("news_headlines.json")
logger.info(f"Data file: {DATA_FILE}")

#####################################
# Define global variables
#####################################

headlines: list = [
    "Delta flight returns to LAX after takeoff over smoke detected midair.",
    "Pope Francis is in critical condition but alert, Vatican says.",
    "Need to attend a meeting, order groceries or book a flight. There's an 'AI Agent' for that.", 
    "Eggs are a hot commodity. On social media, posting about them can help you go viral.",
    "Scientists discover low-cost way to trap carbon using common rocks - and it could help farmers too.",
    "Horses and humans go blind for similar reasons, so this medicine might cure both.",
    "France prepares for largest child abuse trial in its history.",
    "Disability amid disaster: People with disabilities are disproportionately impacted by natural disasters."
]



#####################################
# Define a function to generate buzz messages
#####################################

#Sentiment analysis function
def analyze_sentiment(text: str) -> str:
    """Analyze the sentiment of the provided news headlines. Return either positive, negative, or neutral.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    if polarity < 0:
        return "Negative"
    else: 
        return "Neutral"

def generate_headlines():
    """Generate news headlines in JSON format with sentiment analysis.
    """
    while True: 
        headline = random.choice(headlines)
        sentiment = analyze_sentiment(headline)
        author = random.choice(["NY Times", "NBC News", "CNN", "Associated Press", "USA Today"])
        # Dictionary with all of the above topics
        json_message = {
            "headline": headline,
            "author" : author, 
            "sentiment" : sentiment
        }
        yield json_message



#####################################
# Define main() function to run this producer.
#####################################


def main() -> None:
    """
    Main entry point for this producer.

    It doesn't need any outside information, so the parentheses are empty.
    It doesn't return anything, so we say the return type is None.   
    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented. 
    This is a multiline docstring - a special type of comment 
    that explains what the function does.
    """

    logger.info("START producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Call the function we defined above to get the message interval
    # Assign the return value to a variable called interval_secs
    interval_secs: int = get_message_interval()

    try:
        for message in generate_headlines():
            logger.info(message)
            with DATA_FILE.open("a") as f:
                f.write(json.dumps(message) + "\n")
            time.sleep(interval_secs)
    except KeyboardInterrupt:
        logger.warning("Producer interrupted by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        logger.info("Producer shutting down.")




#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
