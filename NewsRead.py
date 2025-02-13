import requests
import json
import pyttsx3
from typing import Optional, Dict

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate", 170)

def speak(audio: str) -> None:
    engine.say(audio)
    engine.runAndWait()

def latestnews() -> None:
    api_dict: Dict[str, str] = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=180ed6b24190418bab6ed9a3c544ac0d",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=180ed6b24190418bab6ed9a3c544ac0d",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=180ed6b24190418bab6ed9a3c544ac0d", 
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=180ed6b24190418bab6ed9a3c544ac0d",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=180ed6b24190418bab6ed9a3c544ac0d",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=180ed6b24190418bab6ed9a3c544ac0d"
    }

    # Show available categories
    valid_categories = list(api_dict.keys())
    print("\nAvailable news categories:", ", ".join(valid_categories))
    speak("Which field news do you want? Available categories are: " + ", ".join(valid_categories))

    # Get user input with validation
    while True:
        field = input("\nType field news that you want: ").lower().strip()
        if field in valid_categories:
            break
        print(f"Invalid category. Please choose from: {', '.join(valid_categories)}")
        speak("Please select a valid category")

    url = api_dict[field]
    print(f"\nFetching {field} news...")

    try:
        # Make API request with error handling
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        news = response.json()
        
        if news.get("status") != "ok":
            error_msg = news.get("message", "Unknown error")
            print(f"API Error: {error_msg}")
            speak("Sorry, there was an error fetching the news")
            return

        articles = news.get("articles", [])
        if not articles:
            print("No news articles found")
            speak("Sorry, no news articles are available at the moment")
            return

        speak(f"Here are the latest {field} news updates")
        
        for index, article in enumerate(articles, 1):
            print("\n" + "="*50)
            title = article.get("title", "No title available")
            description = article.get("description", "No description available")
            news_url = article.get("url", "No URL available")
            
            print(f"\nNews {index}:")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"For more info visit: {news_url}")
            
            speak(title)
            if description != "No description available":
                speak(description)

            if index < len(articles):
                while True:
                    user_choice = input("\n[press 1 to continue] or [press 2 to stop]: ").strip()
                    if user_choice in ["1", "2"]:
                        break
                    print("Invalid input. Please press 1 to continue or 2 to stop.")

                if user_choice == "2":
                    break

        speak("That's all for now. Thank you for listening!")

    except requests.exceptions.RequestException as e:
        print(f"\nNetwork error: {str(e)}")
        speak("Sorry, I couldn't connect to the news service")
    except json.JSONDecodeError as e:
        print(f"\nError parsing news data: {str(e)}")
        speak("Sorry, I received invalid data from the news service")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        speak("Sorry, an unexpected error occurred while fetching the news")

if __name__ == "__main__":
    latestnews()
