# Example: User Authentication System

This example demonstrates the conversational feature definition process for a user authentication feature.

---

## Initial Request

**User**: "I need to add user authentication to the application. Users should be able to register and login."

---

## The Conversation

**AI**: "I'll help you define this feature clearly. Let me ask some clarifying questions:

1. What authentication method should we use - email/password, OAuth, or both?
2. Do you need password reset functionality?
3. Should sessions persist across browser restarts?
4. What happens if someone tries to register with an existing email?
5. Do you need role-based access control, or just authenticated/not authenticated?
6. Any specific security requirements - password complexity, rate limiting, etc.?"

**User**: "Good questions. Let me answer:
1. Email/password for now, OAuth can come later
2. Yes, password reset is important
3. Yes, sessions should persist - use 'remember me' functionality
4. Show an error message if email already exists
5. Just authenticated/not for now, roles can come in phase 2
6. Passwords should be at least 8 characters with one number and one special character"

**AI**: "Thank you. A few more questions:

7. For password reset - should we send a link via email or use security questions?
8. How long should reset links be valid?
9. Should sessions automatically expire after inactivity?
10. Do you want to limit failed login attempts to prevent brute force?
11. What technology stack - which framework/libraries should we use?"

**User**: "
7. Email link is better
8. 1 hour validity
9. Yes, expire after 30 days of inactivity
10. Yes, lock account after 5 failed attempts in 15 minutes
11. We're using Node.js with Express, use JWT for tokens and bcrypt for password hashing"

**AI**: "Perfect. One last question:

12. When an account is locked from failed attempts, how can it be unlocked - automatic after time period, or manual intervention required?"

**User**: "Automatic unlock after 30 minutes, but also send an email notification that the account was locked"

**AI**: "Excellent. I have all the information I need. I'll create a feature document using the standard template since this is for a production system. Give me a moment..."

---

## Feature Document

# Feature: User Authentication System

**Status**: Approved
**Priority**: Critical
**Version**: 1.0
**Last Updated**: 2025-11-30

---

## Purpose

**Problem**: Application currently has no user authentication. Anyone can access all features and data.

**Solution**: Implement secure email/password authentication with JWT-based sessions, password reset flow, and brute-force protection.

**Users**: All application users (future roles: regular users and admins)

## User Story

**As a** application user
**I want to** create an account and securely login
**So that** my data is private and only accessible to me

**Acceptance Criteria**:
- [ ] Users can register with email and password
- [ ] Users can login with valid credentials
- [ ] Users can reset forgotten passwords via email
- [ ] Sessions persist across browser restarts
- [ ] Failed login attempts are limited to prevent brute force
- [ ] Passwords meet security requirements

---

## Conceptual Flow

### Happy Path: Registration

1. User navigates to registration page
2. User enters email and password
3. System validates email format and password requirements
4. System checks email doesn't already exist
5. System hashes password with bcrypt
6. System creates user record in database
7. System generates JWT token
8. User is logged in automatically
9. System redirects to dashboard

### Happy Path: Login

1. User navigates to login page
2. User enters email and password
3. System validates credentials against hashed password
4. System generates JWT token (7-day expiry if "remember me" checked, otherwise session-only)
5. User is logged in
6. System redirects to dashboard or requested page

### Happy Path: Password Reset

1. User clicks "Forgot Password" on login page
2. User enters email address
3. System generates unique reset token (1-hour validity)
4. System sends email with reset link
5. User clicks link in email
6. System validates token (not expired, not already used)
7. User enters new password
8. System validates password requirements
9. System hashes new password and updates database
10. System invalidates reset token
11. User is redirected to login page with success message

### Error Case: Registration with Existing Email

1. User attempts to register
2. Email already exists in database
3. System returns error: "Email already registered"
4. User is shown error message
5. User can try different email or go to login page

### Error Case: Failed Login Attempts

1. User attempts login with wrong password
2. System increments failed attempt counter
3. After 5 failed attempts in 15-minute window:
   - System locks account for 30 minutes
   - System sends email notification of lock
   - System shows message: "Account locked due to too many failed attempts. Try again in 30 minutes."
4. After 30 minutes, lock automatically expires

---

## Data Model

### Entities

**User**
- `id`: UUID - Primary key
- `email`: string (unique, indexed) - User's email address
- `password_hash`: string - Bcrypt hashed password (never store plain text)
- `created_at`: timestamp - Account creation time
- `last_login_at`: timestamp (nullable) - Last successful login
- `is_locked`: boolean - Account lock status
- `locked_until`: timestamp (nullable) - When lock expires
- `failed_login_attempts`: integer - Counter for failed logins
- `last_failed_attempt`: timestamp (nullable) - Last failed login time

**PasswordReset**
- `id`: UUID - Primary key
- `user_id`: UUID - Foreign key to User
- `token`: string (unique, indexed) - Reset token
- `expires_at`: timestamp - Token expiry (1 hour from creation)
- `used_at`: timestamp (nullable) - When token was used
- `created_at`: timestamp - Token creation time

### Relationships

```
[User] --1:n--> [PasswordReset]
```

One user can have multiple password reset tokens (though only unused, unexpired ones are valid).

### Validation Rules

**Email**:
- Required
- Must be valid email format
- Must be unique (case-insensitive)
- Max length: 255 characters

**Password**:
- Minimum 8 characters
- Must contain at least one number
- Must contain at least one special character (!@#$%^&*)
- Max length: 128 characters

**Security**:
- Passwords hashed with bcrypt (10 rounds)
- JWT tokens signed with secret key
- Reset tokens are cryptographically random (32 bytes)

---

## API Design

### POST /api/auth/register

**Request**:
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response** (201 Created):
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "created_at": "2025-11-30T10:00:00Z"
  },
  "token": "jwt-token-here"
}
```

**Errors**:
- 400: Invalid email or password format
- 409: Email already exists

### POST /api/auth/login

**Request**:
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "remember_me": true
}
```

**Response** (200 OK):
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  },
  "token": "jwt-token-here"
}
```

**Errors**:
- 401: Invalid credentials
- 423: Account locked

### POST /api/auth/forgot-password

**Request**:
```json
{
  "email": "user@example.com"
}
```

**Response** (200 OK):
```json
{
  "message": "If that email exists, a reset link has been sent"
}
```

Note: Always return success even if email doesn't exist (security best practice)

### POST /api/auth/reset-password

**Request**:
```json
{
  "token": "reset-token-here",
  "new_password": "NewSecurePass456!"
}
```

**Response** (200 OK):
```json
{
  "message": "Password successfully reset"
}
```

**Errors**:
- 400: Invalid or expired token
- 400: Password doesn't meet requirements

---

## Key Questions & Decisions

**Q**: Email/password or OAuth?
**A**: Email/password for v1, OAuth deferred to v2
**Reasoning**: Simpler to implement, covers primary use case. OAuth adds complexity for uncertain benefit at this stage.

**Q**: How to handle password reset?
**A**: Email link with 1-hour expiry
**Reasoning**: More secure than security questions, better UX than temporary passwords.

**Q**: Session persistence?
**A**: JWT with 7-day expiry if "remember me" checked, otherwise session-only
**Reasoning**: Balance between convenience and security.

**Q**: Brute force protection?
**A**: Lock account after 5 failed attempts in 15 minutes, auto-unlock after 30 minutes
**Reasoning**: Industry standard, prevents attacks without overly impacting legitimate users.

**Q**: JWT or sessions?
**A**: JWT (JSON Web Tokens)
**Reasoning**: Stateless, scalable, works well with our API architecture. No need for server-side session storage.

---

## Implementation Notes

### Services Needed

**AuthService**:
- `register(email, password)` - Create new user
- `login(email, password, rememberMe)` - Authenticate user
- `logout(userId)` - (JWT doesn't require server-side logout, but may want to blacklist tokens in future)

**PasswordService**:
- `hashPassword(password)` - Bcrypt hash
- `verifyPassword(password, hash)` - Check password
- `validatePasswordStrength(password)` - Check requirements

**TokenService**:
- `generateJWT(userId, expiresIn)` - Create JWT
- `verifyJWT(token)` - Validate JWT
- `generateResetToken()` - Create reset token

**EmailService**:
- `sendPasswordResetEmail(email, resetUrl)` - Send reset link
- `sendAccountLockedEmail(email)` - Send lock notification

### Middleware

**authenticate**: Verify JWT on protected routes

```javascript
const authenticate = async (req, res, next) => {
  const token = req.headers.authorization?.replace('Bearer ', '');
  if (!token) return res.status(401).json({ error: 'No token provided' });

  try {
    const payload = await TokenService.verifyJWT(token);
    req.userId = payload.userId;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' });
  }
};
```

### Security Considerations

- Never log or expose passwords (even hashed)
- Use HTTPS in production
- Set secure, httpOnly cookies if using cookies
- Implement rate limiting on auth endpoints
- Use timing-safe comparison for tokens
- Consider CSRF protection for cookie-based auth

---

## Out of Scope

- ❌ OAuth/Social login (deferred to Phase 2)
- ❌ Two-factor authentication (future enhancement)
- ❌ Role-based access control (separate feature: F002)
- ❌ Email verification (can add later if spam becomes issue)
- ❌ Password change for logged-in users (separate feature: F003)

---

## Dependencies

- None - this is a foundational feature

---

## Success Criteria

### Functional

1. ✅ Users can register with valid email/password
2. ✅ Registration fails appropriately for duplicate emails or weak passwords
3. ✅ Users can login with correct credentials
4. ✅ Login fails for incorrect credentials
5. ✅ Account locks after 5 failed attempts
6. ✅ Account auto-unlocks after 30 minutes
7. ✅ Password reset flow works end-to-end
8. ✅ Reset links expire after 1 hour
9. ✅ JWT tokens work for authentication
10. ✅ Sessions persist across browser restarts (with remember me)

### Technical

1. ✅ Passwords hashed with bcrypt
2. ✅ All tests pass (unit + integration)
3. ✅ API endpoints return appropriate status codes
4. ✅ Sensitive data not logged or exposed
5. ✅ No security vulnerabilities (SQLi, XSS, etc.)

### Quality

1. ✅ Code review approved
2. ✅ Test coverage >80%
3. ✅ API documentation complete
4. ✅ Error messages are user-friendly

---

## Status Changes

- 2025-11-30: Draft created through conversational process
- 2025-11-30: Approved after review

---

## features.json Entry

```json
{
  "id": "F001",
  "name": "User Authentication System",
  "description": "Email/password authentication with JWT, password reset, and brute-force protection",
  "status": "pending",
  "priority": "critical",
  "progress": 0,
  "estimatedEffort": "large",
  "definitionDoc": "docs/features/01-user-authentication.md",
  "dependencies": [],
  "blockers": [],
  "files": [],
  "tests": [],
  "acceptanceCriteria": [
    "Users can register with email and password",
    "Users can login with valid credentials",
    "Password reset flow works via email",
    "Account locks after 5 failed login attempts",
    "Sessions persist with remember me functionality",
    "All security requirements met"
  ],
  "subtasks": [
    {
      "id": "F001.1",
      "name": "Create database schema for users and password resets",
      "status": "pending",
      "estimatedTime": "2h"
    },
    {
      "id": "F001.2",
      "name": "Implement password hashing service with bcrypt",
      "status": "pending",
      "estimatedTime": "1h"
    },
    {
      "id": "F001.3",
      "name": "Create registration endpoint with validation",
      "status": "pending",
      "estimatedTime": "3h"
    },
    {
      "id": "F001.4",
      "name": "Create login endpoint with JWT generation",
      "status": "pending",
      "estimatedTime": "3h"
    },
    {
      "id": "F001.5",
      "name": "Implement brute-force protection logic",
      "status": "pending",
      "estimatedTime": "2h"
    },
    {
      "id": "F001.6",
      "name": "Create password reset request endpoint",
      "status": "pending",
      "estimatedTime": "2h"
    },
    {
      "id": "F001.7",
      "name": "Create password reset confirmation endpoint",
      "status": "pending",
      "estimatedTime": "2h"
    },
    {
      "id": "F001.8",
      "name": "Implement authentication middleware",
      "status": "pending",
      "estimatedTime": "1.5h"
    },
    {
      "id": "F001.9",
      "name": "Set up email service for notifications",
      "status": "pending",
      "estimatedTime": "2h"
    },
    {
      "id": "F001.10",
      "name": "Write comprehensive tests (unit + integration)",
      "status": "pending",
      "estimatedTime": "4h"
    }
  ],
  "startedDate": null,
  "completedDate": null
}
```

---

## Lessons Learned

### What This Example Demonstrates

1. **Conversational Clarity**: Notice how questions revealed details not in initial request (brute-force protection, password requirements, token expiry)

2. **Better Design Through Questions**: The question about account unlocking revealed the need for email notifications, which wasn't originally considered

3. **Documented Decisions**: The "Key Questions & Decisions" section captures WHY choices were made, not just WHAT was decided

4. **Out of Scope Matters**: Explicitly stating OAuth is out of scope prevents scope creep and sets expectations

5. **Subtasks from Implementation**: The feature document's implementation notes directly inform the subtasks in features.json

### Time Investment

- **Conversation**: ~20 minutes
- **Document Creation**: ~15 minutes
- **Total**: ~35 minutes

**Value**: Clear specification prevents hours of rework from misunderstood requirements.
