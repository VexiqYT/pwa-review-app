Review Central – PWA Review App A Progressive Web App built with Python Flask that allows users to register, log in, post reviews, edit/delete their own reviews, and install the app as a PWA.

Requirements Python 3 Flask installed (pip install flask) All project files downloaded (including the templates and static folders)

How to Run the Application: Open the project folder in VS Code or another editor. Open a terminal inside the project folder.

Run the command: python app.py (If port 5000 is blocked on your computer, use python -m flask run --port 5001) Wait for Flask to start. The terminal will show something like:

Running on http://127.0.0.1:5000 Open a web browser and go to the address shown in the terminal.

How to Use the Application:

Register Enter email, username, and password. Email must be unique. Username must be unique.

Login Log in using either email OR username, plus your password.

Reviews Logged‑in users can: Add a review Edit their own reviews Delete their own reviews

Logged‑out users can: View all reviews Cannot add/edit/delete reviews

Rating System Ratings support 1.0 to 10.0, with one decimal place.

PWA Features Installable on desktop and mobile Works offline using a service worker Manifest file included Cached assets allow basic offline functionality

Notes This version uses in‑memory storage, not SQL. Restarting the server clears all users and reviews. The GitHub repository contains all source code and version history.