from django.db import models

from OrangeMall.utils import create_fingerprint
from apps.home.models import Goods

active_choice = (
    (False, "未激活"),
    (True, "已激活"),
)
sex_choice = (
    (1, "男"),
    (2, "女")
)
vip_choice = (
    (0, "普通会员"),
    (1, "黄金会员"),
    (2, "钻石会员"),
    (3, "铂金会员"),
)

default_choice = (
    (True, "默认地址"),
    (False, "非默认地址")
)

order_status_choice = (
    (0, "订单未付款"),
    (1, "订单已完成"),
    (2, "订单待收货"),
)

coupon_status_choice = (
    (1, "未使用"),
    (2, "已使用"),
)

message_status_choice = (
    (True, "已读"),
    (False, "未读")
)

card_type_choice = (
    (1, "农行储蓄卡"),
    (2, "工行信用卡"),
)


class Member(models.Model):
    member_id = models.AutoField("用户编号", primary_key=True)
    email = models.CharField("邮箱", max_length=50)
    nickname = models.CharField("昵称", max_length=100, blank=True)
    login_password = models.CharField("密码", max_length=50)
    phone = models.CharField("手机号", max_length=20, blank=True)
    is_active = models.BooleanField("激活状态", default=False, )
    is_delete = models.BooleanField(default=False)

    def make_password(self, password):
        self.login_password = create_fingerprint(password)

    def verify_password(self, password):
        """
        验证密码
        :param password:
        :return: 密码正确返回True  错误返回False
        """
        if create_fingerprint(password) == self.login_password:
            return True

    def __str__(self):
        return self.nickname if self.nickname else self.email

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        db_table = "member"


class MemberInfo(models.Model):
    info_id = models.AutoField("用户信息编号", primary_key=True)
    real_name = models.CharField("真是姓名", max_length=100, blank=True)
    member_id = models.ForeignKey(Member, verbose_name="关联用户编号",db_column="member_id")
    sex = models.IntegerField("性别", default=0, choices=sex_choice, blank=True)
    birthday = models.DateTimeField("生日", blank=True, auto_now_add=True)
    member_img = models.ImageField("用户头像", upload_to="upload/member/", blank=True)
    pay_password = models.CharField(max_length=50)
    balance = models.DecimalField("余额", max_digits=7, decimal_places=2, default=0, blank=True)
    points = models.IntegerField("积分", default=0, blank=True)
    is_vip = models.IntegerField("会员等级", default=0, choices=vip_choice)
    update_date = models.DateTimeField(auto_created=True)

    def make_password(self, password):
        self.pay_password = create_fingerprint(password)

    def verify_password(self, password):
        """
        验证密码
        :param password:
        :return: 密码正确返回True  错误返回False
        """
        if create_fingerprint(password) == self.pay_password:
            return True

    def img_show(self):
        """
        后台显示图片
        :return:
        """
        return u'<img width=50px src="%s" />' % self.member_img.url

    img_show.short_description = '商品图片'
    # 允许显示HTML tag
    img_show.allow_tags = True

    class Meta:
        verbose_name = "用户资料"
        verbose_name_plural = verbose_name
        db_table = "member_info"


class MemberLoc(models.Model):
    loc_id = models.AutoField("地址编号", primary_key=True)
    member_id = models.ForeignKey(Member, verbose_name="关联用户编号",db_column="member_id")
    province = models.CharField("省份", max_length=200)
    city = models.CharField("城市", max_length=200)
    detail_loc = models.TextField("地址详情")
    is_default = models.BooleanField("默认地址", default=True, choices=default_choice, blank=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "用户地址"
        verbose_name_plural = verbose_name
        db_table = "member_loc"


class Review(models.Model):
    review_id = models.AutoField("评论编号", primary_key=True)
    member_id = models.ForeignKey(Member, verbose_name="关联用户编号",db_column="member_id")
    goods_id = models.ForeignKey(Goods, verbose_name="关联商品编号",db_column="goods_id")
    conten = models.TextField("用户详情")
    image = models.ImageField("图片", upload_to="media/review/")
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

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
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        db_table = "review"


# 订单编号按照时间戳+用户ID+随机数
class Order(models.Model):
    order_id = models.CharField("订单编号", max_length=100, primary_key=True)
    member_id = models.ForeignKey(Member, verbose_name="关联用户编号",db_column="member_id")
    goods_id = models.ForeignKey(Goods, verbose_name="关联商品编号",db_column="goods_id")
    count = models.IntegerField("数量")
    status = models.IntegerField("订单状态", choices=order_status_choice)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name
        db_table = "order"


class ShopCar(models.Model):
    car_id = models.AutoField("购物车编号", primary_key=True)
    member_id = models.ForeignKey(Member, verbose_name="关联用户编号",db_column="member_id")
    goods_id = models.ForeignKey(Goods, verbose_name="关联商品编号",db_column="goods_id")
    count = models.IntegerField("数量")
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        db_table = "shop_car"


class Coupon(models.Model):
    coupon_id = models.AutoField("优惠券编号", primary_key=True)
    member_id = models.ForeignKey(Member, verbose_name="关联用户编号",db_column="member_id")
    value = models.DecimalField("金额", max_digits=7, decimal_places=2)
    begin_date = models.DateTimeField("开始时间")
    invalid_date = models.DateTimeField("失效时间")
    status = models.IntegerField("状态", choices=coupon_status_choice)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "优惠券"
        verbose_name_plural = verbose_name
        db_table = "coupon"


class Collection(models.Model):
    collection_id = models.AutoField("收藏编号", primary_key=True)
    member_id = models.ForeignKey(Member, verbose_name="关联用户编号",db_column="member_id")
    goods_id = models.ForeignKey(Goods, verbose_name="关联商品编号",db_column="goods_id")
    create_date = models.DateTimeField("收藏时间", auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "收藏"
        verbose_name_plural = verbose_name
        db_table = "collection"


class Message(models.Model):
    message_id = models.AutoField("消息编号", primary_key=True)
    sender_id = models.IntegerField(verbose_name="发件人编号")
    receiver_id = models.IntegerField(verbose_name="收件人编号")
    message_title = models.CharField("标题", max_length=100)
    message_img = models.ImageField("图片", upload_to="media/msg/")
    message_content = models.TextField("内容", blank=True)
    status = models.BooleanField(default=False, choices=message_status_choice)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def img_show(self):
        """
        后台显示图片
        :return:
        """
        return u'<img width=50px src="%s" />' % self.message_img.url

    img_show.short_description = '商品图片'
    # 允许显示HTML tag
    img_show.allow_tags = True

    class Meta:
        verbose_name = "消息"
        verbose_name_plural = verbose_name
        db_table = "message"


class BankCard(models.Model):
    card_id = models.AutoField("银行卡编号", primary_key=True)
    member_id = models.ForeignKey(Member, verbose_name="关联用户编号",db_column="member_id")
    card_num = models.CharField("银行卡号", max_length=30)
    card_type = models.IntegerField("类型", choices=card_type_choice)
    create_data = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "银行卡"
        verbose_name_plural = verbose_name
        db_table = "bank_card"
