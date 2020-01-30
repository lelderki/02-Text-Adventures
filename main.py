import time 

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A, B, or C\n")

def intro():
    print ("You are the star player. "
    "You're in the biggest game of the season. "
    "It's all or nothing.")
    time.sleep(1)
    print ("You are Megan Rapinoe. "
    "Number 15 for the USA Women's Soccer Team. "
    "There's not much time left in the game.")
    time.sleep (1)
    print ("You're at centerfield. "
    "It's your turn to make a move.")
    time.sleep (1)
    print ("A. Pass backwards to Julie Ertz (Midfielder).")
    print ("B. Pass to Tobin Heath (Forward) as she makes a diagonal run forward.")
    print ("C. Pass to the other team.")
    choice = input(">>> ") #first choice
    if choice in answer_A:
        option_Julie()
    elif choice in answer_B:
        option_Tobin()
    elif choice in answer_C:
        option_opp()
    else:
        print (required)
        intro()

def option_Julie():
    print ("Julie Ertz now has the ball.")
    time.sleep(1)
    print ("Since you passed backwards, you are now guarded.")
    time.sleep (1)
    print ("What's Julie's next move?")
    time.sleep (1)
    print ("A. Kelley O'Hara gets open, Julie passes to her.")
    print ("B. Tobin is wide open, in the far right corner of the field. "
    "Julie boots the ball across the field.")
    print ("C. Pass back to your goalie, Ashlyn Harris.")
    choice = input(">>> ") 
    if choice in answer_A:
        option_Kelley()
    elif choice in answer_B:
        option_Tobin()
    elif choice in answer_C:
        option_Ashlyn()
    else:
        print (required)
        intro()

def option_Tobin():
    print ("Tobin Heath now has the ball.")
    time.sleep(1)
    print ("Except there are a lot of defenders on her.")
    time.sleep (1)
    print ("What's Julie's next move?")
    time.sleep (1)
    print ("A. Tobin tried to get out of trouble, however, she couldn't find her teammates. The other team got the ball.")
    print ("B. You're open again! Tobin passes to Megan. ")
    print ("C. Pass back to your goalie, Ashlyn Harris.")
    choice = input(">>> ") 
    if choice in answer_A:
        option_opp()
    elif choice in answer_B:
        option_Megan()
    elif choice in answer_C:
        option_Ashlyn()
    else:
        print (required)
        intro()

def option_opp():
    print ("The opposing team now has the ball.")
    time.sleep(1)
    print ("Crystal Dunn (Defender) tries to stop the other team.")
    time.sleep (1)
    print ("She can't stop them herself.")
    time.sleep (1)
    print ("The opposing team takes a shot...")
    time.sleep (1)
    print ("Misses.")
    time.sleep (1)
    print ("Everyone cheers on Ashlyn as she holds the ball up.")
    time.sleep (1)
    print ("What does Ashlyn do now?")
    time.sleep (1)
    choice = input(">>> ") 
    print ("A. She boots the ball high into the sky, you keep your eye on the ball as it falls to the field.")
    print ("B. The other team got the ball again.")
    if choice in answer_A:
        option_Megan()
    elif choice in answer_B:
        option_opp()
    else:
        print (required)
        intro()

def option_Megan():
    print ("You have the ball again.")
    time.sleep(1)
    print ("Be smart.")
    time.sleep (1)
    print ("What's your next move?")
    time.sleep (1)
    print ("A. Dribble and shoot.")
    print ("B. Although you have a nice shot, you pass to Tobin. ")
    print ("C. I don't know.")
    choice = input(">>> ") 
    if choice in answer_A:
        option_shoot()
    elif choice in answer_B:
        option_Tobin()
    elif choice in answer_C:
        option_opp()
    else:
        print (required)
        intro()

def option_Kelley():
    print ("As a defender, Kelley needs to get the ball up the field.")
    time.sleep(1)
    print ("The pressure is on. The other team is moving in.")
    time.sleep (1)
    print ("What's her next move?")
    time.sleep (1)
    print ("A. Dribble while USA gets open. She spots Carli Lloyd.")
    print ("B. You are open. You call for the ball. ")
    print ("C. Kelley didn't realize she had two players on her. The ball gets stolen.")
    choice = input(">>> ") 
    if choice in answer_A:
        option_Carli()
    elif choice in answer_B:
        option_Megan()
    elif choice in answer_C:
        option_opp()
    else:
        print (required)
        intro()

def option_Ashlyn(): 
    print ("As a goalie, the main concern is gettig the ball AWAY from the goal.")
    time.sleep(1)
    print ("The pressure is on.")
    time.sleep (1)
    print ("What's Ashlyn's next move?")
    time.sleep (1)
    print ("A. She spots Carli Lloyd and tries her best to get the ball high enough to make it to her.")
    print ("B. You call for the ball. ")
    print ("C. She drops the ball and the other team rushes her.")
    choice = input(">>> ") 
    if choice in answer_A:
        option_Carli()
    elif choice in answer_B:
        option_Megan()
    elif choice in answer_C:
        option_shoton()
    else:
        print (required)
        intro()

def option_shoot():
    print ("WHAT A SHOT!")
    time.sleep(1)
    print ("The fans watch as the ball sores through the air...")
    time.sleep(1)
    print ("...and hits the post, richochets off...")
    time.sleep (1)
    print ("A. Carli steps in front.")
    print ("B. You follow through for the ball. ")
    print ("C. The other team beat your team to the ball.")
    choice = input(">>> ") 
    if choice in answer_A:
        option_Carli()
    elif choice in answer_B:
        option_Megan()
    elif choice in answer_C:
        option_opp()
    else:
        print (required)
        intro()

def option_Carli():
    print ("After a small battle...")
    time.sleep(1)
    print ("Carli Lloyd now has the ball.")
    time.sleep(1)
    print ("She's so close to the goal and, what looks like, an open shot.")
    time.sleep (1)
    print ("She turns, preps herself for the shot.")
    time.sleep(1)
    print ("Carli looks up.")
    time.sleep(1)
    print ("She shoots.")
    time.sleep (3)
    print ("GOOOOOOOOOOAAAAAALLLLLLLLLLL!!!!!!!")
    time.sleep(1)
    print ("USA WINS!!!! Congratulations!!!!")
    time.sleep (3)
    print ("Thanks for playing!")

def option_shoton():
    print ("The other team is close to the goal.")
    time.sleep(1)
    print ("Ashlyn is preparing to stop the ball.")
    time.sleep(1)
    print ("The opposing team shoots.")
    time.sleep (1)
    print ("With a lucky shot in the top left corner of the goal, it goes in.")
    time.sleep(1)
    print ("Game over. With a score of 0-1, the opposing team wins.")
    time.sleep(1)
    print ("Good game. You'll get them next time.")

intro ()
