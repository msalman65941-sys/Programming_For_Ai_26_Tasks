from support_engine import classify_support, format_message


assert classify_support(59.9, 90, 0) == "High Priority"
assert classify_support(60, 90, 4) == "High Priority"
assert classify_support(74.9, 90, 0) == "Moderate Priority"
assert classify_support(75, 59.9, 0) == "Moderate Priority"
assert classify_support(90, 90, 2) == "Moderate Priority"
assert classify_support(75, 60, 1) == "Routine Monitoring"
assert classify_support(100, 100, 0) == "Routine Monitoring"

print("All tests passed successfully.")
