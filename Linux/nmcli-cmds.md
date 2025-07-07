Here are **sample outputs** of commonly used `nmcli` commands for real-world Linux environments — useful for documentation, scripting, or training.

---

## 🔍 `nmcli general status`

```bash
$ nmcli general status
```

```text
STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled
```

---

## 📡 `nmcli device`

```bash
$ nmcli device
```

```text
DEVICE      TYPE      STATE      CONNECTION         
eth0        ethernet  connected  static-lan         
lo          loopback  unmanaged  --                 
wlan0       wifi      disconnected  --              
```

---

## 🌐 `nmcli connection show`

```bash
$ nmcli connection show
```

```text
NAME             UUID                                  TYPE      DEVICE 
static-lan       d9fb27a1-cab1-4c0e-bf61-5877616b47d4  ethernet  eth0   
MyWiFiHome       a4fdc1b7-b2e6-4eb7-89e2-b8c998621ac1  wifi      --     
```

---

## 📶 `nmcli device wifi list`

```bash
$ nmcli device wifi list
```

```text
IN-USE  SSID             MODE   CHAN  RATE        SIGNAL  BARS  SECURITY  
        MyWiFiHome       Infra  6     54 Mbit/s   78      ▂▄▆_  WPA2      
        PublicWiFi       Infra  1     54 Mbit/s   45      ▂▄__  WPA1 WPA2 
        HiddenNetwork     Infra 11     54 Mbit/s   32      ▂___  WPA2      
```

---

## 🧾 `nmcli device show eth0`

```bash
$ nmcli device show eth0
```

```text
GENERAL.DEVICE:                         eth0
GENERAL.TYPE:                           ethernet
GENERAL.HWADDR:                         52:54:00:12:34:56
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
IP4.ADDRESS[1]:                         192.168.1.100/24
IP4.GATEWAY:                            192.168.1.1
IP4.DNS[1]:                             8.8.8.8
IP4.DNS[2]:                             1.1.1.1
```

---

## 🔁 `nmcli connection up static-lan`

```bash
$ sudo nmcli connection up static-lan
```

```text
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/5)
```

---

## ❌ `nmcli connection delete static-lan`

```bash
$ sudo nmcli connection delete static-lan
```

```text
Connection 'static-lan' (d9fb27a1-cab1-4c0e-bf61-5877616b47d4) successfully deleted.
```

---

Would you like me to generate these into a `.md` or `.txt` file with explanation blocks for a lab guide or training material?
