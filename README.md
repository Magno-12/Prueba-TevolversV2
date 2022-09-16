# Prueba-T-evolversV2

## Explanation
In this test we can find 2 key branches, one is the "master" branch where we have the project running and the other is the "fix-docker" branch where
there is a docker orchestrator with which I tried to do the entire test, dockerizing from the redis, the api to the producer and consumer
applying the concepts that were requested to evaluate my knowledge.

## Minimum requirements for a machine:

1. Python and fastapi Installed in your machine
2. Windows 10 or superior or Linux (ubuntu,debian,mint,etc)
3. Visual Studio Code
4. Virtual enviroment
5. WSL for the redis
6. Docker in your machine

## To run the in my case it was (which is the operation of the producer / consumer without docker) follow the following steps

1. run redis server, in my case(https://www.linode.com/docs/guides/install-redis-ubuntu/)
2. clone repository: git clone https://https://github.com/Magno-12/T-Evolvers-Python-Challenge.git
3. install virtual enviroment: $ pip install virtualenv env
4. activate the virtual environment: $ cd ./env/Scripts/source activate
5. install requirements (env) ./Prueba-T-Evolvers pip install -r requirements.txt
6. run producer (env) ./Prueba-T-Evolvers/producer uvicorn main:app --reload (this is in terminal 1)
7. run consumer (env) ./Prueba-T-Evolvers/consumer uvicorn main:app --reload (this is in terminal 2)
8. to see on the web through a socket that is listening to the passage of data in the tunnel used by redis go to http://localhost:8000/metric


