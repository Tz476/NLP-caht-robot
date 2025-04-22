import time
import os
import sys
import random
from openai import OpenAI

# 全局故事状态
story_state = {
    "communication_fixed": False,
    "trust_level": 0,
    "tasks_failed": 0,
    "modules_repaired": []
}


client = OpenAI(api_key='AIzaSyB-EHuc-woPyvtHp0xuE1b6CJ2k1qhkz08',
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


def initial_sequence():
    # 清屏
    os.system('cls' if os.name == 'nt' else 'clear')

    print("...Command...this...is...TZ...Do...you...copy...")
    print("\nPress Enter to continue...")
    input()

    # 身份验证
    print("Unverified identity information detected... Do you want to initiate identification? (yes/no)")
    while True:
        user_choice = input().lower()
        if user_choice == "yes":
            print("\nInitiating identity verification program...")
            print("Loading... ... ...")
            time.sleep(2)

            # 身份验证信息展示
            print("\n" + "=" * 50)
            print("Emergency Communication System")
            print("=" * 50)
            print("\nAccess Level: Commander")
            print("Security Clearance: ALPHA")
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
                    print("Status: Authenticated")
                    print("Security Protocol: Activated")
                    print("Encryption: Enabled")
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
    # 获取用户姓名
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
            # 模拟简单的对话，不调用API
            if "yes" in user_input.lower() or "can" in user_input.lower():
                print(f"TZ: Very...glad...to receive...your response, Commander {player_name}.")
                time.sleep(1)
                print("TZ: My communication device...is damaged...I need...your help...to repair...")
                time.sleep(1)
                print("TZ: Are you willing...to help me? (yes/no)")
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
                print("TZ: ...Signal...unstable...Please...repeat...")


def mission_sequence(player_name):
    # 模块列表
    # modules = ["Power Module", "Signal Amplifier", "Antenna Calibration", "Data Decoder", "Cooling System"]
    modules = ["Power Module", "Signal Amplifier", "Data Decoder"]
    # random.shuffle(modules)

    for module in modules:
        if story_state["tasks_failed"] >= 2:
            tragic_ending()
            return
       
    #     print(f"\nTZ:Need to repair...{module}...Please choose an action...")

    #     options = generate_options()
    #     while True:
    #         for idx, option in enumerate(options, 1):
    #             print(f"{idx}. {option['description']}")
    #         choice = input("Please choose an option (enter the number): ")
    #         if choice.isdigit() and 1 <= int(choice) <= len(options):
    #             selected_option = options[int(choice) - 1]

    #             # TZ需要时间执行选项，期间询问玩家是否想了解更多
    #             print("TZ: ...Executing the option now, this may take some time...")
    #             time.sleep(1)
    #             print("TZ: ...Would you like to hear more about related matters? (yes/no)")
    #             while True:
    #                 hear_story_choice = input("You: ").lower()
    #                 if hear_story_choice == 'yes':
    #                     tell_war_story(player_name)
    #                     break
    #                 elif hear_story_choice == 'no':
    #                     time.sleep(2)
    #                     print("TZ: ...")
    #                     break
    #                 else:
    #                     print("Please answer 'yes' or 'no'")
    #             # 执行任务
    #             success = perform_task(selected_option)
    #             if success:
    #                 print(f"TZ: ...{module} repair...completed...Thank you...for your help...")
    #                 story_state["modules_repaired"].append(module)
    #                 break
    #             else:
    #                 print("TZ: ...Operation failed...Please try again...")
    #                 story_state["tasks_failed"] += 1
    #                 break
    #         else:
    #             print("Invalid input, please enter a valid option number.")
    #     # 在任务间隙，移除了自动讲故事的部分
    # # 判断结局
    # if story_state["tasks_failed"] >= 2:
    #     tragic_ending()
    # else:
    #     happy_ending(player_name)
        print(f"\nTZ: ...Need to repair...{module}...Please follow the instructions...")
        if module == "Power Module":
            success = repair_power_module()
        elif module == "Signal Amplifier":
            success = repair_signal_amplifier()
        elif module == "Data Decoder":
            success = repair_data_decoder()
        if success:
            print(f"TZ: ...{module} repair completed...Thank you very much for your help...")
            story_state["modules_repaired"].append(module)
        else:
            print(f"TZ: ...Failed to repair {module}...")
            story_state["tasks_failed"] += 1
        # Story interaction
        
        print("TZ: ...Would you like to hear more related stories from me? (yes/no)")
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


# def generate_options():
#     # 生成随机任务选项
#     option_templates = [
#         {"description": "Use standard tools for regular repair. (High success rate, low reward)", "difficulty": 1,
#          "reward": 10},
#         {"description": "Attempt to upgrade the module for better performance. (Medium success rate, medium reward)",
#          "difficulty": 2, "reward": 20},
#         {"description": "Perform advanced optimization to push performance limits. (Low success rate, high reward)",
#          "difficulty": 3, "reward": 30}
#     ]
#     random.shuffle(option_templates)
#     num_options = random.randint(2, 3)
#     return option_templates[:num_options]


# def perform_task(option):
#     # 根据选项的难度和随机因素决定任务成功与否
#     success_chance = {1: 0.9, 2: 0.6, 3: 0.3}
#     chance = success_chance[option["difficulty"]]
#     result = random.random() < chance
#     return result

# mission1
def repair_power_module():
    print("\nTZ: The power circuit needs to be reconnected.")
    print("There are five nodes on the circuit board: A, B, C, D, E.")
    print("You need to start from node A, connect to node E, pass through all nodes without repeating.")
    print("Please enter the connection sequence in the format (e.g., A-B-C-D-E):")
    attempts = 0
    correct_sequence = ['A', 'C', 'B', 'D', 'E']
    while attempts < 3:
        user_input = input("Connection sequence: ").upper().replace(' ', '').split('-')
        if user_input == correct_sequence:
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
    print("The frequency range is between 1000Hz and 5000Hz.")
    print("You have 5 attempts.")
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
    print("Encrypted message: 'KHOOR ZRUOG'")
    print("Hint: Using Caesar cipher with a shift of 3.")
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
    # 将响应拆分为行或段落
    lines = response.strip().split('\n')
    print("\nTZ: ")
    for line in lines:
        if line.strip() != '':
            print(line.strip())
            time.sleep(2)  # 每行间隔2秒
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
    # 从API响应中提取生成的回复
    response_text = response.choices[0].message.content
    return response_text.strip()


def tragic_ending():
    print("\nTZ: ...Signal fading... Unable to maintain... communication...")
    print("As the last sparks of connection dim, you feel an overwhelming sense of loss.")
    print("The vastness of space swallows the remnants of TZ's voice, leaving only silence.")
    print("System: You have lost contact with TZ.")
    print("In the depths of the cosmos, another story ends without closure.")
    print("Game Over.")

def happy_ending(player_name):
    print(f"\nTZ: ...All systems restored... Successfully reestablished communication with the Command Center...")
    print(f"TZ: ...Thank you, Commander {player_name}. Your assistance has reignited hope across the galaxies.")
    print("TZ: ...Your efforts will be remembered as a beacon against the darkness that engulfs our worlds...")
    print("TZ: ...Please share your final message to be transmitted across the stars...")
    ending_message = input("You: ")
    print(f"TZ: ...Your message '{ending_message}' will echo through the cosmos, inspiring countless others...")
    print("As the connection strengthens, you witness a cascade of lights spreading across the starry expanse.")
    print("A new chapter begins, forged by your courage and determination.")
    print("Game Over.")

if __name__ == "__main__":
    start_conversation()
