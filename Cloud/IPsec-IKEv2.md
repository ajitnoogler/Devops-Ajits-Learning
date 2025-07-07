🔐 IKEv2 (Initial Exchanges)

IKEv2 simplifies the negotiation into two compact exchanges, typically completed in 4 messages:

Initiator → Responder: IKE_SA_INIT (SAi1, Ni, KEi)
Responder → Initiator: IKE_SA_INIT (SAr1, Nr, KEr)
    ←— IKE SA created for further exchange ——

Initiator → Responder: IKE_AUTH (IDi, AUTHi, SAi2, TSi, TSr)
Responder → Initiator: IKE_AUTH (IDr, AUTHr, SAr2, ACP, TSr)
    ←— Child SA also established —→

IKE_SA_INIT: negotiates cryptography, exchange nonces & Diffie-Hellman values—usually 2 messages

IKE_AUTH: authenticates both peers, exchanges identities, optionally sets up the first child SA (IPsec tunnel)—usually 2 messages.

Subsequent CREATE_CHILD_SA exchanges handle new or rekeyed IPsec SAs (Phase 2 equivalent).
