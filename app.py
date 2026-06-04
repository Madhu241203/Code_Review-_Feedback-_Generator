import streamlit as st
from model import review_code

st.set_page_config(page_title="Code Review Feedback Generator")

st.title("🤖 Code Review Feedback Generator")

code = st.text_area(
    "Paste your code here",
    height=300
)

if st.button("Review Code"):

    if not code.strip():
        st.warning("Please enter some code.")

    else:

        try:
            result = review_code(code)

            st.subheader("Code Quality Level")
            st.write(result.get("code_quality_level", "Unknown"))

            st.subheader("Identified Issues")
            issues = result.get("identified_issues", [])

            if issues:
                for issue in issues:
                    st.write("•", issue)
            else:
                st.write("No issues found.")

            st.subheader("Improvement Suggestions")
            suggestions = result.get("improvement_suggestions", [])

            if suggestions:
                for suggestion in suggestions:
                    st.write("•", suggestion)
            else:
                st.write("No suggestions.")

            st.subheader("Review Summary")
            st.write(result.get("review_summary", ""))

        except Exception as e:
            st.error(str(e))