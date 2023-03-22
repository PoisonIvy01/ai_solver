import openai
from PIL import Image
import pytesseract
import cv2

img_cv = cv2.imread(r'document.png')

#i have no idea what im doing wheeeeeeeeee
#pytesseract.pytesseract.tesseract_cmd = r'full path to executable'

def askGPT(text):
    openai.api_key = "oopsie daisy"
    response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = text,
            temperature = 0.6,
            max_tokens = 30,
    )
    return print(response.choices[0].text)

def main():
    myQuestion = input("GPT: Ask me a question with good grammar!\n")
    askGPT(myQuestion + "Answer in a single sentence.")
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img_rgb))
    print("finished")

main()
