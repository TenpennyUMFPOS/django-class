from django.db import models

# 2) Modèles complémentaires

class Contract(models.Model):
    type_code = models.CharField(max_length=10)  # ex: FT
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type_code} - {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class JobRecord(models.Model):
    work_year = models.IntegerField()
    experience_level = models.CharField(max_length=2) 
    employment_type = models.ForeignKey(Contract, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    salary = models.IntegerField()
    salary_currency = models.CharField(max_length=10)
    salary_in_usd = models.IntegerField()
    employee_residence = models.CharField(max_length=100)
    remote_ratio = models.IntegerField()
    company_location = models.CharField(max_length=100)
    company_size = models.CharField(max_length=2)
    

    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True)
    skill = models.ManyToManyField(Skill, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.job_title} ({self.work_year})"
