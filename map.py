import tkinter as tk
import random
import os 
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk

'''
MLCH-151 Final Project 

Interactive Chinese Province Map with quiz mode 
'''

num_questions = 10

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class ChineseMapGUI:
    def __init__(self, root):
        
        # User (programmer) definable parameter for how many questions to choose from 

        self.root = root
        self.root.title("Interactive Map of China")

        # Load the image
        self.img = Image.open(resource_path("china-map.png"))
        self.photo = ImageTk.PhotoImage(self.img)

        # Set up the canvas
        self.canvas = tk.Canvas(root, width=self.photo.width(), height=self.photo.height())
        self.canvas.pack()

        # Display the image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Province - Food pair 
        self.province_data = {
            "Beijing": "Capital city with famous Peking Duck.",
            "Sichuan": "Known for spicy Sichuan cuisine.",
            "Xinjiang": "Big Plate Chicken (Da Pan Ji)",
            "Tibet": "Tsampa (roasted barley flour)",
            "Gansu": "Lanzhou Beef Noodle Soup",
            "Qinghai": "Yak Butter Tea",
            "Yunnan": "Crossing the Bridge Noodles",
            "Guizhou": "Sour Soup Fish",
            "Inner Mongolia": "Roasted Whole Lamb",
            "Ningxia": "Lamb Stew with Wolfberries",
            "Shaanxi": "Yang Rou Pao Mo (bread soaked in mutton stew)",
            "Guangxi": "Guilin Rice Noodles",
            "Hainan": "Hainanese Chicken Rice",
            "Guangdong": "Cantonese Dim Sum",
            "Hong Kong": "Egg Tarts",
            "Macco": "Portuguese Egg Tart",
            "Taiwan": "Beef Noodle Soup",
            "Fujian": "Fujian Red Wine Chicken",
            "Hunan": "Chairman Mao's Red Braised Pork",
            "Hubei": "Hot Dry Noodles (Re Gan Mian)",
            "Henan": "Braised Noodles (Lu Mian)",
            "Shanxi": "Knife-Cut Noodles (Dao Xiao Mian)",
            "Tianjin": "Goubuli Baozi",
            "Hebei": "Donkey Burgers",
            "Anhui": "Stinky Tofu",
            "Shanghai": "Xiaolongbao (Soup Dumplings)",
            "Jiangsu": "Sweet and Sour Mandarin Fish",
            "Shandong": "Dezhou Braised Chicken",
            "Liaoning": "Sea Cucumber with Scallions",
            "Jilin": "Ginseng Chicken Soup",
            "Heilongjiang": "Harbin Red Sausage",
            "Jiangxi": "Nanchang Rice Noodles",
            "Zhegiang": "Dongpo Pork",
        }


        # Question bank here.... 
        self.question_bank = [
            ("What is a popular food of Beijing?", "Peking Duck"),
            ("What is a popular food of Sichuan?", "Spicy Sichuan cuisine"),
            ("What is a popular food of Xinjiang?", "Big Plate Chicken (Da Pan Ji)"),
            ("What is a popular food of Tibet?", "Tsampa (roasted barley flour)"),
            ("What is a popular food of Gansu?", "Lanzhou Beef Noodle Soup"),
            ("What is a popular food of Qinghai?", "Yak Butter Tea"),
            ("What is a popular food of Yunnan?", "Crossing the Bridge Noodles"),
            ("What is a popular food of Guizhou?", "Sour Soup Fish"),
            ("What is a popular food of Inner Mongolia?", "Roasted Whole Lamb"),
            ("What is a popular food of Ningxia?", "Lamb Stew with Wolfberries"),
            ("What is a popular food of Shaanxi?", "Yang Rou Pao Mo (bread soaked in mutton stew)"),
            ("What is a popular food of Guangxi?", "Guilin Rice Noodles"),
            ("What is a popular food of Hainan?", "Hainanese Chicken Rice"),
            ("What is a popular food of Guangdong?", "Cantonese Dim Sum"),
            ("What is a popular food of Hong Kong?", "Egg Tarts"),
            ("What is a popular food of Macao?", "Portuguese Egg Tart"),
            ("What is a popular food of Taiwan?", "Beef Noodle Soup"),
            ("What is a popular food of Fujian?", "Fujian Red Wine Chicken"),
            ("What is a popular food of Hunan?", "Chairman Mao's Red Braised Pork"),
            ("What is a popular food of Hubei?", "Hot Dry Noodles (Re Gan Mian)"),
            ("What is a popular food of Henan?", "Braised Noodles (Lu Mian)"),
            ("What is a popular food of Shanxi?", "Knife-Cut Noodles (Dao Xiao Mian)"),
            ("What is a popular food of Tianjin?", "Goubuli Baozi"),
            ("What is a popular food of Hebei?", "Donkey Burgers"),
            ("What is a popular food of Anhui?", "Stinky Tofu"),
            ("What is a popular food of Shanghai?", "Xiaolongbao (Soup Dumplings)"),
            ("What is a popular food of Jiangsu?", "Sweet and Sour Mandarin Fish"),
            ("What is a popular food of Shandong?", "Dezhou Braised Chicken"),
            ("What is a popular food of Liaoning?", "Sea Cucumber with Scallions"),
            ("What is a popular food of Jilin?", "Ginseng Chicken Soup"),
            ("What is a popular food of Heilongjiang?", "Harbin Red Sausage"),
            ("What is a popular food of Jiangxi?", "Nanchang Rice Noodles"),
            ("What is a popular food of Zhejiang?", "Dongpo Pork"),
            # Probably want to add some questions about the captial ? 
        ]


        # Ensure we have at least 10 questions
        if len(self.question_bank) < num_questions:
            raise ValueError(f"Need at least {num_questions} questions in the question bank")

        # Add quiz mode button
        self.quiz_mode_button = tk.Button(root, text="Start Quiz Mode", command=self.start_quiz_mode)
        self.quiz_mode_button.pack()

        

        # Province - [X,Y] coord pair 
        self.province_coord = {

            "Beijing": [631, 240],
            "Sichuan": [424,470],
            "Xinjiang": [177,256],
            "Tibet": [217,450],
            "Gansu": [343,290],
            "Qinghai": [325,399],
            "Yunnan": [408,589],
            "Guizhou": [506,543],
            "Inner Mongolia": [483,276], 
            "Ningxia": [487,335],
            "Shaanxi": [524,405],
            "Guizhou": [501,545],
            "Guangxi": [539,600],
            "Hainan": [501,682],
            "Guangdong": [641,596],
            "Hong Kong": [691,625],
            "Macco": [620,639],
            "Taiwan": [752,587],
            "Fujian": [690,538],
            "Hunan": [582,514],
            "Hubei": [598,451],
            "Henan": [601, 389],
            "Shanxi": [569,341],
            "Tianjin": [706,294],
            "Hebei": [622,308],
            "Anhui": [678,443],
            "Shanghai": [793,437],
            "Jiangsu": [720,393],
            "Shandong": [684,338],
            "Liaoning": [721,229],
            "Jilin": [767,184],
            "Heilongjiang": [779,111], 
            "Jiangxi": [660, 493],
            "Zhegiang": [744, 476] 
        }


        # Adding invisible buttons over provinces (mock positions and sizes)

        for bruh in self.province_coord: 
            coord  = self.province_coord.get(bruh, [0,0])
            if bruh == "Inner Mongolia": 
                self.add_province_button(coord[0] - 20, coord[1] -10, 14, 2, bruh, bruh)
            else: 
                self.add_province_button(coord[0] - 20, coord[1] -10, 10, 2, bruh, bruh)

    def add_province_button(self, x, y, width, height, province, label):
        # Button with label text, can set font and style to match map aesthetics
        button = tk.Button(self.root, text=label, width=width, height=height,
                           relief="flat", borderwidth=0, highlightthickness=0,
                           command=lambda: self.show_province_info(province))
        button.place(x=x, y=y)

    def show_province_info(self, province):
        info = self.province_data.get(province, "No data available.")
        messagebox.showinfo("Province Information", f"{province}: {info}")

    def start_quiz_mode(self):
        # Randomly select questions from the question bank
        selected_questions = random.sample(self.question_bank, num_questions)
        
        # Placeholder for the quiz logic
        # You might replace this with a new window or other UI elements to show questions and get answers
        for question, answer in selected_questions:
            user_answer = simpledialog.askstring("Quiz", question)
            if user_answer.lower() == answer.lower():
                messagebox.showinfo("Correct!", "That's the right answer!")
            else:
                messagebox.showinfo("Incorrect", f"WRONG! The correct answer was {answer}")

def main():
    root = tk.Tk()
    app = ChineseMapGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
