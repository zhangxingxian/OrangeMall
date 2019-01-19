# OrangeMall
悦桔商城,基于Django1.11开发的电商平台.

## 依赖环境
> 见项目目录下requirements.txt文件  
其中xadmin与twisted在文件夹installation_package中


## apps
1. account
> 用户模块:  
    + 自定义Member类(实现密码加码,验证,以及记住状态功能)
    + 用户登录与注册(在Templates中的account文件夹中)  
    + 用户个人中心(在Templates中的person文件夹中)  
    + 用户地址管理  
    + 用户信息修改  
    + 购物车查看  
    + ......  
    
2. cart
> 购物车模块 :  
    + 购物车添加  
    + 订单生成  
    + 支付接入  
  
3. comment
> 评论

4. detail
> 商品详情页 :   
    + 商品详情信息  
    + 商品分类展示  
    + 分页功能  
    
5. home
> 首页 : 
    + 分级菜单  
    + 新闻显示  
    + 商品显示  
    
6. tools 
> 爬虫模块

7. xadmin
>后台管理系统  
使用auth模块中的user



模板中的css和js文件的目录需要,根据相应的路径进行修改   
后续使用模块可自行添加,如有余力可以添加全文检索功能