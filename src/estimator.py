def estimator(data):
    
    period_type = data["periodType"]
    period = data["timeToElapse"]

    no_of_days = normalize_period_to_days(period_type, period)
    factor = no_of_days / 3

    reported_cases = data["reportedCases"]
    # population = data["population"]
    total_hospital_beds = data["totalHospitalBeds"]

    currently_infected_best_case = reported_cases * 10
    infections_by_request_time_best_case = \
        currently_infected_best_case * (2 ** factor)

    currently_infected_worst_case = reported_cases * 50
    infections_by_request_time_worst_case = \
        currently_infected_worst_case * (2 ** factor)

    # Challenge One Ends
    
    # Challenge Two Starts
    severe_cases_by_requested_time_best_case = \
        infections_by_request_time_best_case * 15 / 100
    available_hospital_space_best_case = \
        total_hospital_beds * 35 / 100  # 35% of total available spaces in hospitals
    hospital_bed_by_requested_time_best_case = \
        available_hospital_space_best_case - \
        severe_cases_by_requested_time_best_case

    severe_cases_by_requested_time_worst_case = \
        infections_by_request_time_worst_case * 15 / 100
    available_hospital_space_worst_case = \
        total_hospital_beds * 35 / 100  # 35% of total available spaces in hospitals
    hospital_bed_by_requested_time_worst_case = \
        available_hospital_space_worst_case - \
        severe_cases_by_requested_time_worst_case
    # Challenge Two Ends

    
    # Estimation result
    final_data = {
        "data": data,
        "impact": {
            "currentlyInfected": currently_infected_best_case,
            "infectionsByRequestedTime": infections_by_request_time_best_case,
            "hospitalBedByRequestedTime": hospital_bed_by_requested_time_best_case,
        },
        "severeImpact": {
            "currentlyInfected": currently_infected_worst_case,
            "infectionsByRequestedTime": infections_by_request_time_worst_case,
            "hospitalBedByRequestedTime": hospital_bed_by_requested_time_worst_case,
        },
    }
    return final_data


def normalize_period_to_days(period_type, period):
    return period if period_type == "days" else period * 7 \
        if period_type == "weeks" else period * 30


if __name__ == "__main__":
    input_data = {
        "region": {
            "name": "Africa",
            "avgAge": 19.7,
            "avgDailyIncomeIUSD": 5,
            "avgDailyIncomePopulation": 0.71
        },
        "periodType": "days",
        "timeToTlapse": 58,
        "reportedCases": 674,
        "population": 66622705,
        "totalHospitalBeds": 1380614
    }

    estimated_data = estimator(input_data)
    print(estimated_data)
