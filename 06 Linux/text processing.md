## Text Processing & Inspection

| Command | Description                      | Common Switches                                                              |
| ------- | -------------------------------- | ---------------------------------------------------------------------------- |
| `cat`   | Concatenate & print files        | `-n` (number lines), `-b` (number non‑blank)                                 |
| `less`  | View file page‑by‑page           | *(navigation keys: ↑ ↓ / q)*                                                 |
| `head`  | Show first lines                 | `-n` (number of lines)                                                       |
| `tail`  | Show last lines                  | `-n` (number of lines), `-f` (follow)                                        |
| `grep`  | Search text using patterns       | `-i` (ignore case), `-r` (recursive), `-E` (extended regex), `-n` (line num) |
| `awk`   | Field‑based text processing      | `-F` (field separator), `'{…}'`                                              |
| `sed`   | Stream editor (substitute, etc.) | `-e` (script), `-i` (in‑place)                                               |
| `cut`   | Split & extract fields           | `-d` (delimiter), `-f` (fields)                                              |
| `sort`  | Sort lines                       | `-r` (reverse), `-n` (numeric), `-k` (key)                                   |
| `uniq`  | Remove duplicate lines           | `-c` (count occurrences), `-d` (duplicates only)                             |

---

