from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=10, decimal_places=2)

    #function for string rep of Student obj
    def __str_(self):
        return self.id + '|' + self.name + '|' + self.score
