import streamlit as st
import random
from questions.questions_set1 import questions_set1
from questions.questions_set2 import questions_set2

# Combine all question sets
all_questions = questions_set1 + questions_set2

# -------------------------------
# Initialize session state
# -------------------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = random.sample(all_questions, 30)
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.answered = {}
    st.session_state.correct_count = 0
    st.session_state.submitted = False

# Helper variables
total_questions = len(st.session_state.quiz)
current_index = st.session_state.current_q
current_question = st.session_state.quiz[current_index]

# -------------------------------
# Header + Restart button
# -------------------------------
title_col, restart_col = st.columns([4, 1])
with title_col:
    st.title("🧩 Test your knowledge !!")
    st.caption(" Total 350 Questions. Random set of 30 question on every start")
with restart_col:
    if st.button("🔁 Restart Quiz"):
        st.session_state.quiz = random.sample(all_questions, 30)
        st.session_state.current_q = 0
        st.session_state.answers = {}
        st.session_state.answered = {}
        st.session_state.correct_count = 0
        st.session_state.submitted = False
        st.rerun()

# -------------------------------
# Progress section
# -------------------------------
answered_count = len(st.session_state.answered)
progress = answered_count / total_questions
st.markdown(f"### Progress: {answered_count} / {total_questions} answered")
st.progress(progress)

# Show live score only if at least one question answered
if answered_count > 0:
    st.markdown(f"**Current Score:** {st.session_state.correct_count} / {answered_count} ✅")

st.divider()

# -------------------------------
# Display current question
# -------------------------------
st.markdown(f"### Q{current_index + 1}. {current_question['question']}")

selected = st.radio(
    "Choose your answer:",
    current_question["options"],
    key=f"q{current_index}_option",
    index=current_question["options"].index(st.session_state.answers.get(current_index, current_question["options"][0]))
    if current_index in st.session_state.answers
    else 0,
)

# Save selected answer
st.session_state.answers[current_index] = selected

# -------------------------------
# Submit button per question
# -------------------------------
if st.button("✅ Submit this question"):
    if current_index not in st.session_state.answered:
        st.session_state.answered[current_index] = True
        correct = current_question["answer"]
        user_ans = st.session_state.answers[current_index]

        if user_ans == correct:
            st.success(f"✅ Correct! — {correct}")
            st.session_state.correct_count += 1
        else:
            st.error(f"❌ Incorrect. Your answer: **{user_ans}**")
            st.info(f"💡 Correct answer: **{correct}**")

        st.markdown(f"**Explanation:** {current_question['explanation']}")
        st.rerun()

# Show answer if already submitted
if current_index in st.session_state.answered:
    correct = current_question["answer"]
    user_ans = st.session_state.answers[current_index]
    if user_ans == correct:
        st.success(f"✅ Correct! — {correct}")
    else:
        st.error(f"❌ Incorrect. Your answer: **{user_ans}**")
        st.info(f"💡 Correct answer: **{correct}**")
    st.markdown(f"**Explanation:** {current_question['explanation']}")

st.divider()

# -------------------------------
# Navigation buttons
# -------------------------------
nav1, nav2, nav3 = st.columns([1, 1, 1])

with nav1:
    if st.session_state.current_q > 0:
        if st.button("⬅️ Previous"):
            st.session_state.current_q -= 1
            st.rerun()

with nav2:
    if st.session_state.current_q < total_questions - 1:
        if st.button("Next ➡️"):
            st.session_state.current_q += 1
            st.rerun()

with nav3:
    if answered_count == total_questions:
        if st.button("🏁 Finish Quiz"):
            st.session_state.submitted = True
            st.rerun()

# -------------------------------
# Final results
# -------------------------------
if st.session_state.submitted:
    st.divider()
    st.header("🎯 Final Quiz Results")

    score = st.session_state.correct_count
    for i, q in enumerate(st.session_state.quiz):
        user_ans = st.session_state.answers.get(i, "Not answered")
        correct = q["answer"]
        if user_ans == correct:
            st.success(f"✅ Q{i+1}. {q['question']}")
        else:
            st.error(f"❌ Q{i+1}. {q['question']}")
            st.markdown(f"Your answer: **{user_ans}**")
            st.markdown(f"Correct answer: **{correct}**")
            st.info(f"💡 {q['explanation']}")
        st.markdown("---")

    st.markdown(f"## 🏆 Final Score: {score} / {total_questions}")
