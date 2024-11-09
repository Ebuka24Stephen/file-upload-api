from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)  
    file_size = models.BigIntegerField(null=True, blank=True)  
    
    def save(self, *args, **kwargs):
        
        if self.file:
            self.file_size = self.file.size
        super(UploadedFile, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.file.name} ({self.file_size} bytes)"

