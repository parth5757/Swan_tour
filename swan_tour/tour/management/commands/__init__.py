# Import necessary libraries
import nltk
import random
from nltk.chat.util import Chat, reflections
from django.core.management.base import BaseCommand
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
        tours = tours.filter(tour_type__name__icontains=tour_type)
    if city:
        tours = tours.filter(city__name__icontains=city)
    if place:
        tours = tours.filter(place__name__icontains=place)

    tour_responses = []
    for tour in tours:
        response = f"Tour Name: {tour.name}\n"
        response += f"Tour Type: {tour.tour_type}\n"
        response += f"City: {', '.join([c.name for c in tour.city.all()])}\n"
        response += f"Places: {', '.join([p.name for p in tour.place.all()])}\n"
        response += f"Overview: {tour.overview}\n"
        response += f"Rating: {tour.rating}\n"
        response += f"Total Price: {tour.total_price}\n\n"
        tour_responses.append(response)
    
    return tour_responses

# Define the chatbot responses
pairs = [
    (
        r"hi|hello|hey",
        ["Hello! I'm Disha, your tour chatbot. How can I assist you today?"]
    ),
    (
        r"tour",
        ["Sure! Here are some available tours:\n\n" + "\n\n".join(get_tour_details())]
    ),
    (
        r"tour type (.*) city (.*)",
        lambda tour_type, city: "\n\n".join(get_tour_details(tour_type, city))
    ),
    (
        r"tour type (.*) place (.*)",
        lambda tour_type, place: "\n\n".join(get_tour_details(tour_type, place=place))
    ),
    (
        r"tour type (.*)",
        lambda tour_type: "\n\n".join(get_tour_details(tour_type))
    ),
    (
        r"city (.*)",
        lambda city: "\n\n".join(get_tour_details(city=city))
    ),
    (
        r"place (.*)",
        lambda place: "\n\n".join(get_tour_details(place=place))
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
            print("Chatbot: Exiting the chatbot. Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            if isinstance(response, list):
                for resp in response:
                    print("Chatbot:", resp)
            else:
                print("Chatbot:", response)

class Command(BaseCommand):
    help = 'Chatbot command to interact with the tour chatbot'

    def handle(self, *args, **kwargs):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        disha_chatbot()