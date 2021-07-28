import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

#Define pins for controlling motor driver L298N
IN1=2
IN2=3
IN3=4
IN4=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

#Setting all required pins to low so that robot does 
#not run on bootup of raspberry pi
GPIO.output(IN1,False)
GPIO.output(IN3,False)
GPIO.output(IN2,False)
GPIO.output(IN4,False)
Request = None

#HTTP handles requests sent by app
class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request
    messagetosend = bytes('Hello World',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print(Request)
    if Request == 'w':         #FWD: IN1 & IN3 High, IN2 & IN4 Low 
      GPIO.output(IN1,True)
      GPIO.output(IN3,True)
      GPIO.output(IN2,False)
      GPIO.output(IN4,False)
    if Request == 'a':         #LFT: IN2 & IN3 High, IN1 & IN4 Low
      GPIO.output(IN2,True)
      GPIO.output(IN3,True)
      GPIO.output(IN1,False)
      GPIO.output(IN4,False)
    if Request == 's':         #REV: IN1 & IN3 Low, IN2 & IN4 High
      GPIO.output(IN2,True)
      GPIO.output(IN4,True)
      GPIO.output(IN1,False)
      GPIO.output(IN3,False)
    if Request == 'd':         #RGT: IN1 & IN4 High, IN2 & IN3 Low
      GPIO.output(IN1,True)
      GPIO.output(IN4,True)
      GPIO.output(IN2,False)
      GPIO.output(IN3,False)
    if Request == 'b':         #STP: IN1 & IN3 low, IN2 & IN4 Low
      GPIO.output(IN1,False)
      GPIO.output(IN3,False)
      GPIO.output(IN2,False)
      GPIO.output(IN4,False)
    return

#server runs on port 7000
#IP address of raspberry pi: 192.168.0.110
server_address_httpd = ('192.168.0.110',7000)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting server')
httpd.serve_forever()
GPIO.cleanup()
