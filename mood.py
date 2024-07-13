
#function that provides a statment abased on the users response 
def mood_response(user_mood):
    mood_response = {"Angry": " venting to a friend.", "Sad": " speaking to a loved one.", "Happy": " listening to an upbeat song.", "Confused": " journaling." }
    while True: 
        try:
            for key, value in mood_response.items():
                if user_mood  == key:
                    print(f"You are feeling {key} today. Try{value }")
                    return 
            else: 
                mood = input("Please type one of the listed moods (Angry, Sad, Happy, Confused): ")
        except TypeError:
              print("An error occurred. Please provide a valid mood.")