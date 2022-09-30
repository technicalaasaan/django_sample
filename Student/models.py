from django.db import models

# Create your models here.
class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    stu_name = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.stu_name

    def __repr__(self):
        return self.__str__()


class Subjects(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=200)
    dept = models.CharField(max_length=10, choices=(
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
    ))
    year = models.CharField(max_length=4, choices=(
        ("1st", "1st"),
        ("2nd", "2nd"),
        ("3rd", "3rd"),
        ("4th", "4th")
    ))

    class Meta:
        db_table = "subjects"

    def __str__(self):
        return self.sub_name

    def __repr__(self):
        return self.__str__()
