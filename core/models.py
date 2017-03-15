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
class USER(models.Model):
    username = models.CharField('登录名', max_length=20, blank=True, null=False,unique=True)  # 登录名、昵称，唯一校验
    pwd = models.CharField('密码', max_length=34, blank=True, null=True)
    avt = models.CharField('头像', max_length=200, blank=True, null=True)  # 头像路径
    salt=models.CharField('密码盐值',max_length=32,blank=True,null=True)
    dimDate = models.DateTimeField(auto_created=True)

    class Meta:
        verbose_name = "用户资料表"
        verbose_name_plural = "users"
        ordering = ['id']

    def __str__(self):
        return self.username