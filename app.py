# app.py
# Run using: python -m streamlit run app.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="WPAssist AI", layout="wide")

# -----------------------------
# WordPress Issue Classifier
# -----------------------------
def diagnose_issue(text):
    text = text.lower()

    if any(word in text for word in ["plugin", "update broke", "after update"]):
        return "Plugin Conflict", "High", [
            "Deactivate all plugins temporarily.",
            "Reactivate plugins one by one.",
            "Identify the conflicting plugin.",
            "Update plugin or contact vendor."
        ]

    elif any(word in text for word in ["theme", "layout broken", "design issue"]):
        return "Theme Issue", "Medium", [
            "Switch to default WordPress theme.",
            "Check theme customization settings.",
            "Update theme to latest version.",
            "Review recent code edits."
        ]

    elif any(word in text for word in ["login", "password", "admin access", "locked out"]):
        return "Account Access", "High", [
            "Use password reset option.",
            "Check admin email inbox.",
            "Disable security plugin if locked out.",
            "Reset via database if needed."
        ]

    elif any(word in text for word in ["slow", "performance", "loading time"]):
        return "Performance Issue", "Medium", [
            "Clear site cache.",
            "Optimize images.",
            "Deactivate heavy plugins.",
            "Use CDN / caching plugin."
        ]

    elif any(word in text for word in ["checkout", "payment", "woocommerce"]):
        return "WooCommerce Issue", "High", [
            "Check payment gateway settings.",
            "Test checkout in incognito mode.",
            "Disable conflicting plugins.",
            "Enable WooCommerce logs."
        ]

    elif any(word in text for word in ["ssl", "domain", "https"]):
        return "Domain / SSL Issue", "High", [
            "Verify DNS records.",
            "Check SSL certificate validity.",
            "Force HTTPS in settings.",
            "Clear browser cache."
        ]

    else:
        return "General Support", "Low", [
            "Gather more issue details.",
            "Check recent changes.",
            "Review error messages.",
            "Escalate if unresolved."
        ]

# -----------------------------
# Suggested Support Reply
# -----------------------------
def generate_reply(category):
    replies = {
        "Plugin Conflict": "We detected a possible plugin conflict. Please deactivate plugins temporarily and reactivate one by one.",
        "Theme Issue": "This may be related to your theme settings or recent updates. Please test with a default theme.",
        "Account Access": "We understand you're unable to access your account. Please use the password reset option first.",
        "Performance Issue": "Your site may be affected by caching or heavy plugins. Please clear cache and test speed again.",
        "WooCommerce Issue": "We identified a WooCommerce-related issue. Please review payment gateway and plugin conflicts.",
        "Domain / SSL Issue": "This may be caused by DNS or SSL configuration. Please verify records and certificate status.",
        "General Support": "Thank you for contacting support. We are reviewing your request now."
    }
    return replies.get(category, replies["General Support"])

# -----------------------------
# Sample Dashboard Data
# -----------------------------
df = pd.DataFrame({
    "Issue Type": [
        "Plugin Conflict",
        "Theme Issue",
        "Account Access",
        "Performance",
        "WooCommerce",
        "SSL / Domain"
    ],
    "Tickets": [180, 95, 130, 120, 145, 80]
})

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("WPAssist AI")
page = st.sidebar.radio("Navigation", [
    "Home",
    "Diagnose Issue",
    "Dashboard",
    "About"
])

# -----------------------------
# Home
# -----------------------------
if page == "Home":
    st.title("🚀 WPAssist AI")
    st.subheader("AI-Powered WordPress & WooCommerce Support Assistant")

    st.write("""
    Diagnose common WordPress issues instantly, guide users with solutions,
    and improve support team productivity.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Weekly Tickets", "2,100")
    col2.metric("Avg Resolution Time", "9 hrs")
    col3.metric("CSAT Score", "88%")

# -----------------------------
# Diagnose Page
# -----------------------------
elif page == "Diagnose Issue":
    st.title("🛠 WordPress Issue Diagnosis")

    ticket = st.text_area("Describe your issue")

    if st.button("Analyze Issue"):
        if ticket.strip():
            category, severity, steps = diagnose_issue(ticket)
            reply = generate_reply(category)

            st.success("Diagnosis Complete")

            c1, c2 = st.columns(2)
            c1.metric("Issue Type", category)
            c2.metric("Severity", severity)

            st.subheader("Recommended Fix Steps")
            for step in steps:
                st.write(f"✅ {step}")

            st.subheader("Suggested Support Reply")
            st.info(reply)

            st.caption(
                f"Analyzed at: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
            )
        else:
            st.warning("Please describe your issue.")

# -----------------------------
# Dashboard
# -----------------------------
elif page == "Dashboard":
    st.title("📊 Support Analytics Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Resolved Today", "260")
    col2.metric("Open Critical", "19")
    col3.metric("Automation Rate", "54%")

    st.subheader("Tickets by Issue Type")
    st.bar_chart(df.set_index("Issue Type"))

    st.subheader("Resolution Time Trend")
    trend = pd.DataFrame({
        "Hours": [9, 8, 7, 6, 5, 4, 3]
    })
    st.line_chart(trend)

# -----------------------------
# About
# -----------------------------
elif page == "About":
    st.title("📌 About WPAssist AI")

    st.write("""
    **Project Name:** WPAssist AI

    **Purpose:**  
    AI assistant for WordPress and WooCommerce support teams.

    **Features:**  
    - WordPress issue diagnosis  
    - Troubleshooting guidance  
    - Priority detection  
    - Suggested support replies  
    - Analytics dashboard

    **Tech Stack:**  
    Python, Streamlit, Pandas

    
    """)