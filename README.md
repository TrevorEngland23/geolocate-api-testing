# IP Geolocation API  

[Sign Up Here](https://www.abstractapi.com/api/ip-geolocation-api)  

## What is this?  

Simply put, I was searching for an API for a unrelated project when I came across this. It seemed interesting, so I wanted to try it out. You can read the documentation here.  
[Documentation](https://docs.abstractapi.com/ip-geolocation?_gl=1*1pgdn79*_gcl_au*OTQzNDk0NzQ0LjE3NDA1NDM2MzI.)  

Once you sign up, you'll get an API key and a code snippet to try out. In the url, you'll need to input your api key as a parameter (and optionally an ip address). If you do want to verify the accuracy of the results, I recommend setting an IP from this website and verifying the results.  
[WebPageTestAdmin](https://www.webpagetest.org/addresses.php)  

You'll notice I have a python script in this repository. I started my testing by writing ip data to a json file using Python. Then, I got inspiration from [What's my IP](https://whatismyipaddress.com/) to build my own mini version.  

## To run  

You'll need to create a .env file and specify your api key in there. 

Python: 

```bash
cd Python
python3 find_ip_location.py <IP_ADDRESS>
```  

JS:  

```bash
npm install
node server.js
```  

Then navigate to localhost:3000 in a web browser. This very basic website should have your IP information displayed in a table.
