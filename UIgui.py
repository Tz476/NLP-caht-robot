# gui_tkinter.py
import tkinter as tk
from chatbot_logic import chatbot_reply, reset_story_state

# 发送按钮回调
def on_send():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_log.insert(tk.END, f"You: {user_input}\n")
    reply = chatbot_reply(user_input)
    chat_log.insert(tk.END, f"TZ: {reply}\n\n")
    chat_log.see(tk.END)
    entry.delete(0, tk.END)

# 重置对话
def on_reset():
    reset_story_state()
    chat_log.insert(tk.END, "=== New Session Started ===\n")
    chat_log.insert(tk.END, "TZ: Command this is...TZ Do...Do you...copy...\n")
    chat_log.insert(tk.END, "TZ: Do you want to initiate identification? (yes/no)\n\n")

# 创建窗口
root = tk.Tk()
root.title("TZ Lost War Robot - Chatbot")

# 聊天窗口
chat_log = tk.Text(root, height=25, width=60)
chat_log.pack()

# 输入框
entry = tk.Entry(root, width=60)
entry.pack()

# 发送按钮
send_button = tk.Button(root, text="Send", command=on_send)
send_button.pack()

# 重置按钮
reset_button = tk.Button(root, text="Reset", command=on_reset)
reset_button.pack()

# 启动初始对话
on_reset()

# 启动主循环
root.mainloop()
