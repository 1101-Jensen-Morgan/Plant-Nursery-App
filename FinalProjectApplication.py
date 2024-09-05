#=========================
#Morgan Jensen
#CS 457
#=========================


import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
import FinalProjectDatabase as fpd

#=======================================
#WINDOW SETUP
#=======================================

def make_fullscreen(window):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window size to be the same as the screen size
    window.geometry(f"{screen_width}x{screen_height}")

def Set_Frame_Size(frame,root):

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)  # Set weight for column 1 to expand
    root.grid_columnconfigure(2, weight=1)
    frame.grid(row=0, column=1, sticky="nsew")
    return frame
    
def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()

#=======================================
#Helper functions
#=======================================

#this function ensures that password matches the username
#it is called when the submit button on the log in page is clicked
def varifyingResults(root, frame, userName, passw):

    #ver is a bool variable that is determined by weather or not the password from the user name in the database 
    #matches the password that was entered in the aplication
    check = verifyUserCred(userName, passw)
    if check == True:
        #if true then password matches and user is logged in
        userID = fpd.getUserID(userName)
        Load_Frame_Home(root, frame, userID)
    else:
        #if false then it doesnt match and the user has to try again
        failed_label = tk.Label(frame, text="Either the user name or password is incorrect.\nPlease try again.", 
                                fg='red', font=("Georgia", 12))
        failed_label.pack(pady=10)

#This function checks that the username that the user has chosen doesn't already exist
#It is activated upon clicking the submit button in the new user window
def log_entry(root, frame, new_user_window, uName, passw, fName, lName):

    #ver represents the boolean given from the verifyuniqueUser function.
    #This function verifies that the username doesnt already exist within the database.
    check = verifyUniqeUser(uName)
    if check == True:
        #if ver it true then it means that the user name chosen by the user is unique
        fpd.new_user(uName, passw, fName, lName)
        userID = fpd.getUserID(uName)
        Load_Frame_Home(root, frame, userID)
        new_user_window.destroy()
    else:
        #if false, then the user must change their chosen user name to something that does not already exist.
        failedLabel = tk.Label(new_user_window, text="This user name already exists.\nPlease choose another user name.", fg='red', font=("Georgia", 12))
        failedLabel.pack(pady=10)

def verifyUniqeUser(userN):
    #This function will verify that there are no other users with the same username

    #nList is a list of all the usernames from the database which is retieved by the 
    #getUserNames function
    nList = fpd.getUserNames()
    
    #This then checks every name on the list to ensure that is not the same as the chosen username
    for name in nList:
        if name[0] == userN:
            ver = False
        else:
            ver = True
    return ver

def verifyUserCred(user, password):
    #This function will take the username and ensure that the password matches
    passw = fpd.getPassword(user)
    if passw == password:
        good = True
    else:
        good = False
    return good

#this function add a new plant to the user within the database,
#destroys the pop up window, and refreshes the plants that you can choose from
#on the "view your plants" window
def addNewPlant(user_plants_frame, new_Plant_window, newPlant, userID):
    fpd.new_plant(userID, newPlant)
    new_Plant_window.destroy()
    clear_widgets(user_plants_frame)
    load_user_plants_widgets(user_plants_frame, userID)

#This function removes a plant from a user and refreshes the page. 
#This does not remove the watering record for that plant because I believe it is good to keep those records
def remove_plant(remove_Plant_window, user_plants_frame, plant, userID):
    fpd.remove_plant(userID, plant)
    remove_Plant_window.destroy()
    clear_widgets(user_plants_frame)
    load_user_plants_widgets(user_plants_frame, userID)

#this function contains all the widgts within the "view you plants" page.
#It is in a seperate function so that the view can be refreshed if a new plant is added
def load_user_plants_widgets(user_plants_frame, user_ID):
    user_plants_label = tk.Label(user_plants_frame, text="Here are the plants that you own.", font=("Georgia", 25, "bold"))
    user_plants_label.pack(pady=20)

    v=tk.IntVar()
    def seePlantInfo():
            plant_info = fpd.getPlantInfo(v.get())
            if plant_info[10] == True:
                petSafe = "No"
            else:
                petSafe = "Yes"
            # Display the animals in the text widget
            display_text.delete(1.0, tk.END)
            display_text.insert(tk.END, f"Common Name: {plant_info[1]}\n\nLatin Name: {plant_info[2]}\n\nDescription: {plant_info[3]}\n\nSunlight: {plant_info[5]}\n\nSoil: {plant_info[6]}\n\nWatering: {plant_info[7]}\n\ntemperature (in fehrenheit): {plant_info[8]}\n\nHumidity: {plant_info[9]}\n\nPet Friendly: {petSafe}\n\n")
    
    plant_ids = fpd.getUserPlants(user_ID)
    plant_names = fpd.getPlantNames(plant_ids)
    
    plants = list(zip(plant_ids, plant_names))
    for num, plant in plants:
        tk.Radiobutton(user_plants_frame, text=plant, font=('Georgia', 12), bg="#8dba66", indicatoron=0, width = 20, padx = 20, 
                       variable=v, command=seePlantInfo, value=num).pack()        
        
    display_text = tk.Text(user_plants_frame, height=20, width=45)
    display_text.pack(pady=10)

    # Button to update animals based on selected toggles
    add_new_button = tk.Button(user_plants_frame, text="Add new plant", command=lambda: Open_New_Plant_Window(user_plants_frame, user_ID), font=("Georgia", 12), fg="white", bg="#8dba66")
    add_new_button.pack(pady=15)

    remove_btn = tk.Button(user_plants_frame, text="Remove plant :'(", command=lambda: remove_Plant_window(user_plants_frame, user_ID), font=("Georgia", 12), fg="white", bg="#8dba66")
    remove_btn.pack(pady=10)

#similar to the frame above, this function hols all the widgets for the watering page. It makes it so that it can be refreshed with every new entry
def loadWaterings(Watering_Frame, user_ID):
    Watering_label = tk.Label(Watering_Frame, text="Your watering history.", font=('Georgia', 25, 'bold'))
    Watering_label.pack(pady=20)

    new_wat_btn = tk.Button(Watering_Frame, text='New watering Record', command=lambda: Open_New_watering_Window(Watering_Frame, user_ID), font=("Georgia", 12), fg="white", bg="#8dba66")
    new_wat_btn.pack(pady=20)

    wat_record = tk.Listbox(Watering_Frame, width=80)

    water_record = fpd.getWatLog(user_ID)
    wat_record.pack(pady=10, expand=True)

    for index, record in enumerate(water_record):
        if record[3] == False:
            plant = fpd.get1PlantName(record[6])
            wat_record.insert(index, f"Date: {record[1]},   Amount: {record[2]} oz,   Fertilizer: No,   Plant: {plant}")
        else:
            plant = fpd.get1PlantName(record[6])
            wat_record.insert(index, f"Date: {record[1]},   Amount: {record[2]} oz,   Fertilizer: Yes,   Amount: {record[4]} oz,   Plant: {plant}")
        if index %2 == 0:
            wat_record.itemconfig(index, {'bg':'#a4b893'})
        wat_record.config(font=('Georgia', 12))

# This function takes information from the user and inserts it as a new record in the database
def addNewWat(new_Wat_window, Watering_Frame, dateW, aW, fert, aF, userID, plantID):
    fpd.new_wat_log(dateW, aW, fert, aF, userID, plantID)
    clear_widgets(Watering_Frame)
    loadWaterings(Watering_Frame, userID)
    new_Wat_window.destroy()

#=======================================
#New windows/frames
#=======================================

#Pop up windows for new entries
#------------------------------------------------------------------
def open_new_user_window():

    new_user_window = tk.Toplevel(root)
    new_user_window.title("New User")
    
    # Labels and entry for new username
    userLabel = tk.Label(new_user_window, text="New username:", font=("Georgia", 15))
    userLabel.pack()
    
    uName = tk.Entry(new_user_window, font=("Georgia", 15))
    uName.pack()
    
    # Labels and entry for new password
    passLabel = tk.Label(new_user_window, text="New password:", font=("Georgia", 15))
    passLabel.pack()
    
    passw = tk.Entry(new_user_window, show="*", font=("Georgia", 15))
    passw.pack()
    
    # Labels and entry for new FirstName
    fNameLabel = tk.Label(new_user_window, text="FirstName:", font=("Georgia", 15))
    fNameLabel.pack()
    
    fName = tk.Entry(new_user_window, font=("Georgia", 15))
    fName.pack()
    
    # Labels and entry for new LastName
    lNameLabel = tk.Label(new_user_window, text="LastName:", font=("Georgia", 15))
    lNameLabel.pack()
    
    lName = tk.Entry(new_user_window, font=("Georgia", 15))
    lName.pack()
    
    confirm_button = tk.Button(new_user_window, text="Confirm", 
                               command=lambda: log_entry(root, frame, new_user_window, uName.get(), passw.get(), fName.get(), lName.get()),
                            font=("Georgia", 10), fg="white", bg="#8dba66")
    confirm_button.pack(pady=20)

def Open_New_Plant_Window(user_plants_frame, userID):
    new_Plant_window = tk.Toplevel(root)
    new_Plant_window.title("New Plant")

    label = tk.Label(new_Plant_window, text = "Please Select Your New Plant:", font=('Georgia', 10))
    label.pack(pady=10)
    
    v=tk.IntVar()
    
    #this gets the list of all the plant names from the databse for the user to choose from
    plants = fpd.getAllPlants()
    n = tk.StringVar() 

    #this is the creation and instantiation of the dropdown box that the user can select from
    plantChosen = ttk.Combobox(new_Plant_window, width = 27, textvariable = n)
    plantChosen['values'] = plants

    plantChosen.pack() 
    plantChosen.current() 

    #this is the confirm button which takes the user back to the main application
    confirm_btn = tk.Button(new_Plant_window, text='  Confirm  ', command=lambda: addNewPlant(user_plants_frame, new_Plant_window, plantChosen.get(), userID), font=("Georgia", 10), fg="white", bg="#8dba66")
    confirm_btn.pack(pady=10)

def Open_New_watering_Window(Watering_Frame, userID):
    new_Wat_window = tk.Toplevel(root)
    new_Wat_window.title("New Watering Record")

    label = tk.Label(new_Wat_window, text = "We need some more information:", font=('Georgia', 15, 'bold'))
    label.pack(pady=15)
    
    confirm_btn = tk.Button(new_Wat_window, text='  Confirm  ', 
                            command=lambda: addNewWat(new_Wat_window, Watering_Frame, dateW=cal.get(), aW=amountW_entry.get(), 
                                                      fert=toggle_var.get(), aF=amountF_entry.get(), userID=userID, plantID=getSelection()), 
                            font=("Georgia", 10), fg="white", bg="#8dba66")

    #the label and radio buttons for the user's plants
    plant_label = tk.Label(new_Wat_window, text='Which plant did you water?', font=('Georgia', 12))
    plant_label.pack(pady=10)

    v=tk.IntVar()

    def getSelection():
        plantID = v.get()
        return plantID
    
    plant_ids = fpd.getUserPlants(userID)
    plant_names = fpd.getPlantNames(plant_ids)
    
    plants = list(zip(plant_ids, plant_names))
    for num, plant in plants:
        tk.Radiobutton(new_Wat_window, text=plant, font=('Georgia', 10), width = 20, padx = 20, 
                       variable=v, command=getSelection, value=num).pack()


    #the calender to choose a date from
    dateLabel = tk.Label(new_Wat_window, text="When did you last water your plant?", font=('Georgia', 12))
    dateLabel.pack(pady=10)
    cal = DateEntry(new_Wat_window)
    cal.pack()

    #the label and entry for the amount of water used
    amountW_label = tk.Label(new_Wat_window, text='How much water did you use? (in oz)', font=('Georgia', 12))
    amountW_label.pack(pady=10)
    amountW_entry = tk.Entry(new_Wat_window)
    amountW_entry.pack()

    #the check button and entry for fertilizer
    toggle_var = tk.IntVar()
    amountF_label = tk.Label(new_Wat_window, text="How much did you use? (in oz)", font=('Goergia', 12))
    amountF_entry = tk.Entry(new_Wat_window)
    
    #toggle id handler
    def toggled():
        toggle = toggle_var.get()
        if toggle:
            confirm_btn.forget()
            amountF_label.pack()
            amountF_entry.pack()
            confirm_btn.pack(pady=10)
        else:
            amountF_label.pack_forget()
            amountF_entry.pack_forget()
    
    toggle_button = tk.Checkbutton(new_Wat_window, text="Did you use fertalizer?", font=('Goergia', 12), variable=toggle_var, command=toggled)
    toggle_button.pack()

    #this is the confirm button which takes the user back to the main application
    confirm_btn.pack(pady=10)

def remove_Plant_window(user_plants_frame, userID):
    remove_plant_window = tk.Toplevel(root)
    remove_plant_window.title("New Watering Record")

    v=tk.IntVar()

    plant_ids = fpd.getUserPlants(userID)
    plant_names = fpd.getPlantNames(plant_ids)
    
    plants = list(zip(plant_ids, plant_names))
    for num, plant in plants:
        tk.Radiobutton(remove_plant_window, text=plant, font=('Georgia', 10), width = 20, padx = 20, indicatoron=0, 
                       variable=v, command=lambda: remove_plant(remove_plant_window, user_plants_frame, v.get(), userID), value=num).pack()

#Tabs shown on the main application
#------------------------------------------------------------------
def Create_Watering_Records_Tab(root,user_ID):
    Watering_Frame = tk.Frame(root)
    
    loadWaterings(Watering_Frame, user_ID)
    
    return Watering_Frame
    
def Create_Search_Plants_Tab(root):
    Search_frame = tk.Frame(root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    Search_label = tk.Label(Search_frame, text="What plant would you like to see?", font=('Georgia', 25, 'bold'))
    Search_label .place(x=screen_width/3.5, y=screen_height/22)

    instructions_label = tk.Label(Search_frame, text='Select a plant from the drop down menu, then click on the care attribute that you would like to see.',
                                  font=('Georgia', 12))
    instructions_label.place(x=screen_width/4, y=screen_height/10)

    search = tk.Frame(Search_frame)
    search.place(x=screen_width/4.5, y=screen_height/6)

    info_frame = tk.Frame(Search_frame)
    info_frame.place(x=screen_width/6, y=screen_height/3)

    picture_frame = tk.Frame(Search_frame)
    picture_frame.place(x=screen_width/2, y=screen_height/5)

    def load(pID):
        if pID == 'none':
            image = Image.open("pictures/cartoonPlant.png")
            newImage = image.resize((400, 400))
            img = ImageTk.PhotoImage(newImage)
            
            image_label = tk.Label(picture_frame, image=img)
            image_label.image = img
            image_label.pack(pady=20) 
        else:   
            image = Image.open(f"pictures/{pID}.png")
            newImage = image.resize((400, 400))
            img = ImageTk.PhotoImage(newImage)
            
            image_label = tk.Label(picture_frame, image=img)
            image_label.image = img
            image_label.pack(pady=20)

        def getInfo():
            pID = fpd.getPlantID(plant.get())
            info = fpd.getPlantInfo(pID)
            op = option.get()

            display_text.delete(1.0, tk.END)
            if op == 10:
                if info[10] == True:
                    petSafe = "No"
                else:
                    petSafe = "Yes"
                display_text.insert(tk.END, f"{petSafe}")
            elif op == 8:
                display_text.insert(tk.END, f"{info[op]} degrees farhenheit")
            else:
                display_text.insert(tk.END, f"{info[op]}")

        option=tk.IntVar()
        #radio button to see the care for the chosen plant
        light = tk.Radiobutton(info_frame, text='Light', font=('Georgia', 12), bg="#8dba66", indicatoron=0, width = 20, padx = 20,
                            variable=option, command=getInfo, value=5)
        light.pack()

        water = tk.Radiobutton(info_frame, text='Water', font=('Georgia', 12), bg="#8dba66", indicatoron=0, width = 20, padx = 20,
                            variable=option, command=getInfo, value=7)
        water.pack()

        soil = tk.Radiobutton(info_frame, text='Soil', font=('Georgia', 12), bg="#8dba66", indicatoron=0, width = 20, padx = 20,
                            variable=option, command=getInfo, value=6)
        soil.pack()

        temp = tk.Radiobutton(info_frame, text='Temperature', font=('Georgia', 12), bg="#8dba66", indicatoron=0, width = 20, padx = 20,
                            variable=option, command=getInfo, value=8)
        temp.pack()

        hum = tk.Radiobutton(info_frame, text='Humidity', font=('Georgia', 12), bg="#8dba66", indicatoron=0, width = 20, padx = 20,
                            variable=option, command=getInfo, value=9)
        hum.pack()

        ps = tk.Radiobutton(info_frame, text='Pet Safe?', font=('Georgia', 12), bg="#8dba66", indicatoron=0, width = 20, padx = 20,
                            variable=option, command=getInfo, value=10)
        ps.pack()
            
        display_text = tk.Text(info_frame, height=5, width=45)
        display_text.pack(pady=20)

    def showPlant():
        pID = fpd.getPlantID(plant.get())
        clear_widgets(picture_frame)
        clear_widgets(info_frame)
        load(pID)
 
    #commbox for the plant lst
    plants = fpd.getAllPlants()
    plant = tk.StringVar() 

    #this is the creation and instantiation of the dropdown box that the user can select from
    plantChosen = ttk.Combobox(search, width = 27, textvariable = plant)
    plantChosen['values'] = plants

    plantChosen.pack(pady=20) 
    plantChosen.current() 

    search_btn = tk.Button(search, text='Search', font=('Georgia', 12), bg="#8dba66", fg='white',
                           command=showPlant)
    search_btn.pack(pady=10)

    load('none')

    return Search_frame
    
def Create_Users_Plants_Tab(root,user_ID):
    user_plants_frame = tk.Frame(root)

    load_user_plants_widgets(user_plants_frame, user_ID)
    
    return user_plants_frame
      
def Create_Home_Tab(root, notebook,user_ID):
    Home_Frame = tk.Frame(notebook)
    
    userName = fpd.getSpecFName(user_ID)[0]

    Home_label = tk.Label(Home_Frame, text="Welcome {}, to your Home Plant Nursery!".format(userName), font=("Georgia", 25, "bold"))
    Home_label.pack(pady=20)

    intro_label = tk.Label(Home_Frame, text="This app is designed to help you with all your plant care. You can view the plants that you own, add new ones, and record when you last watered or used fertalizer.\n Are you looking to buy a new plant? In the search tab, you can look to see what care is required for a plant before you buy it!\nHave fun!", font=("Goergia", 16))
    intro_label.pack(pady=15)

    image = Image.open('pictures/otherHomePage.png')
    image = ImageTk.PhotoImage(image)

    image_label = tk.Label(Home_Frame, image=image)
    image_label.image = image
    image_label.pack(pady=10)

    #log out button
    log_out = tk.Button(Home_Frame, text='Log Out',command=lambda: Load_Frame_login(root), fg="white", bg="#8dba66", font=("Georgia", 12))
    log_out.pack()

    return Home_Frame


#two main pages
#------------------------------------------------------------------
def Load_Frame_Home(root,frame,user_ID):
    clear_widgets(frame)
    frame2 = tk.Frame(root)
    Set_Frame_Size(frame2,root)

    Frames = []
    def create_tabs():
        tab_names = ["\t\tHome\t","\tView Your Plants\t", "\tSearch plants\t", "\tWatering records\t\t\t"]
        Frames.append(Create_Home_Tab(root, notebook,user_ID))
        Frames.append(Create_Users_Plants_Tab(notebook,user_ID))
        Frames.append(Create_Search_Plants_Tab(notebook))
        Frames.append(Create_Watering_Records_Tab(notebook,user_ID))

        for i, tab_name in enumerate(tab_names):
            notebook.add(Frames[i], text=tab_name)
            
        # Set the width of all tabs to make them larger
        style = ttk.Style()
        style.configure('TNotebook.Tab',font=("Georgia", 15, "bold"), bg="#8dba66", fg="Black")  # Adjust the width as needed
        style.theme_create('customstyle', parent='alt', settings={
        "TNotebook": {"configure": {"background": "#8dba66"}},
        "TNotebook.Tab": {"configure": {"background": "#8dba66", "font": ("Georgia", 15, "bold")}}
        })
        style.theme_use('customstyle')

    notebook = ttk.Notebook(frame2, style="TNotebook")
    notebook.pack(fill='x', expand=False)

    create_tabs()
    
def Load_Frame_login(root): 
    frame = tk.Frame(root)
    Set_Frame_Size(frame,root)
    
    #login page header label
    welcome_label = tk.Label(frame, text="Welcome to the House Plant Nursery!\nPlease Log In or Sign Up.\n", 
                             fg="black", font=("Georgia", 25, "bold"))
    welcome_label.pack(pady=(10, 0),anchor="center")
    
    
    # Frames for login
    user_frame = tk.Frame(frame)
    user_frame.pack(pady=(0, 5),anchor="center")

    pass_frame = tk.Frame(frame)
    pass_frame.pack(pady=(0, 5),anchor="center")

    button_frame = tk.Frame(frame)
    button_frame.pack(pady=(0, 0),anchor="center")

    # Username label and entry
    uNameLabel = tk.Label(user_frame, text="Username:", fg="#4F6272",font=("Georgia", 15))
    uNameLabel.grid(row=0, column=0)

    userName = tk.Entry(user_frame,font=("Georgia", 15))
    userName.grid(row=0, column=1)

    # Password labeland entry
    passLabel = tk.Label(pass_frame, text=" Password:", fg="#4F6272",font=("Georgia", 15))
    passLabel.grid(row=0, column=0)

    passW = tk.Entry(pass_frame, show="*",font=("Georgia", 15))  # Mask the password input
    passW.grid(row=0, column=1)

    
    login_button = tk.Button(frame, text="    Log In    ", command=lambda: varifyingResults(root, frame, userName.get(), passW.get()), 
                             font=("Georgia", 10), fg="white", bg="#8dba66")
    login_button.pack(pady=(0, 0),anchor="center")

    New_user_button = tk.Button(frame, text="New user?",fg="white", bg="#8dba66", command=open_new_user_window, font=("Georgia", 12))
    New_user_button.pack(pady=(5, 0),anchor="center")

    image = Image.open('pictures/homepage.png')
    newImage = image.resize((750, 400))
    img = ImageTk.PhotoImage(newImage)
    

    image_label = tk.Label(frame, image=img)
    image_label.image = img
    image_label.pack(pady=20)


#Where the window and and application starts
#------------------------------------------------------------------
# Make root for tkinter
root = tk.Tk()

# Make the window fullscreen
make_fullscreen(root)

#title of the main page
root.title("Houese Plant App")
frame = tk.Frame(root)

#load log in page
Load_Frame_login(root)

# Run the Tkinter event loop
root.mainloop()



