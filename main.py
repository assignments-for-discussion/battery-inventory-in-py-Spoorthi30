
def count_batteries_by_health(present_capacities):
  #Initializing counts for each category of battery
  healthy_count=0
  exchange_count=0
  failed_count=0

  #Rated capacity
  rated_capacity=120  #Ah

  for present_capacity in present_capacities:
    SoH = 100 * (present_capacity / rated_capacity)

    if SoH>80:
      healthy_count+=1
    elif 62<=SoH<=80:
      exchange_count+=1
    else:
      failed_count+=1



  return {
    "healthy": healthy_count,
    "exchange": exchange_count,
    "failed": failed_count
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")

  print("Counting batteries by SoH...\n")
  present_capacities = [100,110,90,80,50,60,70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 3)
  assert(counts["exchange"] == 2)
  assert(counts["failed"] == 2)
  print("Done counting :)")

  print("Counting batteries by SoH...\n")
  present_capacities = [100,100,100,100,100,100]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 6)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
