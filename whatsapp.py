# import pywhatkit
# pywhatkit.sendwhatmsg("phone_no","hi dear...",21,27)
import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file into environment
phone_no = os.getenv("phone_no") #create a .env file and add variables phone_no="+91phonenumber" or group_id=" "
keyboard = Controller()
name="POOARAZ"
# Define a dictionary for each letter's pattern
patterns = {
    'P': ["*****", "*   *", "*****", "*    ", "*    "],
    'O': ["*****", "*   *", "*   *", "*   *", "*****"],
    'A': ["  *  ", " * * ", "*   *", "*****", "*   *"],
    'R': ["**** ", "*   *", "**** ", "*   *", "*    "],
    'Z': ["*****", "   * ", "  *  ", " *   ", "*****"]
}
def generate_pattern(n):
    pattern_str = ""

    for i in range(n):
        for j in range(n + 1):
            if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == 8):
                # appending stars to the pattern
                pattern_str += "* "
            else:
                pattern_str += "  "
        pattern_str += "\n"
    
    return pattern_str

# Set the value of n
n = 6

# Generate the pattern and store it in a variable
pattern_output = generate_pattern(n)

plain_text_pattern=" "
for row in range(5):
    for letter in name:
        plain_text_pattern += patterns[letter][row]+" "
    plain_text_pattern += '\n'
plain_text_pattern+="this msg from pooaraz..."
def send_whatsapp_message(msg: str):
    try:
        # pywhatkit.sendwhatmsg_to_group_instantly(
        #     group_id=group_id, 
        #     message=plain_text_pattern,
        #     tab_close=True
        # )
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_no, 
            message=pattern_output,
            tab_close=True
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    send_whatsapp_message(msg="Test message from a Python script!")
    print(plain_text_pattern)
    print(pattern_output)



