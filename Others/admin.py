from django.contrib import admin
from . import models
from .models import MediaImagesAndVideo, MediaAndPresskit
# Register your models here.


class MediaImagesAndVideoAdmin(admin.StackedInline):
    model = MediaImagesAndVideo


@admin.register(MediaAndPresskit)
class MediaAndPresskitAdmin(admin.ModelAdmin):
    inlines = [MediaImagesAndVideoAdmin]

    class Meta:
        model = MediaAndPresskit


@admin.register(MediaImagesAndVideo)
class MediaImagesAndVideoAdmin(admin.ModelAdmin):
    pass

class SuccessStoriesAdmin(admin.ModelAdmin):
    list_display = ('success_stories_heading_name','success_stories_discription','success_stories_created_date','success_stories_last_updated_date','success_stories_published_status','success_stories_published_date')
    search_fields = ['success_stories_heading_name','success_stories_discription','success_stories_created_date','success_stories_last_updated_date','success_stories_published_status','success_stories_published_date']
    ordering = ['success_stories_heading_name','success_stories_discription','success_stories_created_date','success_stories_last_updated_date','success_stories_published_status','success_stories_published_date']
    list_filter = ['success_stories_heading_name','success_stories_created_date','success_stories_last_updated_date','success_stories_published_status','success_stories_published_date']


class SuccessStoriesCategoryAdmin(admin.ModelAdmin):
    list_display= ('success_stories_category_name','success_stories_category_created_date')
    search_fields = ['success_stories_category_name', 'success_stories_category_created_date']
    ordering = ['success_stories_category_created_date']
    list_filter = ['success_stories_category_name', 'success_stories_category_created_date'] 

class NewsEventsAdmin(admin.ModelAdmin):
    list_display = ('news_events_detail','news_events_link')
    search_fields = ['news_events_detail','news_events_link']
    ordering = ['news_events_detail','news_events_link']
    list_filter = ['news_events_detail','news_events_link']


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('blogs_author_name','blogs_heading','blogs_created_date')
    search_dields = ['blogs_author_name','blogs_heading','blogs_created_date']
    ordering = ['blogs_author_name','blogs_heading','blogs_created_date']
    list_filter = ['blogs_author_name','blogs_heading','blogs_created_date']

class ResourcesDataAdmin(admin.ModelAdmin):
    list_display = ('resource_heading_name', 'resource_discription', 'resource_category', 'resource_version_number', 'resource_file_size',
                    'resource_support_document_link', 'resource_uploaded_date', 'resource_last_updated_date', 'resource_download_counter')
    search_fields = ['resource_heading_name', 'resource_category']
    ordering = ['resource_uploaded_date']
    list_filter = ['resource_category', 'resource_heading_name']        
        
        
        
class ToolsDataAdmin(admin.ModelAdmin):
    list_display = ('tool_heading_name', 'tool_discription', 'tool_category', 'tool_version_number', 'tool_file_size',
                    'tool_support_document_link', 'tool_uploaded_date', 'tool_last_updated_date', 'tool_download_counter')
    search_fields = ['tool_heading_name', 'tool_category']
    ordering = ['tool_uploaded_date']
    list_filter = ['tool_category', 'tool_heading_name']




# Register Articles Models


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('article_heading_name', 'article_created_date',
                    'article_last_updated_date', 'article_author_name', 'article_published_status', 'article_published_date')


admin.site.register(models.Articles, ArticlesAdmin)
admin.site.register(models.Category)
admin.site.register(models.ToolsData, ToolsDataAdmin)
admin.site.register(models.ResourcesData, ResourcesDataAdmin)
admin.site.register(models.SuccessStoriesCategory, SuccessStoriesCategoryAdmin)
admin.site.register(models.SuccessStories,SuccessStoriesAdmin)
admin.site.register(models.NewsEvents,NewsEventsAdmin)
admin.site.register(models.UpcomingNewsAndEvents)
admin.site.register(models.Services)
admin.site.register(models.Feedback)
admin.site.register(models.Faq)
admin.site.register(models.UserRegistration)
admin.site.register(models.Country)
admin.site.register(models.States)
admin.site.register(models.City)
# admin.site.register(models.UserProfile)
admin.site.register(models.Blogs , BlogsAdmin)
# admin.site.register(models.MediaAndPresskit)
# admin.site.register(models.MediaImagesAndVideo)
admin.site.register(models.Bookmarks)
