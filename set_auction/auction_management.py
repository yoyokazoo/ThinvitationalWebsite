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

	def get_pending_set():
		pending_sets = SetDraftingSchedule.objects.filter(end_time=None)
		return pending_sets[0] if pending_sets else None

	def pick_new_pending_set():
		print("Picking a pending set")
		pending_set = AuctionManagement.get_pending_set()
		if pending_set:
			return

		pending_set = AuctionManagement.get_random_undrafted_set()
		print("Picked pending set {set}".format(set=pending_set.set_code))
		pending_set = SetDraftingSchedule(set_code=pending_set.set_code, set_name=pending_set.set_name, end_time=None)
		pending_set.save()

	def activate_pending_set():
		pending_set = AuctionManagement.get_pending_set()
		if pending_set:
			pending_set.end_time = AuctionManagement.get_next_day_epoch_time()
			pending_set.save()

	def start_auction():
		print("Starting Auction!")
		# Deleting old data
		SetDraftingSchedule.objects.all().delete()

		# pick first set
		AuctionManagement.pick_new_pending_set()
		AuctionManagement.activate_pending_set()

		# pick pending set
		AuctionManagement.pick_new_pending_set()

	def proceed_to_next_set():
		print("Proceeding to next set (if possible)")
		if AuctionManagement.get_active_set():
			print("Set is active, can't proceed")
			return
		
		# all the bidding logic here
		most_recent_set = AuctionManagement.get_most_recent_inactive_set()
		print("Most recent set: " + str(most_recent_set))

		AuctionManagement.activate_pending_set()
		AuctionManagement.pick_new_pending_set()

	def get_most_recent_inactive_set():
		now = int(datetime.now().timestamp())
		inactive_sets = SetDraftingSchedule.objects.filter(end_time__lte=now, end_time__isnull=False)
		
		if not inactive_sets:
			return None

		return max(inactive_sets, key=lambda x: x.end_time if x else 0)

	def get_active_set():
		now = int(datetime.now().timestamp())
		active_sets = SetDraftingSchedule.objects.filter(end_time__gte=now)
		print(now)
		print(active_sets[0].end_time if active_sets else "no active sets")
		return active_sets[0] if active_sets else None

	def end_set():
		active_set = AuctionManagement.get_active_set()
		if active_set:
			active_set.end_time = int(datetime.now().timestamp()) - 1
			active_set.save()
		AuctionManagement.proceed_to_next_set()

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