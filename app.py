import os
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_code(filename):
    file_path = os.path.join(BASE_DIR, "modules", filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return f"# Error: {filename} not found."


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Data Mining System",
    page_icon="🎓",
    layout="wide"
)

# Custom Error-Box Theme for Code Blocks ONLY
st.markdown(
    """
    <style>
    /* Code block styled exactly like Streamlit error/exception box */
    [data-testid="stCode"],
    .stCode,
    [data-testid="stCodeBlock"] {
        background-color: #371f25 !important;
        border: 1px solid rgba(255, 75, 75, 0.25) !important;
        border-radius: 8px !important;
        padding: 10px !important;
        box-shadow: none !important;
    }

    [data-testid="stCode"] > div,
    [data-testid="stCode"] pre,
    .stCode > div,
    .stCode pre,
    [data-testid="stCodeBlock"] pre {
        background-color: #241215 !important;
        border: 1px solid rgba(255, 75, 75, 0.2) !important;
        border-radius: 6px !important;
        padding: 14px 16px !important;
        margin: 0 !important;
    }

    [data-testid="stCode"] *,
    .stCode *,
    [data-testid="stCode"] code,
    [data-testid="stCode"] span,
    .stCode code,
    .stCode span,
    [data-testid="stCodeBlock"] code,
    [data-testid="stCodeBlock"] code *,
    [data-testid="stCodeBlock"] pre code,
    [data-testid="stCodeBlock"] pre code span {
        color: #ff8282 !important;
        -webkit-text-fill-color: #ff8282 !important;
        font-family: 'Source Code Pro', Consolas, Monaco, monospace !important;
    }

    /* Copy button inside code block */
    [data-testid="stCode"] button,
    .stCode button,
    [data-testid="stCodeBlock"] button {
        color: #ff8282 !important;
        background: transparent !important;
        border: none !important;
    }
    [data-testid="stCode"] button:hover,
    .stCode button:hover,
    [data-testid="stCodeBlock"] button:hover {
        color: #ff4d4f !important;
        background-color: rgba(255, 75, 75, 0.15) !important;
    }

    /* Inline code badges */
    code:not(pre code) {
        background-color: #371f25 !important;
        color: #ff8282 !important;
        border: 1px solid rgba(255, 75, 75, 0.25) !important;
        padding: 2px 6px !important;
        border-radius: 4px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PROJECT TITLE
# =========================================================

st.title("🎓 Student Intelligence and Learning Analytics System")

st.write(
    """
    This project demonstrates different Data Mining techniques
    using student academic, learning, feedback, web, multimedia
    and spatial data.
    """
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📊 Data Mining Techniques")

technique = st.sidebar.selectbox(
    "Select Technique",
    [
        "Home",
        # Data Mining
        "Practical 4: Data Preprocessing and Cleaning",
        "Practical 5: Data Discretization and Visualization",
        "ID3",
        "J48",
        "Naive Bayes",
        "Decision Tree",
        "K-NN",
        "K-Means",
        "Apriori",
        "Text Mining",
        "Web Mining",
        "Multimedia Mining",
        "Spatial Mining",
        # DAA Practicals
        "DAA Practical 1: Time Complexity (Step Counting)",
        "DAA Practical 2: Sorting Algorithms (Bubble, Insertion, Merge)",
        "DAA Practical 3: Singly Linked List Operations",
        "DAA Practical 4: Circular Linked List Operations",
        "DAA Practical 5: Stack & Tower of Hanoi",
        "DAA Practical 6: Balanced Parentheses Checker",
        "DAA Practical 7: Queue Operations (Array, Circular, Deque)",
        "DAA Practical 8: Graph Representation & Traversals (DFS/BFS)",
        "DAA Practical 9: Dijkstra's Shortest Path Algorithm",
        "DAA Practical 10: Searching Techniques (Linear, Binary, Interpolation)",
        "DAA Practical 11: AVL Tree Implementation & Rotations"
    ]
)


# =========================================================
# HOME DASHBOARD
# =========================================================

if technique == "Home":

    st.header("🏠 Project Dashboard")

    st.write(
        """
        The system applies different Data Mining techniques
        to solve different types of problems in education.
        """
    )

    st.subheader("📚 Techniques Covered")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🌳 **ID3**\n\nClassification\n\n*Concept: Information Gain*")
        st.info("🌳 **J48**\n\nClassification\n\n*Concept: C4.5 Decision Tree*")
        st.info("🎲 **Naive Bayes**\n\nClassification\n\n*Concept: Bayes Probability*")
        st.info("🌳 **Decision Tree**\n\nClassification\n\n*Concept: Gini Split Rules*")

    with col2:
        st.info("👥 **K-NN**\n\nClassification\n\n*Concept: Distance / Neighbours*")
        st.info("🔵 **K-Means**\n\nClustering\n\n*Concept: Centroids / Clusters*")
        st.info("🛒 **Apriori**\n\nAssociation Mining\n\n*Concept: Support & Confidence*")
        st.info("📝 **Text Mining**\n\nText Analytics\n\n*Concept: TF-IDF & Tokens*")

    with col3:
        st.info("🌐 **Web Mining**\n\nWeb Behavior\n\n*Concept: Log & Click Analysis*")
        st.info("🎥 **Multimedia Mining**\n\nMedia Mining\n\n*Concept: Audio/Video Features*")
        st.info("📍 **Spatial Mining**\n\nGeographical Analysis\n\n*Concept: Area Coordinates*")

    st.subheader("⚡ 2. Design & Analysis of Algorithms (DAA) Practicals")

    dcol1, dcol2, dcol3 = st.columns(3)

    with dcol1:
        st.success("⏱️ **Practical 1**\n\nTime Complexity Calculation\n\n*Step Counting (Iterative & Recursive)*")
        st.success("⚡ **Practical 2**\n\nSorting Algorithms\n\n*Bubble, Insertion, Merge Sort & Time Benchmark*")
        st.success("🔗 **Practical 3**\n\nSingly Linked List\n\n*Insert, Delete, and Search operations*")
        st.success("🔄 **Practical 4**\n\nCircular Linked List\n\n*Circular traversal, head/end modifications*")

    with dcol2:
        st.success("🥞 **Practical 5**\n\nStack & Recursion\n\n*Array, Linked List, Tower of Hanoi & Underflow*")
        st.success("🔢 **Practical 6**\n\nBalanced Parentheses\n\n*Stack-based expression syntax validator*")
        st.success("🚶 **Practical 7**\n\nQueue Operations\n\n*List, Circular Queue, Deque & Performance*")
        st.success("🕸️ **Practical 8**\n\nGraph Traversals\n\n*Adjacency Matrix/List, DFS & BFS*")

    with dcol3:
        st.success("🗺️ **Practical 9**\n\nDijkstra's Algorithm\n\n*Greedy Single-Source Shortest Path*")
        st.success("🔍 **Practical 10**\n\nSearching Techniques\n\n*Linear, Binary, Interpolation Search*")
        st.success("🎄 **Practical 11**\n\nAVL Tree\n\n*Self-Balancing BST, LL/RR Rotations*")



# =========================================================
# PRACTICAL 4: DATA PREPROCESSING AND CLEANING
# =========================================================

elif technique == "Practical 4: Data Preprocessing and Cleaning":

    st.header("🧹 Practical 04: Data Preprocessing and Cleaning")

    st.write(
        """
        Data preprocessing and cleaning prepare raw, noisy, or incomplete datasets for effective
        data mining and machine learning. This practical covers **Dataset Exploration**,
        **Missing Value Handling & Normalization**, and **Categorical Encoding**.
        """
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "Part A: Dataset Exploration",
        "Part B: Data Cleaning",
        "Part C: Data Transformation",
        "Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("dm_prac4_part_a.py"), language="python")
        st.subheader("📋 Output Highlights")
        st.code(
            """======================================================================
               EMPLOYEE ANALYTICS DATASET
======================================================================
Dimensions: 15 Rows, 12 Columns
Missing Values detected in: Age, Salary, Experience, Performance, Location
Data Types: int64, float64, object""",
            language="text"
        )
        st.info("• Exploration inspects dataset shape, null presence, attribute datatypes, and summary statistics.")

    with tab2:
        st.code(load_code("dm_prac4_part_b.py"), language="python")
        st.subheader("📋 Output Highlights")
        st.code(
            """Handling Missing Values:
• Age -> Median imputation
• Salary -> Mean imputation
• Experience -> Median imputation
• Performance -> Mean imputation
• Location -> Mode imputation
Duplicates Removed: 1 duplicate record dropped
Standardized Gender: ['Male', 'Female']
Standardized Departments: ['IT', 'HR', 'Finance', 'Marketing']""",
            language="text"
        )
        st.info("• Statistical imputation prevents data loss compared to dropping records.")

    with tab3:
        st.code(load_code("dm_prac4_part_c.py"), language="python")
        st.subheader("📋 Output Highlights")
        st.code(
            """Label Encoding Applied to:
['Gender', 'Department', 'Designation', 'Employment_Type', 'Location']

Min-Max Scaling [0, 1] Applied to:
['Age', 'Salary', 'Experience', 'Performance', 'Training_Hours']
Formula: X_scaled = (X - X_min) / (X_max - X_min)
Processed dataset saved as data/Employee_Analytics_Processed.csv""",
            language="text"
        )
        st.info("• Min-Max scaling normalizes numerical scales to [0, 1] to prevent dominant feature bias.")

    with tab4:
        st.code(load_code("dm_prac4.py"), language="python")


# =========================================================
# PRACTICAL 5: DATA DISCRETIZATION AND VISUALIZATION
# =========================================================

elif technique == "Practical 5: Data Discretization and Visualization":

    st.header("📊 Practical 05: Data Discretization and Visualization")

    st.write(
        """
        Data Discretization transforms continuous numeric attributes into discrete intervals
        (bins) to enhance interpretability and classification efficiency. Data Visualization
        provides graphical insights into patterns and distributions.
        """
    )

    tab1, tab2, tab3 = st.tabs([
        "Part A: Data Discretization",
        "Part B: Data Visualization",
        "Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("dm_prac5_part_a.py"), language="python")
        st.subheader("📋 Discretization Rules Applied (`pd.cut`)")
        st.code(
            """• Age -> Young [20-30], Adult [30-40], Senior [40-60]
• Salary -> Low [4L-8L], Medium [8L-9L], High [9L+]
• Experience -> Beginner [0-2], Intermediate [2-5], Experienced [5-10], Expert [10+]
• Performance -> Poor [0-2], Average [2-3.5], Good [3.5-4.5], Excellent [4.5-5]
• Training Hours -> Low [0-20], Medium [20-40], High [40-60], Very High [60+]""",
            language="text"
        )
        st.info("• Equal-width binning converts continuous variables into meaningful categorical buckets.")

    with tab2:
        st.code(load_code("dm_prac5_part_b.py"), language="python")
        st.subheader("📊 Visualizations (Bar Chart, Histogram, Pie Chart, Boxplot)")
        import matplotlib.pyplot as plt
        import pandas as pd
        data_path = os.path.join(BASE_DIR, "data", "Employee_Analytics.csv")
        if os.path.exists(data_path):
            sample_df = pd.read_csv(data_path)
            sample_df['Age_Category'] = pd.cut(sample_df['Age'].fillna(sample_df['Age'].median()), bins=[20, 30, 40, 60], labels=['Young', 'Adult', 'Senior'])
            sample_df['Performance_Category'] = pd.cut(sample_df['Performance'].fillna(sample_df['Performance'].mean()), bins=[0, 2, 3.5, 4.5, 5], labels=['Poor', 'Average', 'Good', 'Excellent'])
            
            vcol1, vcol2 = st.columns(2)
            with vcol1:
                fig1, ax1 = plt.subplots(figsize=(5, 3.5))
                sample_df['Age_Category'].value_counts().plot(kind='bar', ax=ax1, color='#ff6b6b')
                ax1.set_title("Age Category Distribution", color='white')
                ax1.tick_params(colors='white')
                fig1.patch.set_facecolor('#241215')
                ax1.set_facecolor('#371f25')
                st.pyplot(fig1)
            
            with vcol2:
                fig2, ax2 = plt.subplots(figsize=(5, 3.5))
                sample_df['Performance_Category'].value_counts().plot(kind='pie', ax=ax2, autopct='%1.1f%%', textprops={'color':"white"})
                ax2.set_title("Performance Distribution", color='white')
                fig2.patch.set_facecolor('#241215')
                st.pyplot(fig2)

    with tab3:
        st.code(load_code("dm_prac5.py"), language="python")


# =========================================================
# ID3
# =========================================================

elif technique == "ID3":

    st.header("🌳 ID3 Classification")

    st.write(
        """
        ID3 is a decision tree classification algorithm.
        It uses Entropy and Information Gain to select
        the best attribute for splitting the data.
        """
    )

    st.code(load_code("id3.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        **ID3 follows these basic steps:**

        1. Calculate Entropy
        2. Calculate Information Gain
        3. Select the best attribute
        4. Create the Decision Tree
        5. Predict Pass / Fail

        The attribute with the best split becomes an
        important decision point in the tree.
        """
    )


# =========================================================
# J48
# =========================================================

elif technique == "J48":

    st.header("🌳 J48 Classification")

    st.write(
        """
        J48 is Weka's implementation of the C4.5 decision tree.
        In this Python project, an entropy-based decision tree
        is used as a C4.5-style implementation.
        """
    )

    st.code(load_code("j48.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        J48 is based on the C4.5 decision tree approach.

        Tree Depth tells us how deep the tree is.

        Number of Leaves tells us how many final decision
        nodes are present.
        """
    )


# =========================================================
# NAIVE BAYES
# =========================================================

elif technique == "Naive Bayes":

    st.header("🎲 Naive Bayes Classification")

    st.write(
        """
        Naive Bayes uses probability to predict
        the class of a student.
        """
    )

    st.code(load_code("naive_bayes.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Naive Bayes calculates the probability of each class.

        The class having the highest probability
        is selected as the prediction.
        """
    )


# =========================================================
# DECISION TREE
# =========================================================

elif technique == "Decision Tree":

    st.header("🌳 Decision Tree Classification")

    st.write(
        """
        Decision Tree creates decision rules and uses
        them to classify students.
        """
    )

    st.code(load_code("decision_tree.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Decision Tree divides data using decision rules.

        In this practical, Gini is used as the splitting criterion.
        """
    )


# =========================================================
# K-NN
# =========================================================

elif technique == "K-NN":

    st.header("👥 K-Nearest Neighbours (K-NN)")

    st.write(
        """
        K-NN classifies a student based on the classes
        of the closest students in the feature space.
        """
    )

    st.code(load_code("knn.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        K-NN uses distance measures (like Euclidean distance).

        The value of K decides how many neighbours vote
        for the final class.
        """
    )


# =========================================================
# K-MEANS
# =========================================================

elif technique == "K-Means":

    st.header("🔵 K-Means Clustering")

    st.write(
        """
        K-Means is an unsupervised technique that groups
        students into clusters based on similarity.
        """
    )

    st.code(load_code("kmeans.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        K-Means does not need class labels (Pass/Fail).

        It finds natural groupings:
        e.g., Low performers, Average performers, High performers.
        """
    )


# =========================================================
# APRIORI
# =========================================================

elif technique == "Apriori":

    st.header("🛒 Apriori Association Rule Mining")

    st.write(
        """
        Apriori discovers relationships between different
        learning activities of students.
        """
    )

    st.code(load_code("apriori.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Apriori uses Support, Confidence, and Lift.

        Example Rule:
        {Regular Attendance, Completes Assignments} -> {Pass}
        """
    )


# =========================================================
# TEXT MINING
# =========================================================

elif technique == "Text Mining":

    st.header("📝 Text Mining on Student Feedback")

    st.write(
        """
        Text Mining extracts meaningful patterns
        from unstructured text written by students.
        """
    )

    st.code(load_code("text_mining.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Text Mining converts words into numbers using TF-IDF.

        It helps identify common themes and sentiment
        in student feedback.
        """
    )


# =========================================================
# WEB MINING
# =========================================================

elif technique == "Web Mining":

    st.header("🌐 Web Mining on Student LMS Activity")

    st.write(
        """
        Web Mining analyzes how students interact with
        an online learning management portal.
        """
    )

    st.code(load_code("web_mining.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Web Mining analyzes student interaction
        with an online learning system.

        Important variables include:
        • Login Count
        • Pages Visited
        • Video Watching Time
        • Quiz Attempts
        • Assignment Downloads
        """
    )


# =========================================================
# MULTIMEDIA MINING
# =========================================================

elif technique == "Multimedia Mining":

    st.header("🎥 Multimedia Mining")

    st.write(
        """
        Multimedia Mining analyzes educational
        image and video resources.
        """
    )

    st.code(load_code("multimedia_mining.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Multimedia Mining represents multimedia
        using measurable features like Brightness, Size, and Duration.

        Similar resources can then be grouped together.
        """
    )


# =========================================================
# SPATIAL MINING
# =========================================================

elif technique == "Spatial Mining":

    st.header("📍 Spatial Mining")

    st.write(
        """
        Spatial Mining identifies patterns in
        area-level student data.
        """
    )

    st.code(load_code("spatial_mining.py"), language="python")

    st.subheader("💡 What did we learn?")

    st.info(
        """
        Spatial Mining studies patterns related to location.

        In this project we analyze Area, Latitude, Longitude,
        Number of Students, Attendance, and Average Marks.
        """
    )


# =========================================================
# DAA PRACTICAL 1: TIME COMPLEXITY (STEP COUNTING METHOD)
# =========================================================

elif technique == "DAA Practical 1: Time Complexity (Step Counting)":

    st.header("⏱️ DAA Practical 1: Algorithm Analysis – Time Complexity Calculation")

    st.write(
        """
        **Step Counting Method**: In algorithm analysis, the step count method determines
        the exact count of primitive operations performed as a function of problem size $n$.
        """
    )

    tab1, tab2, tab3 = st.tabs([
        "📌 Non-Recursive (Finding Maximum)",
        "📌 Recursive (Factorial)",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac1_max.py"), language="python")

        st.subheader("📋 Output")
        st.code("Maximum Element: 80\nTotal Steps: 9", language="text")

        st.subheader("💡 Complexity Analysis & Step Calculation")
        st.info(
            """
            • **Input Array**: `[10, 50, 20, 80, 40]` (Length $n = 5$)\n
            • **Step breakdown**:
              - 1 step for `maximum = arr[0]`
              - 4 loop iterations ($n-1$ times)
              - Comparisons and assignment steps
              - Total Steps = 9\n
            • **Time Complexity**: $\\mathcal{O}(n)$ (Linear Time)\n
            • **Space Complexity**: $\\mathcal{O}(1)$ (Constant Space)
            """
        )

    with tab2:
        st.code(load_code("daa/prac1_fact.py"), language="python")

        st.subheader("📋 Output")
        st.code("Factorial = 120\nTotal Steps = 5", language="text")

        st.subheader("💡 Complexity Analysis & Step Calculation")
        st.info(
            """
            • **Input**: `num = 5`\n
            • **Calculation**: $5! = 5 \\times 4 \\times 3 \\times 2 \\times 1 = 120$\n
            • **Recurrence Relation**: $T(n) = T(n-1) + 1$, where $T(1) = 1$\n
            • **Total Steps**: 5 recursive function calls\n
            • **Time Complexity**: $\\mathcal{O}(n)$\n
            • **Space Complexity**: $\\mathcal{O}(n)$ due to call stack frames
            """
        )

    with tab3:
        st.code(load_code("daa/prac1_step_count.py"), language="python")


# =========================================================
# DAA PRACTICAL 2: SORTING ALGORITHMS
# =========================================================

elif technique == "DAA Practical 2: Sorting Algorithms (Bubble, Insertion, Merge)":

    st.header("⚡ DAA Practical 2: Implementing and Analyzing Sorting Algorithms")

    st.write(
        """
        Sorting algorithms arrange elements in a sequence. This practical demonstrates
        **Bubble Sort**, **Insertion Sort**, **Merge Sort**, and evaluates their
        comparative execution times for varying input sizes.
        """
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "2(A) Bubble Sort",
        "2(B) Insertion Sort",
        "2(C) Merge Sort",
        "2(D) Compare Execution Times",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac2_bubble.py"), language="python")
        st.subheader("📋 Output")
        st.code("Sorted List: [1, 2, 3, 5, 8]", language="text")
        st.info("• **Logic**: Repeatedly swaps adjacent elements if out of order.\n• **Worst/Average Time**: $\\mathcal{O}(n^2)$\n• **Space**: $\\mathcal{O}(1)$ in-place.")

    with tab2:
        st.code(load_code("daa/prac2_insertion.py"), language="python")
        st.subheader("📋 Output")
        st.code("Sorted List: [1, 2, 3, 5, 8]", language="text")
        st.info("• **Logic**: Inserts current key into its sorted position by shifting elements.\n• **Worst/Average Time**: $\\mathcal{O}(n^2)$\n• **Best Time**: $\\mathcal{O}(n)$ (already sorted).")

    with tab3:
        st.code(load_code("daa/prac2_merge.py"), language="python")
        st.subheader("📋 Output")
        st.code("Sorted List: [1, 2, 3, 5, 8]", language="text")
        st.info("• **Logic**: Divide and Conquer — divides array in halves, sorts, and merges.\n• **Time Complexity**: $\\mathcal{O}(n \\log n)$ in all cases!\n• **Space**: $\\mathcal{O}(n)$ auxiliary.")

    with tab4:
        st.code(load_code("daa/prac2_compare.py"), language="python")
        st.subheader("📋 Execution Benchmark Results")
        st.code(
            """Input Size: 100
Bubble Time: 0.00045 sec
Insertion Time: 0.00021 sec
Merge Time: 0.00015 sec

Input Size: 500
Bubble Time: 0.01240 sec
Insertion Time: 0.00512 sec
Merge Time: 0.00085 sec

Input Size: 1000
Bubble Time: 0.05210 sec
Insertion Time: 0.02130 sec
Merge Time: 0.00192 sec""",
            language="text"
        )
        st.info("Merge Sort ($\\mathcal{O}(n \\log n)$) scales significantly faster than $\\mathcal{O}(n^2)$ sorting as $n$ increases.")

    with tab5:
        st.code(load_code("daa/prac2_sorting.py"), language="python")


# =========================================================
# DAA PRACTICAL 3: SINGLY LINKED LIST OPERATIONS
# =========================================================

elif technique == "DAA Practical 3: Singly Linked List Operations":

    st.header("🔗 DAA Practical 3: Singly Linked List Operations")

    st.write(
        """
        A Singly Linked List is a linear data structure of dynamically allocated nodes.
        Each node stores a `data` value and a `next` pointer reference.
        """
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "3(A) Insert at Beginning",
        "3(B) Insert at End",
        "3(C) Delete from Beginning",
        "3(D) Search Element",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac3_insert_beg.py"), language="python")
        st.subheader("📋 Output")
        st.code("10 -> 20 -> 30 -> None", language="text")
        st.info("• **Operation**: `new.next = head; head = new`\n• **Time Complexity**: $\\mathcal{O}(1)$")

    with tab2:
        st.code(load_code("daa/prac3_insert_end.py"), language="python")
        st.subheader("📋 Output")
        st.code("10 -> 20 -> 30 -> None", language="text")
        st.info("• **Operation**: Traverse to `temp.next is None`, link `temp.next = new`\n• **Time Complexity**: $\\mathcal{O}(n)$")

    with tab3:
        st.code(load_code("daa/prac3_del_beg.py"), language="python")
        st.subheader("📋 Output")
        st.code("20 -> 30 -> None", language="text")
        st.info("• **Operation**: `head = head.next`\n• **Time Complexity**: $\\mathcal{O}(1)$")

    with tab4:
        st.code(load_code("daa/prac3_search.py"), language="python")
        st.subheader("📋 Output (Searching for 20)")
        st.code("Element Found", language="text")
        st.info("• **Operation**: Traverse nodes sequentially comparing `temp.data == key`\n• **Time Complexity**: $\\mathcal{O}(n)$")

    with tab5:
        st.code(load_code("daa/prac3_singly_linked_list.py"), language="python")


# =========================================================
# DAA PRACTICAL 4: CIRCULAR LINKED LIST OPERATIONS
# =========================================================

elif technique == "DAA Practical 4: Circular Linked List Operations":

    st.header("🔄 DAA Practical 4: Circular Linked List Operations")

    st.write(
        """
        In a Circular Linked List, the tail node's `next` pointer references the head node,
        creating an unbroken loop with no `None` terminator.
        """
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "4(A) Insert at Beginning",
        "4(B) Insert at End",
        "4(C) Delete from Beginning",
        "4(D) Delete from End",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac4_insert_beg.py"), language="python")
        st.subheader("📋 Output")
        st.code("5 -> 10 -> 20 -> 30 -> Head", language="text")
        st.info("• Insert 5 at beginning: `new.next = a`, update tail `c.next = new`, `head = new`.")

    with tab2:
        st.code(load_code("daa/prac4_insert_end.py"), language="python")
        st.subheader("📋 Output")
        st.code("10 -> 20 -> 30 -> 40 -> Head", language="text")
        st.info("• Insert 40 at end: `c.next = new`, `new.next = a` (head).")

    with tab3:
        st.code(load_code("daa/prac4_del_beg.py"), language="python")
        st.subheader("📋 Output")
        st.code("20 -> 30 -> Head", language="text")
        st.info("• Delete 10 from beginning: `head = b`, tail updated `c.next = head`.")

    with tab4:
        st.code(load_code("daa/prac4_del_end.py"), language="python")
        st.subheader("📋 Output")
        st.code("10 -> 20 -> Head", language="text")
        st.info("• Delete 30 from end: Second-to-last node `b.next = a`.")

    with tab5:
        st.code(load_code("daa/prac4_circular_linked_list.py"), language="python")


# =========================================================
# DAA PRACTICAL 5: STACK & TOWER OF HANOI
# =========================================================

elif technique == "DAA Practical 5: Stack & Tower of Hanoi":

    st.header("🥞 DAA Practical 5: Stack Operations & Tower of Hanoi")

    st.write(
        """
        A Stack is a Last-In, First-Out (LIFO) data structure.
        This practical covers array and linked list stack implementations,
        stack underflow safeguards, and the recursive **Tower of Hanoi**.
        """
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "5(A) Stack Using Array",
        "5(B) Stack Using Linked List",
        "5(C) Tower of Hanoi",
        "5(D) Underflow Check",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac5_array.py"), language="python")
        st.subheader("📋 Output")
        st.code("Stack: [10, 20, 30]\nPopped: 30\nTop: 20\nStack: [10, 20]", language="text")
        st.info("• Python `list.append()` and `list.pop()` execute in $\\mathcal{O}(1)$ amortized time.")

    with tab2:
        st.code(load_code("daa/prac5_ll.py"), language="python")
        st.subheader("📋 Output")
        st.code("10 -> 20 -> 30 -> None\nPopped: 30\n10 -> 20 -> None", language="text")
        st.info("• Nodes are linked at the top pointer for $\\mathcal{O}(1)$ push and pop operations.")

    with tab3:
        st.code(load_code("daa/prac5_hanoi.py"), language="python")
        st.subheader("📋 Output (3 Disks from A to C via B)")
        st.code("A -> C\nA -> B\nC -> B\nA -> C\nB -> A\nB -> C\nA -> C", language="text")
        st.info("• Number of moves for $n$ disks: $2^n - 1$ (For $n=3$, exactly 7 moves).\n• Time Complexity: $\\mathcal{O}(2^n)$.")

    with tab4:
        st.code(load_code("daa/prac5_underflow.py"), language="python")
        st.subheader("📋 Output")
        st.code("Stack: [10, 20, 30]\nDeleted: 30\nDeleted: 20\nDeleted: 10\nStack Underflow\nFinal Stack: []", language="text")
        st.info("• Underflow verification prevents program termination when attempting to pop from an empty stack.")

    with tab5:
        st.code(load_code("daa/prac5_stack_and_hanoi.py"), language="python")


# =========================================================
# DAA PRACTICAL 6: BALANCED PARENTHESES CHECKER
# =========================================================

elif technique == "DAA Practical 6: Balanced Parentheses Checker":

    st.header("🔢 DAA Practical 6: Balanced Parentheses Checker Using Stack")

    st.write(
        """
        Compilers and expression evaluators use stacks to verify matched delimiters
        like `()`, `[]`, and `{}`. Every closing bracket must correspond to the latest
        opened bracket.
        """
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "6(A) Balanced Expression",
        "6(B) Unbalanced Expression",
        "6(C) Three Types of Brackets",
        "6(D) Multiple Expressions Test",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac6_balanced.py"), language="python")
        st.subheader("📋 Output for `(a+b)*(c-d)`")
        st.code("Balanced", language="text")

    with tab2:
        st.code(load_code("daa/prac6_unbalanced.py"), language="python")
        st.subheader("📋 Output for `(a+b)*(c-d`")
        st.code("Not Balanced", language="text")

    with tab3:
        st.code(load_code("daa/prac6_brackets.py"), language="python")
        st.subheader("📋 Output for `{[()]}`")
        st.code("Balanced", language="text")
        st.info("• Validates curly, square, and round brackets using dictionary mapping.")

    with tab4:
        st.code(load_code("daa/prac6_multiple.py"), language="python")
        st.subheader("📋 Output")
        st.code(
            """(a+b) : Balanced
(a+b : Not Balanced
((a+b)) : Balanced
a+b) : Not Balanced""",
            language="text"
        )

    with tab5:
        st.code(load_code("daa/prac6_parentheses.py"), language="python")


# =========================================================
# DAA PRACTICAL 7: QUEUE OPERATIONS
# =========================================================

elif technique == "DAA Practical 7: Queue Operations (Array, Circular, Deque)":

    st.header("🚶 DAA Practical 7: Queue Using Array and Linked List")

    st.write(
        """
        A Queue is a First-In, First-Out (FIFO) linear data structure.
        This practical explores Python List Queues, Circular Queues using modulo indexing,
        and high-performance Doubly-Linked Deques (`collections.deque`).
        """
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "7(A) Queue Using List",
        "7(B) Circular Queue",
        "7(C) Queue Using Deque",
        "7(D) Compare List vs Deque",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac7_list.py"), language="python")
        st.subheader("📋 Output")
        st.code("Queue: [10, 20, 30]\nDeleted: 10\nQueue: [20, 30]", language="text")

    with tab2:
        st.code(load_code("daa/prac7_circular.py"), language="python")
        st.subheader("📋 Output")
        st.code("Queue Full\nDeleted: 10\n[40, 20, 30]", language="text")
        st.info("• Eliminates memory wastage in arrays using circular wrapping: `(rear + 1) % size`.")

    with tab3:
        st.code(load_code("daa/prac7_deque.py"), language="python")
        st.subheader("📋 Output")
        st.code("Queue: [10, 20, 30]\nDeleted: 10\nQueue: [20, 30]", language="text")

    with tab4:
        st.code(load_code("daa/prac7_compare.py"), language="python")
        st.subheader("📋 Output (10,000 Operations)")
        st.code("List Time: 0.0125 sec\nDeque Time: 0.0018 sec", language="text")
        st.info("• `list.pop(0)` is $\\mathcal{O}(n)$ because remaining elements must shift left.\n• `deque.popleft()` is $\\mathcal{O}(1)$ doubly-linked pointer reassignment.")

    with tab5:
        st.code(load_code("daa/prac7_queue.py"), language="python")


# =========================================================
# DAA PRACTICAL 8: GRAPH TRAVERSALS (DFS / BFS)
# =========================================================

elif technique == "DAA Practical 8: Graph Representation & Traversals (DFS/BFS)":

    st.header("🕸️ DAA Practical 8: Graph Representation and Traversals (DFS & BFS)")

    st.write(
        """
        A Graph is a non-linear data structure with vertices and edges.
        This practical demonstrates Adjacency List & Matrix representations,
        Depth First Search (DFS), and Breadth First Search (BFS).
        """
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "8(A) Adjacency List & Matrix",
        "8(C) Depth First Search (DFS)",
        "8(D) Breadth First Search (BFS)",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac8_adj.py"), language="python")
        st.subheader("📋 Output")
        st.code(
            """0 : [1, 2]
1 : [0, 3]
2 : [0, 4]
3 : [1, 4]
4 : [2, 3]
[0, 1, 1, 0, 0]
[1, 0, 0, 1, 0]
[1, 0, 0, 0, 1]
[0, 1, 0, 0, 1]
[0, 0, 1, 1, 0]""",
            language="text"
        )
        st.info("• Adjacency List stores only existing edges ($\\mathcal{O}(V + E)$ space).\n• Adjacency Matrix stores full $V \\times V$ table ($\\mathcal{O}(V^2)$ space).")

    with tab2:
        st.code(load_code("daa/prac8_dfs.py"), language="python")
        st.subheader("📋 Traversal Output")
        st.code("DFS Traversal:\n0 1 3 4 2", language="text")
        st.info("• Explores as deep as possible before backtracking.\n• Time Complexity: $\\mathcal{O}(V + E)$.")

    with tab3:
        st.code(load_code("daa/prac8_bfs.py"), language="python")
        st.subheader("📋 Traversal Output")
        st.code("BFS Traversal:\n0 1 2 3 4", language="text")
        st.info("• Explores level-by-level using a FIFO queue.\n• Time Complexity: $\\mathcal{O}(V + E)$.")

    with tab4:
        st.code(load_code("daa/prac8_graph.py"), language="python")


# =========================================================
# DAA PRACTICAL 9: DIJKSTRA'S SHORTEST PATH
# =========================================================

elif technique == "DAA Practical 9: Dijkstra's Shortest Path Algorithm":

    st.header("🗺️ DAA Practical 9: Shortest Path Using Dijkstra’s Algorithm")

    st.write(
        """
        Dijkstra's Algorithm solves the single-source shortest path problem on weighted graphs
        with non-negative edge weights using a Greedy approach.
        """
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "9(A) Weighted Graph & All Distances",
        "9(C) Shortest Distance to Vertex 'D'",
        "9(D) Custom Source Input (Interactive)",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac9_graph.py"), language="python")
        st.subheader("📋 Output")
        st.code(
            """A : {'B': 4, 'C': 2}
B : {'A': 4, 'D': 3}
C : {'A': 2, 'D': 1}
D : {'B': 3, 'C': 1}
Shortest Distances: {'A': 0, 'B': 4, 'C': 2, 'D': 3}""",
            language="text"
        )
        st.info("• Path from A to D: A -> C (2) + C -> D (1) = 3.")

    with tab2:
        st.code(load_code("daa/prac9_vertex.py"), language="python")
        st.subheader("📋 Output")
        st.code("Shortest Distance to D: 3", language="text")

    with tab3:
        st.code(load_code("daa/prac9_input.py"), language="python")

        st.subheader("🎮 Interactive Dijkstra Demonstration")
        src = st.selectbox("Select Source Vertex", ["A", "B", "C", "D"], index=0, key="dijkstra_select")
        graph_d = {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'D': 3},
            'C': {'A': 2, 'D': 1},
            'D': {'B': 3, 'C': 1}
        }
        dist = {v: float('inf') for v in graph_d}
        dist[src] = 0
        visited = set()
        while len(visited) < len(graph_d):
            u = min((v for v in graph_d if v not in visited), key=lambda v: dist[v])
            visited.add(u)
            for v, w in graph_d[u].items():
                dist[v] = min(dist[v], dist[u] + w)
        st.write(f"**Computed shortest distances from '{src}':**")
        st.json(dist)

    with tab4:
        st.code(load_code("daa/prac9_dijkstra.py"), language="python")


# =========================================================
# DAA PRACTICAL 10: SEARCHING TECHNIQUES
# =========================================================

elif technique == "DAA Practical 10: Searching Techniques (Linear, Binary, Interpolation)":

    st.header("🔍 DAA Practical 10: Searching Techniques")

    st.write(
        """
        Searching algorithms locate keys within datasets. This practical compares
        **Linear Search** ($\\mathcal{O}(n)$), **Binary Search** ($\\mathcal{O}(\\log n)$),
        and **Interpolation Search** ($\\mathcal{O}(\\log \\log n)$).
        """
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "10(A) Linear Search",
        "10(B) Binary Search",
        "10(C) Interpolation Search",
        "10(D) Execution Time Benchmark",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac10_linear.py"), language="python")
        st.subheader("📋 Output (Searching for 30 in [10, 20, 30, 40, 50])")
        st.code("Found at position 3", language="text")
        st.info("• Sequentially scans all items. Works on unsorted data in $\\mathcal{O}(n)$.")

    with tab2:
        st.code(load_code("daa/prac10_binary.py"), language="python")
        st.subheader("📋 Output (Searching for 30 in [10, 20, 30, 40, 50])")
        st.code("Found at position 3", language="text")
        st.info("• Requires sorted array. Halves search interval each step in $\\mathcal{O}(\\log n)$.")

    with tab3:
        st.code(load_code("daa/prac10_interpolation.py"), language="python")
        st.subheader("📋 Output (Searching for 30 in [10, 20, 30, 40, 50])")
        st.code("Found at position 3", language="text")
        st.info("• Estimates target position using probe formula: `pos = low + (key - a[low])*(high - low)//(a[high] - a[low])`\n• Average Time Complexity: $\\mathcal{O}(\\log \\log n)$.")

    with tab4:
        st.code(load_code("daa/prac10_compare.py"), language="python")
        st.subheader("📋 Benchmark Output (1,000 Elements)")
        st.code(
            """Linear Position: 500 Time: 0.000045 sec
Binary Position: 500 Time: 0.000008 sec
Interpolation Position: 500 Time: 0.000004 sec""",
            language="text"
        )
        st.info("Interpolation and Binary search are orders of magnitude faster on large sorted lists.")

    with tab5:
        st.code(load_code("daa/prac10_searching.py"), language="python")


# =========================================================
# DAA PRACTICAL 11: AVL TREE IMPLEMENTATION
# =========================================================

elif technique == "DAA Practical 11: AVL Tree Implementation & Rotations":

    st.header("🎄 DAA Practical 11: AVL Tree Implementation & Rotations")

    st.write(
        """
        An AVL Tree is a self-balancing Binary Search Tree (BST) where the difference
        between heights of left and right subtrees (Balance Factor) cannot exceed 1.
        Rotations (LL, RR, LR, RL) automatically maintain balance after insertions.
        """
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "11(A) Insert into AVL Tree",
        "11(B) Right Rotation (LL Case)",
        "11(C) Left Rotation (RR Case)",
        "11(D) Automatic Balancing",
        "💻 Complete Practical Code"
    ])

    with tab1:
        st.code(load_code("daa/prac11_insert.py"), language="python")
        st.subheader("📋 Inorder Traversal Output (Keys: [30, 20, 10])")
        st.code("10 20 30", language="text")
        st.info("• Inorder traversal of an AVL tree produces sorted keys in $\\mathcal{O}(n)$ time.")

    with tab2:
        st.code(load_code("daa/prac11_right_rotate.py"), language="python")
        st.subheader("📋 Output (Right Rotate on 30 -> 20 -> 10)")
        st.code("New Root: 20", language="text")
        st.info("• LL imbalance is restored by rotating right around root 30; 20 becomes new root.")

    with tab3:
        st.code(load_code("daa/prac11_left_rotate.py"), language="python")
        st.subheader("📋 Output (Left Rotate on 10 -> 20 -> 30)")
        st.code("New Root: 20", language="text")
        st.info("• RR imbalance is restored by rotating left around root 10; 20 becomes new root.")

    with tab4:
        st.code(load_code("daa/prac11_auto_balance.py"), language="python")
        st.subheader("📋 Preorder Traversal Output (Balanced Tree)")
        st.code("20 10 30", language="text")
        st.info("• Root is 20 with left child 10 and right child 30, proving automatic balance!")

    with tab5:
        st.code(load_code("daa/prac11_avl_tree.py"), language="python")


# =========================================================
# FOOTER
# =========================================================

st.sidebar.markdown("---")

st.sidebar.write(
    "🎓 Student Data Mining Project"
)

st.sidebar.write(
    "Python + Pandas + Scikit-learn + Streamlit"
)
