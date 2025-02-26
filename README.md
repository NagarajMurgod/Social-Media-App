# Social Medai App
A modern social media platform built with React for the frontend and Django for the backend. This app allows users to create accounts, post content, follow other users, and interact with posts through likes and comments.

## Features

- **User Authentication**: Login and Registration.
- **Post Creation**: Users can create posts with text and media (images/videos).
- **Comments & Likes**: Interaction with posts through likes and comments.
- **Follow System**: Users can follow and unfollow other users.
- **Notification system**: (Optional) Notifications for new likes, comments, or follows.
- **Infinite Scrolling** : Infinite scrolling feature like Instagram and Facebook


## Tech Stack

- **Frontend**: React, React Router, Axios (for API requests) and React context for authentication.
- **Backend**: Django Rest Framework
- **Database**: PostgreSQL 
- **Authentication**: Session Authentication
- **Styling**: CSS

## Installation
### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Node.js and npm (for React)
- PostgreSQL (or another DBMS if you prefer)
- Git ( for cloning repo )

### Backend Setup (Django)
1. Clone the repository:

    ``` 
    git clone https://github.com/NagarajMurgod/Social-Media-App.git 
    cd Social-Media-App
    ```
2. Navigate to the backend directory:

    ``` 
    cd api 
    ```

3. Create a virtual environment and install dependencies:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
4. Set up the database (PostgreSQL):

- Ensure PostgreSQL is running, and create a new database for the project.
- Update the database configuration in backend/settings.py with your database credentials.

5. Run migrations to set up the database schema:

    ```
    python manage.py migrate
    ```
6. Create a superuser (for admin access):

    ```
    python manage.py createsuperuser
    ```
7. Start the backend server:

    ```
    python manage.py runserve
    ```

### Frontend Setup (React)

1. Navigate to the frontend directory:

    ```
    cd ../client
    ```
2. Install the required npm dependencies:

    ```
    npm install
    ```
3. Set up environment variables
    - Create a .env file in the frontend directory with the following:

        ```
        VITE_API_URL = 'http://localhost:8000'
        ```
4. Start the frontend development server:

    ```
    npm run dev
    ```

The frontend will now be running at http://localhost:5173/.

## Usage

Once both servers are up, you can access the frontend at http://localhost:5173/ and start interacting with the app.

- Sign Up: Create a new account to start using the platform.
- Create Posts: Share your thoughts with images or text.
- Like & Comment: Engage with others' posts by liking and commenting.
- Follow Users: Keep up with the latest updates from your followed users.

## API Endpoints

The backend exposes the following API endpoints:
1. Authentication
    - ``` POST /auth/signup/``` - user registration
    - ``` POST /auth/login/``` - User Login (Session authentication)
    - ``` POST /auth/logout/ ``` - User logout
    - ``` GET /auth/csrf_cookie/``` - Set CSRF token

2. Posts
    - ``` POST /post/upload/``` - Create a new post ( Images only as of now )
    - ``` GET /post/user_posts/``` - List all  posts
    - ``` GET /post/user_posts/{id}/``` - List all the user posts
    - ``` DEL /post/{post id}/``` - Delete Post
    - ``` POST /post/{post id}/comments/``` Comment on a post
    - ``` GET /post/{post id}/comments/``` - Get Post comments
    - ``` POST /post/{post id}/postLikeDislike/``` - Post like and dislike

3. User
    - ``` POST /user/profile/{user id}/ ```- Get the User profile Info
    - ``` POST /user/profile/{user id}/ ``` - Update the user profile ( Bio , firstname , lastname and profile image)
    - ``` POST /user/profile/follow/{user id}/ ``` - Follow User
    - ``` POST /user/profile/unfollow/{user id}/ ``` - Unfollow User
    - ``` GET /user/list/ ``` - Get all the users
    - ``` GET /user/profile/{user id}/relations/?type=followers ``` - Get the followers of user
    - ``` GET /user/profile/{user id}/relations/?type=followees ``` - Get the followees of user
    - ``` GET /notifications/{user id}/ ``` - Get the Notification for user

## Areas for Contribution
We welcome contributions to this project! If you'd like to contribute

- Integrate user Registration API with Frontend
- Integrate Send Comment api with frontend
- Implement a feature to allow users to send direct messages to each other.
- Instead of just following users, introduce a system for users to send and accept friend requests
- Add more complex media management features, like resizing or auto-cropping images before upload
- Implement real-time notifications for new likes, comments, and follows (using WebSockets or something similar)
- Improve the app’s mobile responsiveness and performance on various devices.
- Implement a dark mode theme for the user interface

## References

- [Frontend Design 1](https://www.youtube.com/watch?v=zM93yZ_8SvE&list=PLj-4DlPRT48nfYgDK00oTjlDF4O0ZZyG8)
- [Frontend design 2](https://www.youtube.com/watch?v=pFHyZvVxce0&list=PLj-4DlPRT48nfYgDK00oTjlDF4O0ZZyG8&index=2)
- [Django RestFramework Views Doc](https://www.cdrf.co/)
- [We all are utilizing this one 😂](https://chatgpt.com/)

## Application Screenshots

![](./Images/login.png | width=100)
