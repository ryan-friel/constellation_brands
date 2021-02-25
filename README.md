# gs-coding-ryan-friel
This project will allow users to look at the Constellation Brands wineries. Users can then plan reservations to visit the wineries.

### Logic
The logic is rather standard. This uses core CRUD principles to handle the different views required for user functionality.

### Logic Continued
Users are expected to register and login to access any parts of the application. Then they can browse the supported CB wineries in a list format.
Afterwards they can navigate to the reservations section and visit a winery at a time of their choice.
Users can then update, delete, and see a detailed view about each reservation they make.

### Requirements
Look at the requirements.txt
django
django-allauth
django-crispy-forms

### Running this project
This project must be run locally.
1) Clone this repository.
2) pip install the requirements.
```python
pip3 install -r requirements.txt
```
3) create a super user.
```python
python3 manage.py createsuperuser
```
4) We can now run our server.
```python
python3 manage.py runserver
```
5) Please create the support wineries in the django admin interface. Visit /admin to do so.
6) Register as a regular user, and now you can explore the supported wineries, and create reservations.

### Questions
Please email rfriel92@gmail.com for any questions relating to this repository.
