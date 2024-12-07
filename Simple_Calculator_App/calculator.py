import streamlit as st

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            st.error("⚠️ Division by zero is not allowed!")
            return None
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            st.error("⚠️ Division by zero is not allowed!")
            return None
        return num1 % num2

def main():
    st.title("🔢 Simple Calculator App 🧮")
    st.markdown("""
    This app allows you to perform basic arithmetic operations: 
    - **Addition**: ➕ 
    - **Subtraction**: ➖
    - **Multiplication**: ✖️
    - **Division**: ➗
    - **Modulus**: %
    """)
    
    # Create input fields
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", format="%.2f")
    with col2:
        num2 = st.number_input("Enter second number", format="%.2f")

    # Select operation
    operation = st.selectbox("Select operation", ["+", "-", "*", "/", "%"])
    
    # Perform calculation and display result
    if st.button("Calculate"):
        result = calculator(num1, num2, operation)
        if result is not None:
            st.success(f"Result: **{result}**")

    
    st.write("""
### - This app is made by **Ghulam Hussain Khuhro**  
Check out the [GitHub repository](https://github.com/ghulamhussainkhuhro/Streamlit_Apps/tree/main/Simple_Calculator_App)  
Connect with me on [LinkedIn](https://www.linkedin.com/in/ghulamhussainkhuhro)
""")


if __name__ == "__main__":
    main()
