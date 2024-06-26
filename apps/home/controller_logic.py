from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime,timezone
from .models import *
from .utilis import *
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def shop_owner_save_logic(request):
    if request.method == 'POST':
        try:
            # Extract form data
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            shop_name = request.POST['shop_name']
            shop_type = request.POST['shopType']
            rcb_agreement = request.POST['rcbAgreement']
            area = request.POST['area']
            city = request.POST['city']
            state = request.POST['state']
            zip_code = request.POST['zip_code']

            
            if len(first_name) < 2:
                return JsonResponse({'error': 'First name must be at least 2 characters long.'}, status=400)
            if len(phone) < 10:
                return JsonResponse({'error': 'Please enter a valid phone number.'}, status=400)
        
            user = Users()
            user.first_name = first_name
            user.last_name = last_name
            user.username = f'{first_name}{last_name}'
            user.phone = phone
            user.email = email
            user.pincode = zip_code
            user.role = 'cluster'
            user.created_at = datetime.now()
            user.updated_at = datetime.now()
            user.save()

            shop_owner = ShopOwner()
            shop_owner.shopowner_number = generate_shop_number()
            shop_owner.user = user
            shop_owner.shop_name=shop_name
            shop_owner.shop_type =shop_type
            shop_owner.rcb_agreement=bool(rcb_agreement)
            shop_owner.area=area
            shop_owner.city=city
            shop_owner.state=state
            shop_owner.created_at = datetime.now()
            shop_owner.updated_at = datetime.now()
            shop_owner.created_by = request.user
            shop_owner.save()

            return JsonResponse({'message': 'OTP Sent. Register Phone number successfully!','path': '/add_transaction/'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    



@csrf_exempt
@login_required
def save_new_transaction_data(request):
    if request.method == 'POST':
        try:
            owner_id = request.POST.get('owner')
            given_bags = request.POST.get('given_bags') == 'yes'
            lifted_status = request.POST.get('lifted_status') == 'yes'
        
       
            shop_owner = ShopOwner.objects.filter(id=owner_id).first()
    
            pickup_transaction = PickupTransaction.objects.create(
                shop_owner=shop_owner,
                given_bags=given_bags,
                lifted_status=lifted_status,
                created_by=request.user
            )
            pickup_transaction.save()

            total_price = 0
            index = 0
            while f'wasteData[{index}][wasteType]' in request.POST:
                waste_type_id = request.POST.get(f'wasteData[{index}][wasteType]')
                price = request.POST.get(f'wasteData[{index}][price]')
                quantity = request.POST.get(f'wasteData[{index}][quantity]')
                
                waste_type = WasteType.objects.filter(id=waste_type_id).first()
            
                new_pickup_waste_data  = PickupWastData.objects.create(
                        waste_type=waste_type,
                        quantity=quantity,
                        price=price,  
                        pickup_transaction=pickup_transaction
                    )
                tot_amount = int(price)*int(quantity)
                total_price += tot_amount
                new_pickup_waste_data.save()
                index += 1

            pickup_transaction.total_amount = total_price
            pickup_transaction.save()

            return JsonResponse({'message': 'successfully add new transaction','path': '/'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


@csrf_exempt   
def get_materials_list(request,material_id):
    materials = PickupWastData.objects.filter(pickup_transaction_id=material_id).values('id','waste_type__wastename', 'price', 'quantity',)
    return JsonResponse({'materials': list(materials)})