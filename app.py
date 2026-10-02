import streamlit as st

from notebook_logic import COSTS, PROMISE, TIME_BLOCKS, ZONES, best_promise


st.set_page_config(page_title="Delivery Promise Recommender")
st.title("Delivery Promise Recommender")

with st.form("recommendation_inputs"):
    zone = st.selectbox("Zone", ZONES)
    time_block = st.selectbox("Time block", TIME_BLOCKS)

    default_minimum_promise = max(5, PROMISE - 20)
    default_maximum_promise = PROMISE + 20
    minimum_promise = st.number_input(
        "Minimum promised time (minutes)",
        min_value=5,
        value=default_minimum_promise,
        step=5,
    )
    maximum_promise = st.number_input(
        "Maximum promised time (minutes)",
        min_value=5,
        value=default_maximum_promise,
        step=5,
    )

    margin = st.number_input(
        "Profit margin per order",
        min_value=0.0,
        value=float(COSTS["margin"]),
        step=0.5,
    )
    churn_orders = st.number_input(
        "Estimated churn per late order (orders)",
        min_value=0.0,
        value=float(COSTS["churn_orders"]),
        step=0.5,
    )
    refund = st.number_input(
        "Refund cost per late order",
        min_value=0.0,
        value=float(COSTS["refund"]),
        step=1.0,
    )

    submitted = st.form_submit_button("Find recommended promise")

if submitted:
    if minimum_promise % 5 != 0 or maximum_promise % 5 != 0:
        st.error("Promised times must be multiples of 5 minutes.")
    elif minimum_promise > maximum_promise:
        st.error("Minimum promised time must not exceed maximum promised time.")
    else:
        promises = list(range(int(minimum_promise), int(maximum_promise) + 1, 5))
        costs = {
            **COSTS,
            "margin": margin,
            "churn_orders": churn_orders,
            "refund": refund,
        }
        recommended_promise, net_profit = best_promise(
            zone,
            time_block,
            promises,
            costs,
        )

        st.subheader("Recommendation")
        st.metric("Promised time", f"{recommended_promise} minutes")
        st.metric("Net profit", f"${net_profit:,.2f}")