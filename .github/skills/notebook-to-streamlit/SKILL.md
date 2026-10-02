---
name: notebook-to-streamlit
description: Convert logic from a Jupyter notebook into a Streamlit app. Use when asked to build or update the Streamlit app that recommends Rosa's best promised delivery time.
---

# Notebook to Streamlit

## Goal
Reuse the notebook's existing logic in a Streamlit app. Do not rewrite or change the calculations.

## Project structure
- `notebook_logic.py` holds the notebook functions: `cost_per_late_order`, `net_profit`, `best_promise`.
- `delivery_times` and `COSTS` come from the `rosa-starter` package (installed with uv). Import them; never redefine them.
- `app.py` is the Streamlit interface and only imports from `notebook_logic.py`.

## Steps
1. Read `notebook_logic.py` and reuse its functions as they are.
2. In `app.py`, build the `costs` dictionary from user inputs, using the same keys as `COSTS`, and pass it to `best_promise`.
3. Use `st.selectbox` for zone and time block. Use inputs for the range of promised times (min, max, step 5), profit margin per order, churn per late order, and refund cost per late order, defaulting to the values in `COSTS`.
4. Call `best_promise` only when the button is clicked, then show the recommended promise and its net profit.
5. Keep results identical to the notebook for the same inputs.

## Conventions
- Zones: Central, North, Far West
- Time blocks: Lunch, Weekday eve, Fri/Sat eve, Other
- COST: refund, churn orders, margin
- Promises are in minutes, in steps of 5.
- Use `uv` for dependencies. Do not add new dependencies without asking.
- Keep code simple and beginner-friendly.