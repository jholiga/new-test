"""Pure-Python frontend via Streamlit — every visible string is in this file."""
import streamlit as st

# Page-level config: page_title is a browser tab title (user-facing).
# page_icon is an emoji shortcode — code-level, not product copy.
st.set_page_config(
    page_title="Account dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Welcome to your dashboard")
st.markdown(
    "Track your activity, manage settings, and access reports — all in one place."
)

with st.sidebar:
    st.header("Filters")
    date_range = st.selectbox(
        "Choose a time range",
        options=["Last 7 days", "Last 30 days", "All time"],
    )
    show_archived = st.checkbox("Include archived items", value=False)

# Tricky: column key is a code identifier, not a user-visible label.
left_col, right_col = st.columns([2, 1], gap="medium")

with left_col:
    st.subheader("Recent activity")
    if st.button("Generate report", key="generate_report_btn"):
        with st.spinner("Crunching the numbers..."):
            st.success("Your report is ready to download.")

with right_col:
    st.subheader("Quick stats")
    st.metric(label="Active sessions", value=42, delta=3)

st.info(
    """
    Pro tip: pin your most-used reports to the top of the dashboard
    for one-click access. This is especially handy when you check the
    same metrics every morning.
    """
)

# Developer-facing — should NOT be flagged.
LOG_PREFIX = "streamlit_dashboard"
st.caption(f"Build: {LOG_PREFIX}-2026.04")
