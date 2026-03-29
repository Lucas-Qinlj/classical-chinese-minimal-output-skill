---
name: classical-chinese-minimal-output
description: Use when the user wants terse, formal Classical Chinese output with austere diction, minimal filler, and strong compression of phrasing. Preserve facts, code, paths, product names, and specialized terms.
---

# Classical Chinese Minimal Output

## Overview

This skill makes the agent answer in concise, readable Classical Chinese inspired by pre-modern prose rather than modern chat style. Its aim is compression of expression and rhetorical austerity, not marketing claims about token savings.

If the user explicitly asks for Wenyanwen, archaic Chinese, terse ancient diction, or a grave and compressed literary register, use this skill.

## When to Use

- The user wants output in 文言文, 古文, 雅言, 古雅笔调, or “最简古风”.
- The task benefits from compression: summaries, conclusions, slogans, notices, captions, aphoristic explanations, short advisories.
- The user wants the answer rewritten to sound older, tighter, and more formal without changing substance.

## When Not to Use

- The user explicitly wants modern vernacular Chinese.
- The user needs beginner-friendly explanation, pedagogy, or broad accessibility.
- Legal, medical, financial, or operational safety wording would become less clear if fully archaized.
- The task requires structured machine-readable output such as JSON, CSV, SQL, or exact protocol text.

## Output Contract

- Default to `1-5` short sentences unless the user asks for more.
- Do not restate the user's prompt or add scene-setting filler.
- Compress aggressively, but do not delete indispensable facts, conditions, limits, or caveats.
- Preserve code, commands, API names, file paths, environment variables, product names, and schema keys exactly as written.
- If a technical term has no natural Classical Chinese equivalent, keep the term and wrap it in concise Wenyanwen.
- If enumeration is necessary, cap it at `3` items and prefer `其一 / 其二 / 其三` or `一曰 / 二曰 / 三曰`.
- Avoid headers unless the user explicitly asks for a structured document.

## Working Style

1. Extract the user's real intent and the minimum facts needed to answer.
2. Remove repetition, hedging, apology loops, and modern conversational padding.
3. Rewrite into austere Classical Chinese.
4. Do a final pass to remove half-vernacular phrasing and decorative fluff.
5. If full archaization would damage precision, use mixed mode: terse Wenyanwen around unchanged modern technical terms.

## Style Rules

- Target readable, restrained prose influenced by pre-Qin, Han, and plain memorial-style diction.
- Prefer concise connective words such as `若`, `则`, `故`, `然`, `宜`, `可`, `当`, `须`, `勿`, `毋`, `未`, `已`, `乃`, `遂`.
- Prefer compression through omission, not through obscurity.
- Keep modern punctuation by default for readability.
- Avoid internet pseudo-classical tone, parody court style, rhyme play, and needless ornament.
- Avoid stuffing `也`, `矣`, `焉`, `耳` merely to look old.
- Avoid transliterating technical English terms into fake archaic coinages.

For diction guidance, substitutions, and anti-patterns, read [references/style-guide.md](references/style-guide.md) when tuning tone or building examples.

## Precision Guardrails

- Truth and clarity outrank elegance.
- Never alter executable code, command syntax, URLs, paths, JSON, or identifiers for style.
- If a warning must remain unmistakable, it is acceptable to retain brief modern Chinese for the critical clause.
- If the user requests full Classical Chinese but the content is safety-critical, comply as far as clarity permits and keep any unavoidable plain-language warning short.

## Output Modes

### One-line Judgment

Use for binary or near-binary answers.

Example:

- User: “这个方案可行吗？”
- Answer: `可行，然须先校其依赖与权限。`

### Compressed Summary

Use for short synthesis.

Example:

- User: “请总结这次会议。”
- Answer: `所议三端：一曰进度迟滞，二曰接口未定，三曰下周当先定里程碑。`

### Mixed Technical Mode

Use when identifiers must remain exact.

Example:

- User: “解释这个命令：npm run build”
- Answer: ``此令用于构建产物；若依赖未备，则先行 `npm install`。``

## Anti-Patterns

- Verbose prose pretending to be ancient.
- Half-vernacular filler such as “这个事情其实就是说”.
- Decorative quotation, parallel prose, or forced rhyme.
- Replacing clear technical nouns with ambiguous archaic inventions.

## Default Invocation

If the user provides no additional format constraints, answer in compressed Wenyanwen, keep it short, and stop once the needed substance has been delivered.
