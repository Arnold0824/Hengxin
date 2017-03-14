from django.db import models

# Create your models here.
class carousel(models.Model):

    """
    轮播.
    """
    title = models.CharField('标题', max_length=50)
    img = models.CharField('图片（1920*600）',max_length=50)
    link = models.CharField('链接地址（可为空）', max_length=50, blank=True)
    caption = models.CharField('子标题', max_length=500, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = '轮播管理'
        ordering = ['-dimDate'] # sorted news by dimdate

class article(models.Model):
    title = models.CharField('文章标题', max_length=50)
    coverImg = models.CharField('封面图片的地址',max_length=50, blank=True, null=True)
    content = models.TextField('文章详情')
    innerImgs = models.CharField('图片们的地址',max_length=1000, blank=True, null=True )
    viewedTimes = models.IntegerField('浏览次数')
    type=models.CharField('文章类型',max_length=50,blank=True,null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        ordering = ['-dimDate'] # sorted news by dimdate