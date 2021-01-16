# Polygon project

## Requirements

- Docker compose

## Get started

- `make start`

## Usage

- Once started, go to https://localhost:8080
- Add, modify, delete Trackings from the db at: mysql://polygon_user:polygon_password@127.0.0.1:3306/polygon_db (I recommend using DBeaver)
- See on the home page that your changes are taken into account in performances computation

## Development

- Using TypeScript for Vue.js static typing
- Using Prettier for typescript formatting
- Using Black for python formatting
- Using Swagger for backend documentation: http://localhost:8000/docs

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

- Using BackgroundTasks shipped with FastAPI on the backend, to avoid blocking request because of entity being saved to db
(also allows asynchronous completion time computation, which is thus reliable truth)
- Using SQLAlchemy for db interface because it's the best tool for data management (fast, scalable, maintainable)
- Using Pydantic schemas (could have been called DTOs) to manage inbound and outbound json data


## Improvements

- Separate backend into Resources, Services and DAO (unrelevant for now because we only have on route and this is a prototype)
- Add MySQL migrations support (to update database schema as we develop)
