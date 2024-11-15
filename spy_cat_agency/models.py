from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.is_complete}"

    def get_mission(self):
        return Mission.objects.filter(targets=self)[0]

class Mission(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, null=True)
    targets = models.ManyToManyField(Target)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} | {self.is_complete}"
