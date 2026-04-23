# Daily Reflection Decision Tree

This project implements a deterministic decision tree for a daily reflection system. The goal is to guide a user through a structured reflection about their day and provide meaningful insights based on their responses.

## Approach

The system is built using a rule-based decision tree. It asks the user three key questions:

1. Overall mood of the day (Good / Okay / Bad)
2. Productivity level (High / Medium / Low)
3. Main challenge faced (Work/Study, Time Management, Personal/Emotional, None)

Based on these inputs, the system follows predefined logical paths to generate a reflection output. The responses are deterministic, meaning the same inputs will always produce the same output.

## Decision Logic

The decision tree combines mood and productivity to determine the primary reflection. Additional refinement is applied based on the type of challenge faced during the day. This ensures that the output is both structured and context-aware.

## Guardrails

To reduce ambiguity and avoid unreliable outputs:
- The system uses fixed input options instead of free text
- Invalid inputs are handled with default values
- No probabilistic or AI-based responses are used
- All outputs are predefined and predictable

## Conclusion

This implementation demonstrates how a simple deterministic system can provide structured and meaningful reflections. It ensures clarity, consistency, and reliability without relying on generative AI.

## Part B: AI Agent Extension

An agent-based version of the system was implemented to handle more natural user inputs. Instead of fixed options, the agent accepts flexible text responses and maps them to structured categories using keyword-based detection.

Guardrails are implemented to ensure reliability:
- Inputs are mapped to predefined categories
- No free-form generation is used
- Outputs remain deterministic

This approach maintains control while improving usability.