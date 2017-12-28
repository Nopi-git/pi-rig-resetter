from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

@app.route("/reset")
def reset():
  GPIO.output(16, True)
  time.sleep(2)
  GPIO.output(16, False)
  return "reset" 
  
  
@app.route("/power")
def power():
  GPIO.output(18, True)
  time.sleep(1)
  GPIO.output(18, False)
  return "power"
  
  
if __name__ == "__main__":
  app.run(port=5000, host="0.0.0.0", debug=True)
