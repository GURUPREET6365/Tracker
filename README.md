# 📚 Revision Scheduler

**Revision Scheduler** is a simple terminal-based study planning system for students who have many subjects and chapters but struggle to organize **what to revise and when to revise it**.

You record your subjects and chapters in the system, and the scheduler helps you decide what to revise based on your **revision history**.

Instead of trying to remember:

> "Which chapter did I revise recently?"
> "Which chapter have I barely revised?"
> "What should I revise today?"

the Revision Scheduler keeps track of this information and creates a revision plan for you.

---

## 🎯 Who is this for?

This is especially useful for students who:

* Have multiple subjects.
* Have many chapters in each subject.
* Complete chapters at different times.
* Forget when they last revised something.
* Struggle to organize revision manually.
* Want a simple system to keep track of revision.
* Want to prioritize chapters that have been revised less frequently.

The scheduler uses the **revision count and revision history** of chapters to help select chapters for your revision plan.

---

# ✨ Features

## 1. Show All Subjects

Displays all the subjects you have created in the system.

Example:

```text
1. Physics
2. Mathematics
3. Computer Science
4. English
```

---

## 2. Show Chapters of a Subject

Select a subject and view all chapters associated with it, along with their stored information.

The information can include:

* Chapter name
* Completion date
* Revision count
* Last revision date
* Strength status
* Revision history

---

## 3. Revision System

Creates a revision schedule for the current day.

You can choose how many subjects/chapters should be included in your daily revision plan through **Personalization**.

The scheduler considers the revision information stored for each chapter and prioritizes chapters that need revision.

> **Note:** You must first create a subject and add it to Personalization before the subject can be used by the Revision System.

---

## 4. Show Today's Schedule

Displays the revision schedule generated for today.

If a schedule has not been generated yet, the system will indicate that there is no schedule available.

---

## 5. Mark Schedule as Completed

Used to mark a scheduled revision as completed.

This can be used for:

* Today's schedule
* Specific-date schedules
* Previously missed revision targets

Completing a revision updates the chapter's revision information so that future scheduling can take it into account.

---

## 6. Update Personalization

Personalization controls how the Revision System behaves for each subject.

You can configure:

### Subject Selection

Choose which subjects should participate in automatic revision planning.

### Revision Interval

Set how many days should pass before a revised chapter becomes eligible for revision again.

For example:

```text
Physics
Revision interval: 3 days
```

If a chapter is revised today, it can become eligible again after the configured interval.

### Daily Chapter Count

Set how many chapters from each subject you want to revise per day.

Example:

```text
Physics       → 2 chapters/day
Mathematics   → 3 chapters/day
Computer      → 1 chapter/day
```

---

## 7. Create New Subject

Creates a new subject that can be used in the system.

You should create your subjects before adding chapters.

Example:

```text
Physics
Mathematics
Chemistry
Computer Science
```

---

## 8. Create New Chapter

Creates a new chapter under a selected subject.

For example:

```text
Subject: Physics
Chapter: Laws of Motion
```

You can then update the chapter information when you complete it.

> **Recommendation:** Add chapters one at a time rather than trying to create many chapters at once.

---

## 9. Update Chapter Data

Used to update information about an existing chapter.

You can update:

* `completed_date`
* `revision_count`
* `strength_status`

This allows the scheduler to understand the current state of your chapters.

---

## 10. Self Choice Subject for Revision

Sometimes you don't want the automatic scheduler to decide everything.

This option allows you to manually select a specific chapter that you want to revise.

The normal Revision System uses revision information to determine what should be revised, while this option gives you direct control.

---

## 11. Exit

Closes the Revision Scheduler.

---

# 🔄 How the System Works

The basic workflow is:

```text
Install Revision Scheduler
          ↓
Create your subjects
          ↓
Add subjects to Personalization
          ↓
Configure revision interval
          ↓
Configure chapters/day
          ↓
Create your chapters
          ↓
Complete your chapters
          ↓
Update chapter data
          ↓
Run Revision System
          ↓
Get today's revision schedule
          ↓
Revise the chapters
          ↓
Mark revisions as completed
          ↓
Scheduler uses the updated data
          ↓
Next revision schedule
```

The important idea is that **the scheduler learns from the data you maintain**.

If you mark revisions correctly, the system can use the revision count and revision history to help prioritize chapters that have received fewer revisions.

---

# ⚠️ Important Usage Recommendation

For now, the system is designed to work best when you perform **one operation at a time**.

For example:

```text
Create Subject
      ↓
Create another Subject
      ↓
Add Chapter
      ↓
Update Chapter
```

Avoid trying to enter multiple chapters or operations together.

Currently, multiple selection is primarily available in the **Revision System's subject/chapter selection**, where you can select multiple items according to your Personalization settings.

---

# 💻 Installation

## Requirements

Before installing Revision Scheduler, you need:

* Windows
* Python 3
* Basic knowledge of opening Command Prompt or PowerShell
* Git *(optional, if cloning the repository)*

---

# 1. Install Python

Download Python from the official Python website:

**https://www.python.org/downloads/**

During installation, make sure you enable:

```text
☑ Add Python to PATH
```

This is important because it allows you to run Python from Command Prompt or PowerShell.

After installation, open PowerShell or Command Prompt and check:

```powershell
python --version
```

You should see something similar to:

```text
Python 3.12.x
```

If `python` does not work, try:

```powershell
py --version
```

If neither command works, Python may not have been installed correctly or may not have been added to PATH.

---

# 2. Download the Project

You can either download the repository as a ZIP file or clone it using Git.

After downloading, extract the project somewhere on your computer.

For example:

```text
D:\MainFolder\Python\Tracker
```

Your project should contain the Revision Scheduler source code and the `setup` directory.

---

# 3. Open the Project in PowerShell

Open PowerShell inside the project directory.

For example:

```powershell
cd D:\MainFolder\Python\Tracker
```

You can verify that you are in the correct directory using:

```powershell
dir
```

You should see the project files and folders.

---

# 4. Create a Virtual Environment

A virtual environment keeps the Python packages required by Revision Scheduler separate from your system-wide Python installation.

Run:

```powershell
python -m venv .venv
```

This creates:

```text
Tracker/
└── .venv/
```

---

# 5. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If you are using Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

After activation, your terminal should show something similar to:

```text
(.venv) PS D:\MainFolder\Python\Tracker>
```

The `(.venv)` indicates that the virtual environment is active.

---

# 6. Install Required Packages

Make sure the virtual environment is activated.

Then run:

```powershell
pip install -r requirements.txt
```

This installs the Python packages required by the project.

---

# 7. Run the Installer

Go to the `setup` directory:

```powershell
cd setup
```

For example:

```text
D:\MainFolder\Python\Tracker\setup>
```

Then run:

```powershell
python install.py
```

The installer will create the required data files and directories for Revision Scheduler.

It will also create:

```text
RevisionScheduler.bat
```

and place a launcher on your Desktop.

---

# 🚀 Running Revision Scheduler

After installation, you don't need to repeatedly activate the virtual environment manually.

Simply double-click:

```text
RevisionScheduler.bat
```

on your Desktop.

The launcher will:

1. Move to the Revision Scheduler project directory.
2. Activate the virtual environment.
3. Start the Revision Scheduler.
4. Keep the terminal open while the program is running.

---

# 🧠 How Revision Planning Works

The Revision System does not simply select chapters randomly.

It uses information stored for chapters, including their revision history and revision count, to determine which chapters should be considered for revision.

For example:

```text
Chapter A → revised 5 times
Chapter B → revised 2 times
Chapter C → revised 0 times
```

The scheduler can prioritize chapters such as:

```text
Chapter C
Chapter B
Chapter A
```

depending on the configured revision interval and other stored information.

The goal is to help prevent chapters from being repeatedly ignored while other chapters receive most of the revision time.

---

# 📅 Example Daily Workflow

A typical day could look like:

### Before studying

Run:

```text
RevisionScheduler.bat
```

Then:

```text
Revision System
      ↓
Generate today's schedule
```

Example:

```text
Today's Revision

Physics
  - Laws of Motion
  - Work, Energy and Power

Mathematics
  - Integration
  - Probability

Computer Science
  - Data Structures
```

Study the chapters.

After completing them:

```text
Mark Schedule as Completed
```

The system then updates the revision information.

---

# 🛠️ Troubleshooting

## `python` is not recognized

If you see an error similar to:

```text
'python' is not recognized as an internal or external command
```

Check:

```powershell
python --version
```

If that does not work, try:

```powershell
py --version
```

If Python is installed but the command is unavailable, reinstall Python and make sure:

```text
Add Python to PATH
```

is selected.

---

## Virtual environment activation fails

Try creating the environment again:

```powershell
python -m venv .venv
```

Then activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you may need to adjust your PowerShell execution policy or use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

---

## `pip install` fails

First make sure the virtual environment is active:

```text
(.venv)
```

should appear in your terminal.

Then try:

```powershell
python -m pip install --upgrade pip
```

and:

```powershell
pip install -r requirements.txt
```

---

## RevisionScheduler.bat does not work

Make sure the `.bat` file was created by running:

```powershell
python install.py
```

from the:

```text
setup
```

directory.

Also make sure the `.venv` directory exists in the project root.

---

# 📁 Project Structure

A simplified version of the project looks like:

```text
Tracker/
│
├── RevisionSystem/
│   ├── ...
│   └── terminalIO.py
│
├── setup/
│   └── install.py
│
├── .venv/
│
├── requirements.txt
├── README.md
└── ...
```

The installer is responsible for preparing the environment and creating the required data structure.

---

# 🔐 Privacy

Revision Scheduler stores your study data locally on your computer.

Your subjects, chapters, revision history, and other information are stored in local JSON files.

The project does not require an online account or cloud database for its basic functionality.

---

# 🚧 Current Limitations

This project is still under development.

Current limitations include:

* Primarily designed for Windows.
* Terminal-based interface.
* Data is stored in JSON files.
* Some operations are intentionally performed one at a time.
* Automatic scheduling logic is still being improved.
* The system currently requires Python to be installed.

More features and improvements may be added in future versions.

---

# 🤝 Contributing

If you find a bug, have an idea, or want to improve the project, feel free to open an issue or submit a pull request.

Suggestions are welcome, especially for:

* Better scheduling algorithms
* User interface improvements
* Data management
* Installation improvements
* Cross-platform support
* Additional study-planning features

---

# 📜 License

See the `LICENSE` file for the license and usage terms of this project.

---

## ⭐ Final Note

The purpose of Revision Scheduler is simple:

> **You focus on studying. The scheduler helps you organize what needs to be revised.**

Set up your subjects, record your chapters, maintain your revision history, and let the system help you plan your revisions.
