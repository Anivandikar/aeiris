from core.brain import think
from voice.tts import speak


def main():
    startup = "Yeah okay… I’m awake."
    print(f"AEIRIS: {startup}")
    speak(startup)

    while True:
        user = input("You: ").strip()

        if user.lower() in ["exit", "quit"]:
            goodbye = "Okay, I’m out. Bye."
            print(f"AEIRIS: {goodbye}")
            speak(goodbye)
            break

        reply = think(user)
        print(f"AEIRIS: {reply}")
        speak(reply)


if __name__ == "__main__":
    main()
