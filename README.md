# 🧑‍💻 My Portfolio Website — mfatihdinc.com

This is the source code of my portfolio website [mfatihdinc.com](https://mfatihdinc.com), where I showcase my projects, research interests, thoughts, and more.

## 🚀 Features

- 🎯 Homepage with a minimal, clean design
- 🧠 Blog-like **Thoughts** section (markdown-supported)
- 💼 Projects section with project details
- 👨‍🚀 About Me page with brief introduction
- 🎨 Custom static assets (CSS/JS/images)
- ✍️ Admin panel support for dynamic content
- 🔒 CSRF protected forms

## ⚙️ Tech Stack

- **Backend**: Django 5.2.3 (Python 3.11)
- **Frontend**: HTML5, CSS3 (custom), JS (vanilla)
- **Deployment**: cPanel (CloudLinux + Passenger WSGI)
- **Database**: SQLite (can be switched to PostgreSQL/MySQL)

## 🗂 Project Structure (Simplified)

mysite/
├── personal/ # Main Django app (views, models, urls, etc.) 
│ ├── templates/ 
│ └── static/ 
├── staticfiles/ # Static files collected by Django 
├── media/ # Uploaded media (optional) 
├── manage.py 
├── requirements.txt 
└── passenger_wsgi.py # Entry point for cPanel Passenger 


## 🛠 Setup & Deploy (Quick)

1. Create virtualenv  
2. Install requirements:
    ```
    pip install -r requirements.txt
    ```
3. Set environment variables and run:
    ```
    python manage.py migrate
    python manage.py collectstatic
    ```

4. For cPanel + Passenger:
    - Use `passenger_wsgi.py` as the startup file
    - Configure `.htaccess` for static files
    - Restart via `touch tmp/restart.txt`

## 🔗 Live Preview

You can visit the live site at:  
👉 [**https://mfatihdinc.com**](https://mfatihdinc.com)
