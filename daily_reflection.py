def get_mood():
    print("\nHow was your day overall?")
    print("1. Good")
    print("2. Okay")
    print("3. Bad")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return "good"
    elif choice == "2":
        return "okay"
    elif choice == "3":
        return "bad"
    else:
        print("Invalid input. Defaulting to 'okay'.")
        return "okay"


def get_productivity():
    print("\nHow productive were you today?")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return "high"
    elif choice == "2":
        return "medium"
    elif choice == "3":
        return "low"
    else:
        print("Invalid input. Defaulting to 'medium'.")
        return "medium"


def get_challenge():
    print("\nWhat was your biggest challenge today?")
    print("1. Work/Study")
    print("2. Time Management")
    print("3. Personal/Emotional")
    print("4. No major challenge")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        return "work"
    elif choice == "2":
        return "time"
    elif choice == "3":
        return "personal"
    elif choice == "4":
        return "none"
    else:
        print("Invalid input. Defaulting to 'none'.")
        return "none"


def generate_reflection(mood, productivity, challenge):

    # Main logic
    if mood == "good" and productivity == "high":
        result = "You had a great and productive day. Try to identify what worked well and repeat it tomorrow."

    elif mood == "good" and productivity == "low":
        result = "You felt good, but productivity was low. Consider setting clearer goals for better output."

    elif mood == "okay" and productivity == "medium":
        result = "Your day was average. Small improvements in planning can make it better."

    elif mood == "bad" and productivity == "low":
        result = "It seems like a difficult day. Take some rest and focus on one small improvement tomorrow."

    else:
        result = "Reflect on your day and try to make small improvements tomorrow."

    # Challenge-based addition
    if challenge == "work":
        result += "\nFocus on prioritization and break tasks into smaller steps."

    elif challenge == "time":
        result += "\nTry using a schedule or time-blocking technique."

    elif challenge == "personal":
        result += "\nTake time to reflect and consider journaling or talking to someone."

    elif challenge == "none":
        result += "\nKeep maintaining your current routine."

    return result


def main():
    print("Daily Reflection System")

    mood = get_mood()
    productivity = get_productivity()
    challenge = get_challenge()

    reflection = generate_reflection(mood, productivity, challenge)

    print("\n--- Reflection Output ---")
    print(reflection)


if __name__ == "__main__":
    main()