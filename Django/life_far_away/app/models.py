from django.db import models


class planetSize(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class starSize(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class measure(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class activity(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class tides(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class plateTectonic(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class carbonCycle(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class plateTectonics(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class magneticFields(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class unitMeasurement(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class age(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class orbit(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name
      
class planet(models. Model):
    name_planet = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'media/static/img/', null = True)
    activity = models.ForeignKey(activity, on_delete=models.CASCADE)
    age = models.ForeignKey(age, on_delete=models.CASCADE) 
    starSize = models.ForeignKey(starSize, on_delete=models.CASCADE)
    orbit = models.ForeignKey(orbit, on_delete=models.CASCADE)
    magneticFields = models.ForeignKey(magneticFields, on_delete=models.CASCADE)
    planetSize = models.ForeignKey(planetSize, on_delete=models.CASCADE)
    composition = models.CharField(max_length=100)
    warm = models.CharField(max_length=100)
    unitMeasurement = models.ForeignKey(unitMeasurement, on_delete=models.CASCADE) 
    ice_sheet_extend = models.CharField(max_length=100)
    oceans = models.CharField(max_length=100)
    ocean_extend = models.CharField(max_length=100)
    tides = models.ForeignKey(tides, on_delete=models.CASCADE)
    carbonCycle = models.ForeignKey(carbonCycle, on_delete=models.CASCADE)
    plateTectonics = models.ForeignKey(plateTectonics, on_delete=models.CASCADE)
    volcanism =models.ForeignKey(measure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_planet

# class characteristics(models.Model):
#     planet_type = models.CharField(max_length=100)
#     discovery_date = models.CharField(max_length=20)
#     mass = models.FloatField()
#     planet_radius = models.CharField(max_length=100)
