# Module 03 – Academic Management

> **Module ID:** M03  
> **Module Name:** Academic Management  
> **Primary User:** Staff  
> **Related Modules:** Module 01 – Batch & Student Management, Module 09 – Student Portal

---

# 1. Overview

The **Academic Management** module enables staff members to manage academic subjects, record student grades, calculate continuous assessment averages (TBKT), and generate official academic transcripts.

Subjects are organized by **batch** and **semester**, allowing academic records to be maintained separately for each cohort and study period.

Student grades entered in this module are later displayed in the **Student Portal**, where students can view their own academic results in read-only mode.

This module is responsible for maintaining the official academic records of every student throughout the training program.

---

# 2. Objectives

This module enables staff members to:

- Create and manage academic subjects.
- Import subjects using CSV.
- Upload student grades through CSV.
- Calculate the Continuous Assessment Average (TBKT).
- Determine eligibility for the final examination.
- Export official transcript PDFs.
- Maintain GPA and letter grades.

---

# 3. Grade Structure

Each subject contains several grading components.

| Grade Component | Score Range | Description |
|-----------------|------------|-------------|
| KT TX (Regular Test) | 0 – 10 | Weight = 1 |
| ĐK1 – ĐK6 (Periodic Tests) | 0 – 10 | Weight = 2 each |
| TCK (Final Exam) | 0 – 10 | Available only when TBKT ≥ 5.0 |
| TLCK (Retake Exam) | 0 – 10 | Optional retake examination |
| Final Score (/10) | 0 – 10 | Entered manually |
| GPA (/4) | 0 – 4 | Entered manually |
| Letter Grade | A+ – F | Entered manually |

---

# 4. TBKT Calculation

TBKT (Continuous Assessment Average) is calculated using the weighted average formula.

```
TBKT =
(KT_TX × 1 + ĐK1 × 2 + ĐK2 × 2 + ... + ĐKn × 2)
/
(1 + 2 × Number of Periodic Tests)
```

---

## Example 1

```
KT TX = 7.0
ĐK1 = 8.0
```

Calculation

```
(7 × 1 + 8 × 2) / 3
= 23 / 3
= 7.67
```

Result

```
Eligible for Final Exam
YES
```

---

## Example 2

```
KT TX = 6.0
ĐK1 = 7.0
ĐK2 = 8.0
ĐK3 = 9.0
```

Calculation

```
(6 + 14 + 16 + 18)
/
7
=
7.71
```

Result

```
Eligible
YES
```

---

## Example 3

```
KT TX = 3.0
ĐK1 = 5.0
```

Calculation

```
(3 + 10)
/
3
=
4.33
```

Result

```
Not Eligible
NO
```

---

# 5. Grade Color Rules

The system displays grade colors according to the following rules.

## Final Score (/10)

| Score | Color |
|--------|-------|
| ≥ 8.0 | 🟢 Green |
| 5.5 – 7.9 | 🟡 Orange |
| < 5.5 | 🔴 Red |

---

## GPA (/4)

| GPA | Color |
|-----|-------|
| ≥ 3.5 | 🟢 Green |
| 2.0 – 3.4 | 🟡 Orange |
| < 2.0 | 🔴 Red |

These colors are displayed in reports and the Student Portal.

---

# 6. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M03-F01 | Course / Subject Creation | Create subjects individually or through CSV import. |
| M03-F02 | Grade Entry Structure | Record Regular Test, Periodic Tests, Final Exam, and Retake Exam scores. |
| M03-F03 | Automatic TBKT Calculation | Automatically calculate the weighted continuous assessment average and determine exam eligibility. |
| M03-F04 | Grade Upload via CSV | Upload grades through CSV using overwrite mode. |
| M03-F05 | Subject Deletion | Permanently remove a subject and all associated student scores. |
| M03-F06 | PDF Transcript Export | Export transcript PDFs for one or multiple students. |
| M03-F07 | Manual GPA & Letter Grade Entry | GPA and Letter Grades are entered manually through CSV. |

---

# 7. Business Rules

## 7.1 Subject Management

Subjects can be created:

- Individually
- Through CSV import

Each subject belongs to:

- One Batch
- One Semester

---

## 7.2 Grade Components

Each subject may contain:

- Regular Test
- One or more Periodic Tests
- Final Examination
- Retake Examination

All scores use the same grading scale.

```
0 – 10
```

---

## 7.3 TBKT Calculation

The system automatically calculates TBKT whenever grades are updated.

TBKT determines whether a student is eligible for the Final Examination.

Rule

```
TBKT ≥ 5.0

Eligible
```

```
TBKT < 5.0

Not Eligible
```

---

## 7.4 Exam Eligibility

Students whose TBKT is below 5.0 are not eligible to take the Final Examination.

The interface displays:

```
YES
```

or

```
NO
```

depending on the calculated TBKT.

---

## 7.5 CSV Grade Upload

Grade upload always uses **Overwrite Mode**.

Meaning:

Existing grades are completely replaced by the imported file.

The system does **not** merge individual cells.

---

## 7.6 Blank Values

Blank cells inside the CSV file have meaning.

```
Blank Cell

↓

Delete Existing Grade
```

The previous score is removed.

---

## 7.7 GPA & Letter Grade

The system does **not** calculate:

- GPA
- Letter Grade

These values must be imported manually.

---

## 7.8 Subject Deletion

Deleting a subject permanently removes:

- Subject information
- Student scores
- Academic records associated with the subject

This action cannot be undone.

---

# 8. CSV Import Rules

## Required Column

```
StudentID
```

If this column is missing,

the entire file is rejected.

---

## Decimal Format

The system only accepts

```
8.5
```

The following format is invalid

```
8,5
```

Incorrect decimal separators may result in incorrect stored values.

---

## Blank Cells

Blank values are interpreted as

```
NULL
```

Existing grades are cleared.

---

## GPA & Letter Grade

These values are imported exactly as provided.

No automatic conversion is performed.

---

# 9. Validation Rules

| Item | Validation |
|------|------------|
| Course Name | Required |
| StudentID | Required for CSV |
| Grade | Must be between 0 and 10 |
| Decimal Format | Must use "." |
| GPA | Entered manually |
| Letter Grade | Entered manually |

---

# 10. Error Handling

| Condition | System Behavior |
|-----------|-----------------|
| Missing StudentID | Reject entire CSV file |
| Invalid decimal separator | Imported value may be incorrect |
| Blank grade | Existing value removed |
| Invalid grade | Validation error |
| Delete subject | Confirmation required before deletion |

---

# 11. Dependencies

This module depends on

- Module 01 – Batch & Student Management

Required master data:

- Batch
- Student
- Semester

Academic results produced by this module are consumed by

- Module 09 – Student Portal

---

# 12. Test Data Preparation

Before executing UAT, prepare:

## Batch

One active batch.

---

## Students

At least five students.

---

## Subjects

Example

```
Programming
English
Database
Soft Skills
```

---

## CSV Files

Prepare the following datasets:

- Valid grade import
- Existing grades
- Blank grade values
- Missing StudentID
- Invalid decimal format (8,5)
- GPA and Letter Grade

---

## TBKT Test Data

Example 1

```
KT TX = 7
ĐK1 = 8
```

Expected

```
TBKT = 7.67
YES
```

---

Example 2

```
KT TX = 3
ĐK1 = 5
```

Expected

```
TBKT = 4.33
NO
```

---

# 13. UAT Test Scenarios

Detailed UAT scenarios are documented separately.

Covered scenarios include:

- AC-01 → AC-13

These scenarios validate:

- Subject creation
- Grade calculation
- TBKT calculation
- Exam eligibility
- CSV import
- Subject deletion
- PDF export

---

# 14. Out of Scope

The following functions are not supported:

- Manual editing of transcript PDF
- Automatic GPA calculation
- Automatic Letter Grade conversion
- Undo subject deletion
- Cell-level merge during CSV upload

---

# 15. Module Summary

The Academic Management module is responsible for maintaining official student academic records.

It provides subject management, structured grade entry, automatic TBKT calculation, CSV-based score import, and transcript generation.

Since academic results are published directly to the Student Portal, maintaining data accuracy, validation, and overwrite consistency is essential to ensure reliable academic records throughout the system.