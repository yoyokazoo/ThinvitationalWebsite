from django.db import models

class SetDraftingSchedule(models.Model):
	set_name = models.CharField(max_length=100)
	end_time = models.BigIntegerField(null=True)

class AuctionableSets(models.Model):
	set_code = models.CharField(max_length=3, db_index=True)
	set_name = models.CharField(max_length=100)