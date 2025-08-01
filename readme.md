# URLs in the Employee Project Management System

Below is an explanation of the URLs used in the project and their functionality:

### `/`
- **Home Page**: Displays a welcome message and navigation options for managing projects. Accessible to all users.

### `/signup/`
- **Sign Up Page**: Allows new users to register an account by providing a username and password.

### `/login/`
- **Login Page**: Enables existing users to log in to their account.

### `/logout/`
- **Logout**: Logs the user out and redirects them to the home page.

### `/projects/current/`
- **Current Projects Page**: Displays a list of all ongoing projects for the logged-in user.

### `/projects/completed/`
- **Completed Projects Page**: Shows a list of all completed projects, including their completion dates.

### `/projects/create/`
- **Create Project Page**: Provides a form for users to create a new project by entering a title and optional description.

### `/projects/<int:project_id>/`
- **View Project Page**: Displays the details of a specific project based on its ID. Users can update, complete, or delete the project.

### `/projects/<int:project_id>/complete/`
- **Mark Project as Completed**: Marks the specified project as completed and moves it to the completed projects list.

### `/projects/<int:project_id>/delete/`
- **Delete Project**: Deletes the specified project