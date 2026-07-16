# Module 09 – Student Portal

> **Module ID:** M09  
> **Module Name:** Student Portal  
> **Primary User:** Student  
> **Related Modules:** Module 03 – Academic Management, Module 06 – Bi-Weekly Internship Reports

---

# 1. Overview

The **Student Portal** provides a dedicated interface for students who log in using their official **@student.passerellesnumeriques.org** account.

The portal allows students to securely access their own academic records and internship reports without exposing any administrative functions.

Unlike the Staff Portal, this module is completely **read-only** for academic information. Students cannot modify grades, GPA, transcripts, or any academic records.

The portal currently consists of a single **Academic** tab, where students can:

- View academic results by semester
- Browse subjects grouped by academic category
- View detailed grades for each subject
- Access Bi-Weekly Internship Reports (when eligible)

This module serves as the official student-facing academic portal.

---

# 2. Objectives

This module enables students to:

- Log in using their official student account.
- View their academic records by semester.
- View detailed subject grades.
- View GPA, final score, and letter grades.
- Identify subjects requiring re-study.
- Access internship reports during the internship period.
- Securely access only their own academic information.

---

# 3. Portal Structure

The Student Portal consists of a single Academic section.

```
Student Portal

└── Academic
      ├── Semester Selector (1–6)
      ├── Subject Categories
      │      ├── Fundamental
      │      ├── IT
      │      ├── English
      │      └── Soft Skills
      │
      ├── Subject Grade Tables
      │
      └── Bi-Weekly Internship Reports
             (Visible only during internship)
```

---

# 4. Academic Grade Display

Each subject displays detailed grading information.

| Column | Description |
|----------|-------------|
| KT TX | Regular Test |
| ĐK1 – ĐK6 | Periodic Tests |
| TCK | Final Examination |
| TLCK | Retake Examination |
| /10 | Final Score |
| /4 | GPA |
| Letter Grade | A+ – F |
| Re-study | Indicates whether the subject must be retaken |

All displayed data is read-only.

---

# 5. Grade Display Rules

## Empty Grades

If a score has not yet been entered,

the system displays

```
—
```

instead of

```
0
```

or an error message.

---

## Score Color Coding

### Final Score (/10)

| Score | Color |
|--------|-------|
| ≥ 8.0 | 🟢 Green |
| 5.5 – 7.9 | 🟡 Orange |
| < 5.5 | 🔴 Red |

---

### GPA (/4)

| GPA | Color |
|------|-------|
| ≥ 3.5 | 🟢 Green |
| 2.0 – 3.4 | 🟡 Orange |
| < 2.0 | 🔴 Red |

Color indicators help students quickly identify their academic performance.

---

# 6. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M09-F01 | Role-based Auto-login | Google OAuth automatically redirects users to the appropriate portal based on their email domain. |
| M09-F02 | Read-only Academic View | Students can view academic results grouped by semester and category without editing permissions. |
| M09-F03 | Empty Grade Display | Missing grades are displayed as "—" instead of zero or an error. |
| M09-F04 | Score Color Coding | Scores are color-coded based on performance thresholds. |
| M09-F05 | Re-study Flag Display | Subjects marked for retake display a red Re-study label. |
| M09-F06 | Quick Access to Bi-Weekly Reports | Internship report shortcut is available only for students currently participating in an On-going internship group. |
| M09-F07 | Data Isolation | Students can access only their own academic information through server-side authorization. |

---

# 7. Business Rules

## 7.1 Authentication

Students log in using Google OAuth.

Only users with

```
@student.passerellesnumeriques.org
```

accounts are allowed to access the Student Portal.

Users from other domains are redirected according to their role or denied access.

---

## 7.2 Semester Selection

Students can switch between available semesters.

The selected semester determines which academic records are displayed.

---

## 7.3 Subject Organization

Subjects are grouped into academic categories.

Example:

- Fundamental
- IT
- English
- Soft Skills

Each category displays its associated subjects.

---

## 7.4 Read-only Access

Students are not allowed to:

- Edit grades
- Delete grades
- Upload transcripts
- Modify GPA
- Change letter grades

No Save, Edit, Delete, or Import buttons are displayed.

---

## 7.5 Empty Grades

Scores that have not yet been entered are displayed as

```
—
```

This avoids confusing students with default values such as zero.

---

## 7.6 Color Indicators

The interface automatically applies colors to:

- Final Score (/10)
- GPA (/4)

based on predefined thresholds.

---

## 7.7 Re-study Subjects

Subjects marked for retake display a visible

```
Re-study
```

badge in red.

---

## 7.8 Internship Report Shortcut

The shortcut to Bi-Weekly Internship Reports appears only when:

- the student belongs to an internship group
- the internship group status is **On-going**

Otherwise, the shortcut is hidden.

---

## 7.9 Data Isolation

Students may only access their own records.

The server validates the authenticated email before returning any academic data.

Requests for another student's information are rejected.

---

# 8. Validation Rules

| Item | Validation |
|------|------------|
| Login Account | Must be authenticated via Google OAuth |
| Email Domain | Must match an authorized account |
| Semester | Must exist |
| Academic Data | Read-only |
| Student Identity | Must match authenticated account |
| Internship Shortcut | Visible only for On-going internship students |

---

# 9. Error Handling

| Condition | System Behavior |
|-----------|-----------------|
| Unauthorized email domain | Access denied |
| Student record not found | Display "No academic records found." |
| Grade not entered | Display "—" |
| No internship assignment | Hide internship report shortcut |
| Unauthorized data request | Reject request with authorization error |

---

# 10. Dependencies

This module depends on:

- Module 03 – Academic Management
- Module 06 – Bi-Weekly Internship Reports

Required data:

- Student account
- Academic grades
- GPA
- Letter grades
- Internship assignment

---

# 11. Test Data Preparation

Before executing UAT, prepare:

## Student Accounts

- One valid student account
- One unauthorized account

---

## Academic Data

Prepare multiple semesters containing:

- Complete grades
- Partial grades
- Empty grades
- Re-study subjects

---

## Internship Data

Prepare:

- One student in an On-going internship group
- One student not assigned to any internship group

---

# 12. UAT Test Scenarios

Detailed UAT scenarios are documented separately.

Covered scenarios include:

- Student login
- Semester switching
- Read-only grade viewing
- Empty grade display
- Score color coding
- Re-study badge display
- Internship report shortcut visibility
- Unauthorized access prevention

---

# 13. Out of Scope

The following features are not supported:

- Editing grades
- Editing GPA
- Editing letter grades
- Transcript export
- Grade import
- Teacher comments
- Viewing other students' records

---

# 14. Module Summary

The Student Portal provides students with secure, read-only access to their academic information and internship reports.

It allows students to review semester-based academic performance, visualize grade status through color coding, identify subjects requiring re-study, and conveniently access internship reports when applicable.

All academic data is protected through authenticated access and strict server-side authorization, ensuring each student can view only their own information.