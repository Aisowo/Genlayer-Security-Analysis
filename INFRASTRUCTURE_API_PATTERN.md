# GenLayer External API Integration Pattern

## Overview
A simple, reusable pattern for Intelligent Contracts to interact with external APIs (weather, price feeds, social data) while keeping API keys private and outputs consistent.

## Problems Addressed
- **Secret exposure**: API keys leaking through contract outputs/logs
- **Non-determinism**: different validators receiving different raw API responses
- **Inconsistent formats**: hard to reach agreement if outputs vary

## Pattern
- Encapsulate API logic in a client (`SecureAPIClient`)
- Keep API keys private (never returned)
- Normalize responses before returning to the contract
- Expose only sanitized fields (`data`, `status`)

## Optional Enhancements
- Add timeouts/retries and response caching
- Fix request windows (e.g., minute buckets) to reduce divergence
- Multi-source aggregation (e.g., median of 3 providers)
- Deterministic post-processing before returning results

## UX / Studio Improvements (Observed)
- Schema errors lack clear guidance on required contract structure
- No early validation for contract shape before deployment
- Limited debugging feedback for failed executions

## Recommendations
- Provide official contract + API templates
- Add real-time schema validation in Studio
- Improve error messages with actionable hints
