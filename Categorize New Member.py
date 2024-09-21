def open_or_senior(data):
    result = ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
    return result
