
### Packet Manager YUM | Dnf

| Task           | `yum` Command         | `dnf` Command         |
| -------------- | --------------------- | --------------------- |
| Install        | `yum install nginx`   | `dnf install nginx`   |
| Remove         | `yum remove nginx`    | `dnf remove nginx`    |
| Reinstall      | `yum reinstall nginx` | `dnf reinstall nginx` |
| List installed | `yum list installed`  | `dnf list installed`  |
| Search package | `yum search nginx`    | `dnf search nginx`    |
| List available | `yum list available`  | `dnf list available`  |

---

### Linux Service Mangement:

| Task                  | Command                               |
| --------------------- | ------------------------------------- |
| Start service         | `systemctl start <service>`           |
| Stop service          | `systemctl stop <service>`            |
| Restart service       | `systemctl restart <service>`         |
| Reload config         | `systemctl reload <service>`          |
| Enable on boot        | `systemctl enable <service>`          |
| Disable on boot       | `systemctl disable <service>`         |
| Check status          | `systemctl status <service>`          |
| Is service active?    | `systemctl is-active <service>`       |
| Is service enabled?   | `systemctl is-enabled <service>`      |
| List running services | `systemctl list-units --type=service` |
