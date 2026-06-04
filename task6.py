target_units = int(input("Enter target units: "))
workers_per_shift = int(input("Enter workers per shift: "))
defect_rate = float(input("Enter defect rate (%): "))

total_produced = 0
total_defects = 0
shift = 1

while total_produced < target_units:

    print(f"\n===== Shift {shift} =====")

    shift_produced = 0
    shift_defects = 0

    # Simulate 3 shifts × 20 machine cycles
    for worker in range(1, workers_per_shift + 1):

        for cycle in range(1, 21):

            item_id = worker * 100 + cycle

            # Random defect rule
            if item_id % int(100 / defect_rate) == 0:
                shift_defects += 1
                total_defects += 1
                continue

            shift_produced += 1
            total_produced += 1

            # Stop when target reached
            if total_produced >= target_units:
                break

        if total_produced >= target_units:
            break

    productivity = shift_produced / workers_per_shift

    print(f"Items Produced : {shift_produced}")
    print(f"Defective Items: {shift_defects}")
    print(f"Productivity   : {productivity:.2f} items/worker")

    shift += 1

print("\n===== PRODUCTION SUMMARY =====")
print(f"Target Units Reached : {target_units}")
print(f"Total Good Items     : {total_produced}")
print(f"Total Defects        : {total_defects}")

if (total_produced + total_defects) > 0:
    defect_percentage = (total_defects /
                         (total_produced + total_defects)) * 100
    print(f"Overall Defect Rate  : {defect_percentage:.2f}%")