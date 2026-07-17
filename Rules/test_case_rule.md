# Test Case Writing Guidelines

Version: 1.0

---

# 1. Purpose

This document defines the standard for writing User Acceptance Test (UAT) test cases for the Student Management System.

The objectives are to:

- Ensure all test cases follow a consistent format.
- Improve readability and maintainability.
- Make test execution repeatable by different testers.
- Reduce ambiguity during testing.
- Ensure expected results are measurable and verifiable.
- Support traceability between Functional Requirements and Test Cases.

---

# 2. Scope

These guidelines apply to all functional test cases in the project, including:

- Module 01 – Batch & Student Management
- Module 02 – Observation Tracking
- Module 03 – Academic Management
- Module 04 – Council Feedback
- Module 05 – Internship Management
- Module 06 – Bi-Weekly Internship Reports
- Module 07 – Training Materials
- Module 08 – Profile Photo Management
- Module 09 – Student Portal
- End-to-End Test Cases

---

# 3. Test Case Definition

A test case is an independent testing scenario designed to verify one functional requirement or one business rule.

Each test case must include:

- Unique identifier
- Module
- Test title
- Objective
- Preconditions
- Test data
- Test steps
- Expected result
- Priority
- Notes

Every test case should be executable without relying on another test case whenever possible.

---

# 4. Test Case Structure

Each test case must contain the following fields.

| Field | Description |
|--------|-------------|
| ID | Unique identifier of the test case |
| Module | Functional module being tested |
| Title | Short description of the scenario |
| Objective | Purpose of the test |
| Preconditions | Required system state before execution |
| Test Data | Input values used during testing |
| Steps | Sequential execution steps |
| Expected Result | Expected system behavior |
| Priority | High / Medium / Low |
| Notes | Additional assumptions or comments |

---

# 5. Test Case ID Convention

The following naming convention must be used.

```
TC-Mxx-###
```

Examples

```
TC-M01-001
TC-M01-045
TC-M03-012
TC-M06-078
TC-E2E-001
```

Where

| Part | Meaning |
|------|---------|
| TC | Test Case |
| M01 | Module number |
| ### | Running number |

For End-to-End testing

```
TC-E2E-001
```

---

# 6. Writing Principles

Test cases should follow these principles.

## 6.1 Independent

Each test case should be executable independently whenever possible.

Avoid depending on another test case.

---

## 6.2 One Objective

Each test case should verify only one requirement or one business rule.

Good example

```
Verify batch name format validation.
```

Poor example

```
Verify batch creation, editing, searching and deletion.
```

---

## 6.3 Clear Steps

Each step should contain only one action.

Good

```
1. Click Create Batch.

2. Enter "PNV26A".

3. Click Save.
```

Poor

```
Create a batch and verify everything works.
```

---

## 6.4 Measurable Expected Results

Expected results must be observable.

Good

```
The batch is created successfully.

A success notification appears.

The new batch is displayed in the list.
```

Poor

```
System works correctly.
```

---

## 6.5 Use Realistic Data

Always use meaningful sample data.

Example

```
Batch Name = PNV26A

Student Code = PNV26001

Email = student01@student.passerellesnumeriques.org
```

Avoid

```
ABC

XYZ

Test123
```

---

## 6.6 Positive and Negative Testing

Every major feature should include both:

Positive scenarios

Example

```
Create batch with valid name.
```

Negative scenarios

Example

```
Create batch with duplicate name.
```

---

## 6.7 Boundary Value Testing

Whenever applicable, include boundary values.

Examples

```
Minimum score

Maximum score

Empty value

Maximum length

Minimum length

Invalid characters
```

---

## 6.8 Business Rule Validation

Every business rule documented in the Functional Requirements should have at least one corresponding test case.

Example

Business Rule

```
Batch name must follow PNVyyX.
```

Required tests

- Valid batch name
- Invalid format
- Duplicate name

---

# 7. Priority Levels

Each test case must define its execution priority.

| Priority | Description |
|-----------|-------------|
| High | Critical business functions |
| Medium | Important but non-critical functions |
| Low | Cosmetic or optional features |

Examples

High

- Login
- Save
- Submit
- Delete
- Permission
- Validation

Medium

- Search
- Filter
- Sorting

Low

- UI layout
- Tooltip
- Animation

---

# 8. Preconditions

Preconditions describe the required system state before execution.

Examples

```
Staff user is logged in.

Batch PNV26A exists.

Student S001 exists.

Internship group is On-going.
```

Avoid embedding execution steps inside Preconditions.

---

# 9. Test Data

Test data should be written using key-value pairs.

Example

```
BatchName=PNV26A

Status=Active
```

or

```
StudentCode=PNV26001;
Email=student01@student.passerellesnumeriques.org
```

CSV files used for import testing should specify:

```
Valid CSV

Duplicate CSV

Missing Required Column

Invalid Data

Blank Values
```

---

# 10. Writing Test Steps

Use imperative sentences.

Examples

```
1. Open Batch Management.

2. Click Create Batch.

3. Enter PNV26A.

4. Click Save.
```

Avoid

```
Verify batch creation.

Check whether it works.
```

---

# 11. Expected Result

Expected results must describe observable outcomes.

Examples

```
Success notification appears.

Student record is created.

Status changes to Active.

Error message is displayed.

Email is sent.

PDF is downloaded.
```

Whenever possible, include the exact system message.

Example

```
Invalid batch name.

Use format PNVyyX.
```

---

# 12. Notes

Notes may include:

- Related Business Rules
- Known Issues
- Temporary limitations
- Assumptions
- Related Requirement IDs

Example

```
Related FR:

M01-F01
```

---

# 13. CSV Format

Each module stores its test cases in a dedicated CSV file.

Recommended filenames

```
Tests/module01_test_cases.csv

Tests/module02_test_cases.csv

Tests/module03_test_cases.csv

...

Tests/module09_test_cases.csv

Tests/e2e_test_cases.csv
```

---

# 14. CSV Header

Each CSV file must use the following header.

```
ID,
Module,
Title,
Objective,
Precondition,
TestData,
Steps,
ExpectedResult,
Priority,
Notes
```

---

# 15. CSV Writing Rules

Steps

- Multiple steps may be separated using semicolons (;).
- Alternatively, line breaks may be used inside quoted cells.

Test Data

- Use key=value pairs.
- Separate multiple values using semicolons.

Text containing commas

- Enclose the entire cell in double quotation marks.

---

# 16. Excel-Compatible CSV Requirements
When generating CSV files, the following rules must be followed to ensure compatibility with Microsoft Excel and the RFC 4180 CSV standard.

## CSV Generation Rules

- Generate an Excel-compatible RFC 4180 CSV.
- Every test case must occupy exactly one CSV record (one row).
- Quote every field using double quotation marks ("), even if quoting is optional.
- Escape embedded double quotation marks by doubling them ("").
- Preserve multiline text inside quoted fields without breaking the CSV structure.
- Separate fields using commas (,).
- Do not add extra spaces before or after delimiters.
- Use UTF-8 encoding.
- The CSV header must exactly match the project standard.
- Do not insert blank rows between records.
- Do not break a single test case across multiple CSV records or physical lines. Each test case must remain a single logical CSV row.

## AI Output Requirements

When an AI assistant generates test cases in CSV format, it must:

- Output only valid RFC 4180 CSV.
- Ensure one test case = one CSV row.
- Quote every field.
- Escape embedded quotes correctly.
- Keep all cell content within its corresponding quoted field.
- Generate UTF-8 encoded text.
- Never split a test case into multiple records.
- Ensure the generated CSV can be opened directly in Microsoft Excel without requiring manual correction.

---
# 17. Traceability

Every Functional Requirement should be covered by one or more test cases.

Example

| Functional Requirement | Test Cases |
|------------------------|------------|
| M01-F01 | TC-M01-001 ~ TC-M01-006 |
| M01-F02 | TC-M01-007 ~ TC-M01-010 |
| M03-F04 | TC-M03-021 ~ TC-M03-035 |

This ensures complete requirement coverage during UAT.

---

# 18. Recommended Test Design Techniques

The following techniques should be applied whenever appropriate.

- Positive Testing
- Negative Testing
- Boundary Value Analysis (BVA)
- Equivalence Partitioning (EP)
- Decision Table Testing
- State Transition Testing
- Error Guessing
- Pairwise Testing (for complex combinations)

---

# 19. Test Coverage Checklist

Each functional feature should be evaluated against the following checklist.

| Area | Covered |
|------|---------|
| Happy Path | ✓ |
| Validation | ✓ |
| Required Fields | ✓ |
| Invalid Input | ✓ |
| Boundary Values | ✓ |
| Business Rules | ✓ |
| Permission | ✓ |
| Error Handling | ✓ |
| Search | ✓ |
| Filter | ✓ |
| Sorting | ✓ |
| Import / Export | ✓ |
| Concurrent Editing (if applicable) | ✓ |
| Performance-sensitive scenarios (if applicable) | ✓ |

---

# 20. Example Test Case

| Field | Value |
|------|------|
| ID | TC-M01-001 |
| Module | Module 01 |
| Title | Create Batch with Valid Name |
| Objective | Verify that a batch can be created using a valid batch name. |
| Preconditions | Staff user is logged in. |
| Test Data | BatchName=PNV26A; Status=Active |
| Steps | 1. Open Batch Management; 2. Click Create Batch; 3. Enter PNV26A; 4. Select Active; 5. Click Save |
| Expected Result | Batch is created successfully. Success notification appears. PNV26A is displayed in the batch list. |
| Priority | High |
| Notes | Related Requirement: M01-F01 |

---

# 21. Revision History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | Initial Release | First version of the Test Case Writing Guidelines |