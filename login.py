import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 
  
app = ctk.CTk() 
app.geometry("400x400") 
app.title("Mason's 3rd Party Example") 

def google_api():
    CLIENT_FILE = 'acct1.json'
    SCOPES = ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.profile','https://www.googleapis.com/auth/contacts.readonly']

    creds = None

    if os.path.exists('token.json'):
        credes = Credentials.from_authorized_user_file('token.json', SCOPES)


    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    new_window = ctk.CTkToplevel(app) 
  
    new_window.title("Google Data") 
  
    new_window.geometry("400x400") 
    service = build('people', 'v1', credentials=creds)

    # Retrieve the user's profile
    profile = service.people().get(resourceName='people/me', personFields='names').execute()

    # Print the user's profile information
    name = f"Name:", profile['names'][0]['displayName']
    birthday = r'Birthday: 07/09/1977'
    address = 'Address: 123 Sesame Street, Oakland CA 999922'
    name_label = ctk.CTkLabel(master=new_window,text=name) 
    name_label.pack(pady=12,padx=10)

    birthday_label = ctk.CTkLabel(master=new_window,text=birthday) 
    birthday_label.pack(pady=12,padx=10)

    address_label = ctk.CTkLabel(master=new_window,text=address) 
    address_label.pack(pady=12,padx=10)
    
    
def login(): 
    '''
    username = "Geeks"
    password = "12345"
    new_window = ctk.CTkToplevel(app) 
  
    new_window.title("New Window") 
  
    new_window.geometry("350x150") 
  
    if user_entry.get() == username and user_pass.get() == password: 
        tkmb.showinfo(title="Login Successful",message="You have logged in Successfully") 
        ctk.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack() 
    elif user_entry.get() == username and user_pass.get() != password: 
        tkmb.showwarning(title='Wrong password',message='Please check your password') 
    elif user_entry.get() != username and user_pass.get() == password: 
        tkmb.showwarning(title='Wrong username',message='Please check your username') 
    else: 
        tkmb.showerror(title="Login Failed",message="Invalid Username and password") 
    '''
  
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
  
label = ctk.CTkLabel(master=frame,text='Sign in or create account') 
label.pack(pady=12,padx=10) 
  
  
user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 
  
user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 
  
  
button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 

button = ctk.CTkButton(master=frame,text='Link Account',command=google_api, fg_color="green") 
button.pack(pady=12,padx=10) 
  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 
  
  
app.mainloop()