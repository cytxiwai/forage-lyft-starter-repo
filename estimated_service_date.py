def estimated_service_date(last_service_date, years):
    return last_service_date.replace(year=last_service_date + years)