from django.db import models



#postapp Application models
class PostCategory(models.Model):
    category     = models.CharField(max_length=300)
    def __str__(self):
        return self.category




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    title       = models.CharField(max_length=500,null=True, blank=True,default='')
    category    = models.ForeignKey(PostCategory,related_name="categoryname",on_delete=models.CASCADE)
    author      = models.CharField(max_length=500,null=True, blank=True)
    content     = models.TextField(null=True, blank=True)
    status      = models.IntegerField(choices=STATUS, default=0)
    created_on  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title




class PostComment(models.Model):
    comment     = models.CharField(max_length=255)
    post        = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    created_on  = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment




class PostMedia(models.Model):
    name        = models.CharField(max_length=255)
    post        = models.ForeignKey(Post,related_name="media",on_delete=models.CASCADE)
    created_on  = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name