# Handoff Prompt for Project Context Keeper Development

**Copy this into a NEW Claude conversation window to pick up where we left off:**

---

Let's start working on adding some features to our project-context-keeper skill in GitHub. This is the Claude skill that manages development context across coding sessions with timeline tracking and auto-activation.

We just finished v3 development and merged it with main. The branch is ready for release, but we identified several opportunities for improvement during dogfooding.

**Project Location:** `C:\GitHub\project-context-keeper`

**Current Status:**
- Version: v3.0
- Branch: v3-timeline (merged, pushed to origin)
- Context file: `devbridge-context.md` (review this first)

**What We Need to Work On:**

1. **Auto-Activation Refinement**
   - The skill didn't auto-trigger when we were working on itself (meta problem!)
   - Need to add special case: if working ON project-context-keeper, always offer tracking
   - Test trigger patterns with real usage and tune false positive/negative rates

2. **Checkpoint UX Improvements**
   - Users need clearer guidance on when to checkpoint vs just continuing
   - Add "smell test" rules: checkpoint frequency, what counts as checkpoint-worthy
   - Consider adding `context: checkpoint --quiet` for trivial saves

3. **Status Display Enhancements**
   - Current condensed view may hide important warnings/blockers
   - Implement tiered display: minimal default, `--full` flag for complete view
   - Surface active blockers prominently with visual indicators

4. **Migration Testing & Validation**
   - Create test fixtures for v1, v2, v3 formats to verify migration paths
   - Add `context: validate` command to check schema compliance
   - Document edge cases (empty fields, malformed dates, etc.)

5. **Timeline Archival Strategy**
   - Context files will grow unbounded over time
   - Design auto-archive for sessions older than 6 months
   - Add `context: compact` to summarize old sessions
   - Implement temporal queries: `context: history --range 2025-01`

6. **Git Workflow Integration**
   - Context saves happen independently of Git commits currently
   - After save, detect uncommitted changes in files_touched
   - Offer to commit with auto-generated message from session summary

7. **Automation Battle-Testing**
   - `context: automate` command documented but not tested in production
   - Need to verify continuous-claude integration and cost tracking
   - Add real automation examples to SKILL.md

**Priority Order:**
Start with #1 (auto-activation refinement) since that's blocking dogfooding. Then tackle #3 (status display) and #2 (checkpoint UX) as they affect daily usage quality. The rest can follow based on user feedback.

**Key Files to Review:**
- `devbridge-context.md` - Our own context (the irony!)
- `SKILL.md` - Main skill documentation with workflows and examples
- `README.md` - User-facing quick start guide

**Development Approach:**
- Make incremental changes and test auto-activation behavior
- Use this project to dogfood changes immediately
- Create checkpoints as we complete each feature
- Save session with full timeline entry at end

Ready to dive in! Let's start by reading the context file to understand where we left off, then pick the first improvement to tackle.

---

**Meta Note:** This prompt itself demonstrates the handoff pattern the skill enables - clear state, prioritized next actions, and decision context. That's the goal for every project using this skill.
