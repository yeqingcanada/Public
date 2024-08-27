class UtilizationSummariesViewSet(ModelViewSet):
    http_method_names = ['get', 'patch']

    def get_queryset(self):
        if self.request.method == "PATCH":
            return UtilizationSummary.objects.filter(id=self.kwargs["pk"])

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return PartialUpdateUtilizationSummarySerializer

    def list(self, request, *args, **kwargs):
        office_id = request.user.office_id
        week_id = self.kwargs["weeks_pk"]

        """ Resources
        resource_id
        resources = {1: {'resource_full_name': 'Ching Yip'},
                        3: {'resource_full_name': 'Qing Ye'},
                        4: {'resource_full_name': 'Monique Vang'},
                        5: {'resource_full_name': 'Q Y'},
                        9: {'resource_full_name': 'Daheng Liu'},
                        10: {'resource_full_name': 'Victoria Ma'},
                        11: {'resource_full_name': 'dh l'},
                        12: {'resource_full_name': 'sss www'}}
        """
        resources = get_office_resources(office_id)
        """ Weeks
        week_id
        weeks = {2: {"week_name": "Week of 2023-03-19"},
                3: {"week_name": "Week of 2023-03-26"},
                4: {"week_name": "Week of 2023-04-02"}}
        """
        weeks = get_15_weeks_with_name(week_id)
        """Working Days
        week_id
        working_days = {2: {'working_days': 5},
                        3: {'working_days': 4},
                        4: {'working_days': 5}}
        """
        working_days = get_15_weeks_working_days(office_id, weeks)
        """ Available Days
        resource_id, week_id
        available_days = {(1, 2): {'available_day_id': 1, 'available_days': Decimal('5.00')},
                        (1, 3): {'available_day_id': 2, 'available_days': Decimal('5.00')}}
        """
        available_days = get_raw_15_weeks_available_days(resources, weeks)
        """ Staffings
        (resource_id, week_id)
        staffings = {
            (1, 2): {"sum_forecasted_days": 5.0},
            (1, 3): {"sum_forecasted_days": 1.0}
        }
        """
        staffings = self.get_sum_staffing(office_id, weeks)
        """ Utilization Summaries
        (resource_id, week_id)
        utlization_summaries = {
            (1, 2): {'utilization_summary_id': 1, 'utilization': Decimal('0.50')}}
        """
        utilization_summaries = self.get_15_weeks_utilization_summaries(
            resources, weeks)

        response_data = []
        for resource_id, resource_info in resources.items():
            utilization_summary_response_data = {'resource_id': resource_id}
            for week_id, week_info in weeks.items():
                utilization_summaries_info = utilization_summaries.get(
                    (resource_id, week_id))
                if utilization_summaries_info is None:
                    utilization_summaries_info = self.create_utilization_summary(
                        working_days, available_days, staffings, week_id, resource_id)

                utilization_summary_response_data[week_id] = {'utilization_summary_id': utilization_summaries_info['utilization_summary_id'],
                                                              'utilization': float(utilization_summaries_info['utilization'])}
            response_data.append(utilization_summary_response_data)
        return Response(response_data, status=status.HTTP_200_OK)

    def get_sum_staffing(self, office_id, weeks):
        """ Weeks
        week_id
        weeks = {2: {"week_name": "Week of 2023-03-19"},
                3: {"week_name": "Week of 2023-03-26"},
                4: {"week_name": "Week of 2023-04-02"}}
        """
        """ Project Roles
        project_role_id
        project_roles = {
            "2": {"project_number": "002-23",
                "project_name": "GLOCAL CF Material Flow GLO-10",
                "resource_id": 1,
                "resource_full_name": "Ching Yip"},
            "3": {"project_number": "003-23",
                "project_name": "Aldi: 3 DC Study Northeast 048-20",
                "resource_id": 1,
                "resource_full_name": "Ching Yip"},
            "4": {"project_number": "004-23",
                "project_name": "Haribo: 3PL Bench Marking 024-20",
                "resource_id": 1,
                "resource_full_name": "Ching Yip"}
        }
        """
        project_roles = get_office_project_roles(office_id)
        """ Staffings
        project_role_id, week_id
        staffings = {
            (2, 2): {'staffing_id': 1, 'forecasted_days': Decimal('3.00')},
            (3, 2): {'staffing_id': 2, 'forecasted_days': Decimal('2.00')},
            (2, 3): {'staffing_id': 3, 'forecasted_days': Decimal('1.00')}}
        """
        staffings = get_raw_15_weeks_staffings(project_roles, weeks)

        staffings_with_resource_week = {}
        for (project_role_id, week_id), staffing in staffings.items():
            resource_id = project_roles[project_role_id]['resource_id']
            sum_forecasted_days = staffing['forecasted_days']

            if (resource_id, week_id) in staffings_with_resource_week:
                staffings_with_resource_week[(
                    resource_id, week_id)]['sum_forecasted_days'] += float(sum_forecasted_days)
            else:
                staffings_with_resource_week[(resource_id, week_id)] = {
                    'sum_forecasted_days': float(sum_forecasted_days)}
        return staffings_with_resource_week

    def get_15_weeks_utilization_summaries(self, resources, weeks):
        resource_ids = ','.join([str(i)
                                 for i in list(resources.keys())])
        week_ids = ','.join([str(i) for i in list(weeks.keys())])

        query = f'''
            SELECT [id],[utilization],[resource_id],[week_id]
            FROM [dbo].[global_manage_utilizationsummary]
            WHERE resource_id IN ({resource_ids})
            AND week_id IN ({week_ids});
        '''

        with connection.cursor() as cursor:
            cursor.execute(query)
            utilization_summaries = {}
            for row in cursor.fetchall():
                utlzt_summary_id = row[0]
                utilization = row[1]
                resource_id = row[2]
                week_id = row[3]
                key = (resource_id, week_id)
                utilization_summaries[key] = {
                    "utilization_summary_id": utlzt_summary_id,
                    "utilization": utilization
                }
        return utilization_summaries

    def create_utilization_summary(self, working_days, available_days, staffings, week_id, resource_id):
        working_day_info = working_days.get((week_id))
        work_days = working_day_info['working_days']

        available_day_info = available_days.get(
            (resource_id, week_id))
        available_days = float(available_day_info['available_days']) if available_day_info else float(
            working_day_info['working_days'])

        staffing_info = staffings.get((resource_id, week_id))
        forecast_days = float(
            staffing_info['sum_forecasted_days']) if staffing_info else 0

        utilization = (work_days - available_days +
                       forecast_days)/work_days
        new_utilization_summary = UtilizationSummary.objects.create(
            utilization=utilization,
            resource_id=resource_id,
            week_id=week_id)
        new_utilization_summary_id = new_utilization_summary.id
        utilization_summaries_info = {
            'utilization_summary_id': new_utilization_summary_id, 'utilization': utilization}
        return utilization_summaries_info
