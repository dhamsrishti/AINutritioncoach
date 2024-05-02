import google.generativeai as genai
import os
from tkinter import *
import tkinter as tk

# Configure Gemini Pro API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

#defining root and size
root=tk.Tk()
root.geometry("1500x800")
root.title("AI Nutrition coach")

# declaring string variable
height_var=tk.StringVar()
weight_var=tk.StringVar()
age_var=tk.StringVar()
gender_var=tk.StringVar()
activity_var=tk.StringVar()
goal_var=tk.StringVar()
diet_var=tk.StringVar()
Output=tk.StringVar()

def clearAll() :
 
    # deleting the content from the entry box
    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    age_entry.delete(0, END)
    Output.delete('1.0',END)


# defining a function that will generate the AI response from Gemini AI using input values.
def submit():
 
    height=height_var.get()
    weight=weight_var.get()
    age=age_var.get()
    gender=gender_var.get()
    activity=activity_var.get()
    diet=diet_var.get()
    goal=goal_var.get()
     
    #Generate response from Gemini AI
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content("Nutrition Plan for a person with height " + height+"and weight "+ weight +" , Age "+ age + ", Gender "+ gender +", Activity level "+ activity +" , Goals " + goal + " and Diet restriction " + diet)
    Output.insert(END,str(response.text))
     
     
# creating a label for height using widget Label
height_label = tk.Label(root, text = 'Height (in Feet)', font=('calibre',10, 'bold'))
  
# creating a entry for input height using widget Entry
height_entry = tk.Entry(root, textvariable = height_var, font=('calibre',10,'normal'))
  
# creating a label for weight using widget Label
weight_label = tk.Label(root, text = 'Weight (in Pound)', font = ('calibre',10,'bold'))
  
# creating a entry for input weight using widget Entry
weight_entry=tk.Entry(root, textvariable = weight_var, font = ('calibre',10,'normal'))

# creating a label for age using widget Label
age_label = tk.Label(root, text = 'Age (in Years)', font=('calibre',10, 'bold'))
  
# creating a entry for input age using widget Entry
age_entry = tk.Entry(root,textvariable = age_var, font=('calibre',10,'normal'))

#gender options
gender_var.set("Female")
genderoptions = ["Female", "Male"]

# creating a label for gender using widget Label
gender_label = tk.Label(root, text = 'Gender', font = ('calibre',10,'bold'))
  
# creating a entry for input gender using widget Entry
gender_entry=tk.OptionMenu(root, gender_var, *genderoptions)

#activity level
activity_var.set("Moderate Activity")
# creating a label for activty using widget Label
activity_label = tk.Label(root, text = 'Activity Level', font = ('calibre',10,'bold'))

options = ["No Activity", "Little Activity", "Moderate Activity", "Intense Activity"]
# creating a entry for input activity using widget Entry
activity_entry=tk.OptionMenu(root, activity_var, *options)

#fitness goals
goaloptions = ["Lose Weight", "Maintain Weight", "Muscle Gain"]

goal_var.set("Maintain Weight")
# creating a label for fitness goal using widget Label
goal_label = tk.Label(root, text = 'Fitness Goals', font = ('calibre',10,'bold'))

# creating a entry for input fitness goal using widget Entry
goal_entry=tk.OptionMenu(root, goal_var, *goaloptions)

#diet options
dietoptions = ["Any", "Vegetarian", "Vegan", "Mediterranean", "Gluten-free", "Keto", "Paleo", "Dairy-Free", "Low Carb"]
diet_var.set("Any")
# creating a label for diet preference using widget Label
diet_label = tk.Label(root, text = 'Diet Preference', font = ('calibre',10,'bold'))

# creating a entry for input diet preference using widget Entry
diet_entry=tk.OptionMenu(root, diet_var, *dietoptions)

# Create a Clear All Button and attached to clearAll function
clearAllEntry = tk.Button(root, text = "Reset", fg = "Black", bg = "Yellow", command = clearAll)
 
# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', fg = "Black", bg = "Light Blue", command = submit)
  
Output = Text(root, height = 30, 
              width = 150, 
              bg = "light cyan")
 
# placing the label and entry in
# the required position using grid
height_label.grid(row=0,column=0)
height_entry.grid(row=0,column=1)
weight_label.grid(row=1,column=0)
weight_entry.grid(row=1,column=1)
age_label.grid(row=2,column=0)
age_entry.grid(row=2,column=1)
gender_label.grid(row=3,column=0)
gender_entry.grid(row=3,column=1)
activity_label.grid(row=4,column=0)
activity_entry.grid(row=4,column=1)
goal_label.grid(row=5,column=0)
goal_entry.grid(row=5,column=1)
diet_label.grid(row=6,column=0)
diet_entry.grid(row=6,column=1)
sub_btn.grid(row=7,column=1)
clearAllEntry.grid(row = 7, column = 0)
Output.grid(row=8,column=1)

mainloop()
