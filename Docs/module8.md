# Module 08 – Profile Photo Management

> **Module ID:** M08  
> **Module Name:** Profile Photo Management  
> **Primary User:** Staff  
> **Related Modules:** Module 01 – Batch & Student Management

---

# 1. Overview

The **Profile Photo Management** module allows staff members to upload, replace, and remove student profile photos.

Profile photos are stored in a designated **Google Drive** folder and are displayed consistently throughout the system wherever student information appears.

This functionality is integrated directly into the **Student Detail** page and is not available as a standalone module.

Students are not permitted to upload or manage their own profile photos.

---

# 2. Objectives

This module enables staff members to:

- Upload profile photos for students.
- Replace existing profile photos.
- Remove profile photos.
- Display profile photos consistently throughout the system.
- Automatically display fallback avatars when photos are unavailable.

---

# 3. Storage Information

| Item | Description |
|------|-------------|
| Storage Location | Google Drive (configured folder) |
| File Name | `{StudentName}_{Timestamp}.jpg` |
| Display URL | `https://drive.google.com/thumbnail?id={photoId}&sz=w200` |
| File Permission | Anyone with the link – View only |

---

# 4. Functional Features

| Feature ID | Feature | Description |
|------------|---------|-------------|
| M08-F01 | Photo Upload | Staff can upload a new profile photo with instant preview before saving. |
| M08-F02 | Photo Replacement | Uploading a new photo automatically removes the previous photo from Google Drive. |
| M08-F03 | Photo Removal | Remove a profile photo by moving the file to Google Drive Trash (soft delete). |
| M08-F04 | Fallback Avatar | If the image cannot be loaded, a two-letter initials avatar is displayed automatically. |
| M08-F05 | Restricted Access | Only staff members can upload, replace, or remove profile photos. Students have read-only access. |

---

# 5. Business Rules

## 5.1 Staff-only Access

Only staff members are authorized to manage profile photos.

Students can:

- View their profile photo.

Students cannot:

- Upload photos
- Replace photos
- Delete photos

---

## 5.2 Photo Upload

When uploading a new profile photo,

the system shall:

- Upload the image to Google Drive.
- Generate a public thumbnail URL.
- Save the URL in the student profile.

The student record is updated only after the upload succeeds.

---

## 5.3 Photo Replacement

Each student can have only one active profile photo.

When a new photo is uploaded,

the system automatically:

1. Uploads the new image.
2. Updates the student profile.
3. Deletes the previous Google Drive file.

```
Upload New Photo

↓

Update Student Record

↓

Delete Previous Drive File
```

Old files are not retained.

---

## 5.4 Photo Removal

Removing a profile photo does not permanently delete the file.

Instead,

the Google Drive file is moved to **Trash**.

```
Remove Photo

↓

Move File to Drive Trash

↓

Student Photo Cleared
```

Permanent deletion is handled by Google Drive.

---

## 5.5 Upload Failure

If the upload process fails,

the student information must remain unchanged.

```
Upload Failed

↓

Do NOT Update Student Record
```

This prevents broken image links from being stored.

---

## 5.6 Broken Image Handling

If the stored image URL returns:

```
HTTP 404
```

or cannot be loaded,

the system automatically displays a fallback avatar.

The fallback avatar consists of the student's two-letter initials.

Example:

```
John Smith

↓

JS
```

No manual action is required.

---

# 6. Display Locations

Profile photos are displayed throughout the system.

| Location | Size |
|----------|------|
| Student List | 52 × 52 px |
| Student Edit Dialog | 120 × 120 px |
| Student Detail Sidebar | 200 × 200 px |
| Home Dashboard | 52 × 52 px |

All profile photos are displayed using a circular avatar style.

---

# 7. Google Drive Integration

Uploaded images are stored in a pre-configured Google Drive folder.

Each uploaded file uses the following naming convention:

```
{StudentName}_{Timestamp}.jpg
```

Example

```
John_Smith_20260718103015.jpg
```

The generated thumbnail URL follows the format:

```
https://drive.google.com/thumbnail?id={photoId}&sz=w200
```

Files are shared using:

```
Anyone with the link

Permission:
View only
```

---

# 8. Validation Rules

| Item | Validation |
|------|------------|
| Student | Required |
| Image File | Required |
| Upload Permission | Staff only |
| Google Drive Upload | Must succeed before saving |
| Replacement | Previous image automatically removed |
| Broken URL | Display fallback avatar |

---

# 9. Error Handling

| Condition | System Behavior |
|-----------|-----------------|
| Upload failed | Student record is not updated |
| Google Drive unavailable | Display upload error |
| Invalid image URL | Display fallback avatar |
| Remove photo | File moved to Google Drive Trash |
| Student attempts upload | Access denied |

---

# 10. Dependencies

This module depends on:

- Module 01 – Batch & Student Management

Required external service:

- Google Drive

Profile photos are displayed throughout the system wherever student information is shown.

---

# 11. Test Data Preparation

Before executing UAT, prepare:

## Students

At least three students.

---

## Images

Prepare:

- Valid JPG image
- Valid PNG image
- Large image
- Replace existing image
- Remove existing image

---

## Google Drive

Prepare:

- Configured upload folder
- Public sharing enabled
- Drive Trash enabled

---

## Failure Scenarios

Prepare:

- Simulated upload failure
- Invalid photo URL
- Deleted Google Drive file
- Student account attempting upload

---

# 12. UAT Test Scenarios

Detailed UAT scenarios are documented separately.

Covered scenarios include:

- Upload profile photo
- Replace existing photo
- Remove photo
- Automatic deletion of previous photo
- Google Drive integration
- Broken image fallback
- Staff permission validation
- Student access restriction

---

# 13. Out of Scope

The following features are not supported:

- Student self-upload
- Image editing
- Image cropping
- Multiple profile photos
- Photo version history
- Permanent deletion from Google Drive

---

# 14. Module Summary

The **Profile Photo Management** module provides centralized management of student profile images through Google Drive integration.

The module ensures that each student has only one active profile photo, automatically removes outdated images, supports soft deletion through Google Drive Trash, and guarantees a consistent user experience by displaying fallback avatars whenever profile images are unavailable.