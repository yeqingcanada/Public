######################################## view ################################################

def partial_update(self, request, *args, **kwargs):
    alternative_ids = list(map(lambda item: item.get('id'), request.data))
    instances = Alternative.objects.filter(id__in=alternative_ids)
    serializer = self.get_serializer(
        instances, many=True, data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    return Response(serializer.data)

######################################## serializer ################################################


class AlternativeListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        alternative_mapping = {
            alternative.id: alternative for alternative in instance}
        data_mapping = {item.get('id'): item for item in validated_data}
        # ret = []
        for alternative_id, data in data_mapping.items():
            # method one:
            updated_alternative = Alternative.objects.filter(
                id=alternative_id).update(isBusinessCase=data.get('isBusinessCase'))
            ret.append(updated_alternative)

            # method two:
            alternative = alternative_mapping.get(alternative_id, None)
            alternative.isBusinessCase = data.get('isBusinessCase')
            ret.append(alternative.save())
        return ret


class PartialUpdateAlternativeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    isBusinessCase = serializers.BooleanField()

    class Meta:
        list_serializer_class = AlternativeListSerializer
