from django.shortcuts import render
from set_auction.models import SetDraftingSchedule

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