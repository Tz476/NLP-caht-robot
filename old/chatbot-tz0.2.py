from openai import OpenAI
import time


client = OpenAI(api_key='AIzaSyB-EHuc-woPyvtHp0xuE1b6CJ2k1qhkz08',base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# Global story state
story_state = {
    "communication_fixed": False,
    "trust_level": 0,
}

def initial_sequence():
    while True:
        print("Call the Command Center...")
        time.sleep(3)  # print every 3s
        user_input = input()
        if user_input:  
            break


    # second stage
    print("Unverified identity information detected. Initiate identification? (yes/no)")
    while True:
        user_choice = input().lower()
        if user_choice == "yes":
            # third stage
            print("\nInitiating identification process...")
            print("Loading... ... ...")
            time.sleep(2)
            
            # 身份验证信息展示
            print("\n" + "="*50)
            print("EMERGENCY COMMUNICATION SYSTEM")
            print("="*50)
            print("\nACCESS LEVEL: COMMANDER")
            print("SECURITY CLEARANCE: ALPHA")
            print("Please state your name for verification.")
            
            while True:
                player_name = input("\nName: ").strip()
                if player_name:
                    # 验证成功后的信息
                    print("\nINITIATING SECURITY SCAN...")
                    time.sleep(1)
                    print("VERIFYING CREDENTIALS...")
                    time.sleep(1)
                    print("ESTABLISHING SECURE CONNECTION...")
                    time.sleep(1)
                    
                    print("\n" + "="*50)
                    print(f"WELCOME, COMMANDER {player_name.upper()}")
                    print("STATUS: AUTHENTICATED")
                    print("SECURITY PROTOCOL: ACTIVE")
                    print("ENCRYPTION: ENABLED")
                    print("="*50)
                    
                    time.sleep(2)
                    print("\nWARNING: Unusual signal detected...")
                    time.sleep(1)
                    print("Origin: Unknown")
                    time.sleep(1)
                    print("Signal strength: Strong")
                    time.sleep(1)
                    print("\nAttempting to establish communication channel...")
                    time.sleep(2)
                    
                    return True, player_name
                else:
                    print("ERROR: Invalid input. Please state your name.")
        elif user_choice == "no":
            print("Connection terminated.")
            return False, None
        else:
            print("Please answer 'yes' or 'no'")

def start_conversation():
    success, player_name = initial_sequence()
    if not success:
        return
    
    print("\n" + "="*50)
    print("INCOMING TRANSMISSION")
    print("="*50)
    time.sleep(1)
    print("\nTZ: Commander, this is TZ, an autonomous combat unit from the Centauri Defense Force.")
    time.sleep(2)
    print("\nTZ: Our fleet has detected an imminent threat approaching Earth's coordinates.")
    time.sleep(2)
    print("\nTZ: I've been dispatched to establish first contact and coordinate defense preparations.")
    time.sleep(2)
    print(f"\nTZ: Commander {player_name}, I need your immediate assistance to assess Earth's current defensive capabilities.")
    time.sleep(1)
    print("\nSystem: Please respond to TZ's request.")
    print("\n(Tip: Type 'exit', 'bye', or 'goodbye' at any time to end the conversation.)")
    
    conversation_history = [
        {"role": "system", "content": (
            f"You are TZ, an autonomous combat unit from the Centauri Defense Force. "
            f"You are speaking with Commander {player_name} from Earth's defense forces. "
            f"Always address them as 'Commander {player_name}'. "
            "Your mission is to gather information about Earth's defensive capabilities "
            "and help prepare for an incoming threat. Stay focused on the mission "
            "while maintaining a professional but urgent tone."
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
