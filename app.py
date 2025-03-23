import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def main():
    st.title("Unit Converter")
    
    category = st.selectbox("Select category", ["Length", "Weight", "Temperature"])
    
    if category == "Length":
        units = ["meters", "kilometers", "miles", "yards", "feet"]
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units)
        value = st.number_input("Enter value", min_value=0.0, format="%.6f")
        if st.button("Convert"):
            result = length_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
    
    elif category == "Weight":
        units = ["grams", "kilograms", "pounds", "ounces"]
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units)
        value = st.number_input("Enter value", min_value=0.0, format="%.6f")
        if st.button("Convert"):
            result = weight_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
    
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units)
        value = st.number_input("Enter value", format="%.2f")
        if st.button("Convert"):
            result = temperature_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    
if __name__ == "__main__":
    main()
