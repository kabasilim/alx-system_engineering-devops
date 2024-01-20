# postmortem

## Postmortem: Web Stack Outage

## Issue Summary:

### Duration:
- Start Time: February 15, 2024, 10:30 AM (UTC)
- End Time: February 16, 2024, 2:45 AM (UTC)
### Impact:
- Service Affected: Web application authentication and authorization
- User Experience: Users faced login failures, impacting 80% of active users
### Root Cause:
- Misconfigured security group settings during routine infrastructure update
## Timeline:

### Detection:
- Detected at 10:30 AM through increased error rates in authentication requests.
### Actions Taken:
- Investigated backend services, suspecting database issues initially.
- Checked network connectivity, leading to a focus on security group configurations.
### Misleading Paths:
- Initial assumption of database issues led to unnecessary database optimizations.
- Considered a DDoS attack due to increased traffic but ruled out with network analysis.
### Escalation:
- Escalated to the infrastructure team at 12:15 PM for deeper network analysis.
### Resolution:
- Identified misconfigured security group settings causing unauthorized traffic blocking.
- Adjusted security group rules to allow legitimate authentication requests.
- System stability restored at 2:45 AM.
## Root Cause and Resolution:

### Cause:
- Misconfigured security groups led to the blocking of legitimate authentication traffic.
- An unintended rule change during routine infrastructure update caused the outage.
### Resolution:
- Security group rules were reverted to the previous state to allow proper traffic.
- Implemented automated checks to monitor and alert on security group changes.
- Corrective and Preventative Measures:

### Improvements:
- Enhanced monitoring for real-time detection of unauthorized security group changes.
- Implement regular security audits during infrastructure updates to catch misconfigurations early.
- Conduct training sessions for the team on identifying and resolving security-related issues.
## Tasks:
### Short-Term:
- Conduct a thorough review of recent infrastructure changes for potential misconfigurations.
- Document and communicate the incident response process to streamline future escalations.
### Mid-Term:
- Implement automated testing for security group changes before applying updates.
- Develop a comprehensive playbook for handling authentication-related outages.
### Long-Term:
- Evaluate the feasibility of a redundant authentication system to minimize future downtime.
- Establish a cross-functional task force to periodically review and enhance overall system security.
