from django.shortcuts import render
from rest_framework import generics
# from test_api.models import Region,FuelUser, Depot, STCMachineDistribution, STCMachinesDistribution, UserLevel,VehicleDetail,VehicleCategory,InsuranceCompany,\
#     IncomingFuel, FuelType,RegionDistribution,MainStock,ClosingTable ,Designation,Requisition,PumpMethod,\
#     Institute,Emp,OtherDistribution,Transaction,STCVehicleDistribution,Contractor,ContractorDistribution,DefaultFuelPrice
# from test_api.serializers import RegionSerializer, UserSerializer,DepotSerializer, UserLevelSerializer,\
#     VehicleDetailSerializer,VehicleCategorySerializer,InsuranceCompanySerializer,IncomingFuelSerializer,\
#     FuelTypeSerializer ,RegionDistributionSerializer,MainStockSerializer,ClosingTableSerializer,serializers ,\
#     RequisitionSerializer,PumpMethodSerializer,RegisterSerializer,ChangePasswordSerializer,UpdateUserSerializer,\
#     DesignationSerializer,InstituteSerializer,EmpSerializer,TransactionSerializer,OtherDistributionSerializer,ContractorDistributionSerializer,\
#     STCVehicleDistributionSerializer,UpdateRequisitionSerializer,ContractorSerializer,DefaultFuelPriceSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from WebApp.models import user
from .serializers import ChangePasswordSerializer, MyTokenObtainPairSerializer, RegisterSerializer, UpdateUserSerializer, userSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Create your views here.

# class DepotDetail(generics.ListCreateAPIView):
#     serializer_class = DepotSerializer
#     pagination_class = LimitOffsetPagination
#     def get_queryset(self):
#         querySet = Depot.objects.all()
#         region_id = self.request.query_params.get('region')

#         if region_id is not None:
#             querySet = querySet.filter(region_id = region_id)
#             if not querySet:
#                 raise serializers.ValidationError({"authorize": "No Records Found."})
#         return querySet

# class DepotList(generics.RetrieveUpdateDestroyAPIView):
#      serializer_class = DepotSerializer
#      queryset = Depot.objects.all()

# class RegionDetail(generics.ListCreateAPIView):
#     serializer_class = RegionSerializer
#     queryset = Region.objects.all()
#     pagination_class = LimitOffsetPagination

# class RegionList(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = RegionSerializer
#     queryset = Region.objects.all()

class userDetail(generics.ListCreateAPIView):
    serializer_class = userSerializer
    queryset = user.objects.all()
    # pagination_class = LimitOffsetPagination

class userList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = userSerializer
    queryset = user.objects.all()

""" 

Extend user and authontication


 """
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

# class FulUserUn(generics.ListCreateAPIView):
#     serializer_class =  UserSerializer  
#     def get_queryset(self):
#         querySet = FuelUser.objects.all()
#         username = self.request.query_params.get('un')

#         if username is not None:
#             querySet = querySet.filter(User__username = username)
#             if not querySet:
#                 raise serializers.ValidationError({"authorize": "No Records Found."})
#         return querySet

# class UpdateRequisitionView(generics.UpdateAPIView):
#     queryset = Requisition.objects.all()
#     serializer_class = UpdateRequisitionSerializer   

# class DefaultFuelPriceDetail(generics.ListCreateAPIView):
#     serializer_class =  DefaultFuelPriceSerializer
#     pagination_class = LimitOffsetPagination
#     def get_queryset(self):
#         querySet = DefaultFuelPrice.objects.all()
#         pump_type_id = self.request.query_params.get('pump')

#         if pump_type_id is not None:
#             querySet = querySet.filter(pump_type_id = pump_type_id)
#         if not querySet:
#                 raise serializers.ValidationError({"authorize": "No Records Found."})
#         return querySet            

# class DefaultFuelPriceList(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = DefaultFuelPriceSerializer
#     queryset = DefaultFuelPrice.objects.all() 
