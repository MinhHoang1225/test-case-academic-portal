# Module 06 – Bi-Weekly Internship Reports

> **Module ID:** M06  
> **Module Name:** Bi-Weekly Internship Reports  
> **Primary User:** Student  
> **Secondary User:** Staff (Read-only)  
> **Related Modules:** Module 05 – Internship Management

---

# 1. Overview

The **Bi-Weekly Internship Reports** module allows students to submit internship progress reports every two weeks throughout their internship period.

Each report summarizes the student's completed tasks, working hours, challenges encountered, and support required from mentors.

Students may save reports as drafts before submitting them. Once submitted, the report becomes permanently read-only and an automatic email notification is sent to the assigned supervisors.

Staff members can later review submitted reports from the student profile but cannot modify the submitted content.

---

# 2. Objectives

This module enables students to:

- Create internship reports.
- Save reports as drafts.
- Edit draft reports.
- Record daily working tasks.
- Calculate working hours automatically.
- Submit reports.
- Notify supervisors automatically by email.

This module also enables staff members to:

- View submitted internship reports.

---

# 3. Report Lifecycle

Every report follows the lifecycle below.

```text
+ New Report

↓

Draft

↓

Save as Draft

↓

Edit Draft (Unlimited)

↓

Submit Report

↓

Confirm Submission

↓

Submitted

↓

Automatic Email Notification

↓

Read-only Forever
```

Once submitted, reports cannot be edited or deleted.

---

# 4. Required Fields for Submission

The following information must be completed before a report can be submitted.

| Field | Validation |
|--------|------------|
| Company Supervisor Name | Required |
| Report Start Date | Required, must be Monday, must be within internship period |
| Report End Date | Automatically calculated |
| PNV Supervisor Email | Required, valid email format |
| Company Supervisor Email | At least one valid email address |
| Tasks | Minimum one completed task |
| Challenges | Required |
| Support Needed | Required |

---

# 5. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M06-F01 | Report Creation | Only students belonging to an **On-going** internship group can create reports. |
| M06-F02 | Draft Saving | Save partially completed reports as drafts for later editing. |
| M06-F03 | Submission Validation | Validate all mandatory fields before allowing submission. |
| M06-F04 | Auto-calculated End Date | Automatically calculate the report end date as Start Date + 13 days. |
| M06-F05 | Dynamic Task Table | Add or remove internship task rows dynamically. |
| M06-F06 | Auto-calculated Total Hours | Automatically calculate daily subtotals and total working hours. |
| M06-F07 | Report Submission | Permanently submit the report and lock it as read-only. |
| M06-F08 | Automatic Email Notification | Automatically send notification emails after successful submission. |
| M06-F09 | Staff View of Student Reports | Allow staff members to view submitted reports from the Student Detail page. |

---

# 6. Business Rules

## 6.1 Report Eligibility

Only students assigned to an **On-going Internship Group** may create internship reports.

Students belonging to:

- Archived groups
- Completed internship groups

cannot create new reports.

The **+ New Report** button is hidden.

---

## 6.2 Draft Reports

Students may save reports at any time before submission.

Draft reports:

- Can be edited unlimited times.
- Remain editable.
- Are not emailed.
- Are not visible as submitted reports.

---

## 6.3 Report Submission

Submitting a report requires confirmation.

```text
Submit Report

↓

Confirmation Dialog

↓

Submitted
```

After submission:

- Status becomes **Submitted**.
- Report becomes read-only.
- Edit button disappears.
- Data cannot be modified.

---

## 6.4 Report Period

The report period begins on a Monday.

Rules:

- Start Date is required.
- Start Date must be Monday.
- Start Date must fall within the student's internship period.

---

## 6.5 End Date Calculation

The End Date is automatically generated.

Formula

```text
End Date

=

Start Date + 13 Days
```

Users cannot manually edit the End Date.

---

## 6.6 Internship Tasks

Each report must contain at least one task.

Every task requires:

- Task Name
- Description
- Result

Incomplete rows are not accepted during submission.

Students may:

- Add new rows
- Remove existing rows

---

## 6.7 Working Hours

Students enter working hours for each day.

The system automatically calculates:

- Daily subtotal
- Total working hours

Totals update immediately whenever values change.

---

## 6.8 Challenges

Students must describe the challenges encountered during the reporting period.

This field cannot be empty.

---

## 6.9 Support Needed

Students must describe any assistance or support required.

This field is mandatory.

---

## 6.10 Email Notification

After successful submission,

the system automatically sends an email.

Recipients

| Type | Recipient |
|------|-----------|
| To | PNV Supervisor + Company Supervisor |
| CC | Student + ero.vietnam@passerellesnumeriques.org |

Subject format

```text
[BatchName]

[Bi-Weekly Internship Report]

StudentName

Company

(Period: dd/mm – dd/mm)
```

---

## 6.11 Email Failure (Non-Fatal)

Email delivery failure does **not** cancel report submission.

Workflow

```text
Report Submitted

↓

Email Sending Failed

↓

Warning Displayed

↓

Report Remains Submitted
```

Students receive a warning.

Example

```text
Email notification failed:

[Reason]
```

Students cannot resend the email themselves.

Manual notification must be performed by staff.

---

## 6.12 Staff Access

Staff members may:

- View submitted reports
- Review internship progress

Staff cannot:

- Edit reports
- Delete reports
- Resubmit reports

---

# 7. Validation Rules

| Item | Validation |
|------|------------|
| Company Supervisor Name | Required |
| Start Date | Required, Monday only |
| Internship Period | Must be within internship duration |
| PNV Supervisor Email | Required, valid format |
| Company Supervisor Email | At least one valid email |
| Task List | Minimum one completed task |
| Challenges | Required |
| Support Needed | Required |
| Submitted Report | Read-only |

---

# 8. Error Handling

| Condition | System Behavior |
|-----------|-----------------|
| Start date is not Monday | Validation error |
| Start date outside internship period | Validation error |
| Missing supervisor email | Submission blocked |
| No task entered | Submission blocked |
| Missing Challenges | Submission blocked |
| Missing Support Needed | Submission blocked |
| Email delivery failure | Report submitted successfully; warning displayed |
| Submitted report | Editing disabled |

---

# 9. Dependencies

This module depends on:

- Module 05 – Internship Management

Required master data:

- Internship Group
- Student Assignment
- Company
- Internship Period
- Supervisor Information

Generated reports are available to:

- Staff members
- Internship supervisors
- PNV administration

---

# 10. Test Data Preparation

Before executing UAT, prepare:

## Internship Group

One **On-going** internship group.

---

## Student

One student assigned to the internship group.

---

## Supervisor Information

Prepare:

- PNV Supervisor Email
- Company Supervisor Email

---

## Internship Tasks

Example

```text
Task Name

Implement Login API

Description

Develop authentication feature

Result

Completed successfully
```

---

## Working Hours

Prepare working hours covering several days to verify automatic calculations.

---

## Email Test

Prepare valid email addresses for:

- PNV Supervisor
- Company Supervisor

Verify:

- Email delivery
- Email recipients
- Email subject format

---

## Email Failure Test

Prepare an environment where email delivery fails.

Verify:

- Report status becomes Submitted.
- Warning message is displayed.
- No automatic resend option is available.

---

# 11. UAT Test Scenarios

Detailed UAT scenarios are documented separately.

Covered scenarios include:

- BR-01 → BR-14

These scenarios validate:

- Report creation
- Draft saving
- Report editing
- Submission validation
- End date calculation
- Dynamic task table
- Total hour calculation
- Report submission
- Automatic email notification
- Email failure handling
- Staff report viewing

---

# 12. Out of Scope

The following functions are not supported:

- Editing submitted reports
- Deleting submitted reports
- Automatic email resend
- Offline report submission
- Multiple report statuses beyond Draft and Submitted
- Supervisor approval workflow

---

# 13. Module Summary

The Bi-Weekly Internship Reports module enables students to document their internship progress through structured reports while ensuring data completeness through validation and automatic calculations.

Its draft workflow, automatic email notifications, immutable submitted reports, and staff review capabilities provide a reliable reporting process that supports internship supervision and communication between students, company supervisors, and PNV staff.