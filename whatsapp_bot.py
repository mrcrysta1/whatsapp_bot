import pandas as pd
import pywhatkit as kit
import pyautogui
import time

# Read the Excel file
df = pd.read_excel('contacts.xlsx')

# Iterate through the rows in the DataFrame
for index, row in df.iterrows():
    number = row['Number']
    message = row['Message']
    image_path = row['Image']
    
    # Send the WhatsApp message with image
    kit.sendwhats_image(f'+{number}', image_path, caption=message, wait_time=20, tab_close=True, close_time=20)
    
    # Wait for the message to be typed out
    time.sleep(15)
    
    # Press the "Enter" key to send the message
    pyautogui.press('enter')
    
    # Wait for a few seconds before sending the next message
    time.sleep(10)

print("Messages sent successfully!")