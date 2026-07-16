# Module 07 – Training Materials

> **Module ID:** M07  
> **Module Name:** Training Materials  
> **Primary User:** Staff  
> **Related Modules:** None

---

# 1. Overview

The **Training Materials** module manages the centralized library of educational resources used throughout the training program.

Learning materials are organized using a **three-level hierarchical structure**:

```
Category
    └── Course
            ├── Session
            └── Exam
```

This hierarchy allows staff to organize training content efficiently while ensuring materials remain easy to maintain and reuse across different batches.

Each **Session** and **Exam** may contain multiple learning resources stored as **Google Drive links**.

---

# 2. Objectives

This module enables staff members to:

- Organize educational resources into categories.
- Manage courses under each category.
- Create and maintain training sessions.
- Create and maintain examinations.
- Attach learning materials using Google Drive URLs.
- Archive completed courses while preserving historical data.
- Import and export session information using CSV.

---

# 3. Content Hierarchy

The system uses the following hierarchy.

```
Category
    └── Course
            ├── Session
            └── Exam
```

## Default Categories

The system provides five predefined categories.

| Category |
|----------|
| IT |
| English |
| PLT (Soft Skills) |
| DA (Digital Arts) |
| Workshops |

Additional courses are created under these categories.

---

# 4. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M07-F01 | Three-tier Hierarchy | Organize educational resources using the structure Category → Course → Session / Exam. |
| M07-F02 | Category Management | Categories can only be renamed. Archiving and deletion are not supported. |
| M07-F03 | Course Archiving / Restoring | Courses can be archived or restored. Archiving hides all child sessions and exams. |
| M07-F04 | Session Deletion | Sessions can only be permanently deleted. Archiving is not supported. |
| M07-F05 | Exam Deletion | Exams can only be permanently deleted. Archiving is not supported. |
| M07-F06 | Material Attachment | Attach one or more Google Drive resources to sessions or exams. |
| M07-F07 | CSV Export / Import | Export sessions to CSV and import updates or new sessions. |

---

# 5. Business Rules

## 5.1 Category Management

Categories are system-defined containers for organizing courses.

Supported operations:

- Rename

Not supported:

- Archive
- Restore
- Delete

Categories always remain available in the system.

---

## 5.2 Course Management

Courses belong to a single category.

Supported operations:

- Create
- Edit
- Archive
- Restore

Permanent deletion is **not allowed**.

Archived courses remain in the database for historical purposes.

---

## 5.3 Course Archive Cascade

When a course is archived,

all child records become hidden automatically.

```
Archive Course

↓

Hide Sessions

+

Hide Exams
```

The session and exam records remain stored in the database.

Restoring the course automatically restores visibility of all child items.

---

## 5.4 Session Management

Sessions represent individual learning lessons.

Supported operations:

- Create
- Edit
- Delete permanently

Sessions cannot be archived.

Deleting a session permanently removes:

- Session information
- Material attachments

This action cannot be undone.

---

## 5.5 Exam Management

Exams represent assessments within a course.

Supported operations:

- Create
- Edit
- Delete permanently

Archiving is not supported.

Deleting an exam permanently removes:

- Exam information
- Material attachments

This action cannot be undone.

---

# 6. Material Attachments

Each Session or Exam may contain multiple learning materials.

Each attachment consists of:

| Field | Required |
|--------|----------|
| Label | Yes |
| Google Drive URL | Yes |

Example

| Label | URL |
|-------|-----|
| Slides | https://drive.google.com/... |
| Exercise | https://drive.google.com/... |

---

## Google Drive URL Validation

Only Google Drive URLs are accepted.

Valid format

```
https://drive.google.com/...
```

Any other URL is rejected.

---

## Attachment Validation

Both fields are mandatory.

### Valid

```
Label ✓
URL ✓

→ Saved
```

### Invalid

```
Label ✓
URL ✗

→ Not Saved
```

```
Label ✗
URL ✓

→ Not Saved
```

---

## Empty Attachment Rows

If both Label and URL are empty,

the row is ignored automatically.

```
Label = Empty
URL = Empty

↓

Skipped
```

No validation error is shown.

---

# 7. CSV Export & Import

The system supports CSV operations for **Sessions only**.

Course information is not affected.

---

## Export

The exported CSV contains:

- Session ID
- Session Name
- Lesson Number
- Description

Material attachments are not exported.

---

## Import Rules

Each row is processed independently.

### Existing Session

If the Session ID matches an existing session,

the system updates:

- Session Name
- Lesson Number
- Description

---

### New Session

If the ID is empty,

or does not exist,

the system creates a new session.

---

### Missing Sessions

Existing sessions that do not appear in the CSV remain unchanged.

No deletion occurs.

---

### Materials Column

The **Materials** column is ignored during import.

Google Drive attachments cannot be imported through CSV.

They must be added manually after import.

---

# 8. Validation Rules

| Item | Validation |
|------|------------|
| Category Name | Required |
| Course Name | Required |
| Session Name | Required |
| Exam Name | Required |
| Material Label | Required when URL exists |
| Material URL | Required when Label exists |
| Material URL | Must start with `https://drive.google.com/` |

---

# 9. Error Handling

| Condition | System Behavior |
|-----------|-----------------|
| Invalid Google Drive URL | Validation error |
| Missing Label | Attachment is not saved |
| Missing URL | Attachment is not saved |
| Empty attachment row | Row skipped automatically |
| Archive course | All child sessions and exams become hidden |
| Delete session | Confirmation required before permanent deletion |
| Delete exam | Confirmation required before permanent deletion |

---

# 10. Dependencies

This module functions independently as the system's learning resource repository.

Its content may later be referenced by:

- Staff
- Students
- Future learning modules

No prerequisite module is required.

---

# 11. Test Data Preparation

Before executing UAT, prepare:

## Categories

- IT
- English
- PLT
- DA
- Workshops

---

## Courses

Example:

- Java Programming
- English Communication
- Graphic Design

---

## Sessions

Example:

- Session 01
- Session 02
- Session 03

---

## Exams

Example:

- Midterm Exam
- Final Exam

---

## Google Drive Links

Prepare:

- Valid Google Drive URLs
- Invalid URLs (Dropbox, OneDrive, etc.)
- Missing Label
- Missing URL
- Empty rows

---

## CSV Files

Prepare:

- Existing Session IDs
- New Sessions
- Mixed Update/Create file
- CSV containing Materials column (to verify it is ignored)

---

# 12. UAT Test Scenarios

Detailed UAT scenarios are documented separately.

Covered scenarios include:

- Category renaming
- Course archive and restore
- Archive cascade behavior
- Session deletion
- Exam deletion
- Google Drive URL validation
- Attachment validation
- CSV export
- CSV import
- Update existing sessions
- Create new sessions
- Ignore Materials column during import

---

# 13. Out of Scope

The following features are not supported:

- Category deletion
- Category archiving
- Permanent course deletion
- Session archiving
- Exam archiving
- Importing Google Drive attachments via CSV
- Automatic synchronization with Google Drive

---

# 14. Module Summary

The **Training Materials** module provides a centralized repository for organizing educational resources through a structured **Category → Course → Session / Exam** hierarchy.

The module enforces strict lifecycle rules for each content type, supports Google Drive–based material management, and allows efficient CSV-based maintenance of session information while preserving the integrity and organization of the training library.