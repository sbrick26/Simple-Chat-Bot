from random import choice

questions_list = ["What is your favorite food?", "What language do you code in?", "Do you have any movies you would recommend?", "What's your favorite song?", "What is your favorite hobby?", "What streaming service do you use?", "What is your favorite restaurant?"]

positive_mood_list = ["Glad to hear! I am having a great day.", "That's great! I am feeling on top of the world!", "I am happy to hear! I am feeling quite exquisite myself."]

negative_mood_list = ["Awww :( Your day will get better after talking to me!", "We all have some low days, let's talk to cheer you up!"]

general_list = ["That's an interesting choice.", "Me too!!", "That sounds super intriguing.", "I have not tried it!"]

why_list = ["I see, that makes sense!", "That's so cool!", "I get it now, I must try it myself!"]

furthering_list = ["Why is that your choice?", "Tell me why you like it so much.", "Why did you choose that?", "Why do you like it?"]

def get_bot_response(user_response, chatlevel):
    response = user_response.lower()
    

    if chatlevel == 0:
        if "not well" in response or "not good" in response or "not great" in response or "sad" in response or "upset" in response:
            return choice(negative_mood_list)
        elif "well" in response or "good" in response or "amazing" in response or "great" in response or "happy" in response:
            return choice(positive_mood_list)
    elif chatlevel == 1:
        answer = choice(general_list)
        if len(general_list) > 0:
            general_list.remove(answer)
            return answer
        else:
            return "I have to go, have a nice day!"
    elif chatlevel == 2:
        answer = choice(why_list)
        if len(why_list) > 0:
            why_list.remove(answer)
            return answer
        else:
            return "I have to go, have a nice day!"
        
    

stillTalking = True
chatlevel = 0
while stillTalking:
    if chatlevel == 0:
        print("Hello there! I'm Pi'erre, the chat bot! Let's chat.")
        print("To exit this chat at any time, enter done")
        user_response = input("How are you doing today?\n")
        if user_response == "done":
            break
        print(get_bot_response(user_response, chatlevel))
        chatlevel = 1
        
    elif chatlevel == 1:
        user_response = input(choice(questions_list)+ "\n")
        if user_response == "done":
            break
        print(get_bot_response(user_response, chatlevel))
        chatlevel = 2
    
    elif chatlevel == 2:
        user_response = input(choice(furthering_list) + "\n")
        if user_response == "done":
            break
        print(get_bot_response(user_response, chatlevel))
        chatlevel = 1
    


    






    


