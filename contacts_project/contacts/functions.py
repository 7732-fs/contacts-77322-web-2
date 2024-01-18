from .models import Contact

def add(form):
    Contact(form).save()

def view():
    pass

def delete(name="name"):
    pass

def update(name="name", phone="phone"):
    pass