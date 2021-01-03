from django.shortcuts import render
from set_auction.models import SetDraftingSchedule, AuctionableSets

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
		print('asdfasdfasdf')
		#mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
	print('ffffffff')

	set_auction_schedule = SetDraftingSchedule.objects.all()
	set_auction_sets = AuctionableSets.objects.all()
	context = {
		'set_auction_schedule': set_auction_schedule,
		'set_auction_sets': set_auction_sets
	}
	return render(request, 'set_auction_admin.html', context)