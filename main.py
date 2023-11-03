
def count_batteries_by_health(present_capacities):
  count_healthy=0
  count_exchange=0
  count_failed=0
  for cpcty in present_capacities:
    rated_cpcty=120
    SoH=(cpcty/rated_cpcty)*100
    if SoH >=80:
      count_healthy+=1
    elif 62<=SoH <80:
      count_exchange+=1
    else:
      count_failed+=1
      
    
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }


def test_bucketing_by_health():
  
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)

  #mixed batteries with boundary values
  present_capacities=[80,62,79,61,63,81,60]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 2)
  
  #All healthy batteries
  present_capacities=[80,90,100,105,95,88]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 6)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)

  #All exchange batteries
  present_capacities=[62,70,65,66,75,79]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 6)
  assert(counts["failed"] == 0)
  
  #All failed batteries
  present_capacities=[50,40,55,53,25,61]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 6)

  # healthy and exchange batteries
  present_capacities=[63,90,77,80,100,99]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 4)
  assert(counts["exchange"] == 2)
  assert(counts["failed"] == 0)

  #healthy and failed batteries
  present_capacities=[50,90,40,105,60,88]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 3)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 3)

  #exchange and failed batteries
  present_capacities=[79,61,55,53,43,62]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 4)

  # mixes batteries with repetative value
  present_capacities=[80,80,100,105,63,63,77,45,45,50]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 4)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 3)

  #empty present capacitance list
  present_capacities=[]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)

  #one item in list
  present_capacities=[120]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 1)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)

  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
