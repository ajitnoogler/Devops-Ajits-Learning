Here are each of the alternate zombie‑spotting commands again—this time with simulated sample outputs you might see on a typical Linux host:

---

### 1. `ps -eo` + `awk`

```bash
ps -eo pid,ppid,stat,cmd | awk '$3 ~ /^Z/ { print "Zombie PID="$1", PPID="$2", CMD="$4 }'
```
======================================================================================================

```
Zombie PID=3245, PPID=3120, CMD=bash
Zombie PID=7890, PPID=4567, CMD=python3
```

---

### 2. `ps -el` + field filtering

```bash
ps -el | awk '$2=="Z" { print "Zombie PID="$4", PPID="$5", CMD="$14 }'
```

```
Zombie PID=3245, PPID=3120, CMD=bash
Zombie PID=7890, PPID=4567, CMD=python3
```

======================================================================================================

### 3. `pgrep` state‑matching

```bash
pgrep -l -x Z
```

```
3245 bash
7890 python3
```
> *Note: only works if your version of `pgrep` supports exact state matching (`-x Z`).*

======================================================================================================

### 4. `top` in batch mode

```bash
top -b -n 1 | awk '$2=="Z" { print $1, $2, $9, $12 }'
```


```
 3245 Z  0.0   bash
 7890 Z  0.0   python3
```

======================================================================================================

### 5. `ps` + `grep` on the STAT column

```bash
ps -eo pid,stat,cmd | grep '^ *[0-9]\+ Z'
```

```
 3245 Z    /bin/bash
 7890 Z    /usr/bin/python3
```

======================================================================================================

---

Use whichever fits best into your scripts or one‑off checks—each will reliably surface any `<defunct>` processes on your system.
