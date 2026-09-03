# RolePilot

RolePilot is a safety-first casting application copilot built for the DevNetwork API + Cloud + AI Hackathon 2026, Xano challenge: Rebuild a SaaS Tool You Hate.

## Live demo

https://default-prod-d95b66-xtbm-3nan-h5yy.f2.xano.io

## Demo video

https://youtu.be/poRH63wko1Y

## What it rebuilds

Traditional casting application portals repeatedly ask actors to translate inconsistent briefs into the same profile fields, media selections, recording requirements, and manual checks.

RolePilot rebuilds that workflow around five steps:

1. Normalize the casting brief into explicit requirements.
2. Match only approved profile assets.
3. Flag missing recordings or review requirements.
4. Persist an application preparation run and audit trail in Xano.
5. Stop at a visible human approval gate before any external action.

## Why Xano matters

Xano is the live backend for the demo, not a mock integration.

It provides:

- opportunity data
- readiness analysis API
- application run persistence
- audit events
- approval state persistence
- static frontend hosting

The production frontend calls the public Xano API group directly.

## API surface

Base URL:

`https://xtbm-3nan-h5yy.f2.xano.io/api:rolepilot`

Endpoints:

- `GET /opportunities`
- `POST /analyze`
- `POST /runs`
- `POST /runs/{id}/approval`
- `POST /setup` for synthetic demo seed data

## Data model

- `opportunity`
- `asset`
- `application_run`
- `audit_event`

## AI build story

Xano Agent with Xano's provided Google Gemini generated the first backend implementation from a detailed product specification.

ChatGPT was used for product architecture, frontend implementation, integration QA, deployment support, and submission packaging.

The hackathon implementation went from Xano setup to a deployed and tested end-to-end demo in roughly 1.5 focused hours.

The readiness logic in this hackathon version is intentionally deterministic so the demo stays reliable and inspectable. The AI contribution is in accelerating product design and backend implementation rather than pretending the runtime business logic is more autonomous than it is.

## Safety boundary

This demo never submits a real casting application. It records preparation state and the human decision, then stops before the consequential external action.

## Repository contents

- `index.html` - public frontend deployed through Xano Static Hosting
- `XANO_BACKEND.md` - backend contract and implementation notes

All sample casting data in this repository is synthetic and created for the hackathon demo.
