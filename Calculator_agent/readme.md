Goal: Create a simple LangChain agent that can use a calculator tool to solve basic arithmetic problems expressed in natural language.

Key Concepts
Tool: A function or utility the agent can call. In this case, we'll use the built-in LangChain LLMMathTool or a simple Python calculator function.

LLM: The brain that decides when and how to use the tool.

AgentExecutor: The runtime that orchestrates the cycle: LLM receives input, decides on a tool and input, executes the tool, and gets the observation back.
