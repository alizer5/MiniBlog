# Mini Blog Website

This is a simple blog website built using Django and Bootstrap. It includes basic features such as user authentication, a contact form, and blog management. The project uses SQLite as its database.

## Features

- **User Registration & Login**: Users can sign up and log in to access the blog platform.
- **Home Page**: Users can view the home page with the latest blog posts.
- **Contact Form**: Users can send messages via the contact form.
- **Blog Management**: 
  - **Author**: Authors can add new blog posts and edit their existing posts.
  - **Admin**: Full access to manage users, blogs, and site content.

## Technology Stack

- **Backend**: Django
- **Frontend**: Bootstrap
- **Database**: SQLite

## Setup Instructions

### Prerequisites
- Python 3.12
- Django
- Bootstrap (Included in the project)

### Installation

1. Clone the repository:

   
   git clone https://github.com/your-username/mini-blog-website.git

2. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

3. Create a superuser for the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

4. Run the server:

   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage

- **Home Page**: View available blog posts.
- **AboutUS Page**: View available about us.
- **Sign Up/Login**: Create an account or log in.
- **Contact Us**: Submit a message using the contact form.
- **Dashboard**: Authors can create and edit blogs. Admins have full access to manage all content.
- 

## Contributing

Feel free to submit issues or contribute to the project by forking the repository and making a pull request.

---
