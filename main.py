def maximize_earnings(jobs):
  sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

  lokesh_jobs = []
  lokesh_earnings = 0

  remaining_jobs = len(jobs)
  remaining_earnings = sum([job[2] for job in jobs])

  for job in sorted_jobs:
    start_time = job[0]
    end_time = job[1]
    profit = job[2]

    conflicts = False
    for i in range(len(lokesh_jobs)):
      if start_time < lokesh_jobs[i][1] and end_time > lokesh_jobs[i][0]:
        conflicts = True
        break
    
    if not conflicts:
      lokesh_jobs.append(job)
      lokesh_earnings += profit
      remaining_jobs -= 1
      remaining_earnings -= profit

  return (remaining_jobs, remaining_earnings)

def parse_input():
  num_jobs = int(input("Enter the number of Jobs:\n"))
  
  jobs = []
  print("Enter job start time, end time, and earnings:")
  
  for i in range(num_jobs):
  
    start_time = int(input())
    end_time = int(input())
    profit = int(input())

    jobs.append((start_time, end_time, profit))
  return jobs


jobs = parse_input()
tasks,earnings = maximize_earnings(jobs)
print('The number of tasks and earnings available for others')
print(f'Tasks: {tasks}')
print(f'Earnings: {earnings}')