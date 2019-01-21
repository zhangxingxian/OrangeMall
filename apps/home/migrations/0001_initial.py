# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('parent_id', models.IntegerField(verbose_name='上一级分类id')),
                ('level', models.IntegerField(choices=[(1, '一级分类菜单'), (2, '二级分类菜单'), (3, '二级分类菜单')], verbose_name='类别')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('creator_name', models.CharField(max_length=200, verbose_name='商家名称')),
                ('goods_name', models.CharField(max_length=200, verbose_name='商品名称')),
                ('band_name', models.CharField(max_length=200, verbose_name='品牌名称 ')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cate_id', models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.CASCADE, to='home.Category', verbose_name='关联分类编号')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('sale_state', models.IntegerField(choices=[(0, '已下架'), (1, '上架中'), (2, '限时促销')], verbose_name='上架状态')),
                ('desc', models.TextField(verbose_name='详情')),
                ('goods_params', models.TextField(verbose_name='商品参数')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('image', models.ImageField(blank=True, upload_to='upload/goods/', verbose_name='图片')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('goods_id', models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.CASCADE, to='home.Goods', verbose_name='关联商品编号')),
            ],
            options={
                'verbose_name': '商品详情',
                'verbose_name_plural': '商品详情',
                'db_table': 'goods_detail',
            },
        ),
        migrations.CreateModel(
            name='GoodsSpu',
            fields=[
                ('spu_id', models.AutoField(primary_key=True, serialize=False, verbose_name='规格编号')),
                ('goods_specs', models.TextField(verbose_name='商品选择参数')),
                ('stock', models.CharField(max_length=100, verbose_name='库存')),
                ('goods_price', models.CharField(max_length=100, verbose_name='商品价格')),
                ('origin_price', models.CharField(blank=True, max_length=100, verbose_name='商品原价')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Goods', verbose_name='关联商品编号')),
            ],
            options={
                'verbose_name': '商品详情',
                'verbose_name_plural': '商品详情',
                'db_table': 'goods_spu',
            },
        ),
    ]