<!-- Important: Any part of this cheatsheet is not written by me, rather by LLM -->
## Neovim

### 1. The Core Sentence Structure
**`[Count] + [Verb] + [Modifier] + [Noun]`**
*Example:* `3diw` → **3** times, **D**elete **I**nside **W**ord.

#### **A. The Verbs (Operators)**
| Verb | Action |
| :--- | :--- |
| `d` | **Delete** (Cut) |
| `c` | **Change** (Delete + Insert Mode) |
| `y` | **Yank** (Copy) |
| `v` | **Visual** (Select) |
| `>` / `<` | **Indent** / **Outdent** |
| `=` | **Auto-format** (Indentation) |

#### **B. The Modifiers (Text Objects)**
| Modifier | Logic |
| :--- | :--- |
| `i` | **Inside** (Contents only) |
| `a` | **Around** (Contents + Containers/Whitespace) |
| `f` / `t` | **Find** / **Till** (To a specific character) |

#### **C. The Nouns (Targets)**
| Noun | Target |
| :--- | :--- |
| `w` / `b` | **Word** / Backwards Word |
| `s` / `p` | **Sentence** / **Paragraph** (Code block) |
| `(` / `[` / `{` | **Brackets/Braces** (Use `b` for `(` and `B` for `{`) |
| `"` / `'` | **Quotes** |
| `t` | **Tag** (XML/HTML) |

---

### 2. The "Immediate" Actions (No Noun Required)
These are single-key or shifted-key commands that perform a combined action instantly.

#### **Entry into Insert Mode**
* `i` / `a`: Insert before / Append after cursor.
* `I` / `A`: Jump to **Start** / **End** of line and Insert.
* `o` / `O`: Open new line **Below** / **Above** and Insert.

#### **Quick Deletion / Substitution**
* `x`: Delete single character.
* `s`: **Substitute** character (Delete + Insert).
* `S`: **Substitute** entire line (Clear + Insert).
* `D` / `C`: Delete / Change from cursor to **End of Line**.

---

### 3. Navigation (The "GPS")
Stop scrolling. Jump exactly where your brain is thinking.

| Motion | Destination |
| :--- | :--- |
| `gg` | **Top** of the file. |
| `G` | **Bottom** of the file. |
| `H` / `M` / `L` | **H**igh / **M**iddle / **L**ow (of the current screen). |
| `0` / `$` | Absolute **Start** / **End** of line. |
| `^` | First **non-blank** character (The start of the code). |
| `%` | Jump to the **matching** bracket/parenthesis. |
| `*` | Search for the word under the cursor **forward**. |

---

### 4. Visual Mode (Selection Logic)
When you need to see what you're doing before you "commit" the verb.

* `v`: **Character-wise** (standard highlighting).
* `V` (Shift + v): **Line-wise** (selects entire rows—perfect for moving Python blocks).
* `Ctrl + v`: **Block-wise** (Vertical selection—great for commenting out multiple lines at once).

> **The Flow:** Press `V`, move `j` or `k` to select your logic, then hit `>` to indent or `d` to delete.

---

### 5. Essential Command Line (The ":" Commands)
* `:w` : Save (Write).
* `:q!` : Quit without saving (The "emergency exit").
* `:wq` : Save and Quit.
* `:%s/old/new/g` : **Search and Replace** everything in the file.
* `:noh` : **No Highlighting** (clears search yellow boxes).