# 🚀 Support System Backend (Django)

## 📌 Overview

This project is a **Query Management & Support System Backend** built using **Django & Django REST Framework**.

It is designed to solve real-world support team problems:

* Uneven workload distribution
* Unanswered queries
* Lack of visibility and accountability

The system ensures:
✅ Every query is assigned
✅ No query goes unanswered
✅ Workload is balanced across team members

---

## 🎯 Features

### 🔹 1. Auto Assignment Engine

* Automatically assigns queries to the **least loaded support member**
* Prevents overload and idle resources

### 🔹 2. SLA Tracking System

* Each query has a **deadline (SLA)**
* Detects delayed queries
* Supports escalation logic

### 🔹 3. Dashboard API

* Provides real-time insights:

  * Total queries
  * Pending queries
  * Resolved queries

### 🔹 4. Role-Based Users

* Support Members
* Admin

---

## 🏗️ Tech Stack

* **Backend:** Django
* **API:** Django REST Framework
* **Database:** SQLite (can scale to PostgreSQL)

---

## 📂 Project Structure

```
support_system/
│── core/
│   ├── models.py        # User & Query models
│   ├── views.py         # API logic
│   ├── utils.py         # Auto-assignment logic
│   ├── urls.py          # API routes
│   ├── admin.py         # Admin panel config
│   └── management/
│       └── commands/
│           └── check_sla.py   # SLA monitoring script
│
│── support_system/
│   ├── settings.py
│   ├── urls.py
│
│── db.sqlite3
│── manage.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd support_system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django djangorestframework
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔌 API Endpoints

### 📊 Dashboard

```
GET /api/dashboard/
```

Response:

```json
{
  "total_queries": 10,
  "pending": 4,
  "resolved": 6
}
```

---

### ➕ Create Query

```
POST /api/create-query/
```

Body:

```json
{
  "title": "Login Issue",
  "description": "User unable to login"
}
```

---

## ⏱️ SLA Monitoring

Run SLA check manually:

```bash
python manage.py check_sla
```

👉 Detects overdue queries and triggers escalation logic.

---

## 🧠 System Design Logic

| Problem            | Solution                |
| ------------------ | ----------------------- |
| Uneven workload    | Auto assignment         |
| Queries unanswered | SLA + escalation        |
| No visibility      | Dashboard API           |
| No ownership       | Assigned user per query |

---

## 🚀 Future Improvements

* Email / Notification system
* Real-time updates using WebSockets
* Priority-based query handling
* React frontend dashboard
* Celery + Redis for async processing

---

## 👨‍💻 Author

**Mangesh Kokare**

---

## 📌 Conclusion

This system demonstrates:

* Strong backend fundamentals
* Real-world problem solving
* Scalable and maintainable architecture

It ensures **efficiency, accountability, and reliability** without increasing team size.

---
