import streamlit as st


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="AI To-Do List",
    page_icon="💜",
    layout="centered"
)


# =========================================================
# COLOUR PALETTE & STYLING
# =========================================================

st.markdown("""
<style>

    /* -------------------------
       MAIN APP
    ------------------------- */

    .stApp {
        background-color: #F5CDD0;
    }

    /* -------------------------
       HEADINGS
    ------------------------- */

    h1, h2, h3 {
        color: #826E8B !important;
    }

    /* -------------------------
       HEADER
    ------------------------- */

    .header {
        background: linear-gradient(
            135deg,
            #826E8B,
            #EB6E9B
        );

        padding: 35px 25px;
        border-radius: 22px;
        text-align: center;
        color: white;
        margin-bottom: 25px;

        box-shadow:
            0 8px 25px rgba(130, 110, 139, 0.25);
    }

    .header h1 {
        color: white !important;
        font-size: 42px;
        margin-bottom: 5px;
    }

    .header p {
        color: white;
        font-size: 17px;
        margin: 0;
    }

    /* -------------------------
       STATISTICS CARDS
    ------------------------- */

    .stat-card {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        text-align: center;

        border: 2px solid #F4B3C7;

        box-shadow:
            0 5px 15px rgba(130, 110, 139, 0.12);
    }

    .stat-number {
        font-size: 30px;
        font-weight: bold;
        color: #826E8B;
    }

    .stat-label {
        color: #826E8B;
        font-size: 14px;
        font-weight: 600;
    }

    /* -------------------------
       TEXT INPUT
    ------------------------- */

    .stTextInput input {
        border: 2px solid #E69CBA;
        border-radius: 12px;
        background-color: white;
    }

    .stTextInput input:focus {
        border-color: #EB6E9B;
        box-shadow: 0 0 0 2px #F4B3C7;
    }

    /* -------------------------
       BUTTONS
    ------------------------- */

    .stButton > button {
        background-color: #EB6E9B;
        color: white;

        border: none;
        border-radius: 12px;

        font-weight: 600;

        padding: 0.6rem 1rem;
    }

    .stButton > button:hover {
        background-color: #826E8B;
        color: white;
    }

    /* -------------------------
       TABS
    ------------------------- */

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        color: #826E8B;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        color: #EB6E9B !important;
    }

    /* -------------------------
       ACTIVE TASK
    ------------------------- */

    .task-card {
        background-color: white;

        padding: 14px 18px;
        border-radius: 14px;

        margin-bottom: 10px;

        border-left: 5px solid #EB6E9B;

        box-shadow:
            0 3px 10px rgba(130, 110, 139, 0.10);
    }

    /* -------------------------
       COMPLETED TASK
    ------------------------- */

    .completed-card {
        background-color: #F4B3C7;

        padding: 14px 18px;
        border-radius: 14px;

        margin-bottom: 10px;

        border-left: 5px solid #826E8B;

        color: #826E8B;

        text-decoration: line-through;

        box-shadow:
            0 3px 10px rgba(130, 110, 139, 0.08);
    }

    /* -------------------------
       AI PLANNER
    ------------------------- */

    .ai-box {
        background: linear-gradient(
            135deg,
            #F4B3C7,
            #E69CBA
        );

        padding: 22px;
        border-radius: 20px;

        margin-top: 30px;

        border: 2px solid #E69CBA;
    }

    .ai-box h2 {
        color: #826E8B !important;
    }

    .ai-box p {
        color: #826E8B;
    }

    /* -------------------------
       PROGRESS BAR
    ------------------------- */

    .stProgress > div > div > div > div {
        background-color: #EB6E9B;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header">

    <h1>💜 My To-Do List</h1>

    <p>
        Get organised. Get things done. ✨
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# STATISTICS
# =========================================================

total_tasks = len(st.session_state.tasks)

completed_count = sum(
    1
    for task in st.session_state.tasks
    if task["completed"]
)


col1, col2 = st.columns(2)


with col1:

    st.markdown(
        f"""
        <div class="stat-card">

            <div class="stat-number">
                {total_tasks}
            </div>

            <div class="stat-label">
                📋 TOTAL TASKS
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="stat-card">

            <div class="stat-number">
                {completed_count}
            </div>

            <div class="stat-label">
                ✅ COMPLETED
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# ADD TASK
# =========================================================

st.markdown("## ➕ Add a Task")


# Using a form allows the input to reset after submission.

with st.form("add_task_form", clear_on_submit=True):

    new_task = st.text_input(
        "Task",
        placeholder="What do you need to get done?",
        label_visibility="collapsed"
    )

    add_task = st.form_submit_button(
        "✨ Add Task",
        use_container_width=True
    )


if add_task:

    if new_task.strip():

        st.session_state.tasks.append(
            {
                "name": new_task.strip(),
                "completed": False
            }
        )

        st.success("Task added! 🎉")

        st.rerun()

    else:

        st.warning(
            "Please enter a task first."
        )


# =========================================================
# TASK LIST
# =========================================================

st.markdown("## 📋 Your Tasks")


# Three task views

tab_all, tab_active, tab_completed = st.tabs(
    [
        f"All ({total_tasks})",
        f"Active ({total_tasks - completed_count})",
        f"Completed ({completed_count})"
    ]
)


# =========================================================
# ALL TASKS
# =========================================================

with tab_all:

    if not st.session_state.tasks:

        st.info(
            "✨ No tasks yet. Add your first task above!"
        )

    else:

        for i, task in enumerate(
            st.session_state.tasks
        ):

            if task["completed"]:

                st.markdown(
                    f"""
                    <div class="completed-card">
                        ✓ &nbsp; {task["name"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                checked = st.checkbox(
                    task["name"],
                    value=False,
                    key=f"all_task_{i}"
                )

                if checked:

                    st.session_state.tasks[i][
                        "completed"
                    ] = True

                    st.rerun()


# =========================================================
# ACTIVE TASKS
# =========================================================

with tab_active:

    active_tasks = [
        (i, task)
        for i, task in enumerate(
            st.session_state.tasks
        )
        if not task["completed"]
    ]

    if not active_tasks:

        st.success(
            "🎉 You have no active tasks!"
        )

    else:

        for i, task in active_tasks:

            checked = st.checkbox(
                task["name"],
                value=False,
                key=f"active_task_{i}"
            )

            if checked:

                st.session_state.tasks[i][
                    "completed"
                ] = True

                st.rerun()


# =========================================================
# COMPLETED TASKS
# =========================================================

with tab_completed:

    completed_tasks = [
        task
        for task in st.session_state.tasks
        if task["completed"]
    ]

    if not completed_tasks:

        st.info(
            "📭 No completed tasks yet."
        )

    else:

        for task in completed_tasks:

            st.markdown(
                f"""
                <div class="completed-card">
                    ✓ &nbsp; {task["name"]}
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# PROGRESS
# =========================================================

st.markdown("## 📊 Your Progress")


if total_tasks > 0:

    progress = (
        completed_count / total_tasks
    )

else:

    progress = 0


st.progress(progress)


st.markdown(
    f"""
    <div style="
        text-align: center;
        color: #826E8B;
        margin-top: -8px;
    ">
        <strong>{completed_count}</strong>
        of
        <strong>{total_tasks}</strong>
        tasks completed
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DELETE COMPLETED TASKS
# =========================================================

if completed_count > 0:

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


# =========================================================
# AI PLANNER
# =========================================================

st.markdown("""
<div class="ai-box">

    <h2>🤖 AI Planner</h2>

    <p>
        Tell your AI assistant what you want to accomplish,
        and it will help break your goal into smaller tasks.
    </p>

</div>
""", unsafe_allow_html=True)


with st.form("ai_planner_form"):

    goal = st.text_input(
        "Your goal",
        placeholder="e.g. Prepare for my Python exam",
        label_visibility="collapsed"
    )

    plan_button = st.form_submit_button(
        "✨ Plan It",
        use_container_width=True
    )


if plan_button:

    if goal.strip():

        st.info(
            "🤖 AI planning will be connected here next!"
        )

    else:

        st.warning(
            "Tell me what you want to accomplish first."
        )
