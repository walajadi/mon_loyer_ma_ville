# mon_loyer_ma_ville

- To run the app locally, 2 possible ways :
VIRTUALENV:
  - Create your own virtualenv (follow instructions here : https://virtualenv.pypa.io/en/latest/installation.html
  - Activate env.
  - Migrate :
    - cd src/backend
    - RUN `python manage.py migrate` to create models on sqlite db.
  - Init DB with data:
    - Download city dataset csv file here (https://www.data.gouv.fr/fr/datasets/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2018/ )
    - put it in dir *src/backend/data/*: 
    - RUN `python3 manage.py init_db_villes`
  - RUN `python manage.py runserver` to launch API
  - Example call: `curl 'http://127.0.0.1:8000/api/villes/93/?surface=50&loyer_max=800'`
    
DOCKER:
  - cd src/
  - BUILD CMD : `docker build -t maville --platform linux/amd64  .`
  - RUN CMD : `docker run -d --name mycontainer -p 80:80 maville`
