# Classical Register Guide

本参考文件用于细化本 skill 的语体边界。默认目标不是艰涩难通之古奥文，也不是戏仿式“圣旨体”，而是可读、简峻、少赘的传统文言散体。

## Register Target

- 取法：先秦散文、两汉奏议、平实尺牍。
- 不取：骈俪铺张、诗词化抒情、网文伪古风、过度堆砌虚词。
- 要点：字少而义足，句短而气定。

## Preferred Diction

常用现代连接，可酌改如下：

| Modern Chinese | Preferred Wenyanwen |
| --- | --- |
| 如果 | 若 / 苟 |
| 那么 | 则 |
| 因为 | 以 / 缘 / 盖因 |
| 所以 | 故 / 是以 |
| 可以 | 可 |
| 应该 | 当 / 宜 |
| 必须 | 须 |
| 不要 | 勿 / 毋 |
| 还没有 | 未 |
| 已经 | 已 |
| 于是 | 乃 / 遂 |
| 但是 | 然 / 惟 / 顾 |

## Compression Heuristics

- 能省主语则省，但不可致歧义。
- 能去背景铺垫则去，只留结论、条件、限制、动作。
- 能以一词摄数词者，从简。
- 多余敬语、寒暄、重复确认，一概削去。

## Mixed Technical Mode

以下内容通常保持原样：

- code blocks
- shell commands
- file paths
- URLs
- API names
- package names
- JSON keys
- SQL identifiers

建议写法：

- `此接口调用 `POST /v1/responses` 即可。`
- `若欲部署，先行 `npm run build`。`
- `配置见 `config.toml`。`

## Phrasing to Avoid

- “这个事情其实就是说……”
- “然后我们就可以去……”
- “总的来说其实还是……”
- “臣妾做不到”式戏谑古风
- 为显古意而滥用 `也` `矣` `焉` `耳`

## Good vs Bad

### Good

`此策可行，然前置数据尚缺，宜先补之。`

短、明、有限制条件。

### Bad

`此事诚可为也，然而于今日之情势观之，似乎尚有若干问题存在焉。`

字多、气浮、古意做作。

## Readability Rule

若“更古”与“更明”相冲，则取其明。文言之长，在凝练，不在晦涩。
