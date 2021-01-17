from django.shortcuts import render
from set_auction.models import SetDraftingSchedule, AuctionableSets
from set_auction.auction_management import AuctionManagement
from django.http import HttpResponseNotFound


def set_auction_index(request):
	set_auction = SetDraftingSchedule.objects.all()
	context = {
		'set_auction': set_auction
	}
	return render(request, 'set_auction_index.html', context)

def set_auction_detail(request, pk):
	set_auction = SetDraftingSchedule.objects.get(pk=pk)
	context = {
		'set_auction': set_auction
	}
	return render(request, 'set_auction_detail.html', context)

def set_auction_admin(request):
	if(request.method == 'POST'):
		if 'start_draft' in request.POST:
			AuctionManagement.start_auction()
		elif 'end_set' in request.POST:
			AuctionManagement.end_set()
		else:
			return HttpResponseNotFound('<h1>Invalid or unknown admin action</h1>')

	set_auction_schedule = SetDraftingSchedule.objects.all()
	set_auction_sets = AuctionableSets.objects.all()
	context = {
		'set_auction_schedule': set_auction_schedule,
		'set_auction_sets': set_auction_sets
	}
	return render(request, 'set_auction_admin.html', context)