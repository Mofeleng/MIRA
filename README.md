# Multi-Agent Intent Router with LangGraph

A LangGraph-powered workflow that intelligently routes user requests based on intent and processes them through specialized agents.

## Overview

This project implements a multi-agent architecture that classifies incoming user requests and routes them to the appropriate workflow:

* **Chat** → General conversation and assistance.
* **Knowledge Base (KB)** → Information retrieval and question answering using Retrieval-Augmented Generation (RAG).
* **Code** → Software development tasks handled by a coding agent with human review.

The goal is to provide a clean separation of concerns while maintaining a flexible and extensible architecture.

---

## Workflow

```text
                                                             Chat
                                                              │
                                                              ▼
Start Node ──► Intent Classifier ─────────────────────────► End

                         │
                         │
                         ▼

                   Knowledge Base
                         │
                         ▼
                     RAG Node
                         │
                         ▼
                        End

                         │
                         │
                         ▼

                     Code Request
                         │
                         ▼
                    Coding Agent
                         │
                         ▼
                 Human Review Node
                   │            │
                   │            │
          Changes Required      Approved
                   │            │
                   ▼            ▼
              Coding Agent     End
```

---

## Components

### Start Node

The entry point of the workflow. Receives the user's request and forwards it to the intent classifier.

### Intent Classifier

Analyzes the user's message and determines the appropriate route:

* **Chat**: Casual conversation, brainstorming, or general assistance.
* **Knowledge Base**: Questions requiring information retrieval.
* **Code**: Requests involving source code creation, modification, debugging, or software development tasks.

### Chat Route

Handles conversational interactions and responds directly to the user before terminating the workflow.

### Knowledge Base Route

Uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant information from the knowledge base and generate an accurate response.

### Coding Agent

Responsible for software development tasks such as:

* Writing new code
* Updating existing code
* Refactoring
* Bug fixing
* Feature implementation

### Human Review Node

Acts as a quality-control checkpoint for code-related tasks.

The reviewer can:

* **Approve** the generated solution, sending the workflow to the end node.
* **Request Changes**, sending feedback back to the Coding Agent for another iteration.

This creates a human-in-the-loop development cycle that ensures code quality and alignment with user requirements.

### End Node

The terminal state of the workflow where the final response is returned to the user.

---

## Key Features

* Intent-based request routing
* Modular LangGraph architecture
* Retrieval-Augmented Generation (RAG) support
* Dedicated coding workflow
* Human-in-the-loop code review
* Iterative feedback loop for code refinement
* Easy extension for additional agents and workflows

---

## Example Request Flow

### Example 1: General Chat

**User:** "Explain recursion like I'm five."

```text
Start → Classifier → Chat → End
```

---

### Example 2: Knowledge Query

**User:** "What is Retrieval-Augmented Generation?"

```text
Start → Classifier → KB → RAG → End
```

---

### Example 3: Code Modification

**User:** "Add authentication to my Next.js application."

```text
Start → Classifier → Code → Coding Agent
                                ↓
                         Human Review
                            ↓     ↓
                    Changes     Approved
                        ↓           ↓
                  Coding Agent    End
```

---

## Future Improvements

* Multi-step planning agents
* Tool calling and external API integration
* Memory and conversation persistence
* Automated testing agents
* Multiple specialized coding agents
* Feedback analytics and workflow monitoring

---

## Tech Stack

* LangGraph
* LangChain
* Python
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)

---

## Design Philosophy

Rather than using a single agent for every task, this project embraces a routing-based architecture where each request is directed to the component best suited to handle it. This improves maintainability, scalability, and overall response quality while keeping the workflow easy to understand and extend.
