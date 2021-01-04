## Mocking bird application

Mockingbird is a set of aws lambda functions allowing you to run the equivalent 
of a mock server wiremock like. 


# How to run locally 
Create a new docker network
```
$ docker network create local-dev
```

Run the dynamo image locally 
```
$ docker run -p 8000:8000 --network local-dev --network-alias=dynamodb --name dynamodb amazon/dynamodb-local
```

Create and activate a localenv
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create the dynamo tables 
```
python create_tables.py
```

Run the application with sam 
```
sam local start-api --docker-network local-dev -t sam.yml
```