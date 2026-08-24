---
applyTo: "**/*.{test,spec}.{py,ts,tsx},functional-test/cypress/**/*.ts"
---

Tests drive implementation through red-green-refactor. Unit tests should be fast and isolated; Cypress should cover complete browser workflows only after their underlying contracts exist. Name tests by observable behavior and avoid testing implementation details.

Every test function, test case, and test description MUST use one of these naming conventions:

1. Recommended BDD/Gherkin format: `should_[expected_behavior]_when_[condition_or_action]`
	- Example: `should_trigger_weather_tool_when_user_asks_for_forecast`
	- Example: `should_return_fallback_message_when_api_times_out`
2. Standard unit-test format: `test_[method_or_feature]_[scenario]_[expected_outcome]`
	- Example: `test_processInput_toolFailure_returnsGracefulError`
	- Example: `test_agentRun_validPrompt_invokesLlmWithCorrectContext`

Names must be descriptive, state the cause and effect, and directly reflect the `GIVEN` setup and `THEN` expectation. Do not use generic names such as `test1`, `test_agent`, or `test_failure`.
