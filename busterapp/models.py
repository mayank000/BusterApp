from django.db import models
from users.models import UserProfile

class Project(models.Model):
	name = models.CharField(max_length=30, )
	added_on = models.DateTimeField(null=True, blank=True, auto_now_add=True)
	updated_on = models.DateTimeField(null=True, blank=True, auto_now=True)
	added_by = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)

	class meta:
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'
		db_table = 'busterapp_project'

	def __str__(self):
		return "%s - %s" %( self.name, self.id )		

class Task(models.Model):
	name = models.CharField(max_length=30, null=True, blank=True)
	parent = models.ForeignKey('self', null=True, blank=True)
	added_on = models.DateTimeField(null=True, blank=True, auto_now_add=True)
	updated_on = models.DateTimeField(null=True, blank=True, auto_now=True)
	added_by = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL )

	class Meta:
		verbose_name = 'Task'
		verbose_name_plural = 'Tasks'
		db_table = 'task'

	def __str__(self):
		return "%s - %s" %( self.name, self.id )
