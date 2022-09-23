import pyautogui as pt
from time import sleep
import pytesseract



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def write(str):
    for letter in str:
        pt.press(letter)


