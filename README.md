User Credentials for Testing:

Test User 1
Auni
123

Test User 2
Md
123

Note: Make as much users as you want to

Setup and Installation Instructions:

Clone the repository:
git clone https://github.com/shihab173066/Shihab-Social-Media-Website.git

Navigate to the project directory:
cd socialmedia

Create a virtual environment (recommended):
virtualenv venv

Activate the virtual environment:
venv\Scripts\activate

Install the project dependencies:
pip install django
pip install pillow

Perform database migrations:
python manage.py migrate

Run server:
python manage.py runserver

Superadmin User -
Username: shihab
Email address: shihab@email.com
Password: 123

python manage.py runserver
Access the application in your web browser at http://127.0.0.1:8000/

Here's an elaborate summary of the features implemented in my social media website project:

1. Edit Profile:
   - Users can update their personal information, such as name, bio, and other details related to their account.
   - The feature also allows users to upload or update their profile picture, ensuring they can personalize their presence on the platform.

2. Explore:
   - A dedicated "Explore" section is available where users can discover new content from various profiles.
   - This feature enables users to interact with posts from other users, expanding their social interactions beyond their network.
   - The section is designed for browsing images, posts, and captions, with easy navigation to different content.

3. Login:
   - A secure login system has been implemented that allows users to authenticate and access their accounts.
   - The system ensures only registered users can log in, maintaining privacy and security for each user's information.
   - This feature uses Django's authentication system to manage user credentials and sessions.

4. Main (Home Page):
   - The home page is the main interface of the platform, displaying the latest posts and updates from followed users or content creators.
   - It serves as the landing page where users can scroll through their feed, like, comment, or share posts, similar to other social media platforms.
   - The page is optimized for easy interaction with content, and new posts are dynamically loaded for a seamless user experience.

5. Profile:
   - Each user has their own profile page, where they can see their personal information, posts, and activities on the platform.
   - Users can view details such as their bio, uploaded images, and the posts they have created or interacted with.
   - The profile serves as a personal hub for each user, showcasing their activity and contributions to the platform.

6. Profile Image Upload:
   - A feature that allows users to upload their own profile image, giving them the ability to personalize their account.
   - The image upload functionality ensures that the profile picture is properly displayed and can be updated whenever necessary.
   - Users can choose to either upload a new image or select one from their existing media.

7. Search:
   - A search functionality has been integrated, enabling users to find other users, posts, and content easily.
   - The search bar lets users search for specific users by username or find posts based on captions or hashtags.
   - This feature enhances the discoverability of content and encourages interaction with a broader community.

8. Signup:
   - New users can register for an account on the platform using a straightforward signup process.
   - The signup process includes form validation to ensure that all fields are correctly filled out, including email, username, and password.
   - Upon successful registration, users gain access to the platform, enabling them to interact with other users, create posts, and explore content.

9. Superadmin (Django): 
   - The application includes a superadmin panel built using Django’s admin interface, which allows administrators to manage users, posts, and other platform-related activities.
   - The superadmin functionality provides full control over the platform, enabling administrators to monitor user behavior, remove inappropriate content, and maintain overall system integrity.
   - The panel can be used to grant or revoke user privileges, manage content, and access system settings.

These features come together to build a fully functional social media website, with both user-facing and administrative capabilities. They provide users with a personalized experience while giving admins control over the platform's operations.
