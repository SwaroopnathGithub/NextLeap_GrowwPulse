# GrowwPulse n8n Workflow

## Import
1. Open your local n8n instance (http://localhost:5678).
2. Workflows → **Import from File** → select `groww-pulse-workflow.json` from this folder.

## Before running
- **Groq Chat Model** node: select your own Groq API credential.
- **Append to Pulse Doc** node: select your Google Docs credential, and replace the placeholder `documentId` value with your target Google Doc's ID.
- **Create Gmail Draft** node: select your own Gmail credential.

## How the approval gate works
The workflow pauses at **Approval Gate (Wait)**. Nothing is appended to the Doc or drafted in Gmail until it's resumed.
- Run the workflow manually (the "Execute Workflow" button).
- When it reaches the Wait node, open that execution in n8n and copy the **Resume URL** it shows.
- Open that URL in a browser to approve and let the rest of the workflow run.
- If you never open the Resume URL, the doc/draft steps simply never fire — that's the reject path.

## What the LLM step does
`Draft Pulse & Fee Explainer` feeds the already-computed 12-week review analysis (rating distribution, theme frequencies, representative quotes — the same data behind `docs/weekly-product-pulse.md` and `docs/fee-explainer.md`) into Groq, which drafts a condensed pulse + fee-explainer pair in markdown for the doc/email.

## Known soft spots
The Google Docs "insert text" action schema and the Wait node's resume options are the two parts of the n8n JSON format that vary most between n8n versions. If either node shows a config error on import, re-pick the equivalent option in the node's UI (insert text at document end; resume on webhook call) — the rest of the workflow doesn't depend on exact field names there.
