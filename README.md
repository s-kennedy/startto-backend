# StART backend

## Tech stack:
- Python/Django
- Postgres
- Docker

## Get started
- Copy `env/dev.env.template` as `env/dev.env`
- Install Docker and docker-compose
- Run `docker-compose up`, sometimes the web app comes up before postgres configuration has ended which can cause a failure, if this happens, run `docker-compose up` again.
- Run `docker ps` to get the container ID for the app container
- Open a shell session in the app container: `docker exec -it <container-id> sh`
- Run migrations: `python manage.py migrate`
- Collect static files: `python manage.py collectstatic`
- Seed the database with fake profiles: `python manage.py seed_database`
- The server should now be running on `localhost:8000`

