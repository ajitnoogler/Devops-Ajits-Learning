Comparison: IKEv1 vs. IKEv2

| Feature              | IKEv1                                  | IKEv2                                                                                                                                                                            |
| -------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Phases               | Phase 1 (Main/Aggressive) + Quick Mode | IKE\_SA\_INIT + IKE\_AUTH (Child SAs)                                                                                                                                            |
| Message Count        | 9+ (6 + 3) or 6+3 in Aggressive mode   | Minimum 4 messages                                                                                                                                                               |
| Authentication       | Separate in Phase 1 and 2              | Combined in IKE\_AUTH (Phase 2)                                                                                                                                                  |
| Built-in Protections | Requires NAT-T workaround              | NAT-T, MOBIKE, keepalives built-in 
| Efficiency           | More round trips                       | Faster, simpler negotiation                                                                                                                                                      |

🎯 Summary

    IKEv1: multi-step, distinct phases (6 + 3 messages) — traditional but more verbose.
    IKEv2: streamlined into two compact exchanges (≥4 messages), combining SA negotiation and authentication.

