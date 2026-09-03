# Xano backend contract

RolePilot uses Xano as the live backend for the hackathon demo.

## Instance

Region: Frankfurt, Germany

API base URL:

`https://xtbm-3nan-h5yy.f2.xano.io/api:rolepilot`

Production frontend:

`https://default-prod-d95b66-xtbm-3nan-h5yy.f2.xano.io`

## Tables

### opportunity

- id
- title
- brand
- deadline
- status
- raw_text
- created_at

### asset

- id
- label
- kind
- tags
- approved
- created_at

### application_run

- id
- opportunity_id
- readiness
- summary
- requirements
- selected_assets
- gaps
- approval_state
- created_at

### audit_event

- id
- run_id
- event
- detail
- created_at

## Endpoints

### GET /opportunities

Returns the synthetic hackathon opportunity queue ordered by ID.

### POST /analyze

Input:

```json
{
  "opportunity_id": 1,
  "raw_text": "optional casting brief text"
}
```

Returns deterministic readiness output for the seeded demo opportunities, including requirements, matched assets, gaps, readiness score, and whether preparation may continue.

The hackathon version deliberately uses deterministic runtime logic so the demonstrated behavior is reliable and inspectable.

### POST /runs

Input:

```json
{
  "opportunity_id": 1
}
```

Creates an application preparation run and writes an audit trail. The workflow is blocked when the opportunity requires new material that is not available.

### POST /runs/{id}/approval

Input:

```json
{
  "approved": true
}
```

Updates the application run to the demo approval state and records the human decision in the audit log.

### POST /setup

Seeds the synthetic demo data used by the hackathon build.

## Safety boundary

There is intentionally no endpoint that submits a real casting application. RolePilot automates preparation and state tracking, then stops before the consequential external action.

## AI implementation workflow

The initial Xano backend was generated with Xano Agent using Xano's provided Google Gemini model from a detailed backend specification. The generated result was then manually tested endpoint by endpoint before publication.
