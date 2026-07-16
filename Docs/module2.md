# Module 02 – Scan Management

> **Module ID:** M02  
> **Module Name:** Scan Management  
> **Primary User:** Staff  
> **Related Modules:** Module 01 – Batch & Student Management

---

# 1. Overview

The **Scan Management** module enables staff members to record daily observations of students throughout the training program.

Each observation evaluates a student's performance across four learning areas:

- Information Technology (IT)
- Personal & Life Skills (PLT)
- English
- Digital Arts (DA)

For every subject, staff members can assign a performance rating and write observation notes.

Observations are organized by **daily sessions**, allowing instructors to monitor completion progress, collaborate with other teachers, and maintain a consistent daily record for each batch.

This module serves as one of the primary sources of behavioral and academic monitoring throughout the student's learning journey.

---

# 2. Objectives

This module enables staff members to:

- Record daily observations for students.
- Record observations individually or in bulk.
- Monitor daily observation progress.
- Prevent duplicate observation records.
- Support collaborative editing among multiple teachers.
- Complete observation sessions.
- Search and manage student observation records efficiently.
- View dashboard statistics related to observation activities.

---

# 3. Key Concepts

## 3.1 Scan Record

A **Scan Record** represents the observation of **one student on one specific date**.

Each Scan Record contains observations for four subjects.

| Subject | Data Stored |
|----------|------------|
| IT | Rating + Notes |
| PLT | Rating + Notes |
| English | Rating + Notes |
| Digital Arts | Rating + Notes |

Each student should normally have only one observation record per day.

---

## 3.2 Scan Session

A **Scan Session** represents all observation records for one batch on one day.

Session status may be:

| Status | Description |
|---------|-------------|
| Incomplete | Observation is still in progress. |
| Complete | Observation session has been closed. |

Sessions help staff monitor observation completion across an entire batch.

---

# 4. Observation Rating

The system supports four observation ratings.

| Symbol | Meaning | System Value |
|---------|---------|--------------|
| G | Excellent | excellent |
| S | Satisfactory | satisfactory |
| NI | Needs Improvement | needs-improvement |
| — | Not Yet Assessed | Empty |

The rating is used for reporting and student performance tracking.

---

# 5. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M02-F01 | Single Observation Entry | Record observations for one student across four subjects. |
| M02-F02 | Auto Rating Suggestion | Suggest an observation rating approximately 400 milliseconds after notes are entered. |
| M02-F03 | Batch Entry – All Subjects | Spreadsheet-style entry for all students simultaneously. |
| M02-F04 | Batch Entry – By Subject | Enter one subject for multiple students. |
| M02-F05 | Observation Editing | Update ratings and notes while keeping observation date locked. |
| M02-F06 | Duplicate Detection & Merge | Merge or reject duplicate observation records according to business rules. |
| M02-F07 | Session Management | Complete an observation session and automatically fill missing observations. |
| M02-F08 | Session Progress | Display completion statistics and progress indicators. |
| M02-F09 | Concurrent Edit Handling | Support collaborative editing using three-way merge. |
| M02-F10 | Search, Filter & Sorting | Search students and organize observation records efficiently. |
| M02-F11 | Dashboard Overview | Display observation statistics and summary dashboards. |

---

# 6. Business Rules

## 6.1 Observation Scope

Each observation contains evaluations for:

- IT
- PLT
- English
- Digital Arts

Every subject includes:

- Rating
- Notes

---

## 6.2 One Record Per Student Per Day

Normally, each student should have only one observation record for a specific date.

The system automatically detects duplicate records.

---

## 6.3 Observation Date

The observation date is fixed once the record is created.

It cannot be modified afterward.

---

## 6.4 Auto Rating Suggestion

While staff members type observation notes, the system analyzes the content.

Approximately **400 milliseconds** after typing stops, the system suggests an appropriate rating.

Possible suggestions include:

- G
- S
- NI

Users may accept or overwrite the suggested rating.

---

## 6.5 Batch Entry

The module supports two batch entry modes.

### All Subjects

Allows staff to complete all subjects for multiple students simultaneously.

Example result:

```
Saved 18 students
Skipped 2 students
```

---

### By Subject

Allows teachers responsible for a single subject to complete only their assigned subject.

Example:

```
Subject: English

Student A
Student B
Student C
```

---

## 6.6 Duplicate Detection

The system determines duplicate observations using:

- Student
- Observation Date

### Rule 1

If fewer than three subjects have already been completed,

the new observation is merged into the existing record.

Example message:

```
Added to existing session.
```

---

### Rule 2

If three or more subjects have already been completed,

the system rejects the new record.

Staff must edit the existing observation instead.

---

## 6.7 Session Completion

When staff selects

```
Mark Session Complete
```

the system:

- closes the session
- automatically assigns **N/A** to students without observation notes
- prevents additional observation creation within the completed session

---

## 6.8 Concurrent Editing

Multiple staff members may edit the same observation simultaneously.

The system uses **Three-Way Merge** to preserve non-conflicting changes.

Conflicting fields generate a warning message.

---

## 6.9 Search & Filtering

Users can:

- Search by full student name
- Search by partial name
- Filter by observation status
- Sort alphabetically
- Sort by observation completion
- Combine search and filtering

---

## 6.10 Dashboard

The dashboard provides real-time statistics including:

- Total Batches
- Total Students
- Active Observation Sessions
- Completed Sessions
- Observation Completion Rate
- Student Distribution
- Course Summary

Dashboard information refreshes automatically when observation data changes.

---

# 7. Three-Way Merge

The module supports collaborative editing.

Example

Original Record

```
IT Comment

Good performance
```

Teacher B saves first

```
Excellent performance
```

Teacher A saves later

```
Very good performance
English Comment added
```

Result

| Field | Final Value |
|--------|-------------|
| IT Comment | Excellent performance |
| English Comment | Saved successfully |

Teacher A receives a warning informing them that another teacher updated the IT Comment.

---

# 8. Validation Rules

| Item | Validation |
|------|------------|
| Observation Date | Required |
| Student | Required |
| Subject | Required |
| Rating | Must be G, S, NI or Empty |
| Notes | Optional |
| Duplicate Record | Checked automatically |
| Session Status | Must be Incomplete before editing |

---

# 9. Error Messages

| Condition | Message |
|-----------|---------|
| Duplicate observation | A feedback record for this date already exists. |
| Existing session merged | Added to existing session. |
| Session outdated | Form may be outdated. |
| Concurrent update | Saved, but some fields were updated by another teacher. |
| Server busy | Server is busy. Please try again later. |

---

# 10. Dependencies

This module depends on:

- Module 01 – Batch & Student Management

The following information must already exist:

- Batch
- Student
- Active student list

Observation data is referenced by:

- Module 04 – Class Council
- Module 09 – Student Portal (future reporting)

---

# 11. Test Data Preparation

Before executing UAT, prepare:

## Accounts

- Two Staff accounts

(Required for concurrent editing tests.)

---

## Batch

One active batch containing at least five students.

---

## Students

Minimum:

```
Student A
Student B
Student C
Student D
Student E
```

---

## Observation Data

Prepare scenarios including:

- Empty observation
- One completed subject
- Three completed subjects
- Completed session
- Incomplete session

These datasets are required for duplicate detection, merge, and session completion testing.

---

# 12. UAT Test Scenarios

The following test scenarios are covered separately:

- SC-01 → SC-12

These scenarios validate:

- Single observation
- Rating suggestion
- Batch entry
- Observation editing
- Duplicate handling
- Session completion
- Progress tracking
- Concurrent editing
- Session timeout

---

# 13. Out of Scope

The following functions are not supported:

- Student self-observation
- Permanent deletion of observation history
- Editing observation dates
- Manual modification of completed sessions

---

# 14. Module Summary

The Scan Management module provides the daily monitoring mechanism used by staff to evaluate student learning progress.

It supports both individual and batch observation entry, intelligent duplicate handling, collaborative editing through three-way merge, and session management for efficient daily operations.

Because observation records contribute to student evaluations and future reporting, maintaining data consistency and preventing duplicate entries are essential responsibilities of this module.