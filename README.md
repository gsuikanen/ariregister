# Äriregister
This is a sample project
### API Server
API server is written in Python (using Flask framework).
Before starting the project, please run the following commands:
```sh
pip install flask
pip install pytest
cd ariregister-api
python3 init.py
```
The command will create database and prepopulate it with needed information.
##### Running
In order to run API server locally, run the following command:
```sh
python3 app_main.py
```

### User Interface
User Interface (UI) is written in Angular framework.
Before starting the project, please make sure you have Node.js installed: [instructions](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
For installing Angular, please use the following command:
```sh
npm install -g @angular/cli
```

##### Running
In order to run UI server locally, run the following commands:
```sh
cd ariregister-ui
npm install --legacy-peer-deps
npm run
```

### Time report
2022-10-06: 2h - initial repo and boilerplate code setup, DB structure

2022-10-08: 3h - creating DB and prepopulating it with lists, API for lists

2022-10-09: 2h - working on GET service for API

2022-10-10: 3h - GET service API + unit testing

2022-10-11: 3h - UI initial setup + home page

2022-10-12: 1h - some progress with UI home page

2022-10-14: 2h - fetching data from API and displaying it in UI

2022-10-15: 4h - form for adding new company (UI)

2022-10-16: 6h - finishing form for new company and working on POST (API)