import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Regulatory Mapping Tool", layout="wide")

# Title
st.title("Regulatory Mapping Tool")
st.write("This application helps map issues to regulatory requirements.")

# Step 1: Select regulatory frameworks
st.header("Step 1: Select Regulatory Frameworks")
frameworks = st.multiselect(
    "Select regulatory frameworks:",
    ["CIS CSC v7.1", "COBIT 2019", "ISO 27001 v2013", "NIST 800-53 rev 5", "NIST CSF v2.0"]
)

# Step 2: Upload regulatory framework file
st.header("Step 2: Upload Regulatory Framework File")
framework_file = st.file_uploader(
    "Upload the regulatory framework file (CSV or Excel):",
    type=["csv", "xlsx"]
)

# Step 3: Upload issues file
st.header("Step 3: Upload Issues File")
issues_file = st.file_uploader(
    "Upload the issues file (CSV or Excel):",
    type=["csv", "xlsx"]
)

# Step 4: Process files and map issues to regulations
if frameworks and framework_file and issues_file:
    st.header("Step 4: Mapping Results")

    # Load regulatory framework file
    if framework_file.name.endswith(".csv"):
        framework_df = pd.read_csv(framework_file)
    else:
        framework_df = pd.read_excel(framework_file)

    # Load issues file
    if issues_file.name.endswith(".csv"):
        issues_df = pd.read_csv(issues_file)
    else:
        issues_df = pd.read_excel(issues_file)

    # Ensure required columns exist
    if "Requirement" not in framework_df.columns or "Description" not in framework_df.columns:
        st.error("Regulatory framework file must contain 'Requirement' and 'Description' columns.")
    elif "Issue" not in issues_df.columns:
        st.error("Issues file must contain an 'Issue' column.")
    else:
        # Perform mapping (example logic)
        mapping_results = []
        for _, issue_row in issues_df.iterrows():
            issue = issue_row["Issue"]
            for _, framework_row in framework_df.iterrows():
                requirement = framework_row["Requirement"]
                description = framework_row["Description"]
                # Example mapping logic: Check if issue is in the description
                if issue.lower() in description.lower():
                    mapping_results.append({
                        "Issue": issue,
                        "Regulatory Framework": ", ".join(frameworks),
                        "Requirement": requirement,
                        "Description": description,
                        "Reasoning": f"The issue '{issue}' is related to the requirement '{requirement}' because it is mentioned in the description."
                    })

        # Display mapping results
        if mapping_results:
            results_df = pd.DataFrame(mapping_results)
            st.write("### Mapping Results")
            st.dataframe(results_df)

            # Allow users to download the mapping results
            st.header("Download Mapping Results")
            output_format = st.selectbox("Select download format:", ["CSV", "Excel"])

            if output_format == "CSV":
                csv = results_df.to_csv(index=False)
                st.download_button(
                    label="Download as CSV",
                    data=csv,
                    file_name="mapping_results.csv",
                    mime="text/csv"
                )
            else:
                excel = results_df.to_excel(index=False)
                st.download_button(
                    label="Download as Excel",
                    data=excel,
                    file_name="mapping_results.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.warning("No mappings found. Please check your input files.")
else:
    st.warning("Please complete all steps to proceed.")