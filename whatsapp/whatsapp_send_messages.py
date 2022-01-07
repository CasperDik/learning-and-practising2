import pywhatkit
import webbrowser as web
import time
import pyautogui as pg

phone_book = {"papa": "+316..."}

message = "test"
receiver = "papa"

try:
    pywhatkit.sendwhatmsg_instantly(phone_book[receiver], message)
    print("Successfully Sent")

except:
    try:
        # or
        time.sleep(5)
        web.open("https://web.whatsapp.com/send?phone=" + phone_book[receiver] + "&text=" + message)
        time.sleep(10)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        time.sleep(8)
        pg.press('enter')
        time.sleep(8)
        pg.hotkey('ctrl', 'w')
        print("Successfully Sent")

    except:
        print("unexpected error")
