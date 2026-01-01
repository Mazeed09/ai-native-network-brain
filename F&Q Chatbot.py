# Simple Student FAQ Chatbot

faq_bot = {
    "what are the school hours": "Our school runs from 8:00 AM to 3:00 PM, Monday through Friday.",
    "how can i apply for admission": "You can apply through the online portal on our school website.",
    "when do exams start": "Exams usually begin in the last week of November.",
    "how do i access my student portal": "Visit portal.school.edu and log in with your student ID and password.",
    "what is the wifi password": "Please contact the IT department to get the current Wi-Fi credentials.",
    "how can i join a club": "Club registrations open at the start of each semester. Visit the student affairs office.",
    "where is the library": "The library is located on the second floor of the main building.",
    "how do i get my student id": "New student IDs are issued at the admissions office.",
    "how many credits do i need to graduate": "You need at least 120 credits to graduate.",
    "can i speak with a counselor": "Yes, appointments can be booked through the student support center.",
    "when are school holidays": "The academic calendar is available on our website under 'Important Dates'.",
    "how do i reset my portal password": "Click 'Forgot Password' on the login page to reset it via your email.",
    "is attendance mandatory": "Yes, students are required to maintain at least 75% attendance."
}


# Fallback responses
fallbacks = [
    "Hmm, I didn't quite catch that. Could you rephrase?",
    "I'm not sure about that. Try checking the student handbook or asking support.",
    "Oops, that's outside my knowledge. Ask the admin office maybe?",
    "Can you try asking that in another way?"
]

import random

print("🤖 Hi there! I'm your Student FAQ Bot. Ask me anything related to your school.")
print("Type 'bye' whenever you’re done. Let’s go!\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "bye":
        print("Bot: Alright! Catch you later, and good luck with your classes 👋")
        break

    response = faq_bot.get(user_input)

    if response:
        print("Bot:", response)
    else:
        print("Bot:", random.choice(fallbacks))