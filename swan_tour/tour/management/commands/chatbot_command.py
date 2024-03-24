# Import necessary libraries
import random
import nltk
from nltk.chat.util import Chat, reflections
from tour.models import Tour

# NLTK reflections for personalized responses
reflections = {
    "I am": "you are",
    "I was": "you were",
    "I": "you",
    "I'm": "you are",
    "I'd": "you would",
    "I've": "you have",
    "I'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define tour details
def get_tour_details(tour_type=None, city=None, place=None):
    tours = Tour.objects.all()
    if tour_type:
        tours = tours.filter(tour_type__icontains=tour_type)
    if city:
        tours = tours.filter(city__icontains=city)
    if place:
        tours = tours.filter(places__icontains=place)

    tour_responses = []
    for tour in tours:
        response = f"Tour Name: {tour.name}\n"
        response += f"Tour Type: {tour.tour_type}\n"
        response += f"City: {tour.city}\n"
        response += f"Places: {tour.places}\n"
        response += f"Overview: {tour.overview}\n"
        response += f"Rating: {tour.rating}\n"
        response += f"Total Price: {tour.total_price}\n\n"
        tour_responses.append(response)
    
    return tour_responses

# Define the chatbot responses
pairs = [
    (
        r"hi|hello",
        ["Hello! I'm Disha, your tour chatbot. How can I assist you today?"]
    ),
    (
        r"tour",
        ["Sure! Here are some available tours:\n\n" + "\n\n".join(get_tour_details())]
    ),
    (
        r"tour type (.*) city (.*)",
        lambda match: "\n\n".join(get_tour_details(match.group(1), city=match.group(2)))
    ),
    (
        r"tour type (.*) place (.*)",
        lambda match: "\n\n".join(get_tour_details(match.group(1), place=match.group(2)))
    ),
    (
        r"tour type (.*)",
        lambda match: "\n\n".join(get_tour_details(match.group(1)))
    ),
    (
        r"city (.*)",
        lambda match: "\n\n".join(get_tour_details(city=match.group(1)))
    ),
    (
        r"place (.*)",
        lambda match: "\n\n".join(get_tour_details(place=match.group(1)))
    ),
    (
        r"exit",
        ["Exiting the chatbot. Goodbye!"]
    ),
    (
        r"(.*)",
        ["I'm sorry, I didn't quite understand. Can you please specify your question about tours, cities, or places?"]
    )
]

# Create the chatbot
def disha_chatbot():
    print("Hello! I'm Disha, your tour chatbot. How can I assist you today?")
    chatbot = Chat(pairs, reflections)
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            if isinstance(response, list):
                for resp in response:
                    print("Disha:", resp)
            else:
                print("Disha:", response)

# Run the chatbot
if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    disha_chatbot()
