import streamlit as st
import pandas as pd
import requests
import io
import plotly.express as px

st.set_page_config(page_title="Log Classifier Dashboard", layout="wide")

st.title("🧠 Log Classification & Analytics Dashboard")

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Classify Logs"

if "classified_df" not in st.session_state:
    st.session_state["classified_df"] = None


# ---------------- PAGE 1: CLASSIFICATION ----------------
if st.session_state["page"] == "Classify Logs":
    uploaded_file = st.file_uploader("Upload a log CSV file", type=["csv"])
    
            # ---------------- SAMPLE LOG FILE DOWNLOAD ----------------
    st.markdown("### 📂 Need a sample log file? Download below:")

    try:
            with open("../Sample_log_files.csv", "rb") as f:
                sample_data = f.read()

            st.download_button(
                label="⬇️ Download Sample Log File",
                data=sample_data,
                file_name="sample_logs.csv",
                mime="text/csv",
            )
    except FileNotFoundError:
            st.error("⚠️ Sample log file not found. Check file path or name.")


    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("📄 Uploaded Logs:")
        st.dataframe(df.head())

        # Classification button
        if st.button("🔍 Classify Logs"):
            with st.spinner("Classifying logs... Please wait ⏳"):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
                    response = requests.post("https://log-classifier-backend-2a78.onrender.com/classify", files=files)

                    if response.status_code == 200:
                        classified_csv = response.content
                        classified_df = pd.read_csv(io.BytesIO(classified_csv))

                        # Save in session
                        st.session_state["classified_df"] = classified_df

                        st.success("✅ Classification Complete!")
                        st.dataframe(classified_df.head())

                    else:
                        st.error(f"❌ API Error: {response.status_code} - {response.text}")

                except Exception as e:
                    st.error(f"🚨 Error: {e}")

        # Show Analyse button only if classification is done
        if st.session_state["classified_df"] is not None:
            st.markdown("---")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.download_button(
                    label="⬇️ Download Classified CSV",
                    data=st.session_state["classified_df"].to_csv(index=False).encode(),
                    file_name="classified_logs.csv",
                    mime="text/csv",
                )
            with col2:
                if st.button("📊 Analyse Logs"):
                    st.session_state["page"] = "Analytics"
                    st.rerun()  # Redirect works properly here


# ---------------- PAGE 2: ANALYTICS ----------------
elif st.session_state["page"] == "Analytics":
    st.subheader("📈 Your Logs Classification Report")

    if "classified_df" in st.session_state and st.session_state["classified_df"] is not None:
        df = st.session_state["classified_df"]

        # ---------------- METRICS ----------------
        st.markdown("### 📊 Quick Metrics Overview")
        total_events = len(df)
        unique_sources = len(df['source'].unique()) if "source" in df.columns else 0
        total_errors = df[df["target_label"].str.lower()=="error"].shape[0] if "target_label" in df.columns else 0
        user_actions = df[df["target_label"].str.lower()=="user action"].shape[0] if "target_label" in df.columns else 0
        security_alerts = df[df["target_label"].str.contains("security alert", case=False, na=False)].shape[0] if "target_label" in df.columns else 0
        critical_errors=df[df["target_label"].str.contains("Critical error", case=False, na=False)].shape[0] if "target_label" in df.columns else 0

        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)

        col1.metric("📁 Total Events", total_events)
        col2.metric("🧩 Unique Sources", unique_sources)
        col3.metric("🚨 Error Logs", total_errors)
        col4.metric("👥 User Actions(Login/Logout)", user_actions)
        col5.metric("🛡️ Security Alerts", security_alerts)
        col6.metric("🔥 Critical Errors", critical_errors)

        # ---------------- CHARTS SECTION ----------------
        st.markdown("---")
        st.subheader("📈 Visual Insights from Logs")

        chart_col1, chart_col2 = st.columns(2)
        if "target_label" in df.columns:
            with chart_col1:
                fig1 = px.histogram(
                    df,
                    x="target_label",
                    title="Distribution of Predicted Log Categories",
                    color="target_label"
                )
                st.plotly_chart(fig1, use_container_width=True)

        if "source" in df.columns:
            with chart_col2:
                source_counts = df["source"].value_counts().reset_index()
                source_counts.columns = ["Source", "Count"]
                fig2 = px.bar(
                     source_counts,
                     x="Source",
                     y="Count",
                     title="Top Log Sources",
                     color="Source"
                )
                st.plotly_chart(fig2, use_container_width=True)

        # ---------------- EVENT TYPE PIE ----------------
        bottom_col1, bottom_col2 = st.columns(2)
        with bottom_col1:
            counts = {
                "Errors": total_errors,
                "Critical_Errors": critical_errors,
                "User Actions": user_actions,
                "Security Alerts": security_alerts,
                
            }
            count_df = pd.DataFrame(list(counts.items()), columns=["Event Type", "Count"])
            fig3 = px.pie(count_df, names="Event Type", values="Count", title="Event Type Proportion")
            st.plotly_chart(fig3, use_container_width=True)

        if "target_label" in df.columns:
            with bottom_col2:
                 label_counts = df["target_label"].value_counts().head(5).reset_index()
                 label_counts.columns = ["Target Label", "Count"]
                 fig4 = px.bar(
                    label_counts,
                    x="Target Label",
                    y="Count",
                    title="Top 5 Target Labels",
                    color="Target Label"
                  )
                 st.plotly_chart(fig4, use_container_width=True)

        # ---------------- SUMMARY TABLE ----------------
        st.markdown("---")
        st.subheader("🧾 Summary Table")
        summary_data = {
            "Total Events": [total_events],
            "Unique Sources": [unique_sources],
            "Error Logs": [total_errors],
            "Critical Errors": [critical_errors],
            "User Actions": [user_actions],
            "Security Alerts": [security_alerts]
        }
        st.dataframe(pd.DataFrame(summary_data))

        # ---------------- BACK BUTTON ----------------
        st.markdown("---")
        if st.button("⬅️ Back to Classification"):
            st.session_state["page"] = "Classify Logs"
            st.rerun()
    else:
        st.warning("⚠️ No classified data found. Please classify logs first from the main page.")