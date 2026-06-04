# Technical Decisions

## Why Provider Abstraction?

A provider abstraction layer allows switching between OpenRouter, OpenAI, and Claude without changing business logic.

## Why Response Schemas?

Schemas ensure all generated content follows a predictable structure.

## Why Validation Layer?

Validation prevents invalid user inputs from reaching business logic.

## Why Retry Logic?

External AI APIs may fail temporarily. Retry logic improves reliability.

## Why Fallback Content Engine?

Users still receive content when AI providers fail or rate-limit requests.
