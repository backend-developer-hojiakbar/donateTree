from django.db import models

class AllTreesCount(models.Model):
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.count)


class PlantedTrees(models.Model):
    class Time(models.TextChoices):
        Today = "TD", "Bugun"
        Month = "MN", "Oylik"
        Year = "YR", "Yillik"

    time = models.CharField(max_length=3,
                             choices=Time.choices,
                             default=Time.Today)
    count = models.IntegerField()
    goalTrees = models.IntegerField(blank=True)
    deadline = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.count)

class MainPageStatic(models.Model):
    title = models.CharField(max_length=300)
    count = models.IntegerField()
    img = models.ImageField(upload_to="statistics/img/")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AboutTrees(models.Model):

    class Regions(models.TextChoices):
        Barchasi = "ALL", "Barchasi"
        ToshkentSH = "TSH", "Toshkent Shahar"
        ToshkentV = "TV", "Toshkent Viloyati"
        Fargona = "FR", "Farg'ona"
        Andijon = "AD", "Andijon"
        Namangan = "NM", "Namangan"
        Jizzax = "JZ", "Jizzax"
        Sirdaryo = "SR", "Sirdaryo"
        Samarqand = "SM", "Samarqand"
        Buxoro = "BX", "Buxoro"
        Xorazm = "XR", "Xorazm"
        Navoiy = "NV", "Navoiy"
        Qoraqolpoq = "QR", "Qoraqolpoq"
        Surxondaryo = "SX", "Surxondaryo"
        Qashqadaryo = "QSH", "Qashqadaryo"

    class Filters(models.TextChoices):
        ManzaraliB = "MB", "Manzalari butalar"
        Yaproq = "YP", "Yaproq bargli"
        Mevali = "MV", "Mevali daraxtlari"
        ManzaraliN = "MN", "Manzalari Ninabarg"

    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to="trees/img/", blank=True)
    image1 = models.ImageField(upload_to="trees/img/", blank=True)
    image2 = models.ImageField(upload_to="trees/img/", blank=True)
    image3 = models.ImageField(upload_to="trees/img/", blank=True)
    image4 = models.ImageField(upload_to="trees/img/", blank=True)
    filterName = models.CharField(max_length=3,
                                    choices=Filters.choices,
                                    default=Filters.ManzaraliN)
    region = models.CharField(max_length=3,
                              choices=Regions.choices,
                              default=Regions.ToshkentSH)
    nameLotin = models.CharField(max_length=500)
    height = models.CharField(max_length=300)
    wide = models.CharField(max_length=350)
    flowers = models.CharField(max_length=1500)
    fruits = models.CharField(max_length=800)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    bio = models.TextField()
    additionBio = models.TextField()
    cleanCO2Year = models.CharField(max_length=180)
    cleanCO2Day = models.CharField(max_length=180)
    cleanCO2Period = models.CharField(max_length=200)
    averageLifeTime = models.CharField(max_length=100)
    leaveSize = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="projects/img")
    required = models.DecimalField(max_digits=15, decimal_places=3)
    funded = models.DecimalField(max_digits=15, decimal_places=3)
    percentage = models.DecimalField(max_digits=3, decimal_places=2)
    sponsorsCount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Companies(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    yourFullName = models.CharField(max_length=200)
    companyWebSite = models.CharField(max_length=300)
    password = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="companies/img")
    treeCount = models.DecimalField(max_digits=12, decimal_places=2)
    offsetCO2 = models.DecimalField(max_digits=15, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Citizen(models.Model):
    fullName = models.CharField(max_length=250)
    image = models.ImageField(upload_to='citizen/', blank=True)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName


class UserTree(models.Model):
    treeId = models.ForeignKey(AboutTrees, on_delete=models.CASCADE)
    userId = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.treeId)








