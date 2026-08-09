from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,10)

@app.route("/")
def main():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWp0aTVnbzJ2d2YxMnQ4aWNuMzM5YjBmcW90N2ZtOXgwanRwdmRoMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Cmr1OMJ2FN0B2/giphy.gif'/>")

@app.route("/<int:number>")
def numbers(number):
    if number == random_number:
        return "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3ZjNGhqY2V4dzd4eWx4Zm53NWxrMHlkeW04aDI2aHZlOWY1eXVqZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2YWykMPCmCb9lLWM/giphy.gif' />"
    elif number < random_number:
        return "<img src= 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3RxcmZzZDZnMXk1ZXRjdzgwcXJ2cHM4bnN4YTF6Z3g1YXF2aHZzYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WfJyRpgey7o6HQi4Kk/giphy.gif' />"
    elif number > random_number:
        return "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3dsdGF5YWxtbjdzdXE4bHdwMHRiYmkyZGI0aDB1aWl0b3Yxa2IyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/19gjcpEUzbIRJ5OpcQ/giphy.gif' />"

if __name__ == "__main__":
    app.run(debug=True)



