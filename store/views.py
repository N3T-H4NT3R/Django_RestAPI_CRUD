from .models import Product
from rest_framework import status
from .serializers import Product_Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(["GET"])
def Get_All_Products(request):
    products = Product.objects.all()
    serialized = Product_Serializer(products, many=True)

    return Response (serialized.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def Get_Each_Product(request, pk):

    if Product.objects.filter(id=pk).exists():
        products = Product.objects.get(id=pk)
        serialized_data = Product_Serializer(products, many=False)

        return Response (serialized_data.data, status=status.HTTP_200_OK)
    
    else:
        return Response (
            {
                "msg":"Product Not Found !"
            },status=status.HTTP_404_NOT_FOUND
            )


@api_view(["POST"])
def Add_Product(request):
    data = request.data
    product = Product.objects.create(
        name=data["name"],
        price=data["price"],
        quantity_in_Stoke=data["quantity"],
    )

    serialized_data = Product_Serializer(product, many=False)

    return Response (serialized_data.data, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def Update_Product(request, pk):
    try:
        Product.objects.filter(id=pk).exists()

        product = Product.objects.get(id=pk)
        serialized_data = Product_Serializer(product, data=request.data, partial=True)

        if serialized_data.is_valid():
            amount_in_stock = product.quantity_in_Stoke
            amount_in_user = serialized_data.validated_data.get("quantity_in_Stoke")

            if amount_in_stock >= amount_in_user and amount_in_stock >= 1:
                result = amount_in_stock - amount_in_user
                product.quantity_in_Stoke = result

                product.save()

                return Response(
                    {
                        "msg": "Status:  Success", 
                        "Data": serialized_data.data
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"msg": f" {amount_in_user} Product in stock not available !"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                serialized_data.errors,
                status=status.HTTP_404_NOT_FOUND
            )
    except Product.DoesNotExist:
        return Response(
            {"msg": "Product Not Found!"}, 
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(["DELETE"])
def Delete_Product(request, pk):
    if Product.objects.filter(id=pk).exists():
        product = Product.objects.get(id=pk)
        product.delete()

        return Response (
            {
                "msg":"Deleted"
            },status=status.HTTP_200_OK
        )
    else:
        return Response (
            {
                "msg":"Product Not Found !"
            },status=status.HTTP_404_NOT_FOUND
            )
