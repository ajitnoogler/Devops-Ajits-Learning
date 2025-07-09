![image](https://github.com/user-attachments/assets/e84bdbaa-e7d0-4497-9efc-0e3d20a5faee)






















[Initiator]                                            [Responder]
     |                                                       |
     | ----> 1. IKE_SA_INIT (Main Mode) --------------------> |
     |        - Initiator Cookie                              |
     |        - Security Association Proposal (encryption,    |
     |          hash, DH group, etc.)                         |
     |                                                       |
     | <---- 2. IKE_SA_RESP --------------------------------- |
     |        - Responder Cookie                              |
     |        - Selected SA proposal                          |
     |        - DH public value                               |
     |                                                       |
     | ----> 3. Key Exchange + Nonce ------------------------>|
     |        - Initiator's DH public value                   |
     |        - Nonce                                         |
     |                                                       |
     | <---- 4. Key Exchange + Nonce ------------------------ |
     |        - Responder's nonce                             |
     |                                                       |
     | ----> 5. IDi + AUTH (Encrypted) ---------------------->|
     |        - Identity (e.g., IP or FQDN)                   |
     |        - Authentication data (PSK/RSA sig)             |
     |                                                       |
     | <---- 6. IDr + AUTH (Encrypted) ---------------------- |
     |        - Identity + Authentication data                |
     |                                                       |
     | ✅ IKE SA established (Phase 1)                        |
     |                                                       |
     | ----> Quick Mode: CHILD_SA Setup --------------------> |
     |        - New SPI, keys, transform proposals            |
     |        - Encryption keys derived from IKE SA           |
     |                                                       |
     | ✅ IPSec Tunnel Established (ESP/AH starts here)       |
