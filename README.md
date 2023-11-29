<h1>Task Manager</h1>

<p>
A simple and flexible task management web application
</p>

[![Actions Status](https://github.com/blacksmokezip/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/blacksmokezip/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9c9b7618329e7e594079/maintainability)](https://codeclimate.com/github/blacksmokezip/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9c9b7618329e7e594079/test_coverage)](https://codeclimate.com/github/blacksmokezip/python-project-52/test_coverage)

---

## About

A task management web application built with Python and [Django](https://www.djangoproject.com/) framework. It allows you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with the system.

To provide users with a convenient, adaptive, modern interface, the project uses the [Bootstrap](https://getbootstrap.com/) framework.

The frontend is rendered on the backend. This means that the page is built by the DjangoTemplates backend, which returns prepared HTML. And this HTML is rendered by the server.

[PostgreSQL](https://www.postgresql.org/) is used as the object-relational database system.

#### --> [Demo](https://task-manager-crsd.onrender.com) <--

---

## Installation

Clone the project:
```bash
>> git clone https://github.com/blacksmokezip/Task-Manager.git && cd Task-Manager
```

Create `.env` file in the root folder and add following variables:
```dotenv
SECRET_KEY={your secret key} # Django will refuse to start if SECRET_KEY is not set
```

And run:
```shell
>> docker-compose up
```

The server is running at http://0.0.0.0:8000

---

## Available Actions:

- **_Registration_** — First, you need to register in the application using the registration form provided;
- **_Authentication_** — To view the list of tasks and create new ones, you need to log in using the information from the registration form;
- **_Users_** — You can see the list of all registered users on the corresponding page. It is available without authorization. You can change or delete information only about yourself. If a user is the author or performer of a task, it cannot be deleted;
- **_Statuses_** — You can view, add, update, and delete task statuses if you are logged in. Statuses corresponding to any tasks cannot be deleted;
- **_Tasks_** — You can view, add, and update tasks if you are logged in. Only the task creator can delete tasks. You can also filter tasks on the corresponding page with specified statuses, performers, and labels;
- **_Labels_** — You can view, add, update, and delete task labels if you are logged in. Labels matching any tasks cannot be deleted.