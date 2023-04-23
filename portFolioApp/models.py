from django.db import models

class PortfolioRegistration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    portfolio_url = models.URLField()
    
    def __str__(self):
        return self.name

class PortfolioImage(models.Model):
    registration = models.ForeignKey(PortfolioRegistration, on_delete=models.CASCADE, default=1,null=True, blank=True)
    image = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return self.image.name
        
    class Meta:
        ordering = ['-id']
        
        
