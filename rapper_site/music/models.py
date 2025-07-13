from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    cover = models.ImageField(upload_to='albums/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='tracks/')
    youtube_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.album})"

