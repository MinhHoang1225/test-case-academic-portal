# Module 05 – Internship Management

> **Module ID:** M05  
> **Module Name:** Internship Management  
> **Primary User:** Staff  
> **Related Modules:** Module 01 – Batch & Student Management, Module 06 – Bi-Weekly Internship Reports

---

# 1. Overview

The **Internship Management** module enables staff members to organize students into internship groups, assign them to partner companies, and monitor internship progress throughout the internship period.

The module supports creating internship groups by academic year, assigning students individually or in bulk, managing partner companies, recording feedback from multiple internal teams, and tracking assignment status.

Internship groups created in this module are later used by the **Bi-Weekly Internship Report** module, where students submit their internship reports.

---

# 2. Objectives

This module enables staff members to:

- Create internship groups.
- Organize batches into internship groups.
- Manage partner companies.
- Assign students to companies.
- Perform bulk company assignments.
- Record internship feedback.
- Track unassigned students.
- Archive completed internship groups.
- Reactivate archived groups.
- Manage internship group navigation.

---

# 3. Core Data Structure

| Entity | Required Fields | Constraints |
|---------|----------------|-------------|
| Internship Group | Name, Year, ≥1 Batch, Start Date | Each batch can belong to only one internship group per year |
| Company | Company Name | Unique (case-insensitive, trimmed) |
| Assignment | Student + Company | One assignment per student per internship group |
| Feedback | Notes | Empty rows are ignored and not saved |

---

# 4. Feedback Teams

Internship feedback can be submitted by different internal teams.

| Team | Description |
|------|-------------|
| Training | Default internship monitoring team |
| ERO | Employer Relations Office |
| Educators | Teaching staff / Educators |

Each feedback entry is associated with exactly one team.

---

# 5. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M05-F01 | Internship Group Creation | Create internship groups with year, batches, and start date. |
| M05-F02 | Group Archiving / Reactivation | Archive completed groups or reactivate archived groups. |
| M05-F03 | Company Management | Add and manage internship partner companies. |
| M05-F04 | Student-to-Company Assignment | Assign students individually or in bulk to companies. |
| M05-F05 | Remove Assignment | Remove a company assignment by selecting **No Company**. |
| M05-F06 | Unassigned Warning Badge | Display warning badges showing the number of unassigned students. |
| M05-F07 | Feedback Recording by Team | Record internship feedback from Training, ERO, or Educators. |
| M05-F08 | Same for All Feedback | Apply identical feedback to multiple students simultaneously. |
| M05-F09 | Feedback Editing | Modify previously saved feedback. |
| M05-F10 | Group List Display | Display internship groups with navigation, expand/collapse behavior, and status indicators. |

---

# 6. Business Rules

## 6.1 Internship Group

An internship group consists of:

- Group Name
- Internship Year
- One or more batches
- Start Date

Each internship group belongs to either:

- Second Year
- Third Year

---

## 6.2 Batch Assignment Rule

Each batch may belong to only one internship group within the same academic year.

Example

```
PNV26A

↓

Internship Group A (2nd Year)

✓ Allowed
```

Attempting to assign the same batch to another 2nd-year group is rejected.

However,

```
PNV26A

↓

2nd Year Group

↓

3rd Year Group
```

is allowed because they belong to different internship years.

---

## 6.3 Company Management

Company names must satisfy the following requirements:

- Required
- Trim leading/trailing spaces
- Case-insensitive uniqueness

Example

```
TechCorp
techcorp
TECHCORP
```

These are considered identical.

Duplicate companies are rejected.

---

## 6.4 Student Assignment

Each student can have only one company assignment within an internship group.

Assignments can be performed:

- Individually
- In bulk

Changing the assigned company replaces the previous assignment.

---

## 6.5 Removing Assignments

Selecting

```
(No Company)
```

removes the assignment.

The student is automatically moved to

```
Unassigned
```

---

## 6.6 Hidden Companies

Companies may be marked as **Hidden**.

Rules:

- Hidden companies do not appear in the assignment dropdown.
- Existing assignments remain valid.
- Students already assigned to a hidden company continue displaying that company.

Example

```
Student A

↓

Assigned to ABC Company

↓

Company Hidden

↓

Student A still shows ABC Company
```

New assignments cannot select that hidden company.

---

## 6.7 Internship Feedback

Feedback records contain:

- Team
- Date
- Notes

Feedback teams include:

- Training
- ERO
- Educators

Each feedback entry belongs to one team.

---

## 6.8 Empty Feedback

Rows containing no notes are ignored.

Example

```
Notes

(empty)

↓

Not Saved
```

The system skips empty rows automatically.

---

## 6.9 Same for All

Staff may enter one feedback message and apply it to multiple selected students.

Example

```
Excellent communication.

↓

Apply to

Student A
Student B
Student C
```

Result

All selected students receive identical feedback.

---

## 6.10 Editing Feedback

Previously saved feedback can be modified.

Editable fields include:

- Notes
- Team
- Date

Changes overwrite the previous version.

---

## 6.11 Unassigned Students

Internship groups automatically calculate the number of students without company assignments.

Example

```
⚠ 2 Unassigned
```

The badge updates automatically whenever assignments change.

---

## 6.12 Internship Group Status

Groups have two possible statuses.

| Status | Description |
|---------|-------------|
| On-going | Active internship group |
| Archived | Internship completed |

Archived groups are hidden from normal operations but can be restored.

---

# 7. Validation Rules

| Item | Validation |
|------|------------|
| Group Name | Required |
| Internship Year | Required |
| Start Date | Required |
| Batch | At least one required |
| Company Name | Required and unique |
| Student Assignment | One company per student |
| Feedback Notes | Empty rows are ignored |

---

# 8. Error Handling

| Condition | System Behavior |
|-----------|-----------------|
| Missing group name | Validation error |
| Missing start date | Validation error |
| Duplicate company name | Reject creation |
| Batch already assigned | Reject group creation |
| Empty feedback | Skip without saving |
| Hidden company | Not available for new assignments |
| Remove assignment | Student moved to Unassigned |

---

# 9. Dependencies

This module depends on:

- Module 01 – Batch & Student Management

Required master data:

- Batch
- Student

Data produced by this module is consumed by:

- Module 06 – Bi-Weekly Internship Reports

Only students belonging to an **On-going Internship Group** can submit internship reports.

---

# 10. Test Data Preparation

Before executing UAT, prepare:

## Internship Groups

At least:

- One On-going group
- One Archived group

---

## Batches

Prepare at least:

- PNV26A
- PNV26B

---

## Students

At least five students.

---

## Companies

Example

```
ABC Technology

TechCorp

PNV Software
```

---

## Hidden Company

Prepare one company that:

- Has assigned students
- Is later marked as Hidden

This is required for validating hidden company behavior.

---

## Feedback

Prepare sample feedback for:

- Training
- ERO
- Educators

---

## Bulk Assignment

Prepare:

- Five unassigned students

Verify bulk assignment to one company.

---

# 11. UAT Test Scenarios

Detailed UAT scenarios are documented separately.

Covered scenarios include:

- IN-01 → IN-18

These scenarios validate:

- Internship group creation
- Group archiving
- Company management
- Student assignment
- Hidden companies
- Assignment removal
- Warning badges
- Feedback creation
- Batch feedback
- Feedback editing
- Group reactivation

---

# 12. Out of Scope

The following functions are not supported:

- Multiple company assignments for one student
- Permanent deletion of internship groups
- Permanent deletion of companies
- Automatic company recommendation
- Internship performance analytics
- Student self-assignment

---

# 13. Module Summary

The Internship Management module serves as the central component for organizing internship activities throughout the academic program.

It provides comprehensive management of internship groups, partner companies, student assignments, and multi-team feedback while ensuring assignment consistency, company visibility rules, and seamless integration with the Bi-Weekly Internship Reporting module.