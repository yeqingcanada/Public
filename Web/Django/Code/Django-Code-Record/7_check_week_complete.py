def check_week_complete(self, user_id, week_id):
    """ 1 is Sunday, 7 is Saturday """
    week_days = [2, 3, 4, 5, 6]
    days = Day.objects.filter(week=week_id).filter(
        day_of_week__in=week_days)
    day_summaries = DaySummary.objects.filter(
        resource=user_id).filter(day__in=days)
    is_complete = day_summaries.count() == 5 and all(
        day_summary.sum_hours >= 8 for day_summary in day_summaries)