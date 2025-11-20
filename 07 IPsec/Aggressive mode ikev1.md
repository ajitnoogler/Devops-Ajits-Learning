
### Main Mode: 6 messages, identities protected until encrypted.

### Aggressive Mode: 3 messages, combines Main Mode messages:

AM1 = MM1 + MM3

AM2 = MM2 + MM4 + MM6

AM3 = MM5

| Aggressive Mode | Combines MM Msgs | Payloads / Parameters Sent                                                                                                                                                                                             |
| --------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AM1**         | MM1 + MM3        | - SA proposal (encryption, hashing, DH groups)  <br> - KE (Diffie-Hellman public value)  <br> - Ni (Initiator Nonce)  <br> - IDi (Initiator ID, e.g., IP/hostname)                                                     |
| **AM2**         | MM2 + MM4 + MM6  | - SA acceptance (agreed proposal)  <br> - KE (Responder DH public value)  <br> - Nr (Responder Nonce)  <br> - IDr (Responder ID)  <br> - AUTH (Responder authentication)  <br> - CERT (optional Responder certificate) |
| **AM3**         | MM5              | - AUTH (Initiator authentication)  <br> - CERT (optional Initiator certificate)                                                                                                                                        |

### Auth:

| Auth Method                       | AUTH Payload (AM3) Details                                                                                                                                      |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pre-Shared Key (PSK)**          | HASH of: <br> - Initiator’s ID (IDi) <br> - Nonces (Ni, Nr) <br> - Diffie-Hellman shared secret <br> - Possibly some SA parameters                              |
| **Digital Signature (RSA / DSA)** | Signature over: <br> - Initiator’s ID (IDi) <br> - Nonces (Ni, Nr) <br> - Diffie-Hellman shared secret or derived key <br> - Optional CERT to convey public key |
| **RSA Encrypted Nonce**           | Encrypts a nonce (Ni) with Responder’s public key to prove identity                                                                                             |


<img width="501" height="596" alt="image" src="https://github.com/user-attachments/assets/a1ca1c0d-aacd-4a92-bdd5-73aad3f43d89" />

#### Aggressive Mode:

<img width="686" height="211" alt="image" src="https://github.com/user-attachments/assets/45ad8cb9-bee3-4190-8735-13ff6c6c3cc0" />

#### Main Mode:

<img width="686" height="372" alt="image" src="https://github.com/user-attachments/assets/a4e95fd0-887d-4700-be02-99de6e178e7b" />
