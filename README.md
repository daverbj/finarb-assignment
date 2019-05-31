# finarb-assignment

#Instruction to run this project

## clone the repo
git clone https://github.com/daveai/finarb-assignment.git

## install pip env
pip install pipenv

## Enter pip env shell
pipenv shell

## Install dependencies
pipenv install

## migrate db
python migrate.py db init

## run the flask app
python run.py

## test with an end point 
http://localhost:5000/api/users

# To run the front end

## install node js, npm and angular cli
## navigate to front end directory
cd frontend
## serve the front end
ng serve

## test
http://localhost:4200



