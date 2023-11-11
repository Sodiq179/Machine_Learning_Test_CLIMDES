import streamlit as st
import pandas as pd
from utils import load_model, select_skills, count_similar_elements, encode_programming_level, encode_education



model = load_model()

classifier = model["model"]
features = model["features"]
encoder = model["OHE_encoder"]
encoder_feat = model["OHE_encoder_feat"]


pred_response = ["You are not eligible for this internship", "Congratulations, you are eligible for this internship"]



def show_predict_page():
    st.title("Internship Success Prediction")

    st.write("""### We need some information to predict the internship success""")


    genders = (
        "Male",
        "Female"
    )

    roles = (
        "Backend",
        "Machine Learning",
        "Frontend"
    )

    durations = (
        "3 Months",
        "6 Months",
        "12 Months"
    )

    programming_levels = (
        'Beginner', 'Intermediate'
    )

    educations = (
        'Student', 'Graduate'
    )

    departments = (
        'Computer Science', 
        'Engineering',
        'Statistics',
        'Mathematics'
        )

    skills = (
        "Python", "Java", "JavaScript", "C++", "Ruby",
        "Excel", "HTML", "CSS", "SQL", "Machine Learning", "Others"
    )


    # Get numerical input from the user
    age = st.number_input("Age", min_value=15, max_value=30)
    academic_gpa = st.number_input("Academic GPA", min_value=0.0, max_value=4.0, value=0.0, step=0.01)
    internship_completed = st.number_input("Number of Internships Completed", min_value=0, max_value=10)
    certification = st.number_input("Number of Relevant Certifications", min_value=0, max_value=10)
    technical_test_score = st.number_input("Technical Test Score", min_value=0, max_value=250)


    gender = st.selectbox("Gender", genders)
    role = st.selectbox("Internship Role", roles)
    duration = st.selectbox("Internship Duration", durations)
    department = st.selectbox("Background", departments )
    education = st.selectbox("Education Level", educations)
    programming_level = st.selectbox("Programming Level", programming_levels)

    intern_skills = st.multiselect("Select programming languages", skills)


    ok = st.button("Check Eligibility")



    intern_details = {
                        'gender': [gender.lower()],
                        'age': [age],
                        'intern_role': [role],
                        'internship_duration': [int(duration.split()[0])],
                        'academic_gpa': [academic_gpa],
                        'number_of_internships_completed': [internship_completed],
                        'number_of_certification': [certification],
                        'programming_level': [encode_programming_level(programming_level)],
                        'technical_interview_score': [technical_test_score],
                        'education': [encode_education(education)],
                        'department': [department],
                        'skills_match': [count_similar_elements(select_skills(role), intern_skills)]
                    }
    
    intern = pd.DataFrame(intern_details)
    encoded_data_intern = encoder.transform(intern[["gender", "intern_role", "department"]])

    # Create a DataFrame with the one-hot encoded columns and proper feature names
    data_encoded_intern = pd.DataFrame(encoded_data_intern, columns=encoder_feat)

    intern_df = pd.concat([intern, data_encoded_intern], axis = 1)[features]
    col = ['age', 'internship_duration', 'academic_gpa',
       'number_of_internships_completed', 'number_of_certification',
       'programming_level', 'technical_interview_score', 'education',
       'skills_match', 'gender_male', 'gender_male', 'intern_role_Frontend',
       'intern_role_Frontend', 'intern_role_Machine Learning',
       'intern_role_Machine Learning', 'department_Computer Science',
       'department_Engineering', 'department_Mathematics']
    if ok:
        pred = classifier.predict(intern_df[col])
        st.subheader(pred_response[int(pred)])

show_predict_page()