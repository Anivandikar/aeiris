from core.brain import think

def main():
    print("AEIRIS booting up… yeah, I’m awake.")

    while True:
        user = input("You: ").strip()
        if user.lower() in ["exit", "quit"]:
            print("AEIRIS: Okay, I’m out. Bye.")
            break

        reply = think(user)
        print(f"AEIRIS: {reply}")

if __name__ == "__main__":
    main()
