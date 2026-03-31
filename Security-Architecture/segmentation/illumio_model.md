# Microsegmentation Model

## Objective
Use application-aware segmentation to reduce attack surface and control east-west traffic.

## Sample Approach
1. Identify application dependencies
2. Label workloads by environment, application, and role
3. Build visibility mode policies first
4. Move high-confidence flows into enforcement
5. Review exceptions and remove broad access

## Example Policy Concepts
- App server can talk to database only on required ports
- Management protocols restricted to admin jump hosts
- Development systems isolated from production

## Evidence to Add Later
- Dependency maps
- Before/after policy sets
- Measured reduction in unnecessary connections
