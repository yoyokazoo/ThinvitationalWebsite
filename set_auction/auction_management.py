from set_auction.models import SetDraftingSchedule, AuctionableSets
import random
from datetime import datetime, timedelta
import pytz

class AuctionManagement():
	def get_random_undrafted_set():
		print("Getting random undrafted set")
		set_auction_schedule = SetDraftingSchedule.objects.all()
		set_auction_existing_sets = [set_drafting_schedule.set_code for set_drafting_schedule in set_auction_schedule]
		print(set_auction_existing_sets)
		set_auction_sets = AuctionableSets.objects.exclude(set_code__in=set_auction_existing_sets)
		
		return random.choice(set_auction_sets)

	def get_next_day_epoch_time():
		print("Getting next day epoch time")
		today_at_5 = datetime.now(pytz.timezone("US/Pacific")).replace(hour=5, minute=0, second=0, microsecond=0)
		tomorrow_at_5 = today_at_5 + timedelta(days=1)
		print(tomorrow_at_5)
		return int(tomorrow_at_5.timestamp())

	def start_auction():
		print("Starting Auction!")
		# Deleting old data
		SetDraftingSchedule.objects.all().delete()

		tomorrow_epoch_time = AuctionManagement.get_next_day_epoch_time()

		# Pick a starting set
		print("Picking new set")
		starting_undrafted_set = AuctionManagement.get_random_undrafted_set()
		print("Picked undrafted set {set}".format(set=starting_undrafted_set.set_code))
		starting_set = SetDraftingSchedule(set_code=starting_undrafted_set.set_code, set_name=starting_undrafted_set.set_name, end_time=tomorrow_epoch_time)
		starting_set.save()

		# Pick the next set
		print("Picking the second set")
		next_undrafted_set = AuctionManagement.get_random_undrafted_set()
		print("Picked undrafted set {set}".format(set=next_undrafted_set.set_code))
		second_set = SetDraftingSchedule(set_code=next_undrafted_set.set_code, set_name=next_undrafted_set.set_name, end_time=None)
		second_set.save()


	def extend_end_time():
		print("Extending end time")

	def shorten_end_time():
		print("Shortening end time")

	def submit_bid():
		print("Submitting bid")

	def pick_winner():
		print("Picking winner for set")

	def deduct_bids():
		print("Deducting bids from wallets")