Services:
    Sensors, controller, manipulator and webapp. 
    Each is built as an image and run as a container 
    using the docker-compose.yml and docker-compose build 

Running the Containers:
    A docker-compose.yml has the specified services, commands and dependants. 
    With the help of docker-compose up -d, all services are started as a daemon.  
    They are stoped by docker-compose down.

For interactive terminal to a service:
    docker exec -it <name_of_image> sh