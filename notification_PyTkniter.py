# Actually this is not a notification but, it's can be visible even if notificaiton is on distrub mode.
# And its was usefull for me hope usefull for you too.
# First install lib with pip, you can search for installing them...
# Oh, before i forgot, it's can be displaying the circle image in notificaiton; Like telegram, i guess...
# Created by me, morztaCFT.


import tkinter as tk
import argparse
from PIL import Image, ImageTk,ImageOps,ImageDraw
import customtkinter

#----------------------------Text Settign Aligment-------------------------------
def detect_language(text):
    
    if 'a' <= text[1] <= 'z':
        return "en"  
    else:
        return "ir" 

def adjust_alignment(widget, lang):
    if lang == 'en':
        widget.config(justify="left")  
    else:
        widget.config(justify="right")  

def show_notification(title, body,duration,image_path,dark_mode,fonts):

    root = tk.Tk()
    root.withdraw()

#------------------------------Screen Section-----------------------------------
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    notification_width = 300
    notification_height = 78
    x_position = screen_width - notification_width - 18
    y_position = screen_height - notification_height - 55

    notification_window = tk.Toplevel(root)
    notification_window.title(title)
    notification_window.geometry(f"{notification_width}x{notification_height}+{x_position}+{y_position}")
    notification_window.overrideredirect(True)

#-------------------------------Image Section-----------------------------------
    img = Image.open(image_path)
    y_wid = notification_height * img.width // img.height
    img = img.resize((y_wid - 10, notification_height - 5), Image.LANCZOS)

   # mask_radius = (notification_height - 20) // 2
    mask = Image.new("L", (notification_height - 20, notification_height - 20), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((1, 1, notification_height - 22, notification_height - 22), fill=255)

    img = ImageOps.fit(img, mask.size, centering=(2, 2))
    img.putalpha(mask)
    img_tk = ImageTk.PhotoImage(img)

    img_label = tk.Label(notification_window, image=img_tk)
    img_label.image = img_tk
    img_label.pack(side="left",anchor="w",padx=3)
#--------------------------------Close X notif--------------------------------------

    close_button = tk.Button(notification_window, text="X",font=("{fonts}",8) ,command=root.quit, bd=0)
    close_button.pack(side="right", anchor="n", padx=10,pady=5)

#--------------------------------Text Section-------------------------------------
    text_frame = tk.Frame(notification_window)
    text_frame.pack(side="right")
    langT = detect_language(title)
    langB = detect_language(body)

    if len(title) > 30:
     title = "..." + title[:28] 

    if len(title) > 30:
     body = body[:80] +  "..."

    title_label = tk.Label(text_frame, text=title, font=("{fonts}", 12, "bold"), wraplength=185)
    title_label.pack(anchor="w")
    adjust_alignment(title_label, langT)

    body_label = tk.Label(text_frame, text=body, wraplength=185)
    body_label.pack(anchor="w")
    adjust_alignment(body_label, langB)
#--------------------------------Dark Mode----------------------------------------
    if dark_mode == True:
        customtkinter.set_appearance_mode("dark")
        notification_window.config(bg="#26242f")
        title_label.config(fg="white")
        body_label.config(fg="white")

    notification_window.after(int(duration * 1000), root.quit)
    root.mainloop()

def main():

  duration = 10 

  parser = argparse.ArgumentParser(description='notification')
  parser.add_argument('--title', type=str, required=True )
  parser.add_argument('--body', type=str, required=True)
  parser.add_argument('--image', type=str, )
  parser.add_argument('--duration', type=int, )
  parser.add_argument('--font', action='store_true')
  args = parser.parse_args()

  show_notification(args.title, args.body, duration,args.image,dark_mode=False,fonts="Arial")
  
if __name__ == "__main__":
  main()

#Example of using it:
# python notifi.py --title "Some_shit_text" --body "Some_other_shit_Text" --image "Your_imagePath"
  
