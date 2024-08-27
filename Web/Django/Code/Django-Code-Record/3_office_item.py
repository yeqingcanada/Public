######################################## view ################################################
class OfficeItemViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    def get_queryset(self):
        return OfficeItem.objects.filter(project=self.kwargs['project_master_pk']).select_related('office').only(('office'))

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OfficeItemSerializer(
            queryset, many=True, fields=('office',))
        new_response_data = [element['office'] for element in serializer.data]
        return Response(new_response_data)

######################################## serializer ################################################


class OfficeItemSerializer(serializers.ModelSerializer):
    office = SimpleOfficeSerializer(read_only=True)
    project = ProjectMasterSerializer(read_only=True)
    office_id = serializers.IntegerField()
    project_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        # 对于不是office的field，将他们pop掉
        fields = kwargs.pop('fields', None)
        super(OfficeItemSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def validate(self, attrs):
        if not Office.objects.filter(pk=attrs['office_id']).exists():
            raise serializers.ValidationError(
                'No office with the given ID was found.')
        if OfficeItem.objects.filter(Q(project=attrs['project_id']) & Q(office=attrs['office_id'])).count() > 0:
            raise serializers.ValidationError(
                'This project already has this office, you cannot add it twice.')
        return super().validate(attrs)

    class Meta:
        model = OfficeItem
        fields = ['id', 'office', 'office_id', 'project_id', 'project']
