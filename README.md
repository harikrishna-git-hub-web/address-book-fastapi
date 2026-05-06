\# Address Book API (FastAPI)



\## 📌 Overview



This project is a simple Address Book API built using FastAPI.

It allows users to create, update, delete, and retrieve addresses with geographic coordinates.



It also supports finding nearby addresses based on distance using the Haversine formula.



\---



\## 🚀 Features



\* Create address

\* Get all addresses

\* Update address

\* Delete address

\* Find nearby addresses using latitude \& longitude



\---



\## 🛠️ Tech Stack



\* FastAPI

\* Python 3

\* SQLite

\* SQLAlchemy



\---



\## ⚙️ Setup Instructions



\### 1. Clone the repository



```bash

git clone https://github.com/harikrishna-git-hub-web/address-book-fastapi.git

cd address-book-fastapi

```



\### 2. Create virtual environment



```bash

python -m venv venv

venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the application



```bash

uvicorn app.main:app --reload

```



\### 5. Access API Docs



Open in browser:



```

http://127.0.0.1:8000/docs

```



\---



\## 📍 API Endpoints



| Method | Endpoint          | Description          |

| ------ | ----------------- | -------------------- |

| POST   | /addresses        | Create address       |

| GET    | /addresses        | Get all addresses    |

| PUT    | /addresses/{id}   | Update address       |

| DELETE | /addresses/{id}   | Delete address       |

| GET    | /addresses/nearby | Get nearby addresses |



\---



\## 📐 Nearby Search Logic



The API calculates distance between two coordinates using the Haversine formula and returns addresses within the specified distance.



\---



\## ✅ Example



```

GET /addresses/nearby?lat=17.385\&lon=78.4867\&distance=10

```



\---



\## 👨‍💻 Author



Harikrishna Kuruva



