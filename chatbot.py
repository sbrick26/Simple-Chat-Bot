from random import choice

questions_list = ["What is your favorite food?", "What language do you code in?", "Do you have any movies you would recommend?", "What's your favorite song?", "What is your favorite hobby?", "What is your favorite streaming service to use?", "What is your favorite restaurant?"]

positive_mood_list = ["Glad to hear! I am having a great day.", "That's great! I am feeling on top of the world!", "I am happy to hear! I am feeling quite exquisite myself."]

negative_mood_list = ["Awww :( Your day will get better after talking to me!", "We all have some low days, let's talk to cheer you up!"]

general_list = ["That's an interesting choice.", "Me too!!", "That sounds super intriguing.", "I have not tried it!", "I would have never guessed that!", "That's a new one!", "I'm gonna go tell my Bot friends about this!"]

why_list = ["I see, that makes sense!", "That's so cool!", "I get it now, I must try it myself!"]

furthering_list = ["Why is that your choice?", "Tell me why you like it so much.", "Why did you choose that?", "Why do you like it?", "Tell me more about it!"]

def get_bot_response(user_response, chatlevel):
    response = user_response.lower()
    

    if chatlevel == 0:
        if "not well" in response or "not good" in response or "not great" in response or "sad" in response or "upset" in response:
            return choice(negative_mood_list)
        elif "well" in response or "good" in response or "amazing" in response or "great" in response or "happy" in response:
            return choice(positive_mood_list)
        else:
            return "Nice."
    elif chatlevel == 1:
        if len(general_list) > 0:
            answer = choice(general_list)
            general_list.remove(answer)
            return "Pi'erre: " + answer
        else:
            return "Pi'erre: I have to go, have a nice day! Enter done to end chat:"
    elif chatlevel == 2:
        answer = "Pi'erre: " + choice(why_list)
        return answer
        
    
name = "New User: "
stillTalking = True
chatlevel = 0
while stillTalking:
    if chatlevel == 0:
        print("Pi'erre: Hello there! I'm Pi'erre, the chat bot! Let's chat.")
        print("Pi'erre: To exit this chat at any time, enter done")
        name = input ("Pi'erre: What is your name?\nUser: ") + ": "
        user_response = input("Pi'erre: How are you doing today?\n" + name)
        if user_response == "done":
            break
        print("Pi'erre: " + get_bot_response(user_response, chatlevel))
        chatlevel = 1
        
    elif chatlevel == 1:
        

        if len(questions_list) > 0:
            answer = choice(questions_list)
            questions_list.remove(answer)
        else:
            print("Pi'erre: I have to go, have a nice day!")
            break
        user_response = input("Pi'erre: " + answer+ "\n" + name)
        if user_response == "done":
            break
        print(get_bot_response("Pi'erre: " + user_response, chatlevel))
        chatlevel = 2
    
    elif chatlevel == 2:
        answer = choice(furthering_list)
        user_response = input("Pi'erre: " + answer + "\n" + name)
        if user_response == "done":
            break
        print(get_bot_response("Pi'erre: " + user_response, chatlevel))
        chatlevel = 1
    


    






    


