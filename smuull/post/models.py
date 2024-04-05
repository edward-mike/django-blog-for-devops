import os
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils import timezone

User = get_user_model()


# Board Model
class Board(models.Model):
    
    created_by = models.ForeignKey(to = User,
                                   related_name='boards',
                                   blank=True,
                                   null=False,
                                   on_delete=models.CASCADE)
    
    title = models.CharField(max_length=55,
                             verbose_name='title',
                             blank=False,
                             null=False)
    
    description = models.TextField(max_length=150,
                                   verbose_name='description',
                                   blank=True,
                                   null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    modified_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ('created_date',)
        verbose_name = "Post Board"
        verbose_name_plural = "Post Boards"
        
    def __str__(self):
        return self.title
    



def post_cover_upload_dir(post_obj,filename):
	# upload function.
	filename,ext = os.path.splitext(filename)
	return os.path.join(
		'post_covers',
		'cover_image_{id}_{filename}{ext}'.format(
			id=post_obj.id,filename=filename.lower(),ext=ext
			))


# Post Model
class Post(models.Model):
    
    author = models.ForeignKey(to=User,
                               verbose_name='author',
                               related_name='posts',
                               blank=True,
                               null=False,
                               on_delete=models.CASCADE)
    
    title = models.CharField(max_length=150,
                             verbose_name="post title",
                             blank=False,
                             null=False)
    
    image  = models.ImageField(upload_to=post_cover_upload_dir,verbose_name="post image",max_length=255,blank=True,null=True)
    
    content = models.TextField(max_length=450,verbose_name="content",blank=False,null=False)
    
    published_date = models.DateTimeField(blank=True,null=True)
    
    board = models.ForeignKey(to = Board, verbose_name="post board",
                              on_delete=models.CASCADE,
                              blank=True,
                              null=False,
                              related_name="board_posts")
    
    viewers = models.PositiveIntegerField(verbose_name="viewers count",blank=True,null=True,default=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    modified_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "Blog Posts"
        verbose_name_plural = "Blog Posts"
        
    
    def __str__(self):
        return self.title
    

    @property
    def timesince_published(self):
        import humanize 
        
        timelapse = self.published_date.replace(tzinfo=None)
        return humanize.naturaltime(timelapse)