# Äriregister
This is a sample project
### API Server
API server is written in Python (using Flask framework).
Before starting the project, please run the following commands:
```sh
pip install flask
pip install pytest
pip install flask-cors
cd ariregister-api
python3 init.py
```
The command will create database and prepopulate it with needed information.
##### Running
In order to run API server locally, run the following command:
```sh
python3 app_main.py
```
##### Database schema
![database schema](/ariregister-api/db-schema.png)

### User Interface
User Interface (UI) is written in Angular 14.2.
Before starting the project, please make sure you have Node.js installed: [instructions](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
If you have Node.js installed, you need to install Angular using the following command:
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
After that, you will be able to view page at http://localhost:4200/