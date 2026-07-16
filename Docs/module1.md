# Module 01 – Batch & Student Management

> **Module ID:** M01  
> **Module Name:** Batch & Student Management  
> **Primary User:** Staff  
> **Related Modules:** All Modules

---

# 1. Overview

The **Batch & Student Management** module is the foundation of the Passerelles Numériques Academic Portal.

It enables staff members to create and manage training batches and student profiles. Every academic activity in the system—including academic records, daily observations, internship management, class council comments, and student portal information—is associated with the batch and student records maintained in this module.

Because all downstream modules depend on the integrity of batch and student data, this module is considered one of the most critical components of the entire system.

---

# 2. Objectives

This module enables staff members to:

- Create and maintain training batches.
- Manage student information.
- Import students using CSV.
- Update student information.
- Archive batches and students without deleting historical data.
- Search and filter students efficiently.
- View dashboard statistics.

---

# 3. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M01-F01 | Batch Creation | Create a new batch following the required naming convention. |
| M01-F02 | Batch Editing | Rename an existing batch to a new unique name. |
| M01-F03 | Batch Archiving | Archive or reactivate a batch by changing its Active status. Permanent deletion is not supported. |
| M01-F04 | Single Student Creation | Create an individual student record. |
| M01-F05 | Bulk Student Import | Import multiple students through CSV (Upsert). |
| M01-F06 | Student Editing | Update student profile information. |
| M01-F07 | Follow-up Flag | Mark or unmark students requiring follow-up. |
| M01-F08 | Student Status Management | Toggle Active / Inactive status with automatic dropout date handling. |
| M01-F09 | Search & Filter | Search students in real time and filter records. |
| M01-F10 | Dashboard Overview | Display batch statistics and student distribution charts. |

---

# 4. Business Rules

## 4.1 Batch Naming Rule

Every batch name must follow the format:

```

PNVyyX

```

Where:

| Part | Description | Example |
|------|-------------|---------|
| PNV | Fixed prefix | PNV |
| yy | Last two digits of the year | 26 |
| X | Uppercase alphabet | A |

Example:

```

PNV26A
PNV26B
PNV25C

```

Invalid examples:

```

Batch26
PNV2026A
PNV26AA
PNV26a
ABC26A

```

If the format is invalid, the system rejects the request.

---

## 4.2 Batch Uniqueness

Batch names must be unique across the entire system.

Comparison is case-insensitive.

Example

```

PNV26A
pnv26a

```

These are considered identical.

---

## 4.3 Student Code

Every student must have a unique Student Code.

Comparison is case-insensitive.

Duplicate student codes are not allowed during:

- Manual creation
- CSV import
- Student editing

---

## 4.4 Student Status

A student may be:

- Active
- Inactive

When changing status:

### Active → Inactive

The system automatically:

- sets Dropout Date = Today

### Inactive → Active

The system automatically:

- clears Dropout Date

No manual editing is required.

---

## 4.5 Batch Deletion

Permanent deletion is **not supported**.

Instead, batches are archived by setting

```

Active = false

```

Archived batches remain in the database for historical records.

---

## 4.6 Student Creation

Students can be created through:

- Manual entry
- CSV import

The following information should be maintained:

- Student Name
- Student Code
- Date of Birth
- Gender
- Email
- Profile Photo

---

## 4.7 Bulk Import

CSV import supports **Upsert** behavior.

Meaning:

- Existing students are updated.
- New students are created.

Duplicate Student Codes are rejected.

---

## 4.8 Follow-up Flag

Staff members can mark students requiring additional attention.

The Follow-up flag:

- toggles instantly
- updates immediately
- does not require page refresh

---

## 4.9 Search & Filter

Student search supports:

- Real-time search while typing
- Name search
- Observation rating filter
- Pagination

Default page size:

```

10 students/page

```

---

## 4.10 Dashboard Overview

The dashboard displays real-time summary information, including:

- Total Batches
- Active Batches
- Total Students
- Active Students
- Inactive Students
- Gender Distribution
- Ethnicity Distribution
- Student Status Summary

Charts should refresh automatically after data changes.

---

# 5. Validation Rules

| Item | Validation |
|------|------------|
| Batch Name | Required |
| Batch Name | Must match PNVyyX |
| Batch Name | Must be unique |
| Student Name | Required |
| Student Code | Required |
| Student Code | Unique |
| Email | Valid email format |
| CSV | Required columns must exist |

---

# 6. Error Messages

| Condition | Message |
|-----------|---------|
| Invalid batch name | Invalid batch name. Use format PNVyyX (e.g., PNV26A). |
| Duplicate batch | A batch named "PNV26A" already exists. |
| Duplicate student code | Duplicate student code: {code}. |
| Server unavailable | Server is busy. Please try again in a moment. |

---

# 7. Dependencies

This module provides master data for:

- Module 02 – Scan Management
- Module 03 – Academic Management
- Module 04 – Class Council
- Module 05 – Internship Management
- Module 06 – Bi-weekly Internship Report
- Module 08 – Photo Management
- Module 09 – Student Portal

If student or batch records are missing, these modules cannot operate correctly.

---

# 8. Test Data Preparation

Before executing UAT, prepare the following:

## Accounts

- Staff account

## Batch Data

```

PNV26A
PNV26B

```

## Student Data

At least five active students.

Example:

| Student Code | Name |
|--------------|------|
| ST001 | Nguyen Van A |
| ST002 | Tran Thi B |
| ST003 | Le Van C |
| ST004 | Pham Thi D |
| ST005 | Hoang Van E |

## CSV File

Prepare a CSV file containing:

- valid students
- duplicate student code
- invalid email
- missing required field

---

# 9. UAT Test Scenarios

All UAT test scenarios for this module are documented in the following section:

- BS-01 → BS-12

These scenarios verify:

- Batch management
- Student management
- CSV import
- Validation
- Search
- Status management

---

# 10. Out of Scope

The following functions are not supported:

- Permanent batch deletion
- Permanent student deletion
- Student self-registration
- Staff self-registration

---

# 11. Module Summary

This module acts as the master data repository for the entire Academic Portal.

All downstream modules depend on the integrity of batches and student records. Therefore, data validation, uniqueness constraints, and archive mechanisms are critical to maintaining system consistency throughout the application.