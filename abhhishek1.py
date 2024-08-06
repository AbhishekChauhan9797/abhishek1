import tkinter as tk
from tkinter import messagebox
class Chatbot:
    def _init_(self):
        self.root = (link)()
        self.root.title("Chatbot")

        self.chat_history = tk.Text(self.root, width=50, height=10)
        self.chat_history.grid(row=0, column=0, columnspan=2)

        self.user_input = tk.Entry(self.root, width=50)
        self.user_input.grid(row=1, column=0)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1)

    def send_message(self):
        user_message = self.user_input.get()
        self.chat_history.insert(tk.END, "You: " + user_message + "\n")

   
        if "hello" in user_message.lower():
            response = "Hello! How can I assist you?"
        elif "bye" in user_message.lower():
            response = "Goodbye! Have a great day!"
        else:
            response = "I'm not sure I understand. Can you please rephrase self.chat_history.insert(tk.END, "Chatbot: " + response + "\n")
        self.user_input.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if _name_ == "_main_":
    chatbot = Chatbot()
    chatbot.run()

