def estimator(data):
    avg_daily_income_in_usd = data["region"]["avgDailyIncomeInUSD"]
    avg_daily_income_population = data["region"]["avgDailyIncomePopulation"]

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

    # Challenge Three Starts
    cases_for_icu_by_requested_time_best_case = \
        infections_by_request_time_best_case * 5 / 100  # 5% of infectionsByRequestedTime
    cases_for_ventilators_by_requested_time_best_case = \
        infections_by_request_time_best_case * 2 / 100  # 2% of infectionsByRequestedTime
    dollars_in_flight_best_case = \
        infections_by_request_time_best_case * avg_daily_income_population * \
        avg_daily_income_in_usd * no_of_days

    cases_for_icu_by_requested_time_worst_case = \
        infections_by_request_time_worst_case * 5 / 100  # 5% of infectionsByRequestedTime
    cases_for_ventilators_by_requested_time_worst_case = \
        infections_by_request_time_worst_case * 2 / 100  # 2% of infectionsByRequestedTime
    dollars_in_flight_worst_case = \
        infections_by_request_time_worst_case * avg_daily_income_population * \
        avg_daily_income_in_usd * no_of_days
    # Challenge Three Ends

    # Estimation result
    final_data = {
        "data": data,
        "impact": {
            "currentlyInfected": currently_infected_best_case,
            "infectionsByRequestedTime": infections_by_request_time_best_case,
            "hospitalBedByRequestedTime": hospital_bed_by_requested_time_best_case,
            "casesForICUByRequestedTime":
                cases_for_icu_by_requested_time_best_case,
            "casesForVentilatorsByRequestedTime":
                cases_for_ventilators_by_requested_time_best_case,
            "dollarsInFlight": dollars_in_flight_best_case,
        },
        "severeImpact": {
            "currentlyInfected": currently_infected_worst_case,
            "infectionsByRequestedTime": infections_by_request_time_worst_case,
            "hospitalBedByRequestedTime": hospital_bed_by_requested_time_worst_case,
            "casesForICUByRequestedTime":
                cases_for_icu_by_requested_time_worst_case,
            "casesForVentilatorsByRequestedTime":
                cases_for_ventilators_by_requested_time_worst_case,
            "dollarsInFlight": dollars_in_flight_worst_case,
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
            "avgDailyIncomeInUSD": 5,
            "avgDailyIncomePopulation": 0.71
        },
        "periodType": "days",
        "timeToElapse": 58,
        "reportedCases": 674,
        "population": 66622705,
        "totalHospitalBeds": 1380614
    }

    estimated_data = estimator(input_data)
    print(estimated_data)
