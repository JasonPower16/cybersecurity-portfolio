# Zero Trust Architecture Design

## Objective
Reduce implicit trust and limit attacker movement across the environment.

## Principles
- Verify explicitly
- Use least privilege
- Assume breach
- Inspect east-west traffic where possible

## Core Components
- Strong identity provider and MFA
- Device trust and compliance signals
- Microsegmentation or policy-based workload controls
- Centralized logging and analytics
- Conditional access for high-risk activity

## Design Considerations
- Protect administrative paths first
- Segment crown-jewel applications
- Build visibility before strict enforcement
- Track exceptions with expiration dates

## Metrics
- Number of implicit trust paths removed
- Reduction in broad network access
- Percentage of critical applications with explicit policy
