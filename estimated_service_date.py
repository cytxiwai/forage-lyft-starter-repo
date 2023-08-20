def estimated_service_date(last_service_date, years):
    calculated_result = last_service_date.replace(year=last_service_date.year + years)
    return calculated_result