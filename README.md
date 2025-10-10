# 🚗 Car/Machine Service Time Prediction


## **Project Overview**

The **Car/Machine Service Time Prediction** project is a **web-based application** that predicts the **service duration** of vehicles and machines based on multiple factors, such as:

- Vehicle condition  
- Service type  
- Staff experience  
- Spare parts availability  
- Workload  
- Year of manufacture  

It integrates **machine learning models** with a **Flask web application** to provide actionable insights for predictive maintenance.

---

## **Features**

- ✅ Simple and user-friendly web interface  
- ✅ Input fields:  
  - Vehicle/Machine Type (Car, Truck, Van)  
  - Condition (Good, Average, Poor)  
  - Spare Parts Availability (Yes/No)  
  - Staff Experience (Years)  
  - Spare Parts Type (New, Own)  
  - Year of Manufacture  
- ✅ Predicts service time using **Random Forest ML model**  
- ✅ Displays results clearly with **recommendations**  

---

## **Tech Stack**

- **Backend:** Python, Flask  
- **Machine Learning:** scikit-learn, pandas, numpy  
- **Frontend:** HTML, CSS, JavaScript  
- **Model Storage:** Pickle (`rf_model.pkl`)  

---

## **Installation & Running Locally**

1. Clone the repository:

```bash
git clone https://github.com/rutupawar6987-byte/car_servicing_time_prediction.git
cd car_servicing_time_prediction


---

2 Create a virtual environment (optional but recommended):
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
3 Install required packages:
pip install flask pandas numpy scikit-learn

4 python app.py

5 Open your browser at http://127.0.0.1:5000

Usage

1 Fill out the vehicle/machine details form.

2 Click Predict Service Time.

3 View the predicted service duration and recommendations on the results page.

Dataset

The dataset includes historical records of vehicle/machine service times.

Features: vehicle_type, condition, service_type, staff_exp, spare_avail, workload, year

Target: predicted_service_time

You can generate your own dataset or use simulated data for testing.

##Project Structure
car_servicing_time_prediction/
│
├─ app.py                # Flask backend
├─ train_models.py       # Script to train ML models
├─ rf_model.pkl          # Trained Random Forest model
├─ dataset.csv           # Sample dataset
├─ templates/
│   ├─ index.html        # Input form
│   └─ result.html       # Results page

##Future Enhancements

Add real-time analytics dashboard for workload vs service time

Mobile-first responsive design

Add multiple ML models for comparison

Integrate with a database for storing historical predictions



