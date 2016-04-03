from django import forms
from django.db import models
from django.contrib import admin
from django.db.models import signals
from django.core.mail import send_mail
from django.contrib.auth.models import User , Group
from django.contrib.admin.helpers import ActionForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.admin.views.main import ChangeList
from DjangoApp.models import Article , Comment , UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# def has_approval_permission(request, obj=None):
# 	if request.user.has_perm('DjangoApp.is_publish'):
# 		return True
# 	return False
   
class UserProfileInline(admin.StackedInline):
	model=UserProfile
	can_delete = False
	
class UserAdmin(BaseUserAdmin):
	list_display = ('username','email',)
	list_filter = ('is_staff', 'is_superuser')
	readonly_fields = ('email','username','first_name','last_name')
	inlines = (UserProfileInline, )

class CommentInline(admin.TabularInline):
	model = Comment
	#ne

class ArticleAdmin(admin.ModelAdmin):
	def Com_Count(self, instance):
		return "1"
	def View_Count(self, instance):
		return "4"

	list_display = ['subject' ,'is_publish','date','Com_Count','View_Count']
	list_editable = ('is_publish',)
	list_display_links = ['subject']
	list_filter = ('date','is_publish')
	ordering = ('date',) # The negative sign indicate descendent order
	search_fields = ['subject']
	readonly_fields = ('Com_Count','View_Count')
	Com_Count.short_description = 'Number of Comments'
	View_Count.short_description = 'Number of views'
	inlines = [CommentInline,]

	
	
class CommentAdmin(admin.ModelAdmin):
	def get_subject(request, queryset):
		return "2" #Article.objects.filter(id = queryset.Article_comment_id).subject
	list_display =['content' , 'date' ,'get_subject']
	list_display_links = ['content' ,'date'] 
	readonly_fields = ('get_subject',)
	get_subject.short_description = "Article subject"
        


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment ,CommentAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.disable_action('delete_selected')
#signals.post_save.connect(notify_admin, sender=User)