######################################## view ################################################
class OfficeItemViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    http_method_names = ['get', 'post']
    serializer_class = OfficeItemSerializer

    @action(detail=False, methods=['GET'])
    def office_not_in_project(self, request, *args, **kwargs):
        project_number = kwargs['project_master_pk']
        if not ProjectMaster.objects.filter(project_number=project_number).exists():
            return Response({'error': 'We could not find relevant data for the project you selected.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        office_id_in_project = [
            office_item["office_id"] for office_item in OfficeItem.objects.filter(
                project_id=project_number).values('office_id')
        ]
        queryset = Office.objects.exclude(
            id__in=office_id_in_project).values('id', 'location')
        serializer = SimpleOfficeSerializer(queryset, many=True)
        new_serializer_data = [{"project_number": project_number, "office_id": item.get("id"),
                                "office": item}for item in list(serializer.data)]
        return Response(new_serializer_data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return OfficeItem.objects.filter(project=self.kwargs['project_master_pk']).select_related('office')

    def create(self, request, *args, **kwargs):
        serializer = OfficeItemSerializer(data=request.data, many=True, context={
            "project_number": kwargs.get('project_master_pk')})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        is_many = isinstance(request.data, list)
        if not is_many:
            return super(OfficeItemViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
######################################## serializer ################################################


"""Why do you need a custom validation: in OfficeItemSerializer, project_number and project_id are poisonous. When using serializers.ValidationError, KeyError will be thrown"""


class PlainValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid input.'
    default_code = "invalid"

    def __init__(self, detail=None, code=None):
        if not isinstance(detail, dict):
            raise serializers.ValidationError("Invalid Input")
        self.detail = detail


class OfficeItemSerializer(serializers.ModelSerializer):
    office = SimpleOfficeSerializer(read_only=True)
    project = ProjectMasterSerializer(read_only=True)
    office_id = serializers.IntegerField()
    """project_id has to be here: validate need this attrs"""
    project_number = serializers.CharField(source='project_id')

    """
    request.... [{'office_id': 5, 'project_number': '001-22'}]
    attrs..... OrderedDict([('office_id', 5), ('project_id', '001-22')])
    The special feature of serializer is that it automatically converts project_number and project_id. At the serializer level, it exists in the form of project_id.
    """

    def validate(self, attrs):
        if not Office.objects.filter(pk=attrs['office_id']).exists():
            raise PlainValidationError(
                {"message": "No office with the given ID was found."})
        if OfficeItem.objects.filter(Q(project=attrs['project_id']) & Q(office=attrs['office_id'])).count() > 0:
            raise PlainValidationError(
                {"message": "This project already has this office, you cannot add it twice."})
        if self.context.get('project_number') != attrs['project_id']:
            raise PlainValidationError(
                {"message": "Project Number dismatched, please refresh the page and try again."})
        return super().validate(attrs)

    def create(self, validated_data):
        if validated_data.get('office_id') == 1 or validated_data.get('office_id') == 2:
            print("send email to Indianapolis or Montreal")
        return super().create(validated_data)

    class Meta:
        model = OfficeItem
        fields = ['id', 'office', 'project',
                  'office_id', 'project_number']

    def get_validation_exclusions(self):
        exclusions = super(OfficeItemSerializer,
                           self).get_validation_exclusions()
        return exclusions + ['project_id']
