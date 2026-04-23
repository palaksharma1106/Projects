import streamlit as st
import ollama

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Email Generator", page_icon="📧", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* -------- REMOVE DEFAULT SPACING -------- */
.block-container {
    padding: 0rem !important;
}
html, body, .stApp {
    margin: 0;
    padding: 0;
}

/* -------- FONT -------- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    color: black !important;
}

/* -------- BACKGROUND IMAGE -------- */
.stApp {
    background: url("https://i.pinimg.com/1200x/0f/68/6e/0f686e475cb7ad69cbb6aa3c52342815.jpg");
    background-size: cover;
    background-position: center;   /* FIXED */
    background-repeat: no-repeat;
    background-attachment: fixed;
    min-height: 100vh;
}

/* -------- LIGHT OVERLAY -------- */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(255, 255, 255, 0.65);
    z-index: -1;
}

/* -------- LABEL TEXT -------- */
label {
    color: black !important;
    font-weight: 600;
}

/* -------- INPUT BOXES (BLACK) -------- */
textarea, input {
    background-color: black !important;
    color: white !important;
    border: 2px solid black !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

/* Placeholder */
textarea::placeholder, input::placeholder {
    color: #bbb !important;
}

/* -------- SELECT BOX (FIXED PROPERLY) -------- */
div[data-baseweb="select"] > div {
    background-color: black !important;
    color: white !important;
    border-radius: 12px !important;
    border: 2px solid black !important;
}

div[data-baseweb="select"] span {
    color: white !important;
}

/* -------- BUTTON -------- */
.stButton button {
    width: 100%;
    background: black;
    color: white;
    border-radius: 12px;
    padding: 12px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
}

/* -------- OUTPUT BOX -------- */
.output-box {
    background: rgba(255, 255, 255, 0.9);
    color: black !important;
    border-radius: 15px;
    padding: 20px;
    margin: 20px auto;
    max-width: 900px;
    width: 90%;
    line-height: 1.6;
}

/* -------- CENTER OUTPUT -------- */
.output-box {
    display: block;
}

/* -------- INPUT FOCUS EFFECT -------- */
textarea:focus, input:focus {
    outline: none;
    box-shadow: 0 0 8px rgba(0,0,0,0.4);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<br>", unsafe_allow_html=True)  # pushes content down

st.markdown(
    "<h1 style='text-align:center; color:black;'>📧 AI Email Generator</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center; color:black;'>Generate professional emails instantly with AI ✨</h3>",
    unsafe_allow_html=True
)



# ---------------- INPUTS ----------------
purpose = st.text_area("📌 Purpose of Email")
recipient = st.text_input("👤 Recipient (Manager, HR, Client)")
tone = st.selectbox(
    "🎯 Select Tone",
    ["Formal", "Friendly", "Apologetic", "Professional", "Casual"]
)


length = st.slider("📏 Email Length (words)", 50, 300, 120)

col1, col2 = st.columns(2)

# ---------------- GENERATE ----------------
with col1:
    if st.button("Generate Email ✨"):
        if purpose and recipient:

            with st.spinner("Generating your email... ✨"):

                prompt = f"""
                Write a professional email.

                Purpose: {purpose}
                Recipient: {recipient}
                Tone: {tone}

                Keep the email around {length} words.

                Format strictly like this:
                Subject:
                <subject line>

                Body:
                <email body>
                """

                response = ollama.chat(
                    model="llama3",
                    messages=[{"role": "user", "content": prompt}],
                    stream=True
                )

                st.markdown(
                      "<h3 style='text-align:center; color:black;'>📩 Generated Email</h3>",
                       unsafe_allow_html=True
)


                output = ""
                placeholder = st.empty()

                for chunk in response:
                    content = chunk["message"]["content"]
                    output += content
                    placeholder.markdown(
                        f'<div class="output-box">{output}</div>',
                        unsafe_allow_html=True
                    )


                st.code(output)

                if st.button("📋 Copy Email"):
                    st.success("Copied! Press Ctrl + C / Cmd + C")

        else:
            st.warning("⚠ Please fill all fields")


with col2:
    if st.button("Clear 🗑"):
        st.rerun()



