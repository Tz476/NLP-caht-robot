import time
import os
import sys
import random
from openai import OpenAI

# Global story state
story_state = {
    "communication_fixed": False,
    "tasks_failed": 0,
    "modules_repaired": []
}


client = OpenAI(api_key='AIzaSyB-EHuc-woPyvtHp0xuE1b6CJ2k1qhkz08',
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


def initial_sequence():
    # clean screem
    # I want to stay more focused in the terminal, so I've added this piece of code.
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Command this is...TZ Do...Do you...copy...")
    print("\nPress Enter to continue...")
    input()

    # identiy information
    # To simulate the authenticity of message sending, waiting intervals are inserted between each message.
    print("Unver..ified identity information detected... Do you want to initiate identification? (yes/no)")
    while True:
        user_choice = input().lower()
        if user_choice == "yes":
            print("\nInitiating identity...verification program...")
            print("Loading... ... ...")
            time.sleep(2)

            # Identity Verification Information Display
            print("\n" + "=" * 50)
            print("Emergency Communication System")
            print("=" * 50)
            time.sleep(1)
            print("\nAccess Level: Commander")
            time.sleep(1)
            print("Security Clearance: ALPHA")
            time.sleep(1)
            print("Please enter your name for verification.")

            while True:
                player_name = input("\nName: ").strip()
                if player_name:
                    print("\nPerforming security scan...")
                    time.sleep(1)
                    print("Verifying credentials...")
                    time.sleep(1)
                    print("Establishing secure connection...")
                    time.sleep(1)

                    print("\n" + "=" * 50)
                    print(f"Welcome, Commander {player_name}")
                    time.sleep(1)
                    print("Status: Authenticated")
                    time.sleep(1)
                    print("Security Protocol: Activated")
                    time.sleep(1)
                    print("Encryption: Enabled")
                    time.sleep(1)
                    print("=" * 50)

                    time.sleep(2)
                    print("\nWarning: Anomalous signal detected...")
                    time.sleep(1)
                    print("Signal Source: Unknown")
                    time.sleep(1)
                    print("Signal Strength: Strong")
                    time.sleep(1)
                    print("\nAttempting to establish communication channel...")
                    time.sleep(2)

                    return True, player_name
                else:
                    print("Error: Invalid input. Please enter your name.")
        elif user_choice == "no":
            print("Connection terminated.")
            return False, None
        else:
            print("Please answer 'yes' or 'no'")


def start_conversation():
    # user name
    success, player_name = initial_sequence()
    if not success:
        return

    print("\n" + "=" * 50)
    print("Incoming transmission from unknown source...")
    print("=" * 50)
    time.sleep(1)
    print(f"\nTZ: Commander {player_name} are you...are you still here?")
    time.sleep(1)
    print("\n(Please respond to TZ's request.Tip: Type 'exit', 'bye', or 'goodbye' at any time to end the conversation.)")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'bye', 'goodbye']:
            print("TZ: Connection terminated...Goodbye...")
            break
        else:
            
            if "yes" in user_input.lower() or "can" in user_input.lower():
                print(f"TZ: Very...glad...to receive...your response, Commander {player_name}.")
                time.sleep(1)
                print("TZ: My communication device...is damaged...I need...your help...to repair...")
                time.sleep(1)
                print("TZ: Are you willing...to help me? ")
                while True:
                    help_choice = input("You: ").lower()
                    if help_choice == "yes":
                        print("TZ: ...Much appreciated...Let's begin...the repair...")
                        story_state["communication_fixed"] = False
                        mission_sequence(player_name)
                        break
                    elif help_choice == "no":
                        print("TZ: ...Understood...Thank you...for your time...")
                        break
                    else:
                        print("Please answer 'yes' or 'no'")
                break
            else:
                print("TZ: Signal...unstable...Please...repeat...")

#three mission
def mission_sequence(player_name):
    modules = ["Power Module", "Signal Amplifier", "Data Decoder"]
    for module in modules:
        if story_state["tasks_failed"] >= 2:
            tragic_ending()
            return
        print(f"\nTZ: ...Need to repair...{module}...Please follow the instructions...")
        if module == "Power Module":
            success = repair_power_module()
        elif module == "Signal Amplifier":
            success = repair_signal_amplifier()
        elif module == "Data Decoder":
            success = repair_data_decoder()
        if success:
            print(f"TZ: ...Thank you for your guidance. I now need some time to proceed with the repair of {module}. Please wait a moment...")
            story_state["modules_repaired"].append(module)
        else:
            print(f"TZ: ...Failed to repair {module}...")
            story_state["tasks_failed"] += 1
        # Use random prompts to ask players if they would like to hear a story.
        story_prompts = [
            "TZ: ...This reminds me of past events. Would you like to hear about them? (yes/no)",
            "TZ: ...Your actions evoke certain memories. Shall I share them with you? (yes/no)",
            "TZ: ...There is a story related to this. Do you wish to hear it? (yes/no)",
            "TZ: ...I have experienced similar situations before. Would you like me to tell you about them? (yes/no)",
            "TZ: ...These circumstances bring back stories. Interested in listening? (yes/no)"
        ]
        prompt = random.choice(story_prompts)
        print(prompt)
        while True:
            hear_story_choice = input("You: ").lower()
            if hear_story_choice == 'yes':
                tell_war_story(player_name)
                break
            elif hear_story_choice == 'no':
                time.sleep(1)
                print("TZ: ...Understood...")
                break
            else:
                print("Please answer 'yes' or 'no'")
    # Determine the ending
    if story_state["tasks_failed"] >= 2:
        tragic_ending()
    else:
        happy_ending(player_name)

# mission1
def repair_power_module():
    print("\nTZ: The power circuit needs to be reconnected.")
    time.sleep(1)
    print("There are five nodes on the circuit board: A, B, C, D, E.")
    time.sleep(1)
    print("You need to start from node A, connect to node E, pass through all nodes. You may need to pass through some nodes more than once.")
    time.sleep(1)
    print("Here is a detailed diagram of the circuit:")
    print("""
                  [A]
                   
              [C]
          
                 [B]     [D]
                      
                    [E]
    """)
    print("Please enter the connection sequence in the format (e.g., A-B-C-D-E):")
    attempts = 0
    correct_sequences = [
        ['A', 'C', 'B', 'D', 'E'],
        ['A', 'C', 'D', 'B', 'E'],
        ['A', 'D', 'C', 'B', 'E']
    ]
    while attempts < 3:
        user_input = input("Connection sequence: ").upper().replace(' ', '').split('-')
        if user_input in correct_sequences:
            return True
        else:
            attempts += 1
            if attempts < 3:
                print("TZ: ...Incorrect connection sequence. Please try again.")
            else:
                print("TZ: ...Multiple failed attempts detected. Initiating backup plan...")
    return False


# mission2
def repair_signal_amplifier():
    print("\nTZ: The signal amplifier needs to be tuned to the correct frequency.")
    time.sleep(1)
    print("The frequency range is between 1000Hz and 5000Hz.")
    time.sleep(1)
    print("You have 5..... no 10 attempts.")
    correct_frequency = 3420
    attempts = 0
    while attempts < 5:
        try:
            frequency = int(input("Please enter the frequency value (Hz): "))
            if frequency == correct_frequency:
                print("TZ: ...Signal stabilized.")
                return True
            elif frequency < 1000 or frequency > 5000:
                print("TZ: ...Frequency out of range.")
            elif abs(frequency - correct_frequency) <= 50:
                print("TZ: ...Very close, signal enhanced.")
            elif frequency < correct_frequency:
                print("TZ: ...Frequency too low, interference increasing.")
            else:
                print("TZ: ...Frequency too high, interference increasing.")
            attempts += 1
        except ValueError:
            print("Please enter a valid numerical frequency.")
            attempts += 1
            if attempts == 10:
                print("TZ: ...Multiple failed attempts detected. Initiating backup plan...")
    return False

# mission3
def repair_data_decoder():
    print("\nTZ: The data decoder needs to decode an encrypted message.")
    time.sleep(1)
    print("Encrypted message: 'KHOOR ZRUOG'")
    time.sleep(1)
    print("Hint: Using Caesar cipher with a shift of 3.")
    time.sleep(1)
    attempts = 0
    while attempts < 3:
        user_input = input("Decoded message: ").upper()
        if user_input == "HELLO WORLD":
            return True
        else:
             attempts += 1
             if attempts < 3:
                print("TZ: ...Decoding error. Please try again.")
             else:
                print("TZ: ...Multiple failed attempts detected. Initiating backup plan...")
    return False



def tell_war_story(player_name):
     # TZ uses LLM to tell a war story
    prompt = (
        f"Act as TZ, an autonomous war robot from an advanced alien civilization. "
        f"You are sharing a poignant and tragic war story with Commander {player_name}. "
        "The story should be about different planets and civilizations experiencing hardships "
        "during energy wars at varying technological levels. Make it emotionally impactful, "
        "but avoid any inappropriate content."
    )
    response = generate_response(prompt)
    # Split the response into lines or paragraphs.
    lines = response.strip().split('\n')
    print("\nTZ: ")
    for line in lines:
        if line.strip() != '':
            print(line.strip())
            time.sleep(2)  
    time.sleep(2)


def generate_response(prompt):
    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        n=1,
        messages=[
            {"role": "system", "content": "You are TZ, an autonomous war robot."},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the generated reply from the API response."
    response_text = response.choices[0].message.content
    return response_text.strip()


def tragic_ending():
    print("\nTZ: ...Signal fading... Unable to maintain... communication...")
    time.sleep(1)
    print("As the last sparks of connection dim, you feel an overwhelming sense of loss.")
    time.sleep(1)
    print("The vastness of space swallows the remnants of TZ's voice, leaving only silence.")
    time.sleep(1)
    print("System: You have lost contact with TZ.")
    time.sleep(1)
    print("In the depths of the cosmos, another story ends without closure.")
    time.sleep(1)
    print("Game Over.")

def happy_ending(player_name):
    print(f"\nTZ: ...All systems restored... Successfully reestablished communication with the Command Center...")
    time.sleep(1)
    print(f"TZ: ...Thank you, Commander {player_name}. Your assistance has reignited hope across the galaxies.")
    time.sleep(1)
    print("TZ: ...Your efforts will be remembered as a beacon against the darkness that engulfs our worlds...")
    time.sleep(1)
    print("TZ: ...Please share your final message to be transmitted across the stars...")
    ending_message = input("You: ")
    print(f"TZ: ...Your message '{ending_message}' will echo through the cosmos, inspiring countless others...")
    time.sleep(1)
    print("As the connection strengthens, you witness a cascade of lights spreading across the starry expanse.")
    time.sleep(1)
    print("A new chapter begins, forged by your courage and determination.")
    time.sleep(1)
    print("Game Over.")

if __name__ == "__main__":
    start_conversation()
