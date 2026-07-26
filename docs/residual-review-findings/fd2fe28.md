# Residual review findings — Day 3 (Guardrails)

Reviewed at `fd2fe28`. Three reviewers ran: accuracy + PM-readability, adversarial
interviewer, boundary + correctness. Everything they raised was either fixed in the
day or is listed below with a reason.

## Applied in the day

Accuracy and sourcing — the mitigation-count characterisation ("five of the seven")
was wrong and contradicted the day's own Tier 3, now re-sorted by whether a control
needs the attack *recognised*; "OWASP lists all of those among its scenarios" was
false for three of six items; the Claude Code working-directory boundary was
overstated by dropping "without explicit permission"; terminal periods had been added
inside quoted list items; the "two kinds of guardrails" quote merged three separate
source elements into one sentence; the IBM video "walks the list" when its own
description says it covers a subset; the Guardrails AI claim that "a validator returns
a degree, not a verdict" was backwards — their validators page documents
`PassResult`/`FailResult` against a threshold *you* pass in.

Readability — `covered entity`, `BAA`, `AICPA`, `PII`, "escape" as a verb and `base64`
were all used or needed without definition; the Python snippet had no gloss for
`async`/`await` or the type annotations, and `guardrail_agent` appeared from nowhere;
"chunks" (Day 4's word) was used in the day's own prose.

Contradictions — the day said Day 1's step cap "is not a safety number", which
reverses what Day 1 teaches three times (it bounds blast radius); now framed as a
refinement of unit rather than a reversal. The one-stream diagram's caption and `<desc>`
both contradicted what the SVG draws (the untrusted fragment is tinted, and sits last,
not between). Two arrows in `four-gates.svg` terminated 30px inside the model box.
"Fence and label retrieved content" was sold in §6's mitigation column while row 2 of
the same table declares that class of control non-enforcing.

Interview failures — the flagship §8 answer conceded the day's own opening scenario
("eight wrong payments to existing suppliers" *is* the supplier-bank-detail attack §1
asks about); the action gate was named load-bearing five times with no worked example
of a check; "remove a leg of the trifecta" had no move when all three legs are the
product; the action-budget method had no ceiling, no value cap and no per-day count;
the threshold method could not produce a first number; human approval was recommended
four times and never interrogated. §8 also rehearsed neither of the day's two knobs —
a numbers pair was restored, and Day 1 and Day 2 both rehearse theirs.

## Deferred, with reasons

**1. SOC 2 Type 1 vs Type 2 is marked `⚠️ Unverified` rather than defined.**
The distinction is real and standard, and the reader will be *told* it in a security
meeting rather than asking it. But no free AICPA page carries the definitions —
checked the SOC suite landing page, the SOC 2 topic page and the Trust Center; the
wording sits behind paid guides. Rather than launder a vendor blog into a definition,
the day states the two questions to ask and tells the reader to confirm the wording
with the customer's auditor. **Standing item:** if a citable primary definition turns
up, replace the marker with it. Day 24 owns the depth and is the natural place.

**2. The exercise tests only detectors, not bounds.** Reviewer 2 is right that both
prescribed tests are detection tests, and that the test which verifies an action
budget is an attempt to exceed it asserting the ninth write never landed. Not added:
§5 is capped at ~300 words and the day is 58 words under the gate's hard ceiling.
Fold it into Day 9 or Day 17, both of which own test construction.

**3. The gate-cost figure is qualitative, not derived.** The day says a gate on every
tool call is twenty extra calls on a twenty-pass run, and that latency binds before
money does. It does not derive a cost, because doing it properly needs a per-model
rate for the small gate model and Day 1's table is priced for a different one.
Day 19 owns cost optimisation and should carry the arithmetic.

**4. Breach notification, network-layer egress, and on-prem enforcement.** A hospital
CISO raises all three inside ten minutes. Day 24's gap-fill line is
"enterprise deployment depth", so they belong there — but Day 24 should know that
Day 3 leaves the reader with the *application-layer* framing of the outbound bound,
and a CISO will have a network-layer one.

**5. Multi-turn injection through summarised memory.** An injection that lands on turn
2, gets summarised into memory, and is acted on at turn 7 defeats an input gate.
Day 4 owns context and memory. Day 3 lists NeMo's dialog rail ("drift over many
turns") in its table and never uses it again, which is the seam Day 4 should pick up.

**6. Pilot scoping ("can we run read-only for 90 days first?").** The CISO's most
likely counter-offer, and the FDE who shapes it wins the deal. Days 22–23 own
pilot/POC scoping per the gap table.

## Found by the revised Rule A check, not by a reviewer

`d23e011` landed while this slice was in flight and added a discharge condition to
Rule A: a term is covered if the day's own §9 table defines it *or* `GLOSSARY.md`
already does from an earlier day — and it tells the writer to open `GLOSSARY.md` and
confirm rather than assume. Running that check against Day 3 caught two terms the
length reconciliation had quietly stranded, including `guardrail`, the day's own title
word. Both §9 rows are restored.

**One gap it surfaced that Day 3 cannot fix.** `pass`, in the sense of one turn of the
loop, is used by Days 1, 2 and 3 and has no `GLOSSARY.md` entry — Day 2's `Turn` row
relies on it ("which may be many passes of the loop") without it being defined
anywhere. Day 3's action-budget derivation and its "20 passes permits 20 payments"
line both lean on it. Fixing it means editing Day 1's §9 table, which is out of scope
for this slice. It should be added to `GLOSSARY.md` as a Day 1 term.
