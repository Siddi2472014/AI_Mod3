import random
from colorama import Fore, Style
import colorama
colorama.init()
print("Hello, what is your name?")
name = input("Enter your name: ")
print(f"Nice to meet you {name}! Where would you like to travel? \n Options: beach, city, culture, history, nature")
destinations = {
    "beach": ["Bali", "Maldives", "Phuket"],
    "city": ["Tokyo", "New York"],
    "culture": ["New York","Paris","Rome"],
    "history": ["London","Rome","Greece"],
    "nature": ["Sydney","India"]
}
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the math book look sad? Because it had too many problems!",
    "Why did the tomato turn red? Because it saw the salad dressing!"]
def normalize_input(user_input):
    return user_input.strip().lower()
user_preferenece = input("Enter your preference: ")
def recommend(user_preference):
    normalized_preference = normalize_input(user_preference)
    print("Your preference:", normalized_preference)
    if normalized_preference in destinations:
        recommended_destinations = destinations[normalized_preference]
        print(f"{Fore.GREEN}Recommended destinations for {normalized_preference}: {', '.join(recommended_destinations)}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Sorry, we don't have recommendations for that preference.{Style.RESET_ALL}")
def show_joke():
    joke = random.choice(jokes)
    print(f"{Fore.YELLOW}{joke}{Style.RESET_ALL}")
recommend(user_preferenece)
print("Would you like to hear a joke? (y/n)")
answer=input("")
if answer == "y":
    show_joke()
else:
    print("No worries! Have a great day!")