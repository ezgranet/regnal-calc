import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta
import csv
from dateutil.parser import parse

def load_csv(filename):
    """Load CSV file and return its contents."""
    with open(filename, 'r') as csvfile:
        return list(csv.reader(csvfile))

def parse_date(date_str):
    """Parse date string to datetime object."""
    return datetime.datetime.strptime(date_str, '%d/%m/%Y')

def calculate_regnal_year(input_date):
    """Calculate regnal year based on input Gregorian date."""
    john_data = load_csv('john.csv')
    kings_data = load_csv('rgnl1.csv')

    # Check date boundaries
    if input_date <= parse_date('13/10/1066'):
        return "Too early!"
    elif input_date >= parse_date('13/10/2072'):
        return "Too far in the future!"

    # Special case for Henry VI Readeption
    if parse_date('3/10/1470') <= input_date <= parse_date('21/5/1471'):
        return "49 Henry VI"

    # Check John's reign
    if parse_date('27/5/1199') <= input_date <= parse_date('19/10/1216'):
        for row in john_data:
            if parse_date(row[1]) <= input_date <= parse_date(row[2]):
                return f"{row[0]} (John)"

    # Check other monarchs
    if parse_date('20/10/1216') <= input_date <= parse_date('12/10/2072'):
        for row in kings_data:
            start_date = parse_date(row[1])
            if start_date <= input_date <= parse_date(row[2]):
                years_diff = relativedelta(input_date, start_date).years + 1
                return f"{years_diff} {row[0]}"

    return "No data found"

def calculate_date_range(monarch, regnal_year):
    """Calculate date range for a specific monarch and regnal year."""
    john_data = load_csv('john.csv')
    kings_data = load_csv('rgnl1.csv')

    # Specific handling for some monarchs
    special_monarchs = {
        'john': (john_data, 'John'),
        '49 henry vi': 'Readeption',
        'charles iii': 44,
        'elizabeth ii': 43,
        'george vi': 42,
        'edward viii': 41,
        'george v': 40,
        'edward vii': 39,
        'victoria': 38,
        'william iv': 37,
        'george iv': 36,
        'george iii': 35,
        'george ii': 34,
        'george i': 33,
        'anne': 32,
        'william iii': 31,
        'william and mary': 30,
        'james ii': 28,
        'charles ii': 27,
        'charles i': 25,
        'james i': 24,
        'elizabeth i': 23,
        'philip and mary': 22,
        'mary': 21,
        'edward vi': 20,
        'henry viii': 19,
        'henry vii': 18,
        'richard iii': 17,
        'edward v': 16,
        'edward iv': 15,
        'henry vi': 14,
        'henry v': 13,
        'henry iv': 12,
        'richard ii': 10,
        'edward iii': 9,
        'edward ii': 8,
        'edward i': 7,
        'henry iii': 6,
        'richard i': 5,
        'henry ii': 4,
        'stephen': 3,
        'henry i': 2,
        'william ii': 1,
        'william i': 0
    }

    # Handle date conversion for special monarchs
    if monarch.lower() in special_monarchs:
        if isinstance(special_monarchs[monarch.lower()], tuple):
            data, monarch_name = special_monarchs[monarch.lower()]
            return f"Use the {monarch_name} CSV for detailed information"
        
        row_val = special_monarchs[monarch.lower()]
        kings_data = load_csv('rgnl1.csv')
        
        try:
            accession_date = parse_date(kings_data[row_val][1])
            start_date = accession_date + relativedelta(years=int(regnal_year) - 1) - relativedelta(days=1)
            end_date = accession_date + relativedelta(years=int(regnal_year)) - relativedelta(days=1)
            return f"{start_date} to {end_date}"
        except:
            return "No data found"

    return "Monarch not found"

def main():
    st.title("Regnal Year Calculator")

    # Tabs for different functionalities
    tab1, tab2 = st.tabs(["Gregorian to Regnal Year", "Regnal Year to Gregorian"])

    with tab1:
        st.header("Calculate Regnal Year for a Gregorian Date")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            year = st.number_input("Year", min_value=1066, max_value=2072, value=2024)
        with col2:
            month = st.number_input("Month", min_value=1, max_value=12, value=1)
        with col3:
            day = st.number_input("Day", min_value=1, max_value=31, value=1)

        if st.button("Calculate Regnal Year for a Gregorian Date"):
            try:
                input_date = datetime.datetime(year, month, day)
                result = calculate_regnal_year(input_date)
                st.success(f"Regnal Year: {result}")
            except ValueError:
                st.error("Invalid date. Please check your input.")

    with tab2:
        st.header("Find Date Range for a Monarch's Regnal Year")
        monarch = st.text_input("Monarch Name (e.g., Elizabeth II, Henry VIII)", 
                                help="Use full name with Roman numeral, like 'Elizabeth II'")
        regnal_year = st.number_input("Regnal Year", min_value=1, max_value=100, value=1)

        if st.button("Find Date Range"):
            result = calculate_date_range(monarch, regnal_year)
            st.success(result)

    # Additional information
    st.markdown("""
    ### Instructions
    - For the first tab, enter a Gregorian date to find its regnal year
    - For the second tab, enter a monarch's name and their regnal year
    - Dates must be between 1066 (and all that) and 2072
    - Use full monarch names with Roman numerals (e.g., 'Elizabeth II')
    - If something is broken or you just want to say something, get in touch with me, Elijah Granet, via e-mail [by clicking this link](mailto:&#101;&#100;&#105;&#116;&#111;&#114;&#64;&#108;&#101;&#103;&#97;&#108;&#115;&#116;&#121;&#108;&#101;&#46;&#99;&#111;&#46;&#117;&#107;)	
    """)

if __name__ == "__main__":
    main()
