from django.db import models

class SetDraftingSchedule(models.Model):
	set_name = models.CharField(max_length=100)
	end_time = models.DateField(null=True)