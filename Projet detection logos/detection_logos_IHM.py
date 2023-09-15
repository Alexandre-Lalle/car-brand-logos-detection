"""
pip install imutils
pip install mysql.connector

create database car_brand_logos;

update database info in reconnaitre_logo() function

"""

import math
from tkinter import filedialog
import cv2
import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import joblib
from skimage.feature import hog
from detection_logo import main_detection

svm_is_logo = joblib.load("./models/model_is_Logo.joblib")
svm_logo = joblib.load("./models/model_reconnaitre_logo.joblib")    

# <---------------------------- Reconnaissance ---------------------------->

def open_img1():
    global img
    imgname = filedialog.askopenfilename(title="Change Image")
    if imgname:
        img = cv2.imread(imgname)
        
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        height, width = img.shape[:2]
        aspect_ratio = width / height
        max_width = 500
        max_height = 500
        if aspect_ratio > max_width / max_height:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_height = max_height
            new_width = int(max_height * aspect_ratio)
        img = cv2.resize(img, (new_width, new_height))
        
        photo = ImageTk.PhotoImage(Image.fromarray(img))
        image_label.configure(image=photo)
        image_label.image = photo
        

def reconnaitre_logo():
    global img
    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="car_brand_logos"
    )
    cursor = db.cursor()

    gray_test_1 = cv2.resize(img, (200, 200))
    gray_test_1 = cv2.cvtColor(gray_test_1, cv2.COLOR_BGR2GRAY)
    fd_test_1, hog_image = hog(gray_test_1, orientations=9, pixels_per_cell=(8, 8),
                            cells_per_block=(2, 2), visualize=True#, multichannel=False
                            )

    fd_test_1 = fd_test_1.reshape(1,-1)

    y_pred_1 = svm_logo.predict(fd_test_1)

    cursor.execute("SELECT * FROM cars WHERE name='" + str(y_pred_1[0]) + "'")
    rows = cursor.fetchall()
    
    right_frame.name_text.config(text=rows[0][1])
    right_frame.country_text.config(text=rows[0][2])
    right_frame.year_text.config(text=rows[0][3])
    right_frame.company_text.config(text=rows[0][4])
    right_frame.description_text.config(text=rows[0][6],wraplength=350)
    
    logo_img = cv2.imread(rows[0][5])
    logo_img = cv2.cvtColor(logo_img,cv2.COLOR_BGR2RGB)
    print("linkkkk :",rows[0][5])
    logo_img = cv2.resize(logo_img, (250, 250))
    photo = ImageTk.PhotoImage(Image.fromarray(logo_img))
    right_frame.logo = photo
    right_frame.logo_label.config(image=photo)
    
    db.close()
    
    
# <---------------------------- Detection ---------------------------->
        
def open_img2():
    global img2
    global imgdetect
    imgname = filedialog.askopenfilename(title="Change Image")
    if imgname:
        img2 = cv2.imread(imgname)
        imgdetect=img2
        img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
        height, width = img2.shape[:2]
        aspect_ratio = width / height
        max_width = math.floor(screen_width*0.45)
        max_height = math.floor(screen_height*0.8)
        if aspect_ratio > max_width / max_height:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_height = max_height
            new_width = int(max_height * aspect_ratio)
        img2 = cv2.resize(img2, (new_width, new_height))
        # img2 = cv2.resize(img2, (300, 300))
        photo = ImageTk.PhotoImage(Image.fromarray(img2))
        image_label2.configure(image=photo)
        image_label2.image = photo


def detecter_logo():
    global img2    
    global imgdetect
    res = main_detection(imgdetect)
    height, width = img2.shape[:2]
    logo_img2 = cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
    logo_img2 = cv2.resize(logo_img2, (width, height))

    photo_image = ImageTk.PhotoImage(Image.fromarray(logo_img2))
    right_frame2.logo = photo_image
    right_frame2.logo_label.config(image=photo_image)
    print(photo_image)

    
# Create the GUI
root = Tk()
space = (" ") * 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title(f"{space}Projet : detection des logo")
root.configure(bg='grey')
root.geometry(f"{math.floor(screen_width)}x{math.floor(screen_height*0.6)}")

# Create the notebook widget
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')



# <---------------------------- Reconnaissance ---------------------------->

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Reconnaissance')

tab1_frame = Frame(tab1)
tab1_frame.pack(side="top", fill="both", expand=True)


left_frame = Frame(tab1_frame, width=math.floor(screen_width*0.45), height=math.floor(screen_height*0.5), bg="gray")
left_frame.pack(side="left", fill="y")
midle_frame = Frame(tab1_frame, width=math.floor(screen_width*0.1), height=math.floor(screen_height*0.5), bg="gray")
midle_frame.pack(side="left", fill="y")
right_frame = Frame(tab1_frame, width=math.floor(screen_width*0.45), height=math.floor(screen_height*0.5), bg="gray")
right_frame.pack(side="right", fill="both", expand=True)

#image de reconaissance
img = cv2.imread("./default-image.png")
img = cv2.resize(img, (500, 500))
photo = ImageTk.PhotoImage(Image.fromarray(img))
image_label = Label(root, image=photo, padx=10, pady=10)
image_label.pack(in_=left_frame, padx=10,pady=30)

#button de reconnaissance
button1 = Button(midle_frame, text="ouvrir image ", bg="white",command=open_img1)
button1.pack(in_=midle_frame, pady=30)
button_rec = Button(root, text="reconaisance", bg="white",command=reconnaitre_logo)
button_rec.pack(in_=midle_frame, padx=10,pady=50)


#logo details
logo_img = Image.open("./default-image.png")
logo_img = logo_img.resize((250, 250))
right_frame.logo = ImageTk.PhotoImage(logo_img)
right_frame.logo_label = Label(right_frame, image=right_frame.logo)
right_frame.name_label = Label(right_frame, text="Marque")
right_frame.country_label = Label(right_frame, text="Pays")
right_frame.year_label = Label(right_frame, text="Année d'établissement")
right_frame.company_label = Label(right_frame, text="Entreprise")
right_frame.description_label = Label(right_frame, text="Description")
right_frame.name_text = Label(right_frame, text="")
right_frame.country_text = Label(right_frame, text="")
right_frame.year_text = Label(right_frame, text="")
right_frame.company_text = Label(right_frame, text="")
right_frame.description_text = Label(right_frame, text="")
        
right_frame.logo_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
right_frame.name_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
right_frame.country_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
right_frame.year_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)
right_frame.company_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)
right_frame.description_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)
right_frame.name_text.grid(row=4, column=1, sticky="w", padx=10, pady=5)
right_frame.country_text.grid(row=5, column=1, sticky="w", padx=10, pady=5)
right_frame.year_text.grid(row=6, column=1, sticky="w", padx=10, pady=5)
right_frame.company_text.grid(row=7, column=1, sticky="w", padx=10, pady=5)
right_frame.description_text.grid(row=8, column=1, padx=10, pady=5)



# <---------------------------- Detection ---------------------------->

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="detection")

tab2_frame = Frame(tab2)
tab2_frame.pack(side="top", fill="both", expand=True)

left_frame2 = Frame(tab2_frame, width=math.floor(screen_width*0.45), height=math.floor(screen_height*0.5), bg="gray")
left_frame2.pack(side="left", fill="y")
midle_frame2 = Frame(tab2_frame, width=math.floor(screen_width*0.1), height=math.floor(screen_height*0.5), bg="gray")
midle_frame2.pack(side="left", fill="y")
right_frame2 = Frame(tab2_frame, width=math.floor(screen_width*0.45), height=math.floor(screen_height*0.5), bg="gray")
right_frame2.pack(side="right", fill="both", expand=True)

#image de detection
img2 = cv2.imread("./default-image.png")
img2 = cv2.resize(img2, (300, 300))
photo2 = ImageTk.PhotoImage(Image.fromarray(img))
image_label2 = Label(root, image=photo2, padx=10, pady=10)
image_label2.pack(in_=left_frame2, padx=10,pady=30)

#button de detection
button2 = Button(midle_frame2, text="ouvrir image", bg="white",command=open_img2)
button2.pack(in_=midle_frame2, pady=30)
button_det = Button(root, text="detection", bg="white",command=detecter_logo)
button_det.pack(in_=midle_frame2, padx=10,pady=50)
button_save = Button(root, text="sauvgarder", bg="white")
button_save.pack(in_=midle_frame2, padx=10,pady=50)

logo_img2 = Image.open("./default-image.png")
# logo_img2 = logo_img2.resize((300, 270))
right_frame2.logo = ImageTk.PhotoImage(logo_img2)
right_frame2.logo_label = Label(right_frame2, image=right_frame2.logo)
right_frame2.logo_label.grid(row=0, column=0, rowspan=4, padx=30, pady=10)

if __name__ == '__main__':

    root.mainloop()