# Passerelles Numériques Academic Portal
# User Acceptance Testing (UAT) Documentation

> Version: **1.0**  
> Project: **Passerelles Numériques Academic Portal**  
> Document Type: **User Acceptance Testing (UAT)**  
> Audience: **Student Intern Testers / UAT Team**  
> Owner: **Mr. Vinh**  
> Last Updated: July 2026

---

# Table of Contents

1. Introduction
2. Project Overview
3. System Context
4. User Roles
5. External Systems
6. Authentication Flow
7. General Business Rules
8. Testing Scope
9. Testing Environment
10. Test Execution Guidelines
11. Test Result Definition
12. Bug Reporting Guideline
13. Severity Definition
14. Evidence Collection
15. Escalation Process
16. UAT Exit Criteria
17. Module Documents
18. Frequently Asked Questions

---

# 1. Introduction

## Purpose

This document provides the overall User Acceptance Testing (UAT) guideline for the **Passerelles Numériques Academic Portal**.

The objective of UAT is to verify that the system satisfies business requirements and is ready to be used by end users before deployment.

This document serves as the entry point of the complete UAT documentation.

Detailed information for each functional module is documented separately.

---

## Objectives

The testing activities aim to verify that:

- All business requirements are implemented correctly.
- Core workflows operate as expected.
- Invalid operations are handled properly.
- User permissions are correctly enforced.
- Data is stored correctly.
- No critical defects remain before Go-Live.

---

## Intended Audience

This documentation is intended for

- Student Intern Testers
- Staff Testers
- Project Supervisor
- Business Analyst
- Developers
- Future Maintenance Team

---

# 2. Project Overview

## System Name

Passerelles Numériques Academic Portal

## System Description

The Academic Portal is an internal web application used by Passerelles Numériques Vietnam to manage:

- Student information
- Academic records
- Daily observations
- Internship management
- Class Council comments
- Training materials
- Student self-service portal

The system is implemented using Google Apps Script and Google Workspace services.

---

# 3. System Context

The Academic Portal interacts with several Google services.

```

```
                    +----------------------+
                    |      Google OAuth    |
                    +----------+-----------+
                               |
                               |
                        User Authentication
                               |
                               |
+------------+        +---------v---------+       +----------------+
| Staff      |------->| Academic Portal   |<------| Student        |
+------------+        +---------+---------+       +----------------+
                               |
             +-----------------+------------------+
             |                 |                  |
             |                 |                  |
      Google Sheets      Google Drive         Gmail
       Business Data      File Storage      Email Service

```

---

# 4. User Roles

There are only two supported user roles.

| Role | Email Domain | Permissions |
|------|--------------|------------|
| Staff | @passerellesnumeriques.org | Full management access |
| Student | @student.passerellesnumeriques.org | Read-only academic information and internship reports |

Users with any other email domain are denied access.

---

# 5. External Systems

The application integrates with the following external services.

| System | Purpose |
|---------|---------|
| Google OAuth | User Authentication |
| Google Sheets | Primary Database |
| Google Drive | File Storage |
| Gmail | Email Notification |

---

# 6. Authentication Flow

The system does not provide a username/password login page.

Authentication is fully handled by Google OAuth.

```

```
User accesses application
        |
Google OAuth Authentication
        |
Check email domain
        |
+-------------------------------+
| Staff Domain                  |
| -> Staff Portal               |
+-------------------------------+

+-------------------------------+
| Student Domain                |
| -> Student Portal             |
+-------------------------------+

+-------------------------------+
| Unknown Domain                |
| -> Access Denied              |
+-------------------------------+

```

---

# 7. General Business Rules

The following rules apply across the entire system.

## Authentication

- Google OAuth only.
- No password is stored.
- Session is managed by Google.

---

## Authorization

Permission is determined entirely by email domain.

Client-side role modification is not allowed.

---

## Data Storage

Business data is stored inside Google Sheets.

Changes become immediately available to other users.

---

## File Storage

Uploaded files are stored in Google Drive.

---

## Email

The system sends automatic emails through Gmail.

---

## User Interface

The application is a Single Page Application (SPA).

Most operations update data without refreshing the browser.

---

# 8. Testing Scope

The current UAT includes nine functional modules.

| Module | Description |
|---------|-------------|
| Module 1 | Batch & Student Management |
| Module 2 | Scan Management |
| Module 3 | Academic Management |
| Module 4 | Class Council |
| Module 5 | Internship Management |
| Module 6 | Bi-weekly Internship Report |
| Module 7 | Training Materials |
| Module 8 | Photo Management |
| Module 9 | Student Portal |

End-to-End scenarios are also included.

---

# 9. Testing Environment

## Browser

Recommended:

- Google Chrome (Latest)

Minimum resolution:

- 1280 × 768

Stable internet connection is required.

---

## Accounts

The following accounts are required.

### Staff Account

```

@passerellesnumeriques.org

```

### Student Account

```

@student.passerellesnumeriques.org

```

---

## Test Data

Only testing data should be used.

Do not modify production data belonging to actual students.

---

# 10. Test Execution Guidelines

For every test case:

1. Read the objective.
2. Prepare required data.
3. Execute all steps.
4. Compare actual result with expected result.
5. Record result.
6. Capture evidence if necessary.
7. Continue with next test.

Do not stop testing after finding a defect.

---

# 11. Test Result Definition

| Result | Meaning |
|---------|---------|
| PASS | System behaves as expected |
| FAIL | Unexpected behavior observed |
| BLOCKED | Cannot continue due to dependency |
| N/A | Not applicable |

---

# 12. Bug Reporting Guideline

Whenever a test fails, a Bug Report should be created.

Each bug should contain:

- Bug ID
- Module
- Test ID
- Summary
- Steps to Reproduce
- Actual Result
- Expected Result
- Severity
- Screenshot
- Video (if necessary)

---

# 13. Severity Definition

| Severity | Description |
|-----------|------------|
| Critical | System unusable or data loss |
| High | Major functionality broken |
| Medium | Functional issue with workaround |
| Low | Cosmetic or minor issue |

---

# 14. Evidence Collection

Recommended evidence includes:

- Screenshot
- Screen Recording
- Browser Console
- Error Message
- Input Data

Suggested naming convention:

```

[TestID]_[PASS|FAIL]_YYYYMMDD.png

```

Example

```

BS-01_FAIL_20260720.png

```

---

# 15. Escalation Process

Critical issues should be reported immediately.

Examples:

- Login failure
- Data loss
- Security issue
- Permission issue

Normal issues should follow the standard bug reporting process.

```

Tester
↓

Bug Report

↓

Mr. Vinh

↓

Developer

↓

Fix

↓

Retest

```

---

# 16. UAT Exit Criteria

The system is considered ready for production when:

- 100% P1 test cases PASS
- At least 90% P2 PASS
- No unresolved Critical defects
- No unresolved High defects
- All defects have been documented

---

# 17. Module Documents

Each functional module has its own documentation.

| Module | File |
|---------|------|
| Module 1 | module-01-batch-student.md |
| Module 2 | module-02-scan.md |
| Module 3 | module-03-academic.md |
| Module 4 | module-04-class-council.md |
| Module 5 | module-05-internship.md |
| Module 6 | module-06-biweekly-report.md |
| Module 7 | module-07-training-material.md |
| Module 8 | module-08-photo-management.md |
| Module 9 | module-09-student-portal.md |

---

# 18. Frequently Asked Questions

## What if the system behaves differently from the documentation?

Record it as **FAIL** and report it.

The project supervisor will determine whether the documentation or the application should be updated.

---

## How long should I wait before reporting a timeout?

Google Apps Script may require 2–5 seconds.

Wait up to 30 seconds before considering it a defect.

---

## I did not receive the notification email.

Check the Spam folder.

If no email is received after five minutes, create a High severity bug report.

---

## Can I delete real student data?

No.

Always use testing data only.

---

# Document Version History

| Version | Date | Author | Description |
|----------|------|---------|-------------|
| 1.0 | July 2026 | UAT Team | Initial version |

---

**End of General Documentation**