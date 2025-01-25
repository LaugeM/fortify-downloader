import tkinter as tk
import ttkbootstrap as ttk
import requests
import json
import os

# Downloading json from builderssanctuary

def SancDownload():
    sanc_code = SancCodeStr.get()
    file_name = NameStr.get()
    if file_name == "":
        file_name = sanc_code
    resp = requests.get(f"https://builderssanctuary.com/download/fortify/{sanc_code}")
    print("checking code")
    if resp.status_code == 200:
        print("Success")
        sanc_json = resp.json()
        CreateFile(sanc_json, file_name)
        return "200"
    elif resp.status_code == 500:
        print("Invalid code")
        return "500"
    else:
        print("Got no response from builderssanctuary.com")
        return "404"


# Save the json file to fortify directory
def CreateFile(BaseJson, filename):
    dir = "D:\SteamLibrary\steamapps\common\FORTIFY\Fortify_Data\Saves"
    full_path = os.path.join(dir, f"{filename}.json")
    with open(full_path, 'w') as f:
        json_string=json.dumps(BaseJson)
        f.write(json_string)


# window
window = ttk.Window(themename = 'cyborg')
window.title('Fortify Downloader')
window.geometry('300x200')


frame = ttk.Frame()

SancCodeStr = tk.StringVar()
NameStr = tk.StringVar()

#Creating the widgets

title_label = tk.Label(frame, text="Sanctuary downloader", font=(16))
code_label = tk.Label(frame, text="Sanc code")
code_entry = tk.Entry(frame, textvariable = SancCodeStr)
name_label = tk.Label(frame, text="File name")
name_entry = tk.Entry(frame, textvariable = NameStr)
submit_button = tk.Button(frame, text="Download", command = SancDownload)


#Creating the grid

title_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
code_label.grid(row=1, column=0)
code_entry.grid(row=1, column=1)
name_label.grid(row=2, column=0, pady=10)
name_entry.grid(row=2, column=1, pady=10)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)


frame.pack()


window.mainloop()