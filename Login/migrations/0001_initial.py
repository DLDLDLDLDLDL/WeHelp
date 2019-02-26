# Generated by Django 2.1.1 on 2018-12-19 14:51

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, unique=True, verbose_name='板块名称')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='板块描述')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False, verbose_name='收藏ID')),
                ('collection_time', models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionCompetition',
            fields=[
                ('collectioncompetition_id', models.AutoField(primary_key=True, serialize=False, verbose_name='收藏比赛ID')),
                ('collectioncompetition_time', models.DateTimeField(auto_now_add=True, verbose_name='比赛收藏时间')),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('competition_id', models.AutoField(primary_key=True, serialize=False)),
                ('competition_poster', models.ImageField(upload_to='competition_img', verbose_name='大赛海报')),
                ('competition_title', models.CharField(default='', max_length=50, verbose_name='大赛主题')),
                ('competition_description', models.CharField(max_length=200, verbose_name='大赛简介')),
                ('competition_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('competition_colletion_times', models.IntegerField(blank=True, default=0, verbose_name='收藏次数')),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')], max_length=30, verbose_name='验证码类型')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('good_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品ID')),
                ('good_portrait', models.ImageField(default='avatar/default.png', upload_to='good_img', verbose_name='商品图片')),
                ('good_name', models.CharField(default='', max_length=20, verbose_name='商品名称')),
                ('good_prize', models.FloatField(max_length=128, verbose_name='价格')),
                ('good_description', models.CharField(blank=True, max_length=256, verbose_name='描述')),
                ('good_time', models.DateTimeField(auto_now_add=True, verbose_name='发出时间')),
                ('fav', models.IntegerField(blank=True, default=0, verbose_name='收藏总次数')),
                ('car', models.IntegerField(blank=True, default=0, verbose_name='加入购物车总次数')),
            ],
        ),
        migrations.CreateModel(
            name='GoodCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_car_time', models.DateTimeField(auto_now_add=True, verbose_name='加入购物车时间')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Good', verbose_name='购物车的商品')),
            ],
            options={
                'verbose_name': 'Pie',
                'verbose_name_plural': '加入购物车',
                'ordering': ['add_car_time'],
            },
        ),
        migrations.CreateModel(
            name='GoodFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_time', models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Good', verbose_name='收藏的商品')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
                'ordering': ['favorite_time'],
            },
        ),
        migrations.CreateModel(
            name='GoodType',
            fields=[
                ('good_type_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品类型')),
                ('good_type_name', models.CharField(blank=True, choices=[('food', '食物'), ('cloth', '衣服'), ('furniture', '家具'), ('book', '书籍'), ('stationary', '文具'), ('others', '其他')], default='食物', max_length=20, null=True, verbose_name='商品类型')),
            ],
            options={
                'verbose_name': '商品类型',
                'ordering': ['good_type_id'],
            },
        ),
        migrations.CreateModel(
            name='MasterFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_time', models.DateTimeField(auto_now_add=True, verbose_name='关注时间')),
            ],
            options={
                'verbose_name': '关注',
                'verbose_name_plural': '关注',
                'ordering': ['fav_time'],
            },
        ),
        migrations.CreateModel(
            name='MasterLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_time', models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')),
            ],
            options={
                'verbose_name': '点赞',
                'verbose_name_plural': '点赞',
                'ordering': ['like_time'],
            },
        ),
        migrations.CreateModel(
            name='MasterType',
            fields=[
                ('master_type_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品类型')),
                ('master_type_name', models.CharField(blank=True, choices=[('delivery', '快递'), ('procurement', '代购'), ('print', '打印'), ('umbrella', '共享伞'), ('others', '其他')], default='delivery', max_length=20, null=True, verbose_name='接单类型')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.IntegerField(primary_key=True, serialize=False)),
                ('txtmessage', models.CharField(max_length=100, verbose_name='留言内容名字')),
                ('message_sender', models.CharField(max_length=100, verbose_name='留言发出者名字')),
                ('message_receiver', models.CharField(max_length=100, verbose_name='留言接收者名字')),
                ('message_receiver_ID', models.CharField(max_length=100, verbose_name='留言接收者ID')),
                ('message_sender_ID', models.CharField(max_length=100, verbose_name='留言发出者ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='留言时间')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='留言标题')),
                ('is_new', models.CharField(blank=True, choices=[('0', '未读'), ('1', '已读')], default='0', max_length=100, null=True, verbose_name='是都已阅')),
                ('is_marked_bysender', models.CharField(blank=True, choices=[('0', '未被发件者标记'), ('1', '已被发件人标记')], default='0', max_length=100, null=True, verbose_name='是否被发件者标注')),
                ('is_marked_byreceiver', models.CharField(blank=True, choices=[('0', '未被收件者标记'), ('1', '已被收件者标记')], default='0', max_length=100, null=True, verbose_name='是否被收件人标记')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('Notice_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='系统通知标题')),
                ('message_fromsystem', models.CharField(max_length=100, verbose_name='系统通知')),
                ('message_receiver', models.CharField(max_length=100, verbose_name='接收系统通知者名字')),
                ('is_new', models.CharField(blank=True, choices=[('0', '未读'), ('1', '已读')], default='0', max_length=100, null=True, verbose_name='是否已读')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='通知发出时间')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=4000, verbose_name='帖子内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='发帖时间')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=4000, verbose_name='举报内容')),
            ],
        ),
        migrations.CreateModel(
            name='suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='用户反馈标题')),
                ('suggestion', models.CharField(max_length=100, verbose_name='用户反馈')),
                ('sender', models.CharField(max_length=100, null=True, verbose_name='反馈者名字')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSend',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID')),
                ('task_category', models.CharField(blank=True, choices=[('delivery', '快递'), ('buy', '代购'), ('print', '打印'), ('umbrella', '共享伞'), ('others', '其他')], default='delivery', max_length=128, null=True, verbose_name='分类')),
                ('task_time', models.DateTimeField(max_length=128, null=True, verbose_name='任务时间')),
                ('task_place', models.CharField(max_length=128, verbose_name='任务地点')),
                ('task_reward', models.IntegerField(blank=True, verbose_name='报酬')),
                ('task_details', models.CharField(blank=True, max_length=128, verbose_name='详情')),
                ('task_send_time', models.DateTimeField(auto_now_add=True, verbose_name='订单发出时间')),
                ('task_img', models.ImageField(default='avatar/default.png', null=True, upload_to='task_img', verbose_name='发单图片')),
                ('task_state', models.CharField(blank=True, choices=[('0', '未接单'), ('1', '已接单')], default='0', max_length=128, null=True, verbose_name='是否被接')),
                ('send_collection_times', models.IntegerField(blank=True, default=0, verbose_name='被收藏次数')),
            ],
            options={
                'verbose_name': '发单表',
                'verbose_name_plural': '发单表',
                'ordering': ['task_send_time'],
            },
        ),
        migrations.CreateModel(
            name='TaskTake',
            fields=[
                ('task_take_id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID')),
                ('task_take_time', models.DateTimeField(auto_now_add=True, verbose_name='接单时间')),
                ('task_take_state', models.CharField(blank=True, choices=[('0', '已完成'), ('1', '未完成')], default='1', max_length=32, null=True, verbose_name='订单状态')),
                ('task_take_mark', models.FloatField(blank=True, max_length=128, null=True, verbose_name='订单评分')),
                ('task_send_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Login.TaskSend', verbose_name='发单表')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='主题名称')),
                ('last_updated', models.DateTimeField(auto_now_add=True, verbose_name='最近更新')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览数')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='Login.Board', verbose_name='所属板块名称')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('college', models.CharField(blank=True, max_length=64, verbose_name='学院')),
                ('major', models.CharField(blank=True, max_length=64, verbose_name='专业')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='邮箱')),
                ('qq_num', models.CharField(blank=True, max_length=64, verbose_name='QQ号')),
                ('avatar', models.ImageField(upload_to='avatar', verbose_name='头像')),
                ('final_remark', models.FloatField(blank=True, max_length=10, null=True, verbose_name='总评分')),
                ('task_take_num', models.IntegerField(blank=True, default=0, verbose_name='接单总次数')),
                ('alike', models.IntegerField(blank=True, default=0, verbose_name='点赞总次数')),
                ('attention', models.IntegerField(blank=True, default=0, verbose_name='关注总次数')),
                ('is_login', models.CharField(choices=[('0', '离线'), ('1', '在线')], default='0', max_length=128, verbose_name='')),
                ('become_master_datetime', models.DateTimeField(auto_now_add=True, verbose_name='成为达人时间')),
                ('master_take_delivery_times', models.IntegerField(blank=True, default=0, verbose_name='接快递总次数')),
                ('master_take_buy_times', models.IntegerField(blank=True, default=0, verbose_name='接代购总次数')),
                ('master_take_print_times', models.IntegerField(blank=True, default=0, verbose_name='接打印总次数')),
                ('master_take_umbrella_times', models.IntegerField(blank=True, default=0, verbose_name='接共享伞总次数')),
                ('master_take_others_times', models.IntegerField(blank=True, default=0, verbose_name='接其他单次数')),
                ('collection_delivery_times', models.IntegerField(blank=True, default=0, verbose_name='收藏取快递总次数')),
                ('collection_buy_times', models.IntegerField(blank=True, default=0, verbose_name='收藏代购总次数')),
                ('collection_print_times', models.IntegerField(blank=True, default=0, verbose_name='收藏代打印总次数')),
                ('collection_umbrella_times', models.IntegerField(blank=True, default=0, verbose_name='收藏共享伞总次数')),
                ('collection_others_times', models.IntegerField(blank=True, default=0, verbose_name='收藏其他任务总次数')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('master_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.MasterType', verbose_name='达人类型')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户资料',
                'verbose_name_plural': '用户资料',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='starter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL, verbose_name='发帖人'),
        ),
        migrations.AddField(
            model_name='tasktake',
            name='task_taker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='接单ID'),
        ),
        migrations.AddField(
            model_name='tasksend',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发出者'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL, verbose_name='举报人'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='Login.Topic', verbose_name='举报帖子'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='发帖人'),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='Login.Topic', verbose_name='帖子主题'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='帖子更新人'),
        ),
        migrations.AddField(
            model_name='masterlike',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='be_like', to=settings.AUTH_USER_MODEL, verbose_name='被赞者'),
        ),
        migrations.AddField(
            model_name='masterlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL, verbose_name='点赞用户'),
        ),
        migrations.AddField(
            model_name='masterfavorite',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='be_fav', to=settings.AUTH_USER_MODEL, verbose_name='被关注者'),
        ),
        migrations.AddField(
            model_name='masterfavorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav', to=settings.AUTH_USER_MODEL, verbose_name='粉丝'),
        ),
        migrations.AddField(
            model_name='goodfavorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏者'),
        ),
        migrations.AddField(
            model_name='goodcar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='加入者'),
        ),
        migrations.AddField(
            model_name='good',
            name='good_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.GoodType', verbose_name='商品分类'),
        ),
        migrations.AddField(
            model_name='good',
            name='good_sender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='卖家'),
        ),
        migrations.AddField(
            model_name='competition',
            name='competition_sender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collectioncompetition',
            name='collectioncompetition_collector_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏者'),
        ),
        migrations.AddField(
            model_name='collectioncompetition',
            name='collectioncompetition_thing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Competition', verbose_name='收藏的比赛'),
        ),
        migrations.AddField(
            model_name='collection',
            name='collection_collector_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏者'),
        ),
        migrations.AddField(
            model_name='collection',
            name='collection_thing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.TaskSend', verbose_name='收藏的商品'),
        ),
    ]
