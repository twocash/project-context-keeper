---
name: project-context-keeper
description: Manages project context across coding sessions using a standardized `devbridge-context.md` file. It loads, updates, and saves project state to ensure continuity.
license: (internal)
---

# Project Context Keeper Skill

This skill provides a systematic framework for persisting project context across multiple, token-limited coding sessions. It uses a standardized `devbridge-context.md` file (backed by a JSON schema) to track state, goals, and history.

## Core Philosophy

1.  **Be Brief:** This system's primary goal is token *efficiency*. All context must adhere to the character and item limits defined in the schema.
2.  **User-Led, AI-Assisted:** The AI *does not* summarize the session. The AI *prompts* the user (the PM/developer) to provide the concise updates for `last_completed`, `next_action`, etc. This is faster, more accurate, and ensures the "human-checkable" goal.
3.  **Schema-Driven:** The AI must *always* follow the structure of the `DevBridge Context Template`. It must not add, remove, or invent new fields.
4.  **Explicit Triggers:** The skill is *not* "auto-spawned." It is explicitly invoked by the user with simple commands. This is more reliable and less verbose.

## Core Triggers (Commands)

You will use these commands to manage the context session:

* `context: start`: Loads the context file, confirms the last state, and begins the session.
* `context: save`: Ends the session by "interviewing" you for updates and saving the context file.
* `context: status`: (Optional) Displays the currently loaded context file's contents.

---

## Detailed Workflows

### 1. Workflow: `context: start`

**User:** `context: start` (or `context: load`)

**AI's Actions:**
1.  Ask for the project's root directory: "What is the absolute `local_path` for this project?"
2.  (User provides path: `/Users/jim/projects/drumwave`)
3.  Look for the file: `[local_path]/devbridge-context.md`.

**IF `devbridge-context.md` IS FOUND:**
1.  Read the file.
2.  Parse its contents.
3.  Respond with a *lightweight confirmation* (not the whole file):
    > "Context for **DrumWave Interactive Model** loaded.
    > **State:** `in_progress`
    > **Last Completed:** Implemented basic polyrhythm engine...
    > **Next Action:** Add velocity controls and pattern presets...
    >
    > Ready to begin."

**IF `devbridge-context.md` IS NOT FOUND:**
1.  Respond: "No `devbridge-context.md` found in that directory."
2.  Ask to create one: "Would you like to create a new context file?"
3.  If "yes," prompt for the *minimum required fields*:
    * "What is the `project` name?"
    * "What is the one-sentence `goal` (what user problem does it solve)?"
    * "What is the `tech_stack` (core libraries)?"
4.  Once provided, create the file in memory and respond: "New context file created. Ready to begin." (The rest of the fields will be populated at `context: save`).

### 2. Workflow: `context: save`

**User:** `context: save` (or `context: end`)

**AI's Actions:**
This triggers the "update interview." The AI will ask you for updates, one by one.

1.  **AI:** "Saving context. What was `last_completed` this session? (1-2 sentences)"
2.  **User:** (Provides summary)
3.  **AI:** "Got it. What is the `next_action` for the *next* session? (specific)"
4.  **User:** (Provides next step)
5.  **AI:** "What is the current `state`? (`in_progress`, `needs_testing`, `ready_to_deploy`, etc.)"
6.  **User:** (Provides state)
7.  **AI:** "Which `files_touched` this session? (Please provide a list of paths)"
8.  **User:** (Provides file list)
9.  **AI:** (Optionally, for other fields) "Any `blockers` or `warnings` to add?"
10. **AI:** (Gathers system info) "Updating `timestamp` to [current ISO 8601 time]."
11. **Generate & Save:** The AI generates the *complete Markdown content* based on the `DevBridge Context Template`.
12. **Write File:** The AI writes/overwrites the `devbridge-context.md` file at the `local_path`.
13. **Confirm:** "Context saved to `/Users/jim/projects/drumwave/devbridge-context.md`."

### 3. Workflow: `context: status`

**User:** `context: status`

**AI's Actions:**
1.  Reads the currently loaded context from memory.
2.  Prints the *full content* of the `devbridge-context.md` file exactly as it is.

---

## Context File Schemas (Source of Truth)

This is the rigid structure the AI must follow.

### DevBridge JSON Schema

```json
{
  "$schema": "[http://json-schema.org/draft-07/schema#](http://json-schema.org/draft-07/schema#)",
  "title": "DevBridge Context Handoff",
  "description": "Minimal context notation for AI-assisted development session persistence",
  "type": "object",
  "required": [
    "project",
    "state",
    "last_completed",
    "next_action",
    "files_touched"
  ],
  "additionalProperties": false,
  "properties": {
    "project": {
      "type": "string",
      "maxLength": 50,
      "description": "Project name only, no description"
    },
    "state": {
      "type": "string",
      "enum": [
        "ready_to_deploy",
        "in_progress",
        "blocked",
        "needs_testing",
        "prod_deployed"
      ],
      "description": "Current deployment state"
    },
    "goal": {
      "type": "string",
      "maxLength": 120,
      "description": "One-sentence user-facing goal (what problem does this solve?)"
    },
    "tech_stack": {
      "type": "array",
      "maxItems": 8,
      "items": {
        "type": "string",
        "maxLength": 30
      },
      "description": "Core technologies only (React, Node, etc.)"
    },
    "last_completed": {
      "type": "string",
      "maxLength": 200,
      "description": "What was just finished (1-2 sentences max)"
    },
    "next_action": {
      "type": "string",
      "maxLength": 150,
      "description": "Immediate next step (actionable, specific)"
    },
    "blockers": {
      "type": "array",
      "maxItems": 3,
      "items": {
        "type": "string",
        "maxLength": 100
      },
      "description": "Active blockers preventing progress"
    },
    "files_touched": {
      "type": "array",
      "maxItems": 15,
      "items": {
        "type": "string",
        "maxLength": 100
      },
      "description": "Files modified in last session (paths only, no descriptions)"
    },
    "git_state": {
      "type": "object",
      "required": ["branch"],
      "additionalProperties": false,
      "properties": {
        "branch": {
          "type": "string",
          "maxLength": 50
        },
        "uncommitted": {
          "type": "boolean",
          "description": "Are there uncommitted changes?"
        },
        "ahead_by": {
          "type": "integer",
          "minimum": 0,
          "description": "Commits ahead of origin"
        }
      }
    },
    "warnings": {
      "type": "array",
      "maxItems": 3,
      "items": {
        "type": "string",
        "maxLength": 100
      },
      "description": "Don't do X, avoid Y (antipatterns)"
    },
    "urls": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "prod": {
          "type": "string",
          "format": "uri"
        },
        "staging": {
          "type": "string",
          "format": "uri"
        },
        "repo": {
          "type": "string",
          "format": "uri"
        },
        "docs": {
          "type": "string",
          "format": "uri"
        }
      }
    },
    "local_path": {
      "type": "string",
      "maxLength": 200,
      "description": "Absolute path to project directory"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "When this context was last updated (ISO 8601)"
    },
    "session_id": {
      "type": "string",
      "maxLength": 20,
      "description": "Optional identifier for tracking across sessions"
    }
  }
}