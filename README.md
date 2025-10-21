# Task Manager

A modern, responsive web application for managing tasks and comments built with React and Flask.

## Features

- **Task Management**: Create, edit, and delete tasks
- **Comments System**: Add, edit, and delete comments for each task
- **Modern UI**: Clean, professional interface with gradient backgrounds and card layouts
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Updates**: AJAX-powered interface for smooth user experience
- **RESTful API**: Well-structured backend API with proper HTTP methods

## Technologies Used

### Frontend
- React 18
- Babel (for JSX compilation)
- Font Awesome (icons)
- CSS3 with modern styling

### Backend
- Flask (Python web framework)
- Flask-CORS (Cross-Origin Resource Sharing)
- RESTful API design

## Project Structure

```
task-manager/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── app.db              # SQLite database file
│   ├── config.py           # Application configuration
│   ├── models.py           # Database models
│   ├── requirements.txt    # Python dependencies
│   ├── schemas.py          # Data validation schemas
│   ├── routes/
│   │   ├── tasks.py        # Task-related API endpoints
│   │   └── comments.py     # Comment-related API endpoints
│   └── tests/
│       ├── conftest.py     # Test configuration
│       └── test_comments.py # Comment API tests
├── frontend/
│   ├── index.html          # Main HTML file
│   └── style.css           # Application styles
└── README.md               # Project documentation
```

## Installation & Setup

### Prerequisites
- Python 3.7+
- A modern web browser

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install required Python packages:
   ```bash
   pip install flask flask-cors
   ```

3. Run the Flask server:
   ```bash
   python app.py
   ```

The backend will start on `http://127.0.0.1:5000`

### Frontend Setup

1. Open `frontend/index.html` in your web browser, or serve it through a local server.

2. For development, you can use Python's built-in server:
   ```bash
   cd frontend
   python -m http.server 8000
   ```

Then navigate to `http://localhost:8000/index.html`

## API Endpoints

### Tasks
- `GET /api/tasks` - Retrieve all tasks
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/<id>` - Update a task
- `DELETE /api/tasks/<id>` - Delete a task

### Comments
- `GET /api/tasks/<task_id>/comments` - Get comments for a task
- `POST /api/tasks/<task_id>/comments` - Add a comment to a task
- `PUT /api/tasks/<task_id>/comments/<comment_id>` - Update a comment
- `DELETE /api/tasks/<task_id>/comments/<comment_id>` - Delete a comment

## Usage

1. **Adding Tasks**: Use the "Add Task" form to create new tasks
2. **Editing Tasks**: Click the pencil icon next to a task title to edit it
3. **Viewing Comments**: Click the "Comments" button to view and manage comments for a task
4. **Adding Comments**: Use the comment form in the comments panel
5. **Deleting Items**: Use the delete buttons with confirmation dialogs

## Features Overview

- **Responsive Grid Layout**: Tasks and comments are displayed in a responsive grid
- **Interactive UI**: Hover effects, smooth transitions, and intuitive controls
- **Form Validation**: Client-side validation for required fields
- **Confirmation Dialogs**: Prevents accidental deletions
- **Real-time Feedback**: Immediate UI updates after operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Screenshots

(Add screenshots here when available)

## Future Enhancements

- User authentication and authorization
- Task categories and tags
- Due dates and reminders
- Task prioritization
- Search and filtering capabilities
- Data persistence with database integration
