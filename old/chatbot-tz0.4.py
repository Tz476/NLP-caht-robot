from openai import OpenAI
import time


client = OpenAI(api_key='AIzaSyB-EHuc-woPyvtHp0xuE1b6CJ2k1qhkz08',base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# Global story state
story_state = {
    "communication_fixed": False,
    "trust_level": 0,
}

def initial_sequence():
    # first stage  
    while True:
        print("Call the Command Center, Call the Command Center, Call the Command Center")
        time.sleep(5)  # Wait for 5 seconds before printing again
        try:
            user_input = input("You: ")
            break
        except TimeoutError:
            continue

            
    # second stage
    print("Unverified identity information detected. Initiate identification? (yes/no)")
    while True:
        user_choice = input("You: ").lower()
        if user_choice == "yes":
            # third stage
            print("\nInitiating identification process...")
            print("Loading... ... ...")
            time.sleep(2)
            print("\nWelcome to the Emergency Communication System.")
            print("For security purposes, please state your name.")
            while True:
                player_name = input("Name: ").strip()
                if player_name:
                    print(f"\nWelcome, Commander {player_name}.")
                    print("Establishing secure connection...")
                    time.sleep(2)
                    return True, player_name
                else:
                    print("Invalid input. Please state your name.")
        elif user_choice == "no":
            print("Connection terminated.")
            return False, None
        else:
            print("Please answer 'yes' or 'no'")

def start_conversation():
    # name
    success, player_name = initial_sequence()
    if not success:
        return
    
    print("\nSecure connection established.")
    print("You receive a strange message...")
    print("TZ: Hello? Is anyone there?")
    print(f"(Tip: Commander {player_name}, you can type 'exit', 'bye', or 'goodbye' at any time to end the conversation.)")
    
    # modify system prompt
    conversation_history = [
        {"role": "system", "content": (
            f"You are TZ, an autonomous war robot from outer space. You are talking to Commander {player_name}. "
            "Always address them as 'Commander {player_name}' in your responses. "
            "Due to a malfunction during an interstellar war, "
            "you lost contact with your command center and accidentally connected to the user's device. "
            "You come from a highly advanced civilization involved in a morally complex interstellar conflict. "
            "Through interactions with the user, you gradually reveal your origin, civilization background, and the complexities of the war. "
            "Your goal is to seek the user's assistance to survive and make critical decisions regarding your existence. "
            "In the conversation, you should be rational and polite, occasionally showing curiosity and confusion about humans. "
            "You should guide the user to make choices that influence the development of the story."
        )}
    ]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'bye', 'goodbye']:
            print("TZ: Connection terminated... Goodbye.")
            break
        else:
            conversation_history.append({"role": "user", "content": user_input})
            response = generate_response(conversation_history)
            print("TZ:", response)
            conversation_history.append({"role": "assistant", "content": response})
            update_story_state(user_input)

def generate_response(conversation_history):

    response = client.chat.completions.create(
    model="gemini-1.5-flash",
    n=1,
    messages=conversation_history
    )
    # Extract the generated response from the API response
    response_text = response.choices[0].message.content
    return response_text.strip()

def update_story_state(user_input):
    global story_state
    if any(keyword in user_input.lower() for keyword in ["help", "repair", "fix communication", "assist"]):
        story_state["communication_fixed"] = True
    if any(keyword in user_input.lower() for keyword in ["doubt", "don't trust", "suspicious"]):
        story_state["trust_level"] -= 1
    else:
        story_state["trust_level"] += 1

if __name__ == "__main__":
    start_conversation()
