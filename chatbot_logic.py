# chatbot_logic.py
import time
import random

# 简单状态
story_state = {
    "authenticated": False,
    "player_name": None,
    "chat_stage": "initial",  # 可以是 'initial', 'chatting', 'mission', 'ending'
    "communication_fixed": False,
    "tasks_failed": 0,
    "modules_repaired": []
}

# 用于 GUI，输入一条 user_input，返回一条机器人回复
def chatbot_reply(user_input):
    global story_state

    # 初始阶段：身份认证
    if story_state["chat_stage"] == "initial":
        if not story_state["authenticated"]:
            if user_input.lower() in ["yes", "y"]:
                story_state["authenticated"] = True
                story_state["chat_stage"] = "ask_name"
                return "Initiating identity verification... Please enter your name:"
            elif user_input.lower() in ["no", "n"]:
                story_state["chat_stage"] = "ending"
                return "Connection terminated."
            else:
                return "Do you want to initiate identification? (yes/no)"
        else:
            return "Already authenticated. Please enter your name:"

    # 输入名字
    elif story_state["chat_stage"] == "ask_name":
        if user_input.strip() == "":
            return "Error: Invalid input. Please enter your name."
        else:
            story_state["player_name"] = user_input.strip()
            story_state["chat_stage"] = "chatting"
            return f"Welcome, Commander {story_state['player_name']}.\n\nAnomalous signal detected...\nSignal Source: Unknown.\n\nTZ: Commander {story_state['player_name']}, are you still here?"

    # 聊天阶段
    elif story_state["chat_stage"] == "chatting":
        if user_input.lower() in ['exit', 'bye', 'goodbye']:
            story_state["chat_stage"] = "ending"
            return "TZ: Connection terminated... Goodbye..."
        elif "yes" in user_input.lower() or "can" in user_input.lower():
            story_state["chat_stage"] = "mission"
            return f"TZ: Very glad to receive your response, Commander {story_state['player_name']}.\nMy communication device is damaged. I need your help to repair it.\nAre you willing to help me? (yes/no)"
        else:
            return "TZ: Signal unstable... Please repeat..."

    # 任务阶段
    elif story_state["chat_stage"] == "mission":
        if user_input.lower() == "yes":
            story_state["chat_stage"] = "mission_started"
            return "TZ: ...Much appreciated... Let's begin the repair..."
        elif user_input.lower() == "no":
            story_state["chat_stage"] = "ending"
            return "TZ: ...Understood... Thank you for your time..."
        else:
            return "Please answer 'yes' or 'no'"

    # 修复任务（先占位，后面我们可以加完整的 mission_sequence 逻辑）
    elif story_state["chat_stage"] == "mission_started":
        # 这里你可以调用 repair_xxx 函数
        return "TZ: Starting repair mission... (mission system coming soon!)"

    # 结束阶段
    elif story_state["chat_stage"] == "ending":
        return "System: Conversation ended."

    # 默认 fallback
    else:
        return "TZ: ...System error... Please restart the connection."

# 初始化状态（可以给 GUI 用来重置游戏）
def reset_story_state():
    global story_state
    story_state = {
        "authenticated": False,
        "player_name": None,
        "chat_stage": "initial",
        "communication_fixed": False,
        "tasks_failed": 0,
        "modules_repaired": []
    }