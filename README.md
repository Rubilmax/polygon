# Polygon project

Not production-ready!

## Requirements

- Docker compose

## Get started

- `make start`

Alternatively, if you don't have `make`, you can just `docker-compose up -d --build`

## Usage

- Once started, go to https://localhost:3000
- The first time you query /performances, you'll get unknown completion time, as you've just made the first query to the backend. Just re-query it to get not-unknown results!
- Add, modify, delete Trackings from the db at: mysql://polygon_user:polygon_password@127.0.0.1:3306/polygon_db (I recommend using DBeaver)
- See on the home page that your changes are taken into account in performances computation

## Development

#### Technical stack

- Using TypeScript for Vue.js static typing
- Using Prettier for typescript formatting
- Using Black for python formatting
- Using Swagger for backend documentation: http://localhost:5000/docs
- Also using ReDoc for backend documentation: http://localhost:5000/redoc

#### Start development

- `make start-db`
- `make start-client`
- `make start-server`

## Implementation

#### Frontend

- Using Vuetify on the frontend for quick, scalable and maintainable UI prototyping
- Separated logic from components, moving it to `services/`, declaring global components under `components/`
and managing pages/views inside `pages/`, which in turn also contains local components
([see my article on this architecture using React](https://www.sipios.com/blog-tech/how-to-develop-a-modern-react-project-at-scale))

#### Backend

- Process trackings in Middleware so that we record what's happening in the request (get the status code and completion time)
(could have moved this logic inside an asynchronous task to avoid blocking the request)
- Using SQLAlchemy for db interface because it's the best tool for data management (fast, scalable, maintainable)
- Using Pydantic schemas (could have been called DTOs) to manage inbound and outbound json data


## Improvements

- Separate backend routes into Resources (unrelevant for now because we only have on route and this is a prototype)
- Add MySQL migrations support (to update database schema as we develop)
- Change Docker images to slim/alpine for production and ship production-ready commands
- Separate backend dev requirements from requirements.txt
- Use environment variables for db credentials inside backend
