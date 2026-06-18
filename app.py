import streamlit as st
from modules.classifier import classify_complaint
from modules.entity_extractor import extract_entities
from modules.responder import generate_response_to_complaint
from database import init_db, save_ticket, get_all_tickets

# Initialize database on app start
init_db()

st.set_page_config(page_title="AI Customer Support System", layout="wide")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Submit Complaint", "Dashboard"])

if page == "Submit Complaint":
    st.title("🎫 AI-Powered Customer Support System")
    st.write("Submit a complaint and let AI classify, analyze, and respond.")
    st.caption("📌 This system classifies complaints into one of three categories: **Technical Issue**, **Billing Inquiry**, or **Product Feedback**.")
    complaint = st.text_area("Enter customer complaint:", height=120)

    if st.button("Submit"):
        if not complaint.strip():
            st.warning("Please enter a complaint first.")
        else:
            with st.spinner("Analyzing complaint..."):
                category = classify_complaint(complaint)
                entities = extract_entities(complaint)
                response = generate_response_to_complaint(complaint)

                save_ticket(
                    complaint=complaint,
                    category=category,
                    product=entities.get("product", "Unknown"),
                    issue_summary=entities.get("issue_summary", "Unknown"),
                    urgency=entities.get("urgency", "Unknown"),
                    sentiment=entities.get("sentiment", "Unknown"),
                    response=response
                )

            st.success("Ticket processed and saved!")

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Classification")
                st.write(f"**Category:** {category}")
                st.write(f"**Product:** {entities.get('product')}")
                st.write(f"**Urgency:** {entities.get('urgency')}")
                st.write(f"**Sentiment:** {entities.get('sentiment')}")

            with col2:
                st.subheader("AI Response")
                st.write(entities.get("issue_summary"))
                st.info(response)

elif page == "Dashboard":
    st.title("📊 Support Ticket Dashboard")

    tickets = get_all_tickets()

    if not tickets:
        st.info("No tickets yet. Submit a complaint first.")
    else:
        import pandas as pd
        df = pd.DataFrame(tickets, columns=[
            "ID", "Complaint", "Category", "Product",
            "Issue Summary", "Urgency", "Sentiment", "Response", "Created At"
        ])

        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            category_filter = st.multiselect("Filter by Category", df["Category"].unique())
        with col2:
            urgency_filter = st.multiselect("Filter by Urgency", df["Urgency"].unique())
        with col3:
            sentiment_filter = st.multiselect("Filter by Sentiment", df["Sentiment"].unique())

        filtered_df = df
        if category_filter:
            filtered_df = filtered_df[filtered_df["Category"].isin(category_filter)]
        if urgency_filter:
            filtered_df = filtered_df[filtered_df["Urgency"].isin(urgency_filter)]
        if sentiment_filter:
            filtered_df = filtered_df[filtered_df["Sentiment"].isin(sentiment_filter)]

        st.dataframe(filtered_df, use_container_width=True)
        st.caption(f"Showing {len(filtered_df)} of {len(tickets)} total tickets")