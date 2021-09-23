"""CLUTCH TIME: A choose your own adventure game including different sports!"""

__author__: str = "730308364"
from random import randint

player: str
points: int = 0
next: str = str("Thanks for playing that sport! Let's play another sport now.")
BASK: str = str("\U0001F3C0")
FOOT: str = str("\U0001F3C8")
BASE: str = str("\U000026BE")


def main() -> None:
    """Entrypoint to the game."""
    global points
    greet()
    decision()
    

def greet() -> None:
    """Greets the user with a welcome and breifing."""
    print("Welcome to CLUTCH TIME!")
    print("In this game, you, the player, must try to make the game winning play.")
    print(f"\nYou may try your hand at basketball {BASK}, football {FOOT}, or baseball {BASE}!")
    global player
    player = input("Let's start by getting you a jersey. What name is going on the back? ")
    print(f"\n{player}, try to gain as many points as possible.")
    print("Making safe choices will reward fewer points, but succeed more often.")
    print("Making risky choices will reward more points, but succeed less often.")
    print(f"Good luck, {player}!")
    

def decision() -> None:
    """Player makes a decision which sport to pursue."""
    global points
    print("\nTo earn the most points, you should try every sport once before ending the game.")
    print(f"Your current points total is {points} points.")
    choice: str = str(input("\nWill you play: basketball, football, baseball, or end game? "))
    if choice == "basketball":
        basketball()
    else:
        if choice == "football":
            points = int(football(points))
            decision()
        else:
            if choice == "baseball":
                points = baseball(points)
                decision()
            else:
                if choice == "end game":
                    end_game(points)
      

def basketball() -> None:
    """Runs basketball simulation."""
    global points
    global player
    print(f"\n{player}, the clock is winding down and your team is down by 2 points.")
    print("The ball is in your hands! You have an open three-pointer, but your teammate sets a screen and the lane to the basket opens up...")
    print("If you make the risky three, you'll win the game. If you drive and make a layup, the game will go to overtime.")
    shoot_or_drive: str = str(input("Will you shoot or drive? "))
    if shoot_or_drive == "shoot":
        shoot_percent: int = randint(0, 100)
        if shoot_percent > 65:
            points = points + 100
            print(f"\n{player} puts it up... and it GOES IN!!! YOUR TEAM WINS!!!")
        else:
            print(f"\n{player} puts it up... and misses. Your team loses the game.")
    if shoot_or_drive == "drive":
        layup_percent: int = randint(0, 100)
        if layup_percent > 35:
            points = points + 50
            print(f"\n{player} drives to the basket... and makes a layup! This game is going to overtime!")
            print("Coach decides to bench you for overtime, but you watch as your team takes home the victory!")
        else:
            print(f"\n{player} drives to the basket... and misses the layup. Your team loses the game.")
    print(next)
    decision()


def football(x: int) -> int:
    """Runs football simulation."""
    global player
    y: int = 0
    print("It's 4th and goal with one second left on the clock. Your team is down by 2.")
    print(f"{player}, YOU are the quarterback. You can either pass to your trusty receivers, handoff to your 5-star running back, or trust your own legs to take you to the endzone.")
    rpo: str = str(input("Will you pass, handoff, or run? "))
    while rpo == "run":
        print("\nOh no! You were stopped at the goal line. Your team loses.")
        y = y + 0
        rpo = "done"
    while rpo == "pass":
        rec_percent: int = randint(0, 100)
        if rec_percent > 70:
            print(f"\n{player} throws the ball... and ITS CAUGHT by #84!!! Your team wins the game!")
            y = y + 100
        else:
            print(f"\n{player} throws the ball... and its dropped by #84. Your team loses the game.")
        rpo = "done"
    while rpo == "handoff":
        run_percent: int = randint(0, 100)
        if run_percent > 40:
            print("\nThe ball is handed off to #32... who barrels into the endzone for a touchdown. Your team wins!!!")
            y = y + 50
        else:
            print("\nThe ball is handed off to #32... who is stopped at the goal line. Your team loses the game.")
        rpo = "done"
    print(next)
    points_two: int = x + y
    return points_two


def baseball(x: int) -> int:
    """Runs baseball simulation."""
    global player
    z: int = 0
    print("You're up to bat. The bases are loaded and you need the GRAND SLAM to win the game.")
    print("You are sitting with a full count: three balls and two strikes.")
    print("If you swing at the next pitch, you may hit a dinger into the yard or strikeout. If you stay, you may take a walk and force a run in, or strikeout.")
    swing_or_stay: str = str(input("The choice is youres: will you swing or stay? "))
    pitch_speed: int = randint(60, 100)
    if swing_or_stay == "swing":
        if pitch_speed > 85:
            print(f"\n{player} swings and... the ball just gets by him. STRIKEOUT. And that's the game")
        else:
            z = z + 100
            print(f"\n{player} swings and... makes contact! It's going, going,... GONE!! Your team wins the game!")
    if swing_or_stay == "stay":
        if pitch_speed > 70:
            print("\nLooks like the pitch was inside the strike zone. You're OUT!")
        else:
            z = z + 50
            print(f"\nThe pitch is coming and... {player} makes a smart move to stay and take the walk.")
            print("The next batter bangs in a GRAND SLAM for the WIN!")
    print(next)
    points_three: int = x + z
    return points_three


def end_game(x: int) -> None:
    """Ends the game."""
    global player
    print(f"\n{player}, your final point score is: {x}!")
    print("Thanks for playing CLUTCH TIME!")


if __name__ == "__main__":
    main()