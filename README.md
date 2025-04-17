# Simple Task Manager API

## Description

This is a simple RESTful API for managing tasks. It allows users to create, read, update, and delete tasks stored in a MySQL database.

## How to Run/Setup

1.  **Install Dependencies:**
    ```bash
    pip install fastapi uvicorn mysql-connector-python
    ```

2.  **Setup MySQL:**
    * Make sure you have MySQL installed and running.
    * Create a database named `task_manager_db` and run the `schema.sql` script to create the `tasks` table. You can do this using a MySQL client or the command line:
        ```bash
        mysql -u your_mysql_user -p < schema.sql
        ```
        (Replace `your_mysql_user` with your MySQL username).

3.  **Configure Database Credentials:**
    * Open the `database.py` file and update the `DB_CONFIG` dictionary with your MySQL host, user, password, and database name.

4.  **Run the API:**
    ```bash
    uvicorn main:app --reload
    ```

    The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

* **POST /tasks/**: Create a new task.
    * Request Body:
        ```json
        {
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": false
        }
        ```
    * Response:
        ```json
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": false
        }
        ```
* **GET /tasks/**: Get a list of all tasks.
    * Response:
        ```json
        [
            {
                "id": 1,
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "completed": false
            },
            ...
        ]
        ```
* **GET /tasks/{task\_id}**: Get a specific task by ID.
    * Example: `/tasks/1`
    * Response:
        ```json
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": false
        }
        ```
* **PUT /tasks/{task\_id}**: Update an existing task.
    * Example: `/tasks/1`
    * Request Body (fields to update):
        ```json
        {
            "completed": true
        }
        ```
    * Response:
        ```json
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": true
        }
        ```
* **DELETE /tasks/{task\_id}**: Delete a task by ID.
    * Example: `/tasks/1`
    * Response: `204 No Content`

## ERD (Conceptual)

# Simple Task Manager API

## Description

This is a simple RESTful API for managing tasks. It allows users to create, read, update, and delete tasks stored in a MySQL database.

## How to Run/Setup

1.  **Install Dependencies:**
    ```bash
    pip install fastapi uvicorn mysql-connector-python
    ```

2.  **Setup MySQL:**
    * Make sure you have MySQL installed and running.
    * Create a database named `task_manager_db` and run the `schema.sql` script to create the `tasks` table. You can do this using a MySQL client or the command line:
        ```bash
        mysql -u your_mysql_user -p < schema.sql
        ```
        (Replace `your_mysql_user` with your MySQL username).

3.  **Configure Database Credentials:**
    * Open the `database.py` file and update the `DB_CONFIG` dictionary with your MySQL host, user, password, and database name.

4.  **Run the API:**
    ```bash
    uvicorn main:app --reload
    ```

    The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

* **POST /tasks/**: Create a new task.
    * Request Body:
        ```json
        {
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": false
        }
        ```
    * Response:
        ```json
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": false
        }
        ```
* **GET /tasks/**: Get a list of all tasks.
    * Response:
        ```json
        [
            {
                "id": 1,
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "completed": false
            },
            ...
        ]
        ```
* **GET /tasks/{task\_id}**: Get a specific task by ID.
    * Example: `/tasks/1`
    * Response:
        ```json
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": false
        }
        ```
* **PUT /tasks/{task\_id}**: Update an existing task.
    * Example: `/tasks/1`
    * Request Body (fields to update):
        ```json
        {
            "completed": true
        }
        ```
    * Response:
        ```json
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": true
        }
        ```
* **DELETE /tasks/{task\_id}**: Delete a task by ID.
    * Example: `/tasks/1`
    * Response: `204 No Content`



