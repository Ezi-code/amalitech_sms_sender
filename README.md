# SMS Sender

**Project Description:**
SMS Sender is a web application designed to facilitate digital marketers, like Ronald Rolling, in sending SMS messages to multiple users. The platform provides features such as sending messages to multiple mobile numbers simultaneously, creating message templates, associating mobile numbers with templates, quick sending of messages using templates, and accessing controls for editing before sending or sending immediately. Additionally, users can view a history of sent SMS messages and utilize controls like resend and edit before send. The application utilizes the Africa's Talking platform for sending SMS.

**Customer Requirements:**

1. Send a message to multiple mobile numbers at once.
2. Create message templates and associate mobile numbers with templates.
3. Utilize templates for quick message sending.
4. Access controls for editing before sending or sending immediately.
5. View a history of sent SMS messages with controls for resend and edit before send.
6. Use the AfricasTalking platform for sending SMS.

**Deliverables:**

- Web application source code hosted on GitHub with Git flow implementation, including a well-written README file.
- Entity-Relationship (ER) diagram illustrating the database design.
- Deployed link for the web application.

**Technologies Used:**

- Django framework for backend development.
- HTML, bootstrap css/js for frontend development.
- Africa's Talking API for sending SMS messages.

- Git for version control.

**Installation and Setup:**

1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Create superuser accounts: `python manage.py createusperuser`
    - username:`root`
    - password: `asdf`
    - email: `root@demo.com`\
    **NOTE**:  
        - you can choose your custom username, email and password
        - you need to have an accounts to have access to the system's funtionalities
4. Run the development server: `python manage.py runserver`
5. Access the application in your web browser at `http://localhost:8000/`
6. Acess the admin panel `http://localhost:8000/admin`

**Usage:**

1. Create message templates and associate mobile numbers with templates.
2. Send messages to multiple mobile numbers using templates or by composing new messages.
3. View the history of sent SMS messages, with options to resend or edit before sending again.

**Contributing:**

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/NewFeature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/NewFeature`
5. Submit a pull request.

**Credits:**
Developed by Ezra Yendau

**Contact Information:**
For inquiries, contact `ezrayendau2000@gmail.com`
