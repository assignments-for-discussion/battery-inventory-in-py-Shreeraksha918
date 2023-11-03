
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
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
