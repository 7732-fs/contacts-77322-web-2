from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=2)
    phone=models.CharField(max_length=200)
    email=models.EmailField(default="")

    def __repr__(self) -> str:
        return f"{self.name}:{self.phone}"
    
    def __str__(self) -> str:
        return f"{self.name}:{self.phone}"