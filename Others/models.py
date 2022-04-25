from django.db import models
from django.db.models.deletion import CASCADE
# from validators import validate_file_extension
from django.conf import settings


# Create your models here.

class ResourcesData(models.Model):
    resource_heading_name = models.CharField(max_length=100)
    resource_discription = models.CharField(max_length=5000)

    category_types = (
        ('Citizen', 'Citizen'),
        ('Developer', 'Developer'),
        ('Android', 'Android'),
        ('Translator', 'Translator'),
        ('Training', 'Training')
    )
    resource_category = models.CharField(
        choices=category_types, max_length=50, default="")
    resource_image = models.ImageField(
        upload_to='images/resources', height_field=None, width_field=None, max_length=None)
    resource_version_number = models.CharField(max_length=10)
    resource_file_size = models.CharField(max_length=30)
    resource_support_document_link = models.CharField(max_length=200)
    resource_upload_support_document = models.FileField(upload_to='supportDocument/', default=None)
    resource_upload_file = models.FileField(upload_to='Others/static/others/resource/', default=None)
    resource_download_link = models.CharField(max_length=200)
    resource_uploaded_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    resource_last_updated_date = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    resource_download_counter = models.IntegerField()

    class Meta:
        verbose_name_plural = "Resources Data"
        ordering = ['id']

    def __str__(self):
        return self.resource_heading_name



# TOOLSDATA TABLES MODEL

class ToolsData(models.Model):
    tool_heading_name = models.CharField(max_length=100)
    tool_discription = models.CharField(max_length=5000)

    category_types = (
        ('Citizen', 'Citizen'),
        ('Developer', 'Developer'),
        ('Android', 'Android'),
        ('Translator', 'Translator')
    )
    tool_category = models.CharField(
        choices=category_types, max_length=50, default="")
    tool_image = models.ImageField(
        upload_to='images/tools', height_field=None, width_field=None, max_length=None)
    tool_version_number = models.CharField(max_length=10)
    tool_file_size = models.CharField(max_length=30)
    tool_support_document_link = models.CharField(max_length=200)
    tool_upload_support_document = models.FileField(upload_to='supportDocument/', default=None)
    tool_upload_file = models.FileField(upload_to='Others/static/others/tool/', default=None)
    tool_download_link = models.CharField(max_length=200)
    tool_uploaded_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    tool_last_updated_date = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    tool_download_counter = models.IntegerField()

    class Meta:
        verbose_name_plural = "Tools Data"
        ordering = ['id']

    def __str__(self):
        return self.tool_heading_name


# CATEGORY TABLES MODEL

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Citizen', 'Citizen'),
        ('Android', 'Android'),
        ('Developer', 'Developer'),
        ('Translator', 'Translator'),
        ('Training', 'Training')
    ]

    category_name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    category_created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category_name


# SUCCESS STORIES CATEGORY TABLES MODEL

class SuccessStoriesCategory(models.Model):
    SUCCESSSTORIES_CATEGORY_CHOICES = [
        ('Startup Deployment', 'Startup Deployment'),
        ('Localisation Deployment', 'Localisation Deployment'),
        ('Proof of concept/Demo', 'Proof of concept/Demo'),
        ('Services Deployment', 'Services Deployment'),
        ('AP Success Stories', 'AP Success Stories'),
        ('Advanced Features', 'Advanced Features'),
        ('Archive', 'Archive'),
    ]

    success_stories_category_name = models.CharField(max_length=50, choices=SUCCESSSTORIES_CATEGORY_CHOICES)
    success_stories_category_created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "SuccessStoriesCategory"
        ordering = ['success_stories_category_name']

    def __str__(self):
        return self.success_stories_category_name


# SERVICES TABLES MODEL

class Services(models.Model):
    service_name = models.CharField(max_length=50)
    service_description = models.CharField(max_length=10000, default="")

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.service_name


# UPCOMING NEWS TABLE MODEL

class UpcomingNewsAndEvents(models.Model):
    upcomingnews_heading = models.CharField(max_length=500)
    upcomingnews_link = models.URLField(max_length=200)
    upcomingupdated_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "UpcomingNewsAndEvents"

    def __str__(self):
        return self.upcomingnews_heading


# FAQ TABLES MODEL

class Faq(models.Model):
    faq_question = models.CharField(max_length=10000)
    faq_answer = models.CharField(max_length=10000)

    class Meta:
        verbose_name_plural = "Faq"

    def __str__(self):
        return self.faq_question


# ARTICLES TABLES MODELS


class Articles(models.Model):
    article_heading_name = models.CharField(max_length=100)
    article_discription = models.TextField(max_length=10000)
    article_images = models.ImageField(
        upload_to='Others/static/others/images/', height_field=None, width_field=None, max_length=None)
    article_created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    article_last_updated_date = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    article_author_name = models.CharField(max_length=100, null=True)
    article_published_status = models.BooleanField(default="")
    article_published_date = models.DateTimeField(
        auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.article_heading_name


# USER_REGISTRATION TABLES MODEL


class UserRegistration(models.Model):
    userregistration_user_id = models.AutoField(primary_key=True)
    userregistration_first_name = models.CharField(max_length=60)
    userregistration_middle_name = models.CharField(max_length=60)
    userregistration_last_name = models.CharField(max_length=60)
    userregistration_email_field = models.EmailField(
        unique=True, max_length=30)
    userregistration_mobile_no = models.IntegerField()
    userregistration_password = models.CharField(max_length=30)
    userregistration_confirm_password = models.CharField(max_length=30)
    userregistration_active_status = models.BooleanField(default=False)
    userregistration_registration_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "UserRegistration"

    def __str__(self):
        return self.userregistration_first_name + " " + self.userregistration_last_name


# COUNTRY TABLES MODEL


class Country(models.Model):
    country_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Country"

    def __str__(self):
        return self.country_name


# STATES TABLES MODEL

class States(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=96)
    state_abbr = models.CharField(max_length=24, blank=True)

    class Meta:
        verbose_name_plural = "States"

    def __str__(self):
        return self.state_name


# CITY TABLES MODEL


class City(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=96)
    city_abbr = models.CharField(max_length=24, blank=True)

    class Meta:
        verbose_name_plural = "City"

    def __str__(self):
        return self.city_name


# USER_PROFILE TABLES MODEL


# class UserProfile(models.Model):

#     userprofile_country = models.ForeignKey(
#         Country, on_delete=models.SET_NULL, null=True)
#     userprofile_state = models.ForeignKey(
#         States, on_delete=models.SET_NULL, null=True)
#     userprofile_city = models.ForeignKey(
#         City, on_delete=models.SET_NULL, null=True)
#     userprofile_uid = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     userprofile_date_of_birth = models.DateTimeField(
#         auto_now_add=True, null=True, blank=True)
#     gender_choices = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Others'),
#     )
#     userprofile_gender = models.CharField(
#         choices=gender_choices, max_length=10)
#     userprofile_address = models.CharField(max_length=100)
#     userprofile_nationality = models.CharField(max_length=30)
#     userprofile_pincode = models.IntegerField()
#     identity_proof_choices = (
#         ('Pancard', 'PANCARD'),
#         ('Aadhar Card', 'AADHAR CARD'),
#         ('Other', 'OTHER'),
#     )
#     userprofile_identity_proof = models.CharField(
#         choices=identity_proof_choices, max_length=50)
#     userprofile_identity_proof_number = models.CharField(max_length=25)

#     qualification_choices = (
#         ('UG', 'undergraduate'),
#         ('G', 'graduate'),
#         ('PG', 'postgraduate'),
#         ('PHD', 'Doctor of Philosophy'),
#     )
#     userprofile_qualifications = models.CharField(
#         choices=qualification_choices, max_length=300)
#     domain_expert_choices = (
#         ('LE', 'language expert'),
#         ('VE', 'validation expert'),
#         ('TE', 'technical expert'),
#         ('TE', 'translation expert'),
#     )
#     userprofile_domain_expert = models.CharField(
#         choices=domain_expert_choices, max_length=50)
#     userprofile_image = models.ImageField(
#         upload_to='images/userprofileimages', height_field=None, width_field=None, max_length=None)

#     class Meta:
#         verbose_name_plural = "UserProfile"

#     def __str__(self):
#         return self.userprofile_uid.userregistration_user_id + " " + self.userprofile_uid.userregistration_email_field


# BLOGS TABLES MODEL


class Blogs(models.Model):
    blogs_author_name = models.CharField(max_length=100)
    blogs_heading = models.CharField(max_length=200)
    blogs_content = models.CharField(max_length=3000)
    blogs_created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    blogs_images = models.ImageField(
       upload_to='Others/static/others/blogs/', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.blogs_heading


# FEEDBACK TABLES MODEL


class Feedback(models.Model):
    feedback_uid = models.ForeignKey(
        UserRegistration, on_delete=models.SET_NULL, null=True)
    feedback_description_text = models.CharField(max_length=20000)
    feedback_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.feedback_uid


# MediaAndPresskit TABLES MODEL


class MediaAndPresskit(models.Model):
    mediaandpresskit_media_heading = models.CharField(max_length=100)
    mediaandpresskit_media_images = models.FileField(blank=True)
    mediaandpresskit_videos = models.FileField(blank=True)
    mediaandpresskit_media_description = models.CharField(max_length=3000)
    mediaandpresskit_media_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MediaAndPresskit"

    def __str__(self):
        return self.media_heading


class MediaImagesAndVideo(models.Model):
    mediaimagesandvideo_mediaandpress = models.ForeignKey(
        MediaAndPresskit, default=None, on_delete=models.CASCADE)
    mediaimagesandvideo_images = models.FileField(upload_to='images/')
    mediaimagesandvideo_videos = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name_plural = "MediaImagesAndVideo"

    def __str__(self):
        return self.mediaimagesandvideo_mediaandpress.mediaandpresskit_media_heading


class Bookmarks(models.Model):
    bookmarks_tools = models.ForeignKey(
        ToolsData, on_delete=CASCADE, null=True)
    bookmarks_uid = models.ForeignKey(
        UserRegistration, on_delete=CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Bookmarks"

    def __str__(self):
        return self.bookmarks_tools.tool_heading_name

class NewsEvents(models.Model):
    
    news_events_detail = models.CharField(max_length=100)
    news_events_link   = models.URLField(max_length=300)

    class Meta:
        verbose_name_plural = "NewsEvents"
    
    def __str__(self):
        return self.news_events_detail


# SUCCESS STORIES MODEL

class SuccessStories(models.Model):
    success_stories_heading_name = models.CharField(max_length=100)
    
    SUCCESSSTORIES_CATEGORY_TYPES = [
        ('Startup Deployment', 'Startup Deployment'),
        ('Localisation Deployment', 'Localisation Deployment'),
        ('Proof of concept/Demo', 'Proof of concept/Demo'),
        ('Services Deployment', 'Services Deployment'),
        ('AP Success Stories', 'AP Success Stories'),
        ('Advanced Features', 'Advanced Features'),
        ('Archive', 'Archive'),
    ]

    success_stories_category = models.CharField(
        choices=SUCCESSSTORIES_CATEGORY_TYPES, max_length=50, default="")


    success_stories_link = models.URLField(max_length=200)
    success_stories_discription = models.TextField(max_length=10000)
    success_stories_uploadimages = models.ImageField(
        upload_to='Others/static/others/success_stories_images/', height_field=None, width_field=None, max_length=None)
    success_stories_imagelink = models.CharField(max_length=200)    
    success_stories_created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    success_stories_last_updated_date = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    success_stories_published_status = models.BooleanField(default="")
    success_stories_published_date = models.DateTimeField(
        auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "SuccessStories"

    def __str__(self):
        return self.success_stories_heading_name


