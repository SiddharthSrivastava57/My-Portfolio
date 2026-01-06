# My Portfolio

A modern, responsive personal portfolio website built with Django, showcasing my skills, projects, and professional background as a software engineer.

## 🚀 Features

- **Responsive Design**: Fully responsive layout that works on all devices
- **Contact Form**: Functional contact form with Django backend and database storage
- **Project Showcase**: Display of key projects with GitHub links
- **Skills Section**: Visual representation of technical skills
- **Resume Download**: Direct link to download resume PDF
- **Social Links**: Integration with LinkedIn, GitHub, and Instagram

## 🛠️ Tech Stack

- **Backend**: Django 6.0
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 6.1.1
- **Styling**: Custom CSS with responsive design

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SiddharthSrivastava57/portfolio.git
   cd portfolio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the Django project directory**
   ```bash
   cd portfolio
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser and visit**
   ```
   http://127.0.0.1:8000/
   ```

## 📁 Project Structure

```
portfolio/
├── portfolio/              # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── Base/                   # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── home.html
├── static/                 # Static files
│   ├── css/
│   │   └── style.css
│   ├── images/
│   └── pdf/
│       └── resume.pdf
├── templates/              # Global templates
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## 🎯 Key Components

### Models
- **Contact**: Stores contact form submissions with fields for name, email, phone, and message

### Views
- **contact**: Handles contact form submission and validation

### Templates
- **home.html**: Main portfolio page with all sections

## 🔒 Security Notes

- DEBUG is set to True for development
- SECRET_KEY should be changed for production deployment
- ALLOWED_HOSTS should be configured for production

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production-ready database (PostgreSQL recommended)
4. Set up proper static file serving
5. Use environment variables for sensitive data

## 📞 Contact

**Siddharth Srivastava**
- LinkedIn: [siddharth-srivastava-774a3b259](https://www.linkedin.com/in/siddharth-srivastava-774a3b259/)
- GitHub: [SiddharthSrivastava57](https://github.com/SiddharthSrivastava57)
- Instagram: [sidd_573](https://www.instagram.com/sidd_573?igsh=c204cG8xc3NtdW52)

## 📄 License

© 2026 Siddharth Srivastava. All Rights Reserved.

---

*Built with ❤️ using Django*</content>
<parameter name="filePath">/Users/siddharthsrivastava/Desktop/My Portfolio/README.md
