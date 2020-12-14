# togger
<div align="center">

[![Build status](https://github.com/jb-delafosse/togger/workflows/build/badge.svg?branch=master&event=push)](https://github.com/jb-delafosse/togger/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/togger.svg)](https://pypi.org/project/togger/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/jb-delafosse/togger/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/jb-delafosse/togger/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/jb-delafosse/togger/releases)
[![License](https://img.shields.io/github/license/jb-delafosse/togger)](https://github.com/jb-delafosse/togger/blob/master/LICENSE)

Togger is an easy to use sign up sheet for volunteers. Also can be used for various events planing like football matches 
or going out with friends
</div>

## demo
URL: https://togger-app.herokuapp.com (can take few moments for a cold boot)  
user: demo@github.com  
pass: demo

Registration doesn't require an email verification (but it will still annoy you because this is an only way to recover lost password). 
## features
* Plan events. Even recurrent ones. Resize and drag em how you want
* Sign up yourself or your friend for a shift
* Share calendar with your collective/family/friends
* Count number of shifts per person for a given period
* Control an access
* Different colors for events based on number of people signed up: gray - nobody yet, orange - one person, green - two or more
* Mobile friendly
* Powered by Python, Flask, Flask-Login, Fullcalendar, rrule, WTForms, SQLAlchemy and many more

## How to use
### Create an event
1. Click the *Edit* button to activate an edit mode
2. Select the date to create an event (you can select multiple days, resize and drag events)
3. Put in the event title, description and recurrent preference
4. Click the *Save changes* button
5. Click the *Stop* button to go back to the View mode

### Sign up for an event
1. Select an event
2. Press the *I'm in* button or manually put a name into the field
3. Click the *Save changes* button

## Screenshots
![week view](/screenshots/week_view.png?raw=true "Week View")
![event view](/screenshots/event_view.png?raw=true "Event View")
![create view](/screenshots/create_view.png?raw=true "Create View")
![report_view](/screenshots/report_view.png?raw=true "Report View")

## docker-compose
```
version: '3'
services:
  togger:
    restart: always
    environment:
      - SECRET_KEY=change-me
      - FLASK_ENV=development
      - SQLALCHEMY_DATABASE_URI=sqlite:///resources/database.db
      - MODULE_NAME=togger.main
      - VARIABLE_NAME=application
      - APP_URL=localhost
      - SMTP_LOGIN=
      - SMTP_MAILBOX=
      - SMTP_PASSWORD=
      - SMTP_PORT=
      - SMTP_SERVER=
    build: .
    ports:
      - "5001:80"
```
* Change SECRET_KEY to something more secure
* Put your database uri in SQLALCHEMY_DATABASE_URI or use sqlite by default (was tested with sqlite and postgresql only)
* Change APP_URL to you real app url (used in emails)
* Put SMTP parameters for an email validation and a password recovery
* Change FLASK_ENV according to your environment

run

`$ docker-compose up`

Currently ARM isn't supported, but feel free to use your own base image.

The repository also contains Procfile to run the app on heroku

## TODO
* add LDAP auth
* ????


## Very first steps

### Initial

1. Initialize `git` inside your repo:

```bash
git init
```

2. If you don't have `Poetry` installed run:

```bash
make download-poetry
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
```

4. Upload initial code to GitHub (ensure you've run `make install` to use `pre-commit`):

```bash
git add .
git commit -m ":tada: Initial commit"
git remote add origin https://github.com/jb-delafosse/togger.git
git push -u origin master
```

### Poetry

All manipulations with dependencies are executed through Poetry. If you're new to it, look through [the documentation](https://python-poetry.org/docs/).

<details>
<summary>Notes about Poetry</summary>
<p>

Poetry's [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:

- `poetry add numpy`
- `poetry run pytest`
- `poetry build`
- etc

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/jb-delafosse/togger/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

For Pull Request this labels are configured, by default:

|               **Label**               |  **Title in Releases**  |
|:-------------------------------------:|:----------------------:|
| `enhancement`, `feature`              | 🚀 Features             |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
| `build`, `ci`, `testing`              | 📦 Build System & CI/CD |
| `breaking`                            | 💥 Breaking Changes     |
| `documentation`                       | 📝 Documentation        |
| `dependencies`                        | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/jb-delafosse/togger/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
