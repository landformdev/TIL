from django.db import models
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)

    # 이미지를 리사이징해 캐시에 새롭게 저장
    # image_thumbnail = ImageSpecField(source='image',
    #                                   processors=[ResizeToFill(200, 200)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})

    # DB에 저장할때 부터 원본 이미지를 리사이징
    image = ProcessedImageField(upload_to='image/%Y/%m/%d/',
                                           processors=[ResizeToFill(200, 200)],
                                           format='JPEG',
                                           options={'quality': 60})
    created_at = models.DateTimeField(auto_now_add=True)