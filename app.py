from flask import Flask, request, render_template
import geocoder
import logging
from user_agents import parse

# Configure logging
logging.basicConfig(filename='visitors.log', level=logging.INFO, format='%(asctime)s %(message)s')

app = Flask(__name__)

@app.route('/')
def home():
    # Get the visitor's IP address
    visitor_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    # Get the visitor's user agent
    user_agent = parse(request.headers.get('User-Agent'))

    # Optional: Get an approximate location (using a service like ipinfo.io)
    g = geocoder.ip(visitor_ip)
    visitor_location = g.latlng  # (latitude, longitude)
    visitor_address = g.address if g.address else 'Location not available'

    # Log the visit
    log_message = f"IP: {visitor_ip}, Location: {visitor_address}, User Agent: {user_agent}, Browser: {user_agent.browser.family}, OS: {user_agent.os.family}, Device: {user_agent.device.family}"
    logging.info(log_message)
    print(log_message)  # Print to the terminal as well

    # Process the IP and location data here (e.g., save to a database, analytics, etc.)

    # Render a webpage (can be a simple HTML or a template)
    return render_template('index.html', user_agent=str(user_agent))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
