# Demographic Data Analyzer | Python + Pandas

Analyzed 32,000+ census records from the 1994 US Census using Python and Pandas to answer 9 business questions about age, education, income, working hours, and country.

## What I did
- Cleaned and analyzed `adult.data.csv` with Pandas (groupby, filtering, percentage calculation)
- Answered 9 questions: race distribution, average age, education vs income, minimum working hours, top country for high income, top occupation in India
- Validated results with unit test - `Ran 1 test - OK`

## Key Findings
- Average age of men: 39.4 years
- Only 16.4% have a Bachelor's degree, but 46.5% of highly educated earn >50K vs 17.4% without higher education
- Country with highest % of high earners: Iran (41.9%)
- Top occupation for high earners in India: Prof-specialty

## How this applies to Admin / Finance work
Same technique I use for finance work:
Census data -> Expense / SPJ data, Demographic groups -> Vendor / Category, Income >50K -> Expense anomaly / Budget variance.
I can clean messy Excel / CSV, build monthly reports, and find patterns for management.

## How to run
pip install -r requirements.txt
python main.py

## Skills: Python, Pandas, Data Cleaning, Data Analysis, Reporting
