# Vetty-Test

# File Viewer Flask App

A simple Flask application to view the content of text files with preserved markup. The application supports rendering files in English, including files containing Chinese characters. It provides a single GET route, allowing users to specify the target file name as part of the URL. Optional URL query parameters can be used to define start and end line numbers, allowing users to view a specific range of lines in the file.

# Features

Single GET route for viewing file content
Preserved markup in the rendered HTML page
Optional variable part of the URL for specifying the target file
Optional URL query parameters for start and end line numbers
Graceful handling of exceptions with detailed error pages

# Deployment

Utilizes Python virtual environment (REQUIREMENTS.txt included)
Git version control for easy collaboration and deployment

# Usage

Clone the repository: git clone [repository_url]
Set up a virtual environment: python -m venv venv (activate based on your OS)
Install dependencies: pip install -r REQUIREMENTS.txt
Run the Flask application: python app.py
Visit http://127.0.0.1:5000/ in your browser to explore the file content.
