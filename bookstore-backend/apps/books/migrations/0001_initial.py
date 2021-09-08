# Generated by Django 2.2.15 on 2020-08-11 09:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='书籍名称', max_length=100, verbose_name='书籍名称')),
                ('author', models.CharField(help_text='作者', max_length=30, verbose_name='作者')),
                ('price', models.FloatField(default=0, help_text='市场价格', verbose_name='价格')),
                ('discount', models.FloatField(default=1, help_text='折扣', verbose_name='折扣')),
                ('imgUrl', models.ImageField(blank=True, help_text='图片', null=True, upload_to='books/images/', verbose_name='图片')),
                ('bigImgUrl', models.ImageField(blank=True, help_text='大图', null=True, upload_to='books/images/big/', verbose_name='大图')),
                ('bookConcern', models.CharField(help_text='出版社', max_length=100, verbose_name='出版社')),
                ('publishDate', models.DateField(blank=True, help_text='出版日期', null=True, verbose_name='出版日期')),
                ('brief', models.CharField(blank=True, help_text='简介', max_length=200, null=True, verbose_name='简介')),
                ('inventory', models.IntegerField(default=0, help_text='库存', verbose_name='库存')),
                ('detail', models.TextField(blank=True, default='', help_text='详情', null=True, verbose_name='详情')),
                ('newness', models.BooleanField(default=False, help_text='是否新品', verbose_name='是否新品')),
                ('hot', models.BooleanField(default=False, help_text='是否热销', verbose_name='是否热销')),
                ('specialOffer', models.BooleanField(default=False, help_text='特别优惠', verbose_name='特别优惠')),
                ('slogan', models.CharField(blank=True, help_text='标语', max_length=200, null=True, verbose_name='标语')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名称')),
                ('root', models.BooleanField(default=True, help_text='是否为根分类', verbose_name='是否为根分类')),
            ],
            options={
                'verbose_name': '图书分类',
                'verbose_name_plural': '图书分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', help_text='评论内容', verbose_name='评论内容')),
                ('commentDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books', verbose_name='图书外键')),
            ],
            options={
                'verbose_name': '图书评论',
                'verbose_name_plural': '图书评论',
            },
        ),
    ]