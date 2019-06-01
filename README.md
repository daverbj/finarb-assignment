# Instruction to run this project

## Using Docker

git clone https://github.com/daveai/finarb-assignment.git

<b>install docker and docker-compose and run following command</b>

docker-compose up -d
Test with swagger UI
http://localhost:5000/docs



# Using manual setup
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



