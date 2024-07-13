#import custom module 
import mood
# recieve the user input and print response by sengin to mood module 
user_mood = input("How are you feeling today (Angry, Happy, Sad, Confused)? :  ")
print(mood.mood_response(user_mood))

