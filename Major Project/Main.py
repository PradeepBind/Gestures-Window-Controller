import tkinter as tk
import subprocess
import os
from PIL import Image, ImageTk 


hand_gesture_process = None
face_gesture_process = None

 
def hand_gesture_function():
    global hand_gesture_process
    script_path = "HandGestureWindowControl.py"  
    if os.path.exists(script_path):
        try:
            print("Running hand gesture control script...")
            hand_gesture_process = subprocess.Popen(["python", script_path])
        except Exception as e:
            print(f"Error running hand gesture control script: {e}")
    else:
        print(f"Error: Hand gesture control script '{script_path}' not found.")


def face_gesture_function():
    global face_gesture_process
    script_path = "EyeGestureWindowControl.py"  
    if os.path.exists(script_path):
        try:
            print("Running hand gesture control script...")
            face_gesture_process = subprocess.Popen(["python", script_path])
        except Exception as e:
            print(f"Error running hand gesture control script: {e}")
    else:
        print(f"Error: Hand gesture control script '{script_path}' not found.")


def open_hand_tutorial():
    hand_tutorial_window = tk.Toplevel(root)
    hand_tutorial_window.title("INSTRUCTION")
    hand_tutorial_window.geometry("750x550")

    # Add content to the Toplevel window
    tutorial_label = tk.Label(hand_tutorial_window, text="Hand Gestures", font=("Calibri", 20, "bold"))
    tutorial_label.pack()

    # Create a canvas to contain the images and descriptions
    canvas = tk.Canvas(hand_tutorial_window, width=700, height=200)  # Adjust width and height as needed
    canvas.pack(side='top', fill='both', expand=True)

    # Create a frame inside the canvas to hold the images and descriptions
    frame = tk.Frame(canvas)
    frame.pack(fill='both', expand=True)

    # Add scrollbar
    scrollbar = tk.Scrollbar(hand_tutorial_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Configure canvas to scroll with mousewheel
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    # Add frame to canvas
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # Function to update scroll region
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind update_scroll_region to configure event of frame
    frame.bind("<Configure>", update_scroll_region)

    photos = [
        {"path": "assets/img1.jpg", "description": "Simply move your index finger to hover"},
        {"path": "assets/img2.jpg", "description": "To perform a right-click operation, bring your index and thumb fingers closer together."},
        {"path": "assets/img3.jpg", "description": "To perform a left-click operation, bring your index and middle fingers closer together."},
        {"path": "assets/img4.jpg", "description": "Show your palm to perform scroll operation"},
        {"path": "assets/img5.jpg", "description": "Show your thumb finger to perform left arrow click"},
        {"path": "assets/img6.jpg", "description": "Show your niddle finger to perform right arrow click"},
        {"path": "assets/img7.jpg", "description": "Simply close your palm to  Play Pause Video/Audio"},
        {"path": "assets/img8.png", "description": "Raise your three finger (index , middle , ring) to perform zoom out"},
        {"path": "assets/img9.jpg", "description": "Raise your four finger (index , middle , ring, pinky) to perform zoom in"},
        {"path": "assets/img10.jpg", "description": "Raise your index and pinky for volumn Up"},
        {"path": "assets/img11.jpg", "description": "Raise your thumb and pinky for volumn down"}
    ]

    photo_objects = []  # To hold references to PhotoImage objects

    for photo_data in photos:
        # Load photo
        photo_path = photo_data["path"]
        print("Attempting to load image from:", photo_path)
        photo = Image.open(photo_path)  # Open image file
        photo = photo.resize((200, 200), Image.LANCZOS)  # Resize the image if needed
        photo_image = ImageTk.PhotoImage(photo)  # Convert the image for tkinter
        photo_objects.append(photo_image)  # Keep a reference to the PhotoImage object

        # Create frame to hold image and description
        item_frame = tk.Frame(frame)
        item_frame.pack(fill='x', pady=5)  # Adjust padding as needed

        # Display photo
        photo_label = tk.Label(item_frame, image=photo_image)
        photo_label.image = photo_image  # Keep a reference to the image to prevent garbage collection
        photo_label.pack(side='left')

        # Display description
        description_label = tk.Label(item_frame, text=photo_data["description"])
        description_label.pack(side='left', padx=10)
        description_label.configure(anchor="center")

    hand_tutorial_window.mainloop()  # Start the main event loop for the Toplevel window


def open_eye_tutorial():
    hand_tutorial_window = tk.Toplevel(root)
    hand_tutorial_window.title("INSTRUCTION")
    hand_tutorial_window.geometry("750x550")

    # Add content to the Toplevel window
    tutorial_label = tk.Label(hand_tutorial_window, text="Face Gestures", font=("Calibri", 20, "bold"))
    tutorial_label.pack()

    # Create a canvas to contain the images and descriptions
    canvas = tk.Canvas(hand_tutorial_window, width=700, height=200)  # Adjust width and height as needed
    canvas.pack(side='top', fill='both', expand=True)

    # Create a frame inside the canvas to hold the images and descriptions
    frame = tk.Frame(canvas)
    frame.pack(fill='both', expand=True)

    # Add scrollbar
    scrollbar = tk.Scrollbar(hand_tutorial_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Configure canvas to scroll with mousewheel
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    # Add frame to canvas
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # Function to update scroll region
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind update_scroll_region to configure event of frame
    frame.bind("<Configure>", update_scroll_region)

    photos = [
        {"path": "assets/fimg1.jpg", "description": "Simply Move your head to hover"},
        {"path": "assets/fimg2.jpg", "description": "To perform left-click operation blink the left eye"},
        {"path": "assets/fimg3.jpg", "description": "To perform right-click operation blink the right eye"}
        
    ]

    photo_objects = []  # To hold references to PhotoImage objects

    for photo_data in photos:
        # Load photo
        photo_path = photo_data["path"]
        print("Attempting to load image from:", photo_path)
        photo = Image.open(photo_path)  # Open image file
        photo = photo.resize((200, 200), Image.LANCZOS)  # Resize the image if needed
        photo_image = ImageTk.PhotoImage(photo)  # Convert the image for tkinter
        photo_objects.append(photo_image)  # Keep a reference to the PhotoImage object

        # Create frame to hold image and description
        item_frame = tk.Frame(frame)
        item_frame.pack(fill='x', pady=5)  # Adjust padding as needed

        # Display photo
        photo_label = tk.Label(item_frame, image=photo_image)
        photo_label.image = photo_image  # Keep a reference to the image to prevent garbage collection
        photo_label.pack(side='left')

        # Display description
        description_label = tk.Label(item_frame, text=photo_data["description"])
        description_label.pack(side='left', padx=10)
        description_label.configure(anchor="center")

    hand_tutorial_window.mainloop()  # Start the main event loop for the Toplevel window


def terminate_program():
        global hand_gesture_process, face_gesture_process
        if hand_gesture_process is not None:
            hand_gesture_process.terminate()
        if face_gesture_process is not None:
            face_gesture_process.terminate()
        root.destroy()




def main():
    global root, hand_gesture_process, face_gesture_process
    root = tk.Tk()
    root.title("Gesture Based Window Controller")
    root.geometry("750x650")
    root.configure(bg="lightblue")      

    # Function to run when Hand Gesture Control button is clicked
    def on_hand_gesture_click():
        hand_gesture_function()

    # Function to run when Face Gesture Control button is clicked
    def on_face_gesture_click():
        face_gesture_function()

    heading_label = tk.Label(root, text="Gesture Window Controller", font=("Arial", 30, "bold"),bg="yellow")
    heading_label.pack(pady=10)


    button_frame = tk.Frame(root)
    button_frame.pack()

    # Create buttons
    hand_gesture_button = tk.Button(button_frame, text="HAND GESTURE WINDOW CONTROLLER", command=on_hand_gesture_click, padx=10, pady=15, bg="lightgreen", font=("Arial", 10, "bold"))
    hand_gesture_button.pack(side=tk.LEFT)   

    spacer1 = tk.Label(button_frame, text="", padx=10, bg="lightblue")
    spacer1.pack(side=tk.LEFT)  # Add space between buttons

    face_gesture_button = tk.Button(button_frame, text="FACE GESTURE WINDOW CONTROLLER", command=on_face_gesture_click, padx=10, pady=15, bg="lightgreen",  font=("Arial", 10, "bold"))
    face_gesture_button.pack(side=tk.RIGHT)

    spacer2 = tk.Label(root, text="", pady=10, bg="lightblue")
    spacer2.pack()


    

    hand_tutorial_button = tk.Button(root, text="HAND GESTURE'S INSTRUCTIONS", command=open_hand_tutorial,padx=10, pady=15, bg="lightgreen",  font=("Arial", 10, "bold"))
    hand_tutorial_button.pack()
    

    spacer3 = tk.Label(root, text="", pady=10, bg="lightblue")
    spacer3.pack()

    
    eye_tutorial_button = tk.Button(root, text="EYE GESTURE'S INSTRUCTIONS", command=open_eye_tutorial,padx=10, pady=15, bg="lightgreen",  font=("Arial", 10, "bold"))
    eye_tutorial_button.pack()

    
    spacer4 = tk.Label(root, text="", pady=10, bg="lightblue")
    spacer4.pack()
    
    note='''
NOTE:-
Please read the gesture instructions carefully before launching the program, 
by clicking on the provided buttons for both hand and face-based controllers.

'''

    note_label = tk.Label(root, text=note, bg="lightblue",  font=("Calibri", 16, "normal") ,justify="left")
    note_label.pack(side=tk.BOTTOM, anchor=tk.W, pady=10)

    spacer5 = tk.Label(root, text="", pady=10, bg="lightblue")
    spacer5.pack()


    terminate_button = tk.Button(root, text="Terminate Program", command=terminate_program, padx=10, pady=15, bg="red",  font=("Arial", 10, "bold"))
    terminate_button.pack()

    root.protocol("WM_DELETE_WINDOW", terminate_program) 

    root.mainloop()

  

if __name__ == "__main__":
    main()
