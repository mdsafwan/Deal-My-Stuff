from django.shortcuts import render
from advertisements.models import advertisement, category
from django.utils import timezone

def home(request):
	return render(request, "index.html", {})

def post_advertisement(request):
	if request.POST:
		Title = request.POST.get('title')
		Advertisement_Tag1 = request.POST.get('adv_tag1')
		Advertisement_Tag2 = request.POST.get('adv_tag2')
		Advertisement_Tag3 = request.POST.get('adv_tag3')
		MRP = request.POST.get('mrp')
		Selling_Price = request.POST.get('selling_price')
		Image1 = request.POST.get('image1')
		Description = request.POST.get('description')
		Category = request.POST.get('category')
		Post_Date = timezone.now()
		Status = "Not Sold"
  		
		temp1 = advertisement.objects.values('Advertisement_ID').latest('Advertisement_ID')
		Advertisement_ID = temp1['Advertisement_ID']
  		
		strip123 = Advertisement_ID[4:]
		add = int(strip123) + 1
		Advertisement_ID = "ADV_" + str(add)
		Product_ID = "PRD_" + str(add) 
		
		advertisement.objects.create(Advertisement_ID = Advertisement_ID,
  									Title = Title,
  									Post_Date = Post_Date,
  									Status = Status,
  									MRP = MRP,
  									Image1 = Image1,
  									Selling_Price = Selling_Price,
  									Advertisement_Tag1 = Advertisement_Tag1,
  									Advertisement_Tag2 = Advertisement_Tag2,
  									Advertisement_Tag3 = Advertisement_Tag3,
  									Description = Description
  									)

 		category.objects.create(Product_ID = Product_ID,
 					 			Advertisement_ID = Advertisement_ID,
 					 			Category = Category)


		#category, user_id not done
	return render(request, "post_advertisement.html", {})

def display_advertisement(request):
	Category = request.GET.get('C')
	if Category == "CAT_1000":
		ads = []
		electronic_gadgets_ad_ids = category.objects.filter(Category="CAT_1000").all()
		#print electronic_gadgets_ad_ids
 		for x in electronic_gadgets_ad_ids:
 		#	print x.Product_ID
 		#	print x.Advertisement_ID
 		#	print x.Category
 			y = advertisement.objects.filter(Advertisement_ID=x.Advertisement_ID.Advertisement_ID).all()
 			ads.append(y[0]) #get first object in tuple
 		heading = "Electronic Gadgets"
  			
 	elif Category == "CAT_1001":
		ads = []
		books_ad_ids = category.objects.filter(Category="CAT_1001").all()
 		for x in books_ad_ids:
 			y = advertisement.objects.filter(Advertisement_ID=x.Advertisement_ID.Advertisement_ID).all()
 			ads.append(y[0])
 		heading = "Books"
  					
 	elif Category == "CAT_1002":	 	 		 	 	
 	 	ads = []
		vehicles_ad_ids = category.objects.filter(Category="CAT_1002").all()
 		for x in vehicles_ad_ids:
 			y = advertisement.objects.filter(Advertisement_ID=x.Advertisement_ID.Advertisement_ID).all()
 			ads.append(y[0])
 		heading = "Vehicles"
  		
 	elif Category == "CAT_1003":	 	 		 	 	
 	 	ads = []
		household_items_ad_ids = category.objects.filter(Category="CAT_1003").all()
 		for x in household_items_ad_ids:
 			y = advertisement.objects.filter(Advertisement_ID=x.Advertisement_ID.Advertisement_ID).all()
 			ads.append(y[0])
 	 	heading = "Household Items"
  	 	
 	return render(request, "display_advertisement.html", {'ads' : ads,
														'heading' : heading,
													})