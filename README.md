# CRM Backend using Django

## Overview

This project is a Customer Relationship Management (CRM) backend application built using Django, designed to help businesses manage their customer interactions, track leads, and streamline sales processes. It provides features for managing contacts, accounts, opportunities, and more. It also includes integration with stripe for payments.

## Features

- **Contact Management:** Manage customer contacts and interactions.
- **Account Management:** Track accounts and their associated contacts.
- **Opportunity Tracking:** Monitor sales opportunities and their progress.
- **Task Management:** Assign tasks and track their completion status.
- **Reporting:** Generate reports to analyze sales performance and customer data.



## URL Endpoints

### Authentication

- **Registration:** `api/v1/users/`
- **Login:** `api/v1/token/login/`
- **Logout:** `api/v1/token/logout/`


### Teams

- **Get my team:** GET `api/v1/teams/get_my_team/`
- **Create Team:** POST `api/v1/teams/`
- **Edit Team:** PUT/PATCH `api/v1/teams/<int:id>/`
- **Delete Team:** DELETE `api/v1/teams/<int:id>/`
- **Add member :** DELETE `api/v1/teams/add_member/`



### Leads
- **Leads List:** GET `api/v1/leads/`
- **Create Lead:** POST `api/v1/leads/` 
- **Edit Lead:** PUT/PATCH `api/v1/leads/<int:id>/`
- **Delete Lead:** POST `api/v1/leads/delete_lead/<int:id>/`


### Clients

- **Client List:** GET `api/v1/clients/` 
- **Create Client:** POST `api/v1/clients/` 
- **Edit Client:** PUT/PATCH `api/v1/clients/<int:id>/`
- **Delete Client:** DELETE `api/v1/clients/delete_client/<int:id>/`


### Notes

- **Notes List (with client_id as query param):** GET `api/v1/notes/?client_id=<int:id>` 
- **Create Note:** POST `api/v1/notes/`
- **Edit note (with client_id as query param):** PATCH `api/v1/notes/1/?client_id=1`


## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. Clone the repository:

```bash
git clone https://github.com/armshahs/crm_backend_django.git
```

2. Navigate to the project directory:

```bash
cd crm_backend_django
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```


## Usage

1. Register for a new account or login if you already have one.
2. Create contacts by navigating to the Contacts section and adding contact details.
3. Manage accounts by creating accounts and associating contacts with them.
4. Track sales opportunities by creating opportunities and updating their status.
5. Assign tasks to team members and monitor their progress.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/my-feature` or `git checkout -b bugfix/fix-issue`.
3. Make your changes and commit them: `git commit -am 'Add new feature'`.
4. Push to your branch: `git push origin feature/my-feature`.
5. Submit a pull request detailing your changes.
