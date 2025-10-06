# aixclone Project

## Overview
The aixclone project is a Django web application designed to manage and showcase various tools. It allows users to submit new tools, view details about existing tools, and filter tools based on categories and pricing.

## Features
- User-friendly interface for browsing tools.
- Submission form for users to add new tools.
- Admin interface for managing tools, categories, and submissions.
- Web scraping functionality to import tools from external sources.

## Installation

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd aixclone
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Navigate to the submission page to add new tools.
- Browse the list of tools and view details for each tool.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.