from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

##Customizing the token view to get user and password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import GroceriesSerializer
from base.models import Groceries

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/token/refresh/',
        '/api/groceries/',
        '/api/calculate_total_price/',
    ]

    return Response(routes)
    # return JsonResponse(routes, safe=False)

# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def getGroceries(request):
#     user = request.user
#     groceries = Groceries.objects.all();
    
#     # groceries = user.groceries_set.all()
#     # groceries = Groceries.objects.filter(user=user)
#     serializer = GroceriesSerializer(groceries,many=True);
#     return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getGroceries(request):
    user = request.user
    groceries = Groceries.objects.all()
    serializer = GroceriesSerializer(groceries, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def calculate_total_price(request):
    print(request.data) 
    selected_items = request.data
    total_price = 0
    
    for item in selected_items:
        grocery_id = item['groceryId']
        quantity = int(item['quantity'])
        
        try:
            grocery = Groceries.objects.get(id=grocery_id)
            total_price += grocery.price * quantity
        except Groceries.DoesNotExist:
            return Response({'error': f'Grocery with id {grocery_id} does not exist'}, status=400)
    
    return Response({'total_price': total_price})
    