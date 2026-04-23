def detect_mood(text):
    text = text.lower()

    if "good" in text or "great" in text:
        return "good"
    elif "bad" in text or "terrible" in text:
        return "bad"
    else:
        return "okay"


def detect_productivity(text):
    text = text.lower()

    if "high" in text or "productive" in text:
        return "high"
    elif "low" in text or "not productive" in text:
        return "low"
    else:
        return "medium"


def detect_challenge(text):
    text = text.lower()

    if "work" in text or "study" in text:
        return "work"
    elif "time" in text:
        return "time"
    elif "stress" in text or "emotional" in text or "personal" in text:
        return "personal"
    else:
        return "none"


def generate_reflection(mood, productivity, challenge):

    if mood == "good" and productivity == "high":
        result = "You had a great and productive day. Try to repeat what worked well."

    elif mood == "good" and productivity == "low":
        result = "You felt good, but productivity was low. Consider setting clearer goals."

    elif mood == "okay" and productivity == "medium":
        result = "Your day was average. Small improvements can make it better."

    elif mood == "bad" and productivity == "low":
        result = "It seems like a difficult day. Focus on one small improvement tomorrow."

    else:
        result = "Reflect on your day and try to improve gradually."

    if challenge == "work":
        result += "\nFocus on prioritizing tasks."

    elif challenge == "time":
        result += "\nTry using a schedule or time-blocking."

    elif challenge == "personal":
        result += "\nTake time to reflect or talk to someone."

    elif challenge == "none":
        result += "\nKeep maintaining your routine."

    return result


def main():
    print("Daily Reflection Agent")

    mood_input = input("\nHow was your day? ")
    productivity_input = input("How productive were you? ")
    challenge_input = input("What was your main challenge? ")

    mood = detect_mood(mood_input)
    productivity = detect_productivity(productivity_input)
    challenge = detect_challenge(challenge_input)

    reflection = generate_reflection(mood, productivity, challenge)

    print("\n--- Reflection Output ---")
    print(reflection)


if __name__ == "__main__":
    main()