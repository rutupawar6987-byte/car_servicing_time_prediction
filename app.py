from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    vehicle_type = request.form['vehicle_type']
    condition = request.form['condition']
    spare_avail = request.form['spare_avail']
    staff_exp = int(request.form['staff_exp'])
    parts_type = request.form['parts_type']
    year = int(request.form['year'])

    # Base time depending on vehicle type
    vehicle_time = {
        "Car": 2,
        "Van": 2.5,
        "Truck": 4,
        "Bus": 5,
        "Machine": 6,
        "Tractor": 4,
        "Crane": 6,
        "Bike": 1,
        "Scooter": 1.5
    }

    base_time = vehicle_time.get(vehicle_type, 2)  # default 2 hours

    # Modifiers
    if condition == "Poor":
        base_time += 1
    elif condition == "Average":
        base_time += 0.5

    if spare_avail.lower() == "no":
        base_time += 0.5
    elif spare_avail.lower() == "partial":
        base_time += 0.3
    elif spare_avail.lower() == "delayed":
        base_time += 0.7

    if staff_exp < 2:
        base_time += 0.5
    elif staff_exp < 5:
        base_time += 0.3

    if parts_type.lower() == "new":
        base_time -= 0.3
    elif parts_type.lower() == "refurbished":
        base_time += 0.3
    elif parts_type.lower() == "local":
        base_time += 0.2
    elif parts_type.lower() == "imported":
        base_time -= 0.1

    if year < 2000:
        base_time += 0.5
    elif year < 2010:
        base_time += 0.3

    pred_time = f"{round(base_time, 1)} hours"

    # Recommendation
    if base_time <= 2:
        recommendation = "Standard service schedule is sufficient."
    elif base_time <= 4:
        recommendation = "Consider extra inspection for worn parts."
    else:
        recommendation = "Full maintenance check recommended before service."

    # Map vehicle to icon
    icon_map = {
        "Car": "fa-car",
        "Truck": "fa-truck",
        "Van": "fa-van-shuttle",
        "Bus": "fa-bus",
        "Machine": "fa-industry",
        "Tractor": "fa-tractor",
        "Crane": "fa-dharmachakra",
        "Bike": "fa-motorcycle",
        "Scooter": "fa-motorcycle"
    }
    vehicle_icon = icon_map.get(vehicle_type, "fa-car")

    return render_template('result.html',
                           pred_time=pred_time,
                           vehicle_icon=vehicle_icon,
                           vehicle_type=vehicle_type,
                           condition=condition,
                           spare_avail=spare_avail,
                           staff_exp=staff_exp,
                           parts_type=parts_type,
                           year=year,
                           recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)
