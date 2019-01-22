from django.db import models

# Create your models here.
level_choice = (
    (1, "一级分类菜单"),
    (2, "二级分类菜单"),
    (3, "二级分类菜单")
)

state_choice = (
    (0, "已下架"),
    (1, "上架中"),
    (2, "限时促销")
)


class Category(models.Model):
    cate_id = models.AutoField(primary_key=True, verbose_name="编号")
    name = models.CharField("名称", max_length=100)
    parent_id = models.IntegerField("上一级分类id")
    level = models.IntegerField("类别", choices=level_choice)
    create_date = models.DateTimeField("创建时间", auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = verbose_name
        db_table = "category"

    def __str__(self):
        return self.name


class Goods(models.Model):
    goods_id = models.AutoField("编号", primary_key=True)
    cate_id = models.ForeignKey(Category, verbose_name="关联分类编号", db_column='cate_id')
    creator_name = models.CharField("商家名称", max_length=200)
    goods_name = models.CharField("商品名称", max_length=200)
    brand_name = models.CharField("品牌名称 ", max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.goods_name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name
        db_table = "goods"


class GoodsDetail(models.Model):
    detail_id = models.AutoField("编号", primary_key=True)
    goods_id = models.ForeignKey(Goods, verbose_name="关联商品编号", db_column="cate_id")
    sale_state = models.IntegerField("上架状态", choices=state_choice)
    goods_params = models.TextField("商品参数")
    title = models.CharField("标题", max_length=200)
    image = models.ImageField("图片", max_length=100, upload_to="upload/goods/", blank=True)
    is_delete = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def img_show(self):
        """
        后台显示图片
        :return:
        """
        return u'<img width=50px src="%s" />' % self.image.url

    img_show.short_description = '商品图片'
    # 允许显示HTML tag
    img_show.allow_tags = True

    class Meta:
        verbose_name = "商品详情"
        verbose_name_plural = verbose_name
        db_table = "goods_detail"


class GoodsSpu(models.Model):
    spu_id = models.AutoField("规格编号",primary_key=True)
    goods_id = models.ForeignKey(Goods,verbose_name="关联商品编号",db_column="goods_id")
    goods_specs = models.TextField("商品选择参数")
    stock = models.CharField("库存",max_length=100)
    goods_price = models.CharField("商品价格",max_length=100)
    origin_price = models.CharField("商品原价",max_length=100,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "商品详情"
        verbose_name_plural = verbose_name
        db_table = "goods_spu"

