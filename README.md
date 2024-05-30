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

- **Registration:** `/register/`
- **Login:** `/login/`
- **Logout:** `/logout/`

### Contacts

- **Create Contact:** `/contact/create/`
- **Edit Contact:** `/contact/<contact_id>/edit/`
- **Delete Contact:** `/contact/<contact_id>/delete/`

### Accounts

- **Create Account:** `/account/create/`
- **Edit Account:** `/account/<account_id>/edit/`
- **Delete Account:** `/account/<account_id>/delete/`

### Opportunities

- **Create Opportunity:** `/opportunity/create/`
- **Edit Opportunity:** `/opportunity/<opportunity_id>/edit/`
- **Delete Opportunity:** `/opportunity/<opportunity_id>/delete/`

### Tasks

- **Create Task:** `/task/create/`
- **Edit Task:** `/task/<task_id>/edit/`
- **Delete Task:** `/task/<task_id>/delete/`

### Reports

- **Generate Contact Report:** `/report/contacts/`
- **Generate Account Report:** `/report/accounts/`
- **Generate Opportunity Report:** `/report/opportunities/`
- **Generate Task Report:** `/report/tasks/`

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
