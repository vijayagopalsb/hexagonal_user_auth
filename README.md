## Hexagonal User Authentication


This project implements a modular and extensible user authentication system based on **Hexagonal Architecture** (Ports & Adapters Pattern) using Python and FastAPI.


### Project Features

- User Registration and Login
- Email validation
- Exception handling using custom errors
- Database access through clean abstractions
- Designed with **Hexagonal Architecture** for better testability and scalability

### roject Architecture

This project follows the **Hexagonal Architecture** (also known as Ports and Adapters), which ensures a clean separation between:

- **Core Domain Logic** (Business Rules)
- **Inbound Adapters** (e.g., REST API)
- **Outbound Adapters** (e.g., Database Access)
- **Application Services** (use cases)

```plaintext
+-----------------------+
|     REST API (FastAPI)|
+----------+------------+
           |
+----------v-----------+
|  Application Service |
+----------+-----------+
           |
+----------v-----------+
|    Domain Logic      |
+----------+-----------+
           |
+----------v-----------+
|  DB Adapter (SQLite) |
+----------------------+
```

### Project Structure

```plaintext
hexagonal_user_auth/
├── app/
│   ├── domain/         # Core domain models & interfaces
│   ├── service/        # Application logic (use cases)
│   ├── adapters/       # Inbound (API) and outbound (DB) adapters
│   ├── main.py         # FastAPI entry point
├── user.db             # SQLite DB (recommend .gitignore this)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

### Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/vijayagopalsb/hexagonal_user_auth.git
cd hexagonal_user_auth
```

2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Run the Application
```bash
uvicorn app.main:app --reload
```

### Testing
Coming soon... 

### Future Enhancements

- JWT-based token authentication

- Role-based access control

- OAuth2 or social login

- Docker support

- CI/CD pipeline

### License

This project is licensed under the MIT [License](/LICENSE). See the LICENSE file for details.