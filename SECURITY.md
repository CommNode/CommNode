# Security Policy

## Supported Versions

Use this table to tell which versions of your project are currently being supported with security updates.

| Version | Supported          |
|---------|--------------------|
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it as soon as possible.

### How to Report

1. **Do not** disclose the vulnerability publicly until it has been resolved
2. **Contact** the project maintainers directly via email or open a security advisory
3. **Provide** as much details as possible including:
   - Steps to reproduce
   - Platform and environment details
   - Potential impact

### Security Contact

Please send reports to: security@commnode.local

### Preferred Approach

We prefer reports sent directly to the maintainers via private email. Please do not create public issues for security vulnerabilities.

### Response Timeline

- **Initial response**: Within 48 hours of report receipt
- **Triage**: Within 7 days to assess severity
- **Fix deployment**: Within 30 days for critical issues, 90 days for medium/low severity

### severity Classification

- **Critical**: Remote code execution, complete system compromise
- **Medium**: Authentication bypass, data exposure, privilege escalation
- **Low**: Information disclosure, denial of service

## Acknowledgments

Security researchers who report vulnerabilities will be acknowledged in the project's release notes (unless you prefer to remain anonymous).

## Secure Development

- Dependencies are regularly updated
- Code follows security best practices
- Input validation is implemented for all user-provided data
- Error handling prevents information leakage