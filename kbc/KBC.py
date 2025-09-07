import pyttsx3
import random #pip install pyttsx3
# import speech_recognition as sr


#making the text to speech function
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# def Command_from_user():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("\nListening...") 
#         r.pause_threshold = 1
#         # r.adjust_for_ambient_noise(source, duration=5)
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         # r.adjust_for_ambient_noise(source, duration=5)
#         print("User said: ", query)
#     except Exception as e:
#         print(e)
#         print("Say that again please...")
#         return "None"
#     return query 
def thank_you():
    speak("Thank you for using this program.")
    print("\n\n\nThis Program is made by MOHAK JAIN !!!!!")
def asking_questions():

    score=0

    opt11 = "1. Pandit Jawaharlal Nehru"
    opt12 = "2. Shri Narendra Modi"
    opt13 = "3. Rahul Gandhi"
    opt14 = "4. Abdul Kalam"
    print("\nQuestion number 1:", Q1)
    print("\nOptions:")
    print()
    speak("Question Number 1:")
    speak(Q1)
    print(opt11,opt12,opt13,opt14)
    ans1 = input("\nPls write the answer like '1','2','3' or '4':")
    answer1 = int(2)
    if ans1 == answer1 or "2":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
    elif ans1 == 2:
        speak("Congratulations, your answer is correct")
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt21 = "1. 1957"
    opt22 = "2. 1967"
    opt23 = "3. 1947"
    opt24 = "4. 1937"
    print("\nQuestion number 2:", Q2)
    print("\nOptions:")
    print()
    speak("Question Number 2:")
    speak(Q2)
    print(opt21,opt22,opt23,opt24)
    ans2 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer2 = "3"
    # print(ans2)
    if ans2==answer2 or "3":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt31 = "1. Politician"
    opt32 = "2. Freedom Fighter"
    opt33 = "3. Rebel"
    opt34 = "4. Army Official"
    print("\nQuestion number 4:", Q3)
    print("\nOptions:")
    print()
    speak("Question Number 3:")
    speak(Q3)
    print(opt31,opt32,opt33,opt34)
    ans3 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer3 = "2"
    # print(ans2)
    if ans3==answer3 or "2":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt41 = "1. Shri Narendra Modi"
    opt42 = "2. Rajiv Gandhi"
    opt43 = "3. Abdul Kalam"
    opt44 = "4. Pandit Jawaharlal Nehru"
    print("\nQuestion number 4:", Q4)
    print("\nOptions:")
    print()
    speak("Question Number 4:")
    speak(Q4)
    print(opt41,opt42,opt43,opt44)
    ans4 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer4 = "4"
    # print(ans4)
    if ans4==answer4 or "4":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt51 = "1. Freedom Fighter"
    opt52 = "2. Prime Minister of India"
    opt53 = "3. Rebel"
    opt54 = "4. Home Minister"
    print("\nQuestion number 5:", Q5)
    print("\nOptions:")
    print()
    speak("Question Number 5:")
    speak(Q5)
    print(opt51,opt52,opt53,opt54)
    ans5 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer5 = "2"
    # print(ans5)
    if ans5==answer5 or "2":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt61 = "1. Freedom Fighter"
    opt62 = "2. Prime Minister of India"
    opt63 = "3. Rebel"
    opt64 = "4. Home Minister"
    print("\nQuestion number 6:", Q6)
    print("\nOptions:")
    print()
    speak("Question Number 6:")
    speak(Q6)
    print(opt61,opt62,opt63,opt64)
    ans6 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer6 = "2"
    # print(ans5)
    if ans6==answer6 or "2":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt71 = "1. Mahatma Gandhi"
    opt72 = "2. Jawaharlal Nehru"
    opt73 = "3. Narendra Modi"
    opt74 = "4. BR Ambedkar"
    print("\nQuestion number 7:", Q7)
    print("\nOptions:")
    print()
    speak("Question Number 7:")
    speak(Q7)
    print(opt71,opt72,opt73,opt74)
    ans7 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer7 = "1"
    # print(ans5)
    if ans7==answer7 or "1":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt81 = "1. Mahatma Gandhi"
    opt82 = "2. Jawaharlal Nehru"
    opt83 = "3. Narendra Modi"
    opt84 = "4. BR Ambedkar"
    print("\nQuestion number 8:", Q8)
    print("\nOptions:")
    print()
    speak("Question Number 8:")
    speak(Q8)
    print(opt81,opt82,opt83,opt84)
    ans8 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer8 = "4"
    # print(ans5)
    if ans8==answer8 or "4":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt91 = "1. French"
    opt92 = "2. Dutch"
    opt93 = "3. Portugese"
    opt94 = "4. British"
    print("\nQuestion number 9:", Q9)
    print("\nOptions:")
    print()
    speak("Question Number 9:")
    speak(Q9)
    print(opt91,opt92,opt93,opt94)
    ans9 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer9 = "4"
    # print(ans5)
    if ans9==answer9 or "4":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("Next question")

    opt101 = "1. Malyalam"
    opt102 = "2. Punjabi"
    opt103 = "3. English"
    opt104 = "4. Hindi"
    print("\nQuestion number 10:", Q10)
    print("\nOptions:")
    print()
    speak("Question Number 10:")
    speak(Q10)
    print(opt101,opt102,opt103,opt104)
    ans10 = input("\nPls write the answer like '1','2','3' or '4': ")
    answer10 = "4"
    # print(ans5)
    if ans10==answer10 or "4":
        speak("Congratulations, your answer is correct and one point has been added to your score.")
        score = score+1
        print("Your current score is: ", score)
        speak("Your current score is")
        # speak(score)
    else:
        speak("Sorry, your answer is wrong")
    speak("The quiz is over")
    if score=="10" or 10:
        gift_code1 = random.randint(1000, 9999)
        gift_code2 = random.randint(1000, 9999)
        gift_code3 = random.randint(1000, 9999)
        gift_code4 = random.randint(1000, 9999)
        print("\nCongrats You won $1000")
        speak("Congrats You won $1000")
        print("Your gift code is: (Use this code on amazon)")
        print(gift_code1, "-", gift_code2, "-", gift_code3, "-", gift_code4)
        thank_you()
    else:
        thank_you()
#Questions
Q1 = "Who is the current prime minister of India?"
Q2 = "In which year did India got its freedom from the british rule?"
Q3 = "Who was Mahatma Gandhi?"
Q4 = "Who was the first prime minister of India?"
Q5 = "Who was APJ Abdul Kalam?"
Q6 = "Who was Bhagat Singh?"
Q7 = "Who was known as the father of the nation?"
Q8 = "Who was known as the father of the constitution? (Hint: He belonged to the Mahar Caste)"
Q9 = "Which people captured India and misused India's resources?"
Q10 = "Name the national language of India?"

#Writing some starting rules and some info about the game
print("\nWelcome to the KBC game.")
print("This game is a replica of the orignal KBC.")
print("In this me, Daniel will ask 10 questions. and if you answer all the questions correctly you will get a $1000 Amazon gift card. Don't worry this is not fake")
print("The rules of the game are pretty simple, we i will ask you a question and the question would also be displayed in the command line, i will give you 4 options for the questions and one amongst all the 4 options would be correct. You just need to write the option number.")


speak("Welcome to the KBC game.")
speak("This game is a replica of the orignal KBC.")
speak("In this me, Daniel will ask 10 questions, and if you answer all the questions correctly you will get a $1000 Amazon gift card. Don't worry this is not fake")
speak("The rules of the game are pretty simple, I will ask you a question and the question would also be displayed in the command line, i will give you 4 options for the questions and one amongst all the 4 options would be correct. You just need to write the option number.")

speak("So are you ready to start?")
ready = input("Press y if you are ready and any other alphabet to end it: ")

if ready=="y":
    speak("So let's go")
    asking_questions()
else:
    thank_you()
    exit()
