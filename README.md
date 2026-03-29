# Classical Chinese Output Skill

以雅正文言，为 AI Agent 立一极简输出之 Skill。

本仓库之宗旨，不在鼓吹“必可节省 token”，而在借文言文之凝练特性，减少赘述，压缩表达，使答复更短、更峻、更有古意。

## Positioning

- 目标：令 Agent 以传统文言文输出，少铺陈，重撮要。
- 主张：通过古雅表达减少输出长度，提高简洁度。
- 非主张：不以“稳定减少 token 消耗”作为卖点或承诺。

## What This Skill Does

- 将答复改写为雅正、简峻、少赘之文言文。
- 保留事实、逻辑、结论与关键技术标识。
- 在代码、命令、路径、API 名称与数据结构周围使用简洁文言，而不篡改原始标识。
- 默认避免半白半文、网络伪古风与空泛堆砌。

## Repository Layout

```text
.
├── .github/workflows/validate.yml
├── examples/
│   └── invocations.md
├── scripts/
│   └── validate_skill.py
├── skills/
│   └── classical-chinese-minimal-output/
│       ├── agents/openai.yaml
│       ├── references/style-guide.md
│       └── SKILL.md
├── .gitignore
├── LICENSE
└── README.md
```

## Install

将 [`skills/classical-chinese-minimal-output`](skills/classical-chinese-minimal-output) 复制到你的技能目录，例如：

```bash
cp -R skills/classical-chinese-minimal-output "$CODEX_HOME/skills/"
```

## Invoke

显式调用示例：

```text
Use $classical-chinese-minimal-output to rewrite the following answer in austere Classical Chinese.
```

亦可直接以中文下令：

```text
请用最简雅正文言作答，勿增新义，勿赘述。
```

更多示例见 [`examples/invocations.md`](examples/invocations.md)。

## Sample Outputs

以下示例皆为示意，重在呈现此 skill 之风格：文言为主，简峻少赘，技术标识原样保留，不故作艰深。

## Before / After

以下对照采用“普通白话回答”与“Skill 输出”之比较，只看示例中的字符压缩效果，不代表对一切任务皆有同等幅度。

按本页示例中的 `6` 组白话回答与 Skill 输出对照计：

- 平均字符数减少约 `19.1%`
- 示例范围约为 `3.6% - 36.1%`
- 技术标识愈多，压缩幅度通常愈小

| Scenario | Plain Chinese | Skill Output | Reduction |
| --- | ---: | ---: | ---: |
| Feasibility | `24` chars | `22` chars | `8.3%` |
| Meeting summary | `34` chars | `30` chars | `11.8%` |
| Support reply | `30` chars | `22` chars | `26.7%` |
| Root-cause summary | `43` chars | `31` chars | `27.9%` |
| Feature update | `28` chars | `27` chars | `3.6%` |
| Safety reminder | `36` chars | `23` chars | `36.1%` |

是以，此 skill 之价值在于：

- 以文言压缩铺陈
- 以古雅收束语气
- 在不改原意之前提下，使答复更短、更峻、更利于一览

### 1. 可行性判断

输入：

```text
这个方案可行吗？需要注意什么？
```

输出：

```text
可行。然先须校其依赖、权限与回滚之策。
```

### 2. 会议总结

输入：

```text
请总结今天的会议：项目继续推进，但测试还不完整，接口也没最终定稿，下周先把范围收敛。
```

输出：

```text
此议可续行。然测试未备，接口未定。下周宜先敛范围，而后徐进。
```

### 3. 技术命令解释

输入：

```text
解释这个命令：npm run build
```

输出：

```text
此令用于构建产物。若依赖未备，则先行 `npm install`。
```

### 4. 风险提示

输入：

```text
写一句比较严肃的提醒：不要直接在生产环境执行这条 SQL。
```

输出：

```text
此 SQL 勿径施于生产环境，宜先验于测试库。
```

### 5. 客服回复

输入：

```text
帮我回复用户：我们已经收到你的反馈，问题正在排查，修复后会第一时间通知你。
```

输出：

```text
所陈已悉闻，今正排检其因。俟修毕，当即告君。
```

### 6. 产品更新公告

输入：

```text
帮我写一个很短的功能更新说明：我们新增了批量导出功能，支持 CSV 和 JSON。
```

输出：

```text
今增批量导出之能，支持 `CSV` 与 `JSON`。
```

### 7. 长句压缩

输入：

```text
请把这段话压缩成很短的话：
这个功能上线以后，注册速度明显变快了，但是客服工单没有减少。我们后来发现，问题不在注册流程，而在注册完成后的权限说明太复杂。
```

输出：

```text
功能既上，注册虽速，工单未减。其病不在注册，而在权限说明过繁。
```

### 8. 混合技术模式

输入：

```text
请解释一下为什么要把 API gateway 放在服务前面。
```

输出：

```text
置 `API gateway` 于诸服务之前，所以统鉴权、限流、路由与审计也；由是后端可专司其职。
```

### 9. 同一内容，不同力度

原始需求：

```text
请简要说明：这个方案可以做，但要先确认数据质量、接口稳定性和上线窗口。
```

偏稳妥版：

```text
此方案可行，然须先核数据质量、接口稳定与上线之期。
```

更古更峻版：

```text
事可为，然先当核数据、稳接口、定窗口。
```

## Development

本仓库附带一个无第三方依赖之校验脚本：

```bash
python3 scripts/validate_skill.py
```

校验项包括：

- `SKILL.md` 是否存在且含合法 frontmatter
- `agents/openai.yaml` 是否存在且含基础 UI 字段
- Skill 内部 Markdown 相对链接是否可解析

GitHub Actions 亦会于推送与 Pull Request 时自动执行校验。

## License

本仓库采用 MIT License。详见 [`LICENSE`](LICENSE)。
