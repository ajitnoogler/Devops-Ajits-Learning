### 🔐 IKEv1 (Main Mode + Quick Mode)

```text
Initiator → Responder: MM1 → SA Proposal
Responder → Initiator: MM2 → SA Selection
Initiator → Responder: MM3 → DH Key
Responder → Initiator: MM4 → DH Key + Nonce
Initiator → Responder: MM5 → Auth, ID
Responder → Initiator: MM6 → Auth, ID
    ←— IKE SA (Phase 1) established —→

Initiator → Responder: QM1 → Quick SA Proposal + Nonce
Responder → Initiator: QM2 → Quick SA Selection + Nonce
Initiator → Responder: QM3 → AUTH + optional PFS/DH
    ←— Child SA (Phase 2) established —→
```


# Main Mode: 6 messages establish a secure, authenticated channel (SA) between peers—messages 1–4 negotiate algorithms and keys; 5–6 handle authentication
# Quick Mode: 3 messages under the protection of Phase 1’s SA to set up IPsec—encrypts user data traffic 
