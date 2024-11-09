from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # Directory where the file will be stored
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the current timestamp when file is uploaded
    file_size = models.BigIntegerField(null=True, blank=True)  # Stores the file size in bytes
    
    def save(self, *args, **kwargs):
        # Calculate and store the file size before saving the model
        if self.file:
            self.file_size = self.file.size
        super(UploadedFile, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.file.name} ({self.file_size} bytes)"

