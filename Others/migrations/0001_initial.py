# Generated by Django 3.2.9 on 2021-12-16 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_heading_name', models.CharField(max_length=100)),
                ('article_discription', models.TextField(max_length=10000)),
                ('article_images', models.ImageField(upload_to='Others/static/others/images/')),
                ('article_created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('article_last_updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('article_author_name', models.CharField(max_length=100, null=True)),
                ('article_published_status', models.BooleanField(default='')),
                ('article_published_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogs_author_name', models.CharField(max_length=100)),
                ('blogs_heading', models.CharField(max_length=200)),
                ('blogs_content', models.CharField(max_length=3000)),
                ('blogs_created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('blogs_images', models.ImageField(upload_to='images/blogs')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=96)),
                ('city_abbr', models.CharField(blank=True, max_length=24)),
            ],
            options={
                'verbose_name_plural': 'City',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_question', models.CharField(max_length=10000)),
                ('faq_answer', models.CharField(max_length=10000)),
            ],
            options={
                'verbose_name_plural': 'Faq',
            },
        ),
        migrations.CreateModel(
            name='MediaAndPresskit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaandpresskit_media_heading', models.CharField(max_length=100)),
                ('mediaandpresskit_media_images', models.FileField(blank=True, upload_to='')),
                ('mediaandpresskit_videos', models.FileField(blank=True, upload_to='')),
                ('mediaandpresskit_media_description', models.CharField(max_length=3000)),
                ('mediaandpresskit_media_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'MediaAndPresskit',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_description', models.CharField(default='', max_length=10000)),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=96)),
                ('state_abbr', models.CharField(blank=True, max_length=24)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Others.country')),
            ],
            options={
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='ToolsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_heading_name', models.CharField(max_length=100)),
                ('tool_discription', models.CharField(max_length=5000)),
                ('tool_category', models.CharField(choices=[('Citizen', 'Citizen'), ('Developer', 'Developer'), ('Android', 'Android'), ('Translator', 'Translator')], default='', max_length=50)),
                ('tool_image', models.ImageField(upload_to='images/tools')),
                ('tool_version_number', models.CharField(max_length=10)),
                ('tool_file_size', models.CharField(max_length=30)),
                ('tool_support_document_link', models.CharField(max_length=200)),
                ('tool_download_link', models.CharField(max_length=200)),
                ('tool_uploaded_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('tool_last_updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('tool_download_counter', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Tools Data',
            },
        ),
        migrations.CreateModel(
            name='UpcomingNewsAndEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upcomingnews_heading', models.CharField(max_length=500)),
                ('upcomingnews_link', models.URLField()),
                ('upcomingupdated_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'UpcomingNewsAndEvents',
            },
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('userregistration_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('userregistration_first_name', models.CharField(max_length=60)),
                ('userregistration_middle_name', models.CharField(max_length=60)),
                ('userregistration_last_name', models.CharField(max_length=60)),
                ('userregistration_email_field', models.EmailField(max_length=30, unique=True)),
                ('userregistration_mobile_no', models.IntegerField()),
                ('userregistration_password', models.CharField(max_length=30)),
                ('userregistration_confirm_password', models.CharField(max_length=30)),
                ('userregistration_active_status', models.BooleanField(default=False)),
                ('userregistration_registration_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'UserRegistration',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userprofile_date_of_birth', models.DateTimeField(auto_now_add=True, null=True)),
                ('userprofile_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=10)),
                ('userprofile_address', models.CharField(max_length=100)),
                ('userprofile_nationality', models.CharField(max_length=30)),
                ('userprofile_pincode', models.IntegerField()),
                ('userprofile_identity_proof', models.CharField(choices=[('Pancard', 'PANCARD'), ('Aadhar Card', 'AADHAR CARD'), ('Other', 'OTHER')], max_length=50)),
                ('userprofile_identity_proof_number', models.CharField(max_length=25)),
                ('userprofile_qualifications', models.CharField(choices=[('UG', 'undergraduate'), ('G', 'graduate'), ('PG', 'postgraduate'), ('PHD', 'Doctor of Philosophy')], max_length=300)),
                ('userprofile_domain_expert', models.CharField(choices=[('LE', 'language expert'), ('VE', 'validation expert'), ('TE', 'technical expert'), ('TE', 'translation expert')], max_length=50)),
                ('userprofile_image', models.ImageField(upload_to='images/userprofileimages')),
                ('userprofile_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Others.city')),
                ('userprofile_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Others.country')),
                ('userprofile_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Others.states')),
            ],
            options={
                'verbose_name_plural': 'UserProfile',
            },
        ),
        migrations.CreateModel(
            name='MediaImagesAndVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaimagesandvideo_images', models.FileField(upload_to='images/')),
                ('mediaimagesandvideo_videos', models.FileField(upload_to='videos/')),
                ('mediaimagesandvideo_mediaandpress', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Others.mediaandpresskit')),
            ],
            options={
                'verbose_name_plural': 'MediaImagesAndVideo',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_description_text', models.CharField(max_length=20000)),
                ('feedback_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('feedback_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Others.userregistration')),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Others.states'),
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmarks_tools', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Others.toolsdata')),
                ('bookmarks_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Others.userregistration')),
            ],
            options={
                'verbose_name_plural': 'Bookmarks',
            },
        ),
    ]
