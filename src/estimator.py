def estimator(data):

  period_type = data["period_type"]
  period = data["time_to_elapse"]
  
  no_of_days = normalize_period_to_days(period_type, period)
  factor = no_of_days / 3
  
  reported_cases = data["reported_cases"]
  
  currently_infected_best_case = reported_cases * 10
  infections_by_request_time_best_case = \
    currently_infected_best_case * (2 ** factor)
   
  currently_infected_worst_case = reported_cases * 50
  infections_by_request_time_worst_case = \
    currently_infected_worst_case * (2 ** factor)

# challenge One Ends


# Estimation result

final_data = {
  "data": data,
  "impact": {
    "currently_infected": currently_infected_best_case,
    "infections_by_request_time": infections_by_request_time_best_case,
  },
  "severe_impact": {
    "currently_infected": currently_infected_worst_case,
    "infections_by_request_time": infections_by_request_time_worst_case, 
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
      "avg_age": 19.7,
      "avg_daily_income_in_USD": 5,
      "avg_daily_income_population": 0.71
    },
    "period_type": "days",
    "time_to_elapse": 58,
    "reported_cases": 674,
    "population": 66622705,
    "total_hospital_beds": 1380614
  }
  
  estmated_data = estimator(input_data)
  print(estmated_data)