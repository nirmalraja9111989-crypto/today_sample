# crop_analyzer.py

def analyze_crop(soil_type, rainfall):
    soil_type = soil_type.lower()

    if rainfall < 0:
        raise ValueError("Rainfall cannot be negative")

    if soil_type == "clay" and rainfall > 200:
        return ["Rice"]

    elif soil_type == "sandy" and rainfall < 100:
        return ["Millet"]

    elif soil_type == "loamy" and 100 <= rainfall <= 200:
        return ["Wheat", "Maize"]

    elif soil_type == "black" and 50 <= rainfall <= 150:
        return ["Cotton"]

    else:
        return ["No suitable crop found"]

print("Success")
