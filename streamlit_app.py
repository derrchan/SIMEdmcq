import streamlit as st

# Define questions and the correct answer for each
questions_set_1 = [
    {
        "question": "The following are risk factors for the carcinoma of the breasts:",
        "options": ["Late Menarche", "Family history of carcinoma of the breast", "Nulliparous", "Late menopause", "Personal history of carcinoma of breast"],
        "answer": "Late Menarche"
    },
    {
        "question": "A 47 year old lady was found to have a 3 cm ductal carcinoma in situ in her left breast at 2 o'clock position. The most appropriate treatment option is?",
        "options": ["Close surveillance", "Excisional Biopsy", "Radiation Therapy", "Simple Mastectomy", "Tamoxifen"],
        "answer": "Simple Mastectomy"
    },
    {
        "question": "Which of the following is the most appropriate treatment for cyclical mastalgia?",
        "options": ["Gamolenic Acid", "Vitamin D", "Ranitidine", "Aspirin", "Clarithomycin"],
        "answer": "Gamolenic Acid"
    },
    {
        "question": "Which of the following does not belong to the chronic cystic mastitis group?",
        "options": ["Papillomatosis", "Blunt duct adenosine", "Sclerosing adenosine", "Apocrine metaplasia", "Mondor’s disease"],
        "answer": "Mondor’s disease"
    },
]

questions_set_2 = [
    {
        "question": "The following are contraindications of breast conserving surgery in a patient with carcinoma of the breast except:",
        "options": ["Tumour size is greater than 4 cm", "Tumour beneath areola", "Old age", "Small breasts", "Multi-focal disease"],
        "answer": "Old age"
    },
    {
        "question": "The least common site for spread of carcinoma of the breast is?",
        "options": ["Bone", "Liver", "Kidney", "Lungs", "Pleura"],
        "answer": "Kidney"
    },
    {
        "question": "Modified radical mastectomy removes the following tissues except?",
        "options": ["Pectoralis Major", "Axillary Lymphatic Tissue", "Breast Tissue", "Pectoral Fascia", "Nipple"],
        "answer": "Pectoralis Major"
    },
    {
        "question": "Contraindications to breast conservative surgery for breast cancer is?",
        "options": ["Age beyond 70 years", "Bilateral breast cancer", "Lymph node involvement", "Size>2cm", "Multifocal lesions"],
        "answer": "Multifocal lesions"
    },
]

# Initialize session state variables
if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = set()
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_questions" not in st.session_state:
    st.session_state.show_questions = True
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False
if "display_set_1" not in st.session_state:
    st.session_state.display_set_1 = True

def show_questions(questions):
    for idx, q in enumerate(questions, start=1):
        st.write(f"Question {idx}) {q['question']}")
        if idx not in st.session_state.answered_questions:
            for i, option in enumerate(q['options'], start=1):
                if st.button(f"{chr(64+i)}) {option}", key=f"q{idx}_option{i}"):
                    st.session_state.answered_questions.add(idx)
                    if option == q['answer']:
                        st.success(f"Correct! The answer is: {q['answer']}")
                        st.session_state.score += 1
                    else:
                        st.error(f"Wrong. The correct answer is: {q['answer']}")
        else:
            st.write("Answered")

def admin_login():
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.admin_logged_in = True
            st.session_state.show_questions = True
            st.session_state.answered_questions.clear()
            st.session_state.score = 0
        else:
            st.sidebar.error("Incorrect username or password")

# Sidebar for login
admin_login()

# Main app body
if st.session_state.admin_logged_in and st.session_state.show_questions:
    st.title("Breast Surgery MCQs")

    # Show report card message only when displaying question set 2
    if not st.session_state.display_set_1:
        report_card = ("You have done quite well with the questions on benign diseases of the breasts "
                       "but you are struggling with the questions on breast CA. "
                       "I suggest you work more on these questions.")
        st.write(report_card)

    # Determine which question set to show
    questions = questions_set_1 if st.session_state.display_set_1 else questions_set_2
    show_questions(questions)
    st.write(f"Your score: {st.session_state.score}/{len(questions)}")

    if st.button("Exit"):
        st.session_state.admin_logged_in = False
        st.session_state.show_questions = False
        st.session_state.display_set_1 = not st.session_state.display_set_1
        st.experimental_rerun()  # Rerun the app to refresh the page content

if not st.session_state.show_questions and not st.session_state.admin_logged_in:
    st.title("Breast Surgery MCQs")
