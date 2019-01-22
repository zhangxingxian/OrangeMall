from django.shortcuts import render, redirect
from django.http import HttpResponse

def cart_add(request):
    return render(request, 'cart/shopcart.html')









from alipay import AliPay
from OrangeMall import settings
def pay(request):
    alipay = AliPay(
        appid=settings.AAP_ID,
        app_notify_url=None,
        app_private_key_string=settings.APP_PRIVATE_STRING,
        alipay_public_key_string= settings.APP_PUBLIC_STRING,
        # 坑点1
        sign_type="RSA2",
        debug= True
    )
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单号
        out_trade_no='123456',
        # 商品总价
        total_amount='0.01',  # 将Decimal类型转换为字符串交给支付宝
        # 订单标题
        subject="悦桔商城-{}".format(9527),
        # 支付成功之后 前端跳转的界面
        return_url='https://baidu.com/',
        # 支付成功后台跳转接口
        notify_url=None  # 可选, 不填则使用默认notify url
    )
    # 让用户进行支付的支付宝页面网址
    url = settings.ALI_PAY_URL + "?" + order_string
    # 坑点2 路由设置不要设置为主页
    return redirect(url)