import time
import os  
import sys
import random
import openai

# 全局故事状态  
story_state = {
    "communication_fixed": False,
    "trust_level": 0,
    "tasks_failed": 0,
    "modules_repaired": []
}

# 使用你的 OpenAI API 密钥
openai.api_key = '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'

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
            print("\n" + "="*50)
            print("Emergency Communication System")
            print("="*50)
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
                    
                    print("\n" + "="*50)
                    print(f"Welcome, Commander {player_name}")
                    print("Status: Authenticated")
                    print("Security Protocol: Activated")
                    print("Encryption: Enabled")
                    print("="*50)
                    
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
    
    print("\n" + "="*50)
    print("...Incoming transmission from unknown source...")
    print("="*50)
    time.sleep(1)
    print(f"\nTZ: ...Commander {player_name}...can...you...hear...me...")
    time.sleep(2)
    print("\nSystem: Please respond to TZ's request.")
    time.sleep(1)
    print("\n(Tip: Type 'exit', 'bye', or 'goodbye' at any time to end the conversation.)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'bye', 'goodbye']:
            print("TZ: ...Connection terminated...Goodbye...")
            break
        else:
            # 模拟简单的对话，不调用API
            if "yes" in user_input.lower() or "can" in user_input.lower():
                print(f"TZ: ...Very...glad...to receive...your response, Commander {player_name}.")
                time.sleep(1)
                print("TZ: ...My communication device...is damaged...I need...your help...to repair...")
                time.sleep(1)
                print("TZ: ...Are you willing...to help me? (yes/no)")
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
    modules = ["Power Module", "Signal Amplifier", "Antenna Calibration", "Data Decoder", "Cooling System"]
    random.shuffle(modules)
    
    for module in modules:
        if story_state["tasks_failed"] >= 2:
            tragic_ending()
            return
        print(f"\nTZ: ...Need to repair...{module}...Please choose an action...")
        options = generate_options()
        while True:
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option['description']}")
            choice = input("Please choose an option (enter the number): ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                selected_option = options[int(choice)-1]
                success = perform_task(selected_option)
                if success:
                    print(f"TZ: ...{module} repair...completed...Thank you...for your help...")
                    story_state["modules_repaired"].append(module)
                    break
                else:
                    print("TZ: ...Operation failed...Please try again...")
                    story_state["tasks_failed"] += 1
                    break
            else:
                print("Invalid input, please enter a valid option number.")
        # 在任务间隙，TZ使用LLM讲述战争故事
        if len(story_state["modules_repaired"]) < len(modules):
            tell_war_story(player_name)
    # 判断结局
    if story_state["tasks_failed"] >= 2:
        tragic_ending()
    else:
        happy_ending(player_name)

def generate_options():
    # 生成随机任务选项
    option_templates = [
        {"description": "Use standard tools for regular repair. (High success rate, low reward)", "difficulty": 1, "reward": 10},
        {"description": "Attempt to upgrade the module for better performance. (Medium success rate, medium reward)", "difficulty": 2, "reward": 20},
        {"description": "Perform advanced optimization to push performance limits. (Low success rate, high reward)", "difficulty": 3, "reward": 30}
    ]
    random.shuffle(option_templates)
    num_options = random.randint(2, 3)
    return option_templates[:num_options]

def perform_task(option):
    # 根据选项的难度和随机因素决定任务成功与否
    success_chance = {1: 0.9, 2: 0.6, 3: 0.3}
    chance = success_chance[option["difficulty"]]
    result = random.random() < chance
    return result

def tell_war_story(player_name):
    # TZ使用LLM讲述战争故事
    prompt = (
        f"Act as TZ, an autonomous war robot from an advanced alien civilization. "
        f"You are sharing a poignant and tragic war story with Commander {player_name}. "
        "The story should be about different planets and civilizations experiencing hardships "
        "during energy wars at varying technological levels. Make it emotionally impactful, "
        "but avoid any inappropriate content."
    )
    response = generate_response(prompt)
    print("\nTZ: " + response)
    time.sleep(2)

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are TZ, an autonomous war robot."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    # Extract the generated response from the API response
    response_text = response['choices'][0]['message']['content']
    return response_text.strip()
   

def tragic_ending():
    print("\nTZ: ...Signal lost...Unable to continue...communication...")
    print("System: You have lost contact with TZ.")
    print("Game Over.")

def happy_ending(player_name):
    print(f"\nTZ: ...All modules repaired...Successfully restored communication with Command Center...")
    print(f"TZ: ...Thank you very much...for your help, Commander {player_name}.")
    print("TZ: ...Please leave your final message...")
    ending_message = input("You: ")
    print(f"TZ: ...Received your message: {ending_message}...Wishing you all the best...")
    print("Game Over.")

if __name__ == "__main__":
    start_conversation()
