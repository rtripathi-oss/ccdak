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
    st.session_state.answers = {}          # answers[i] = scalar (single) OR list (multi)
    st.session_state.answered = {}         # answered flags per question
    st.session_state.correct_count = 0     # number of correct questions
    st.session_state.submitted = False

# Helper variables
total_questions = len(st.session_state.quiz)
current_index = st.session_state.current_q
current_question = st.session_state.quiz[current_index]

def is_multi_answer(q):
    # Treat as multi-answer when "answer" is a list (or tuple)
    return isinstance(q.get("answer"), (list, tuple))

# -------------------------------
# Header + Restart button
# -------------------------------
title_col, restart_col = st.columns([4, 1])
with title_col:
    st.title("🧩 Test your knowledge !!")
    st.caption("Total 350 Questions. Random set of 30 questions on every start")
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
progress = answered_count / total_questions if total_questions else 0
st.markdown(f"### Progress: {answered_count} / {total_questions} answered")
st.progress(progress)

if answered_count > 0:
    st.markdown(f"**Current Score:** {st.session_state.correct_count} / {answered_count} ✅")

st.divider()

# -------------------------------
# Display current question
# -------------------------------
st.markdown(f"### Q{current_index + 1}. {current_question['question']}")

multi = is_multi_answer(current_question)
options = current_question["options"]

# Prepare default/previous selection
prev = st.session_state.answers.get(current_index, None)

if multi:
    # For multi-answer, use multiselect; store as a list
    if prev is None:
        default_selection = []
    else:
        # ensure list for default
        default_selection = list(prev) if isinstance(prev, (list, tuple)) else ([prev] if prev else [])
    selected = st.multiselect(
        "Choose all that apply:",
        options,
        default=default_selection,
        key=f"q{current_index}_multi",
    )
    # Save selected answers as list
    st.session_state.answers[current_index] = selected
else:
    # For single-answer, use radio; store as scalar
    if prev is None:
        default_index = 0
    else:
        try:
            default_index = options.index(prev)
        except ValueError:
            default_index = 0
    selected = st.radio(
        "Choose your answer:",
        options,
        index=default_index,
        key=f"q{current_index}_single",
    )
    # Save selected answer as scalar
    st.session_state.answers[current_index] = selected

# -------------------------------
# Submit button per question
# -------------------------------
if st.button("✅ Submit this question"):
    if current_index not in st.session_state.answered:
        st.session_state.answered[current_index] = True

        correct = current_question["answer"]
        user_ans = st.session_state.answers[current_index]

        if multi:
            # Compare as sets for exact match
            correct_set = set(correct)
            user_set = set(user_ans)
            if user_set == correct_set:
                st.success(f"✅ Correct! — {', '.join(correct)}")
                st.session_state.correct_count += 1
            else:
                st.error(f"❌ Incorrect.")
                st.markdown(f"Your answer: **{', '.join(user_ans) if user_ans else 'None'}**")
                st.info(f"💡 Correct answer: **{', '.join(correct)}**")
        else:
            if user_ans == correct:
                st.success(f"✅ Correct! — {correct}")
                st.session_state.correct_count += 1
            else:
                st.error(f"❌ Incorrect. Your answer: **{user_ans}**")
                st.info(f"💡 Correct answer: **{correct}**")

        # Explanation (if present)
        if "explanation" in current_question and current_question["explanation"]:
            st.markdown(f"**Explanation:** {current_question['explanation']}")

        st.rerun()

# Show answer if already submitted
if current_index in st.session_state.answered:
    correct = current_question["answer"]
    user_ans = st.session_state.answers.get(current_index, [] if multi else None)

    if multi:
        if set(user_ans) == set(correct):
            st.success(f"✅ Correct! — {', '.join(correct)}")
        else:
            st.error("❌ Incorrect.")
            st.markdown(f"Your answer: **{', '.join(user_ans) if user_ans else 'None'}**")
            st.info(f"💡 Correct answer: **{', '.join(correct)}**")
    else:
        if user_ans == correct:
            st.success(f"✅ Correct! — {correct}")
        else:
            st.error(f"❌ Incorrect. Your answer: **{user_ans}**")
            st.info(f"💡 Correct answer: **{correct}**")

    if "explanation" in current_question and current_question["explanation"]:
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
        multi_i = is_multi_answer(q)
        user_ans = st.session_state.answers.get(i, [] if multi_i else "Not answered")
        correct = q["answer"]

        is_correct = set(user_ans) == set(correct) if multi_i else (user_ans == correct)

        if is_correct:
            st.success(f"✅ Q{i+1}. {q['question']}")
        else:
            st.error(f"❌ Q{i+1}. {q['question']}")

        if multi_i:
            ua_disp = ", ".join(user_ans) if user_ans else "None"
            ca_disp = ", ".join(correct)
            st.markdown(f"Your answer: **{ua_disp}**")
            st.markdown(f"Correct answer: **{ca_disp}**")
        else:
            st.markdown(f"Your answer: **{user_ans}**")
            st.markdown(f"Correct answer: **{correct}**")

        if "explanation" in q and q["explanation"]:
            st.info(f"💡 {q['explanation']}")

        st.markdown("---")

    st.markdown(f"## 🏆 Final Score: {score} / {total_questions}")