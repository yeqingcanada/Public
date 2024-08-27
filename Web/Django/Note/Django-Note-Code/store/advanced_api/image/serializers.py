from rest_framework import serializers

from ...models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductImage
        """we don't want to return product ID here, because it's already available from the url"""
        fields = ['id', 'image']