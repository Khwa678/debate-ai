from nodes import scientist, philosopher

def main():
    topic = input("Enter debate topic: ")
    state = {"topic": topic}

    state = scientist(state)
    print("\nScientist:", state["scientist_response"])

    state = philosopher(state)
    print("\nPhilosopher:", state["philosopher_response"])

if __name__ == "__main__":
    main()
