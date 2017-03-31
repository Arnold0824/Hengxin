from django.db import models
class picture(models.Model):
    title = models.CharField('标题', max_length=20)
    caption = models.CharField('内容', max_length=34, blank=True, null=True)
    filepath = models.CharField('文件地址', max_length=200, blank=True, null=True)  # 头像路径
    dimDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = "图片库"
        ordering = ['id']

    def __str__(self):
        return self.title
# Create your models here.
class carousel(models.Model):

    """
    轮播.
    """
    title = models.CharField('标题', max_length=50)
    imgs = models.ManyToManyField(picture)
    link = models.CharField('链接地址（可为空）', max_length=50, blank=True)
    caption = models.CharField('子标题', max_length=500, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播管理'
        ordering = ['-dimDate'] # sorted news by dimdate


class article(models.Model):
    '''
    文章
    '''
    title = models.CharField('文章标题', max_length=50)
    imgs = models.ForeignKey(picture, to_field='id', null=True)
    content = models.TextField('文章详情')
    viewedTimes = models.IntegerField('浏览次数')
    type = models.CharField('文章类型',max_length=50,blank=True,null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        ordering = ['-dimDate'] # sorted news by dimdate


class user(models.Model):
    username = models.CharField('登录名', max_length=20, blank=True, null=False,unique=True)  # 登录名、昵称，唯一校验
    pwd = models.CharField('密码', max_length=34, blank=True, null=True)
    avt = models.ForeignKey(picture,to_field='id',null=True)
    salt=models.CharField('密码盐值',max_length=32,blank=True,null=True)
    type = models.CharField('用户类型', max_length=32, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "用户资料表"
        verbose_name_plural = "users"
        ordering = ['id']

    def __str__(self):
        return self.username
