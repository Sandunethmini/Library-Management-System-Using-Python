📚 Library Management System

      A simple Library Management System built using Flask. 
      This system allows users to add books, borrow books, return books, and view available or borrowed books via RESTful API 
      endpoints.


🚀 Features

            ➕ Add a new book (title, author, ISBN)
            
            📖 Borrow a book by ISBN
            
            🔄 Return a borrowed book
            
            ✅ View all available books
            
            📕 View all borrowed books with borrow dates


🛠️ Tech Stack

            Python
                  
            Flask
                  
            Flask-CORS
                  
            Datetime


📂 Project Structure

            library-management/
            
            │-- app.py               # Main Flask application
            
            │-- templates/
            
            │   └── index.html       # Home page template
            
            │-- requirements.txt     # Project dependencies
            
            │-- README.md            # Project documentation



⚙️ Installation & Setup

      1️⃣ Clone the repository
            git clone https://github.com/your-username/library-management.git
            cd library-management

      2️⃣ Create a virtual environment (recommended)
            python -m venv venv
            source venv/bin/activate   # On macOS/Linux
            venv\Scripts\activate      # On Windows

      3️⃣ Install dependencies
            pip install flask flask-cors

      4️⃣ Run the application
            python app.py

      5️⃣ Open in browser
            Navigate to: http://127.0.0.1:5000/



🤝 Contribution

            Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.


📜 License

            This project is licensed under the MIT License.

