import streamlit as st

# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="AI To-Do List",
    page_icon="💜",
    layout="centered"
)

# -----------------------------
# CUSTOM STYLING
# -----------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #faf9ff;
    }

    /* Gradient header */
    .header {
        background: linear-gradient(135deg, #7c3aed, #a855f7, #c084fc);
        padding: 35px 25px;
        border-radius: 22px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.20);
    }

    .header h1 {
        font-size: 42px;
        margin-bottom: 5px;
    }

    .header p {
        font-size: 17px;
        margin: 0;
    }

    /* Statistics cards */
    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        border: 1px solid #ede9fe;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.08);
    }

    .stat-number {
        font-size: 30px;
        font-weight: bold;
        color: #7c3aed;
    }

    .stat-label {
        color: #6b7280;
        font-size: 14px;
    }

    /* Section headings */
    .section-title {
        color: #4c1d95;
        font-size: 22px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 12px;
    }

    /* Task cards */
    .task-card {
        background: #f5f3ff;
        padding: 15px 18px;
        border-radius: 14px;
        margin-bottom: 10px;
        border-left: 4px solid #8b5cf6;
    }

    /* AI section */
    .ai-box {
        background: linear-gradient(135deg, #f5f3ff, #ede9fe);
        padding: 22px;
        border-radius: 20px;
        margin-top: 30px;
        border: 1px solid #ddd6fe;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION STATE
# -----------------------------

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
<div class="header">
    <h1>💜 My To-Do List</h1>
    <p>Get organised. Get things done. ✨</p>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# STATISTICS
# -----------------------------

total_tasks = len(st.session_state.tasks)

completed_tasks = sum(
    task["completed"]
    for task in st.session_state.tasks
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{total_tasks}</div>
        <div class="stat-label">📋 TOTAL TASKS</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{completed_tasks}</div>
        <div class="stat-label">✅ COMPLETED</div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# ADD TASK
# -----------------------------

st.markdown(
    '<div class="section-title">➕ Add a Task</div>',
    unsafe_allow_html=True
)

new_task = st.text_input(
    "Task",
    placeholder="e.g. Complete my Python assignment",
    label_visibility="collapsed"
)

if st.button("✨ Add Task", use_container_width=True):

    if new_task.strip():

        st.session_state.tasks.append({
            "name": new_task.strip(),
            "completed": False
        })

        st.success("Task added! 🎉")
        st.rerun()

    else:
        st.warning("Please enter a task first.")


# -----------------------------
# TASK LIST
# -----------------------------

st.markdown(
    '<div class="section-title">📋 Your Tasks</div>',
    unsafe_allow_html=True
)

if not st.session_state.tasks:

    st.info("No tasks yet. Add your first task above! 😊")

else:

    for i, task in enumerate(st.session_state.tasks):

        completed = st.checkbox(
            task["name"],
            value=task["completed"],
            key=f"task_{i}"
        )

        st.session_state.tasks[i]["completed"] = completed


# -----------------------------
# PROGRESS
# -----------------------------

if total_tasks > 0:

    progress = completed_tasks / total_tasks

    st.markdown(
        '<div class="section-title">📊 Your Progress</div>',
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.write(
        f"**{completed_tasks} of {total_tasks} tasks completed**"
    )


# -----------------------------
# DELETE COMPLETED TASKS
# -----------------------------

if completed_tasks > 0:

    if st.button(
        "🗑️ Delete Completed Tasks",
        use_container_width=True
    ):

        st.session_state.tasks = [
            task
            for task in st.session_state.tasks
            if not task["completed"]
        ]

        st.rerun()


# -----------------------------
# AI PLANNER
# -----------------------------

st.markdown("""
<div class="ai-box">

<h2>🤖 AI Planner</h2>

<p>
Tell your AI assistant what you want to accomplish,
and it can help break your goal into smaller tasks.
</p>

</div>
""", unsafe_allow_html=True)

goal = st.text_input(
    "Your goal",
    placeholder="e.g. Prepare for my Python exam",
    label_visibility="collapsed"
)

if st.button("✨ Plan It", use_container_width=True):

    if goal.strip():

        st.info(
            "🤖 AI planning will be connected here next!"
        )

    else:

        st.warning("Tell me what you want to accomplish first.")
