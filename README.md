Installing the PWA:
Review Central can be installed on desktop or mobile devices for quick access.

Desktop (Chrome / Edge)
Open the application in your browser.
Look for the “Install App” icon in the address bar.
Click Install.
The app will appear as a standalone window and can be launched from your Start Menu or Applications folder.

Mobile (Android / Chrome)
Open the site in Chrome.
Tap the menu (⋮).
Select Add to Home screen.
Confirm installation.

iOS (Safari)
Open the site in Safari.
Tap the Share icon.
Select Add to Home Screen.
Confirm installation.
Once installed, the app behaves like a native application and can be launched without opening a browser.

Using the Application

Home Page
The home page displays:
A welcome message
Login/Register options
A disabled “Add Review” button if logged out
Category shortcuts (Games, Movies, Books)
A preview of recent reviews
Navigation updates automatically depending on whether you are logged in.

Registering an Account
Open the Register page.

Enter:
Email
Username
Password
Submit the form.

Requirements:

Email must be unique
Username must be unique
If either is already taken, an error message will appear.

Logging In
Open the Login page.

Enter:
Email or Username
Password
Submit the form.
If credentials are incorrect, an error message will be displayed.
Once logged in, you will see:
“Add Review” enabled
“Logout (your username)” in the navigation
Edit/Delete options on your own reviews

Adding a Review
Click Add Review (only visible when logged in).
Fill in:
Category (Games, Movies, Books)
Title
Rating (1.0–10.0)
Review text
Submit the form.

Validation:
Rating must be between 1.0 and 10.0
All fields are required
If validation fails, an error message will appear.

Viewing Reviews
The All Reviews page shows every review in the system.
You can:
Filter by category
Click a review to view full details
See who posted each review
Logged‑out users can view reviews but cannot add, edit, or delete them.

Editing a Review
Open a review you created.
Click Edit Review.
Update the fields.
Submit the form.

Only the original author can edit a review.
Other users will not see the Edit button.

Deleting a Review
Open a review you created.
Click Delete Review.
Confirm deletion.

Only the original author can delete a review.
Other users will not see the Delete button.

Offline Mode
Review Central includes basic offline support through a service worker.

When offline:
A banner appears at the top of the screen
“Add Review”, “Edit”, and “Delete” buttons are disabled
Cached pages (Home, Login, Register, Reviews) still load
The app remains installable and launchable
When the connection returns, full functionality is restored automatically.

Data Storage
This version uses in‑memory storage, meaning:
Data resets when the server restarts
No SQL database is used
This is intentional for the assessment
A future version could use JSON or SQL for persistence.