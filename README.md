# 🎓 Quiz Management System

![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![HTML](https://img.shields.io/badge/HTML-5-orange?style=for-the-badge&logo=html5)
![CSS](https://img.shields.io/badge/CSS-3-blue?style=for-the-badge&logo=css3)

📚 A modern **Quiz Management System** built with **Django** where teachers/admins can create quizzes, add questions & choices, and students can attempt quizzes online with instant scoring.  

---

## 🚀 Features

✅ Admins can:
- Create, update, and delete quizzes  
- Add questions with multiple choices  
- Mark correct answers  
- View student submissions and scores  

✅ Students can:
- Enter their **Name & Student ID** before starting a quiz  
- Attempt quizzes online  
- Submit answers and get instant results  
- See their score after submission  

✅ Other highlights:
- Clean & responsive UI  
- Data stored securely in SQL database  
- Automatic time-stamps for submissions  

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Database:** SQLite (default) or any SQL database (PostgreSQL, MySQL, etc.)  
- **Admin Panel:** Django Admin for full quiz control  

---

📊 Database Design
- Quiz → Contains title, description, time, publish status
- Question → Linked to Quiz, has multiple choices
- Choice → Belongs to a Question, marked correct/incorrect
- Submission → Stores student info, quiz attempted, score
- Answer → Links Submission with selected choices

👩‍💻 Contribution
- Contributions are welcome! 🚀
- Fork this repo
- Create a new branch (feature/awesome-feature)
- Commit changes
- Push to your branch
- Open a Pull Request 🎉

📜 License
This project is licensed under the MIT License 📝

⭐ Show your support
If you like this project, give it a star ⭐ on GitHub and share it with others!
