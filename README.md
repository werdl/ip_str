## ip_str
- A Python library and JSON endpoint that converts IP addresses to a list of nouns
- They are easier to remember!

### For example...
`192.0.2.234`

aka 

`gas.zero.home.mike`


### Even IPv6!
`2001:db8:85a3:8d3:1319:8a2e:370:7348`

alias 

`ausbruch:malchus:schoenes:ano:delay:loaf:hief:cuadro`

---
### Python API

```py
import ipstr

str_out=ip_str.ip_str("192.0.2.234") # gas.zero.home.mike

myip=ip_str.str_ip(str_out) # 192.0.2.234

```
---
### JSON API

### /gen/\<ip>
### `/gen/192.0.2.234`
```json
"gas.zero.home.mike"
```
---
### /ip/\<str>
### `/ip/gas.zero.home.mike`
```json
"192.0.2.234"
```