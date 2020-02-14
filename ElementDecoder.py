# This program will take in an electron configuration and then spit out the element that is associated with said element
# Ensure that the user can also input shorthand configuration of the electron configuration as well

import periodictable as pt
import tkinter as tk
class Decoder:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("400x100")
        
        self.top_frame = tk.Frame()
        self.bottom_frame = tk.Frame()
        self.button_frame = tk.Frame()
        
        self.config_label = tk.Label(self.top_frame, text="Please enter the electron configuration you would like to decode")
        self.config_entry = tk.Entry(self.top_frame, width=65)

        self.element_label = tk.Label(self.bottom_frame, text="Element: ")
        self.element_var = tk.StringVar()
        self.element_display = tk.Label(self.bottom_frame, textvariable=self.element_var)

        self.decode_button = tk.Button(self.button_frame, text="Decode!", command=self.decode)
        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.main_window.quit)

        
        self.config_label.pack()
        self.config_entry.pack()

        self.element_label.pack(side="left")
        self.element_display.pack(side="left")

        self.decode_button.pack(side="left")
        self.quit_button.pack(side="left")

        
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()
        
        self.main_window.mainloop()

    def decode(self):
        self.total_electrons = 0

        self.electron_config_input = self.config_entry.get()
        
        self.electron_config_list = self.electron_config_input.split(" ")

        self.beginning_index = 0
        self.ending_index = 0
        self.element_in_question = ""
        self.exists = False
        
        # Checking if the element is in shorthand notation
        if "[" in self.electron_config_list[0] and "]" in self.electron_config_list[0]:
            for letter in self.electron_config_list[0]:
                if letter == "[":
                    self.beginning_index = self.electron_config_list[0].index("[")
                elif letter == "]":
                    self.ending_index = self.electron_config_list[0].index("]")
                else:
                    self.element_in_question += letter
                    
        else:
            self.element_var.set("Invalid electron configuration")

        
        if self.beginning_index == 0 and (self.ending_index != self.beginning_index or self.ending_index != self.beginning_index + 1):
            for elements in pt.elements:
                if elements.symbol == self.element_in_question:
                    self.exists = True
                    self.total_electrons += elements.number
                    break

            if self.exists:
                del self.electron_config_list[0]
            else:
                self.element_var.set("Invalid electron configuration")
                    
        else:
            self.element_var.set("Invalid electron configuration")

            
        try:
            for x in self.electron_config_list:
                if len(x) == 3:
                    self.total_electrons += int(x[2].lstrip())
                elif len(x) == 4:
                    self.total_electrons += int(x[2].lstrip() + x[3].lstrip())
            for elementNums in pt.elements:
                if elementNums.number == self.total_electrons:
                    self.element_var.set(elementNums.name.title())
        except ValueError:
            self.element_var.set("Invalid electron configuration")


d1 = Decoder()
