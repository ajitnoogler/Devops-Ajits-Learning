[Initiator]                                            [Responder]
     |                                                       |
     | ----> IKE_SA_INIT -----------------------------------> |
     |        - SA proposal (cipher suites, DH group)         |
     |        - KEi (DH public key)                           |
     |        - Ni (Nonce)                                    |
     |                                                       |
     | <---- IKE_SA_INIT ------------------------------------ |
     |        - Chosen proposal                               |
     |        - KEr (DH public key)                           |
     |        - Nr (Nonce)                                    |
     |        - Optional cookie (for DoS protection)          |
     |                                                       |
     | ----> IKE_AUTH --------------------------------------> |
     |        - IDi (Initiator identity)                      |
     |        - AUTH (based on PSK or certs)                  |
     |        - SA for CHILD_SA                               |
     |        - TSi (Traffic Selector - source)               |
     |        - TSr (Traffic Selector - destination)          |
     |                                                       |
     | <---- IKE_AUTH --------------------------------------- |
     |        - IDr (Responder identity)                      |
     |        - AUTH                                          |
     |        - CHILD_SA accepted                             |
     |        - TSi / TSr                                     |
     |                                                       |
     | ✅ IKE SA + CHILD_SA established                       |
     | ✅ Encrypted IPSec traffic begins (ESP/AH)             |
