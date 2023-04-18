from django.db import models

class Person(models.Model):
  date_missing = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  first_name = models.CharField(max_length=30)
  age_at_missing = models.IntegerField()
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=20)
  gender = models.CharField(max_length=1)
  race = models.CharField(max_length=1)
  
  def __str__(self):
    return '%s %s %s %i %s %s %s %s' % (self.date_missing, self.last_name, self.first_name,
                      self.age_at_missing, self.city, self.state, self.gender, self.race)
