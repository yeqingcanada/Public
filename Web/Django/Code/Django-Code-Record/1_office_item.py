######################################## view ################################################
class OfficeItemViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    http_method_names = ['get', 'post']

    @action(detail=False, methods=['GET'])
    def office_not_in_project(self, request, *args, **kwargs):
        office_id_in_project = [
            office_item["office_id"] for office_item in OfficeItem.objects.filter(
                project_id=kwargs['project_pk']).values('office_id')
        ]
        queryset = Office.objects.exclude(
            id__in=office_id_in_project).values('id', 'location')
        serializer = SimpleOfficeSerializer(
            queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        """SimpleOfficeSerializer need to be used externally, for the data from frontend be neat and in office format"""
        if self.request.method == 'POST':
            return SimpleOfficeSerializer
        return OfficeItemSerializer

    def get_queryset(self):
        return OfficeItem.objects.filter(project=self.kwargs['project_pk']).select_related('office')

    """
    need to be from this path: /global_manage/projects/5/office_items/office_not_in_project/
    post--->create in views--->choose a serializer--->validate in seria--->perform_create--->save in seria--->create in seria
    只有在detail位置,post才会被trigger,注意这个comment的第一行
    """

    def post(self, request, *args, **kwargs):
        print('post...')
        print('request.data:', request.data)
        requst_data = [{"office_id": item.get(
            'id'), "project_id": self.kwargs['project_pk']} for item in request.data]
        request.data.clear()
        request.data.extend(requst_data)
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print('create in views...')
        print('request.data:', request.data)
        serializer = OfficeItemSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

######################################## serializer ################################################


class OfficeItemSerializer(serializers.ModelSerializer):
    office = SimpleOfficeSerializer(read_only=Truen)
    project = SimpleProjectSerializer(read_only=True)
    office_id = serializers.IntegerField()
    """project_id has to be here: validate need this attrs"""
    project_id = serializers.IntegerField()

    def validate(self, attrs):
        print('attrs...', attrs)
        if not Office.objects.filter(pk=attrs['office_id']).exists():
            raise serializers.ValidationError(
                'No office with the given ID was found.')
        if OfficeItem.objects.filter(Q(project=attrs['project_id']) & Q(office=attrs['office_id'])).count() > 0:
            raise serializers.ValidationError(
                'This project already has this office, you cannot add it twice.')
        return super().validate(attrs)

    # def create(self, validated_data):
    #     print('create in serializers...')
    #     return super().create(validated_data)

    class Meta:
        model = OfficeItem
        fields = ['id', 'office', 'project', 'office_id', 'project_id']
