import streamlit as st
import random
from questions.questions_set1 import questions_set1
from questions.questions_set2 import questions_set2

# -------------------------------
# Combine all question sets
# -------------------------------
all_questions = questions_set1 + questions_set2

# -------------------------------
# Initialize session state
# -------------------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = random.sample(all_questions, 335)
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.answered = {}
    st.session_state.correct_count = 0
    st.session_state.submitted = False

# Exam control variable
if "exam_started" not in st.session_state:
    st.session_state.exam_started = False

# Helper variables
total_questions = len(st.session_state.quiz)

# -------------------------------
# Function: multi vs single
# -------------------------------
def is_multi_answer(q):
    return isinstance(q.get("answer"), (list, tuple))

# -------------------------------
# Start Exam Page
# -------------------------------
if not st.session_state.exam_started and not st.session_state.submitted:
    st.title("🧠 Kafka Learning !!")
    st.markdown("""
    - 🧩 **Questions:** All questions
    - 🚀 Start when ready
    """)
    if st.button("Go For It!"):
        st.session_state.exam_started = True
        st.rerun()
    st.stop()

# -------------------------------
# Header
# -------------------------------
title_col, restart_col = st.columns([5, 1.5])

with title_col:
    st.title("🧩 Test your knowledge !!")
    st.caption("Total 350 Questions.")

with restart_col:
    if st.button("🔁 Restart Quiz"):
        st.session_state.clear()
        st.rerun()

# -------------------------------
# If exam submitted: Show results
# -------------------------------
if st.session_state.submitted:
    st.warning("Exam is over. Review your results below.")
    st.header(f"🏆 Final Score: {st.session_state.correct_count} / {total_questions}")

else:
    # -------------------------------
    # Progress
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
    current_index = st.session_state.current_q
    current_question = st.session_state.quiz[current_index]

    st.markdown(f"### Q{current_index + 1}. {current_question['question']}")

    multi = is_multi_answer(current_question)
    options = current_question["options"]

    prev = st.session_state.answers.get(current_index, None)
    answered = current_index in st.session_state.answered

    # -------------------------------
    # Options
    # -------------------------------
    if multi:
        default_selection = list(prev) if prev else []
        selected = st.multiselect(
            "Choose all that apply:",
            options,
            default=default_selection,
            key=f"q{current_index}_multi",
            disabled=answered,
        )
    else:
        default_index = options.index(prev) if prev in options else 0
        selected = st.radio(
            "Choose your answer:",
            options,
            index=default_index,
            key=f"q{current_index}_single",
            disabled=answered,
        )

    if not answered:
        st.session_state.answers[current_index] = selected

    st.divider()

    # -------------------------------
    # Buttons Section
    # -------------------------------
    col_submit, col_prev, col_next = st.columns([2, 1, 1])

    with col_submit:
        if not answered and st.button("Submit this question", use_container_width=True):
            st.session_state.answered[current_index] = True
            correct = current_question["answer"]
            user_ans = st.session_state.answers[current_index]

            if multi:
                if set(user_ans) == set(correct):
                    st.success(f"Correct! — {', '.join(correct)}")
                    st.session_state.correct_count += 1
                else:
                    st.error("Incorrect.")
                    st.markdown(f"Your answer: **{', '.join(user_ans) if user_ans else 'None'}**")
                    st.info(f"Correct answer: **{', '.join(correct)}**")
            else:
                if user_ans == correct:
                    st.success(f"Correct! — {correct}")
                    st.session_state.correct_count += 1
                else:
                    st.error(f"Incorrect. Your answer: **{user_ans}**")
                    st.info(f"Correct answer: **{correct}**")

            if "explanation" in current_question and current_question["explanation"]:
                st.markdown(f"**Explanation:** {current_question['explanation']}")

            st.rerun()

    with col_prev:
        if st.session_state.current_q > 0 and st.button("⬅️ Previous", use_container_width=True):
            st.session_state.current_q -= 1
            st.rerun()

    with col_next:
        if st.session_state.current_q < total_questions - 1 and st.button("Next ➡️", use_container_width=True):
            st.session_state.current_q += 1
            st.rerun()

    # -------------------------------
    # If answered: Show correct result
    # -------------------------------
    if answered:
        correct = current_question["answer"]
        user_ans = st.session_state.answers.get(current_index, [] if multi else None)

        if multi:
            if set(user_ans) == set(correct):
                st.success(f"Correct! — {', '.join(correct)}")
            else:
                st.error("Incorrect.")
                st.markdown(f"Your answer: **{', '.join(user_ans) if user_ans else 'None'}**")
                st.info(f"Correct answer: **{', '.join(correct)}**")
        else:
            if user_ans == correct:
                st.success(f"Correct! — {correct}")
            else:
                st.error(f"Incorrect. Your answer: **{user_ans}**")
                st.info(f"Correct answer: **{correct}**")

        if "explanation" in current_question and current_question["explanation"]:
            st.markdown(f"**Explanation:** {current_question['explanation']}")

    # -------------------------------
    # Finish button
    # -------------------------------
    if answered_count == total_questions:
        st.markdown("---")
        if st.button("Finish Quiz", use_container_width=True):
            st.session_state.submitted = True
            st.rerun()

# -------------------------------
# Final Results
# -------------------------------
if st.session_state.submitted:
    st.divider()
    st.header("🎯 Final Quiz Results")

    for i, q in enumerate(st.session_state.quiz):
        multi_i = is_multi_answer(q)
        user_ans = st.session_state.answers.get(i, [] if multi_i else "Not answered")
        correct = q["answer"]

        is_correct = set(user_ans) == set(correct) if multi_i else (user_ans == correct)

        if is_correct:
            st.success(f"Q{i+1}. {q['question']}")
        else:
            st.error(f"Q{i+1}. {q['question']}")

        if multi_i:
            st.markdown(f"Your answer: **{', '.join(user_ans) if user_ans else 'None'}**")
            st.markdown(f"Correct answer: **{', '.join(correct)}**")
        else:
            st.markdown(f"Your answer: **{user_ans}**")
            st.markdown(f"Correct answer: **{correct}**")

        if "explanation" in q and q["explanation"]:
            st.info(f"{q['explanation']}")

        st.markdown("---")
