from django.shortcuts import render
from advertisements.models import advertisement, category, electronic_gadget, book, vehicle, household_item
from login.models import user_login
from django.utils import timezone
from django.http.response import HttpResponseRedirect, HttpResponse

def home(request):
	user_logged_in = user_login.objects.filter(Logged_Out_Time__isnull=True)
	if not user_logged_in:
		return HttpResponseRedirect('/login_error/')
	return render(request, "index.html", {})

def post_advertisement(request):
	user_logged_in = user_login.objects.filter(Logged_Out_Time__isnull=True)
	if not user_logged_in:
		return HttpResponseRedirect('/login_error/')
	Category = request.GET.get('C')
	if request.POST:
		Title = request.POST.get('title')
		Advertisement_Tag1 = request.POST.get('adv_tag1')
		Advertisement_Tag2 = request.POST.get('adv_tag2')
		Advertisement_Tag3 = request.POST.get('adv_tag3')
		MRP = request.POST.get('mrp')
		Selling_Price = request.POST.get('selling_price')
		Image1 = request.POST.get('image1')
		Description = request.POST.get('description')
		Post_Date = timezone.now()
		Status = "Not Sold"
		
		temp1 = advertisement.objects.values('Advertisement_ID').latest('Advertisement_ID')
		Advertisement_ID = temp1['Advertisement_ID']
  		
		strip123 = Advertisement_ID[4:]
		add = int(strip123) + 1
		Advertisement_ID = "ADV_" + str(add)
		Product_ID = "PRD_" + str(add) 
		
		user_id_of_user_logged_in = user_login.objects.last()
		Seller_User_ID = user_id_of_user_logged_in.User_ID
		Buyer_User_ID = Seller_User_ID
		
		advertisement.objects.create(Advertisement_ID = Advertisement_ID,
  									Title = Title,
  									Post_Date = Post_Date,
  									Seller_User_ID = Seller_User_ID,
  									Buyer_User_ID = Buyer_User_ID,
  									Status = Status,
  									MRP = MRP,
  									Image1 = Image1,
  									Selling_Price = Selling_Price,
  									Advertisement_Tag1 = Advertisement_Tag1,
  									Advertisement_Tag2 = Advertisement_Tag2,
  									Advertisement_Tag3 = Advertisement_Tag3,
  									Description = Description
  									)
		
		ad_id = advertisement.objects.filter(Advertisement_ID = Advertisement_ID).last()
		category.objects.create(Product_ID = Product_ID,
 					 			Advertisement_ID = ad_id,
 					 			Category = Category)
		
		pr_id = category.objects.filter(Product_ID = Product_ID).last()
		
		Category = request.GET.get('C')
		if Category == "CAT_1000":
			Brand = request.POST.get('brand')
			Product_Model = request.POST.get('model')
			Specification = request.POST.get('specification')
			electronic_gadget.objects.create(Product_ID = pr_id,
											Brand = Brand,
											Product_Model = Product_Model,
											Specification = Specification)
			
		elif Category == "CAT_1001":
			Genre = request.POST.get('genre')
			Langauge = request.POST.get('language')
			Publisher = request.POST.get('publisher')
			book.objects.create(Product_ID = pr_id,
								Genre = Genre,
								Book_Language = Langauge,
								Publisher = Publisher)
		
		elif Category == "CAT_1002":
			Manufacturer = request.POST.get('manufacturer')
			Product_Model = request.POST.get('model')
			Year = request.POST.get('year')
			vehicle.objects.create(Product_ID = pr_id,
								Manufacturer = Manufacturer,
								Product_Model = Product_Model,
								Year = Year)
		
		elif Category == "CAT_1003":
			Type = request.POST.get('type')
			Brand = request.POST.get('brand')
			household_item.objects.create(Product_ID = pr_id,
										Type = Type,
										Brand = Brand)
		
		#category, user_id not done
		return render(request, "post_success.html", {})
	return render(request, "post_advertisement.html", {'Category' : Category})

def display_advertisement(request):
	user_logged_in = user_login.objects.filter(Logged_Out_Time__isnull=True)
	if not user_logged_in:
		return HttpResponseRedirect('/login_error/')
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
 	
 
def product_display(request):
	user_logged_in = user_login.objects.filter(Logged_Out_Time__isnull=True)
	if not user_logged_in:
		return HttpResponseRedirect('/login_error/')
	
	Advertisement_ID = request.GET.get('P')
	Number = Advertisement_ID[4:]
	Product_ID = "PRD_" + Number
	
	x = advertisement.objects.filter(Advertisement_ID=Advertisement_ID)
	ad = x[0]
	return render(request, "product.html", {'ad' : ad})

def advertisement_select_category(request):
	user_logged_in = user_login.objects.filter(Logged_Out_Time__isnull=True)
	if not user_logged_in:
		return HttpResponseRedirect('/login_error/')
	
	if request.POST:
		Category = request.POST.get('category')
		url = "/post_advertisement?C=" + Category
		return HttpResponseRedirect(url)
	return render(request, "post_advertisement_select_category.html", {})

def contact_us(request):
	user_logged_in = user_login.objects.filter(Logged_Out_Time__isnull=True)
	if not user_logged_in:
		return HttpResponseRedirect('/login_error/')
	
	return render(request, "contact.html", {})