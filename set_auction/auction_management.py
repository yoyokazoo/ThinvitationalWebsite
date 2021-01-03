from set_auction.models import SetDraftingSchedule, AuctionableSets
import random

class AuctionManagement():
	def get_random_undrafted_set():
		print("Getting random undrafted set")
		set_auction_schedule = SetDraftingSchedule.objects.all()
		set_auction_existing_sets = [set_drafting_schedule.set_code for set_drafting_schedule in set_auction_schedule]
		print(set_auction_existing_sets)
		set_auction_sets = AuctionableSets.objects.all()

		# for debug
		undrafted_sets = [auctionable_sets.set_code for auctionable_sets in set_auction_sets]
		print(undrafted_sets)
		
		return random.choice(set_auction_sets)

	def start_auction():
		print("Starting Auction!")
		# Deleting old data
		SetDraftingSchedule.objects.all().delete()

		# Pick a starting set
		print("Picking new set")
		starting_undrafted_set = AuctionManagement.get_random_undrafted_set()
		print("Picked undrafted set {set}".format(set=starting_undrafted_set.set_code))
		starting_set = SetDraftingSchedule(set_code=starting_undrafted_set.set_code, set_name=starting_undrafted_set.set_name, end_time=1234567)
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