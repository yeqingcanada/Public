@action(detail=False, methods=["GET"], url_path='status_invoices/(?P<status_id>[^/.]+)')
def status_invoices(self, request, *args, **kwargs):
    project_master_pk = self.kwargs["project_master_pk"]
    status_id = self.kwargs["status_id"]
    queryset = self.get_queryset().filter(
        project_id=project_master_pk, status_id=status_id)
    serializer_data = self.get_serializer(queryset, many=True).data
    return Response(serializer_data)
