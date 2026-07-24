# Module 04 – Class Council Management

> **Module ID:** M04  
> **Module Name:** Class Council Management  
> **Primary User:** Staff  
> **Related Modules:** Module 01 – Batch & Student Management, Module 03 – Academic Management

---

# 1. Overview

The **Class Council Management** module enables teachers and staff members to record end-of-semester evaluations for each student.

Each evaluation summarizes the student's overall learning performance, strengths, weaknesses, and recommendations from different teaching departments.

A Class Council record consists of comments from multiple teachers and may include an academic warning when necessary.

The module supports collaborative editing through **3-way merge conflict resolution**, automatic draft saving, batch feedback entry, and PDF report generation.

Each student can have **only one Class Council record per semester**.

---

# 2. Objectives

This module enables staff members to:

- Record end-of-semester evaluations.
- Maintain one council record per student per semester.
- Record comments from multiple teaching departments.
- Record academic warnings.
- Save drafts automatically.
- Recover unsaved drafts.
- Enter comments for multiple students simultaneously.
- Prevent duplicate records.
- Handle concurrent editing safely.
- Export Class Council reports as PDF.

---

# 3. Record Structure

Each Class Council record contains the following sections.

| Field | Description |
|--------|-------------|
| General Comment | Overall evaluation of the student |
| IT Comment | Feedback from IT teacher |
| English Comment | Feedback from English teacher |
| PLT Comment | Feedback from PLT (Soft Skills) teacher |
| Educator Comment | Feedback from Educators |
| Warning | Academic warning flag |
| Warning Reason | Explanation of the warning |

---

# 4. Comment Badges

After saving a record, the system displays badges representing available comments.

| Badge | Meaning |
|--------|---------|
| G | General Comment |
| IT | IT Teacher Comment |
| EN | English Teacher Comment |
| PLT | PLT Teacher Comment |
| ED | Educator Comment |
| ⚠ | Academic Warning |

Badges provide a quick overview of which sections have been completed.

---

# 5. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M04-F01 | Council Feedback Record | Create one Class Council record per student per semester containing General, IT, English, PLT, and Educator comments. |
| M04-F02 | Academic Warning Flag | Record academic warnings and warning reasons; display a warning badge (⚠). |
| M04-F03 | Duplicate Record Prevention | Prevent creating multiple council records for the same student in the same semester. |
| M04-F04 | Auto Draft Saving | Automatically save drafts locally while users are typing. |
| M04-F05 | Draft Recovery / Discard | Restore unsaved drafts or discard them to revert to the last saved version. |
| M04-F06 | Batch Feedback Entry | Enter the same type of feedback for multiple students simultaneously. |
| M04-F07 | Concurrent Edit Conflict Handling | Support 3-way merge when multiple teachers edit the same record concurrently. |
| M04-F08 | PDF Report Export | Export Class Council reports to PDF with semester-based trend charts. |

---

# 6. Business Rules

## 6.1 One Record per Student per Semester

Each student can have only one Class Council record for a given semester.

Attempting to create another record results in an error.

```
Student A
Semester 2

✓ One record allowed

✗ Second record rejected
```

---

## 6.2 Optional Fields

All comment fields are optional.

The following fields may remain empty:

- General Comment
- IT Comment
- English Comment
- PLT Comment
- Educator Comment
- Warning
- Warning Reason

Saving an empty record is allowed.

---

## 6.3 Academic Warning

When a warning is added:

- Warning Badge (⚠) appears.
- Warning Reason should explain the issue.

Example:

```
Warning

✓ Academic Performance

Reason

Attendance below required level
```

---

## 6.4 Badge Display

Each completed comment automatically activates its corresponding badge.

Example

| Comment | Badge |
|----------|-------|
| General Comment | G |
| IT Comment | IT |
| English Comment | EN |
| PLT Comment | PLT |
| Educator Comment | ED |
| Warning | ⚠ |

Badges disappear when the corresponding content is removed.

---

## 6.5 Automatic Draft Saving

While typing,

the system automatically saves the current draft.

Characteristics:

- No manual save required
- Runs in background
- Saved to browser Local Storage
- Device-specific

Drafts are **not synchronized** between computers.

---

## 6.6 Draft Recovery

If the browser is closed before saving,

the next time the record is opened,

the system displays

```
Unsaved Draft
```

Users may choose to:

- Continue editing
- Discard draft

Discarding restores the last saved version.

---

## 6.7 Batch Feedback

Teachers can enter the same feedback type for multiple students simultaneously.

Example

```
IT Comment

Student A
Student B
Student C

↓

Save All
```

The system reports

```
Saved 3 students
```

---

## 6.8 Concurrent Editing (3-Way Merge)

Multiple teachers may edit the same record simultaneously.

The system compares:

- Original version
- First saved version
- Current edited version

Non-conflicting fields are merged automatically.

Conflicting fields preserve the value saved first.

The second editor receives a warning.

---

### Example

Original

```
IT Comment

Good
```

Teacher B saves first

```
Excellent
```

Teacher A saves later

```
Very Good

English Comment
Good communication
```

Final Result

| Field | Final Value |
|--------|-------------|
| IT Comment | Excellent |
| English Comment | Good communication |

Teacher A receives

```
Saved, but these fields were updated by another teacher:

IT Comment
```

---

## 6.9 PDF Export

Class Council reports can be exported as PDF.

Each report includes:

- Student information
- Semester
- Teacher comments
- Warning information

---

## 6.10 Trend Chart

Trend charts appear only when historical data exists.

Rule

| Semester | Trend Chart |
|-----------|-------------|
| Semester 1 | Not displayed |
| Semester 2 or later | Displayed |

---

# 7. Validation Rules

| Item | Validation |
|------|------------|
| Student | Required |
| Semester | Required |
| Duplicate Record | Not allowed |
| Draft Saving | Automatic |
| Warning Reason | Optional |
| PDF Export | Available after saving |

---

# 8. Error Handling

| Condition | System Behavior |
|-----------|-----------------|
| Duplicate student + semester | Display duplicate record error |
| Concurrent update conflict | Preserve first saved value and notify second editor |
| Browser closed unexpectedly | Recover local draft |
| Draft discarded | Restore last saved data |
| Empty comments | Record can still be saved |

---

# 9. Dependencies

This module depends on:

- Module 01 – Batch & Student Management
- Module 03 – Academic Management

Required master data:

- Student
- Semester
- Batch

Generated Class Council records are used for:

- Student performance evaluation
- End-of-semester reports
- PDF exports

---

# 10. Test Data Preparation

Before executing UAT, prepare:

## Students

At least five active students.

---

## Semesters

Prepare at least:

- Semester 1
- Semester 2

Semester 2 is required to verify trend chart generation.

---

## Teacher Accounts

Prepare two staff accounts to test concurrent editing.

---

## Warning Data

Example

```
Warning

Poor attendance

Reason

Attendance below minimum requirement
```

---

## Draft Recovery

Prepare a browser session by:

- Opening a council record
- Typing comments
- Closing the browser without saving

---

## Concurrent Editing

Teacher A

```
IT Comment

Very Good
```

Teacher B

```
IT Comment

Excellent
```

Verify:

- Conflict warning
- Merge behavior
- Final saved values

---

# 11. UAT Test Scenarios

All UAT test scenarios for this module are documented in [module04_test_cases.csv](file:///F:/code/Test/test-case-academic-portal/Tests/csv/module04_test_cases.csv) and [module04_test_cases.xlsx](file:///F:/code/Test/test-case-academic-portal/Tests/excel/module04_test_cases.xlsx):

- **Test Cases:** TC-M04-001 → TC-M04-034 (34 Total Test Cases)

### Test Case Breakdown by Feature

| Feature ID | Feature Name | Test Cases | Priority | Description / Scenarios Covered |
|------------|--------------|------------|----------|--------------------------------|
| M04-F01 | Council Feedback Record | TC-M04-001, TC-M04-002, TC-M04-022, TC-M04-023, TC-M04-024, TC-M04-031 | High / Medium | Create record, empty optional fields, update comments, required validations (Student/Semester), multiline/special characters |
| M04-F02 | Academic Warning Flag | TC-M04-003, TC-M04-004, TC-M04-013, TC-M04-014, TC-M04-021 | High / Medium | Set warning flag & reason, empty reason, badge display activation (G, IT, EN, PLT, ED, ⚠), badge deactivation on content removal, clear warning flag |
| M04-F03 | Duplicate Record Prevention | TC-M04-017, TC-M04-018 | High | Block duplicate record for same student in same semester, allow record for same student in different semester |
| M04-F04 | Auto Draft Saving | TC-M04-005, TC-M04-016, TC-M04-028, TC-M04-033 | High / Medium / Low | Local storage draft saving, device-specific draft isolation, draft purge on successful save, offline draft retention |
| M04-F05 | Draft Recovery / Discard | TC-M04-006, TC-M04-007, TC-M04-032 | High / Medium | Draft recovery prompt after browser crash, discard draft to restore DB data, manual form discard button |
| M04-F06 | Batch Feedback Entry | TC-M04-008, TC-M04-009, TC-M04-025, TC-M04-026 | High / Medium / Low | Batch comment entry by feedback type, preservation of unedited comment fields, clearing comments in batch mode, no-op batch save |
| M04-F07 | Concurrent Edit Conflict Handling | TC-M04-010, TC-M04-011, TC-M04-027 | High / Medium | 3-way merge non-conflicting edits, flag conflict on same field edit, identical concurrent edit handling |
| M04-F08 | PDF Report Export | TC-M04-012, TC-M04-019, TC-M04-020, TC-M04-030, TC-M04-034 | High / Medium | PDF report generation, Semester 1 trend chart omission, Semester 2 trend chart generation, batch report PDF export, partial comment PDF export |
| M04-SEC | Access Control & Security | TC-M04-015, TC-M04-029 | High | Block unauthorized email domain login, block Student role access to council edit forms |

---

# 12. Out of Scope

The following functions are not supported:

- Multiple Class Council records for the same semester
- Cloud synchronization of drafts
- Automatic AI-generated comments
- Real-time collaborative editing
- Editing PDF after export
- Trend charts for Semester 1

---

# 13. Module Summary

The Class Council Management module centralizes end-of-semester student evaluations by allowing teachers to record structured feedback, academic warnings, and recommendations.

Its support for automatic draft saving, batch comment entry, concurrent editing protection, and PDF reporting ensures that evaluation data remains accurate, consistent, and secure throughout the academic review process.