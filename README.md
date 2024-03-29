# Welcome to May Yashar's book store!

__If you need this project - you probably work for me (or your name is Yossi and you are my lecturer)__

__on the fastapi **or** on localhost:8000/Books-shop you can see all the books in our store,__

__and as a store employee you will be able to add new books we received to the store, updatade and delete if anything has changed.__

# good luck!

## Developer Info💻:

### May Yashar 👨🏼‍💻
- Github - [mayyashar](https://github.com/mayyashar)
- Linkedin - [May Yashar](https://www.linkedin.com/in/may-yashar-0b78a4239/)

##  Set-up 🛠🧰

1. First clone the repository to your local system :

``` git clone https://github.com/mayyashar/eass_final_project.git```

2. Then to start the application simply write the command : 

``` docker-compose up ```

this will create 3 containers for frontend, backend and postgres.

(if one of the container stay down, try to reset the specific container)

<img width="711" alt="image" src="https://github.com/mayyashar/eass_final_project/assets/129296688/c24aea58-4805-43d1-81db-05e8de27f846">

## Usage 📈

- To enter the Backend FastAPI UI - open your browser and enter the URL : 

   ``` localhost:8000/docs ```

- To enter the Frontend UI - enter URL : 

   ``` localhost:8000/Books-shop ```

you can also see logs inside the container.
 
## Architecture 👷🏽

This project follows a microservice architecture. The main components of the architecture are:

Frontend: The frontend is built with Streamlit, providing an interactive map interface to view the real-time status of the books store.

Backend: The backend is built with FastAPI, which fetches the ISS location data through an API call. The backend serves two endpoints.

postgres: postgres is used saving the books store data.

Docker: Docker is used for containerization and deployment. Dockerfiles and Docker Compose are used to define and build the containers for the frontend, backend, and Jenkins.

## Demo 🎥

[YouTube Link](https://youtu.be/eRPvvbIALms)



