from django.db import models
from common.models import TimeStampedModel
from django.contrib.auth import get_user_model
from common.utils import image_path
import os

User = get_user_model()


class Tag(TimeStampedModel):

    title = models.CharField(max_length=50,unique=True)

    def clean(self):
        super().clean()
        self.title = self.title.lower()
    
    def __str__(self):
        return "#" + str(self.title)


class Post(TimeStampedModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to=image_path)
    caption = models.CharField(max_length=255)
    like_count= models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, through="PostTag",related_name="posts")

    def __str__(self):
        return str(self.id)+" posted by "+str(self.user_id)
    

    def delete(self,*args, **kwargs):
        if self.image:
            file_path = self.image.path
            print(file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)

        super().delete(*args, **kwargs)



class PostLike(TimeStampedModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_likes")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["post_id","user_id"],name="unique_post_likes"
            )
        ]
    
    def __str__(self):
        return str(self.post_id) + " liked by "+str(self.user_id)


class Comment(TimeStampedModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="list_comments",null=True, blank=True)
    comment = models.ForeignKey('self', on_delete=models.CASCADE,related_name="replies", null=True,blank=True)
    detail = models.TextField(default='')


class PostTag(TimeStampedModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["post_id", "tags_id"],
                name = "unique_post_tag"
            )
        ]
