# quick-ip-app
A quick flask app that can be spun up on a vm in order to grab ip and location.


![DALL·E 2024-01-17 12 27 11 - An abstract representation of a digital landing page, featuring a network of connected nodes symbolizing links and data transfer, with subtle hints of](https://github.com/pronsSec/quick-ip-app/assets/93559326/8a9bf945-fa27-4dae-9bc1-34980a5ebe28)


This repository contains a Flask application that serves as a free alternative to URL shortening and landing page services like Bitly. It's designed to quickly spin up a landing page and track visits, including IP addresses and approximate locations.

## Features

- Flask web server for serving landing pages
- IP and location tracking for visitors
- Easy deployment on VPS (Virtual Private Server)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- A VPS (e.g., DigitalOcean droplet, AWS EC2 instance)
- Domain name (optional, for custom domain setup)

## Server Setup

### Step 1: Install Python and Required Packages

1. Update your package list:

    ```bash
    sudo apt update
    ```

2. Install Python and pip:

    ```bash
    sudo apt install python3 python3-pip
    ```

3. Install Git:

    ```bash
    sudo apt install git
    ```

### Step 2: Clone the Repository

1. Clone the repository:

    ```bash
    git clone https://github.com/pronsSec/quick-ip-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository-name
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Step 3: Run the Application

1. Start the Flask application:

    ```bash
    python3 app.py
    ```

## Connecting a Domain

If you own a domain and wish to connect it to your landing page application, follow these steps:

### Step 1: Point Your Domain to Your VPS

1. Log in to your domain registrar's website (e.g., GoDaddy, Namecheap).
2. Navigate to your domain's DNS settings.
3. Create an `A` record pointing to your VPS's IP address.

    - **Host**: The subdomain you want to use (e.g., `@` for root domain, `www` for www subdomain).
    - **Points to**: Your VPS's IP address.
    - **TTL**: Time to live (you can leave this as the default).

### Step 2: Update Your VPS Configuration (Optional)

If you're using a web server like Nginx or Apache, ensure that it's configured to serve your Flask application on the domain you've set up.

### Step 3: Secure Your Connection (Recommended)

Consider setting up an SSL/TLS certificate for your domain to secure the connection:

1. You can obtain a free certificate from [Let's Encrypt](https://letsencrypt.org/).
2. Follow the instructions to set up the certificate on your server.

## Usage

Once set up, your landing page will be accessible at the domain you've configured. Visitors' IP addresses and approximate locations will be logged, allowing you to track visits.

## Contributing

Contributions to this project are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is open-source and available under the [MIT License](LICENSE).
