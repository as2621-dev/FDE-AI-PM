# Glossary

Every term the course introduces, defined once. If you hit a word in a day and it
isn't explained there, it's because an earlier day owned it — look here.

**How this file grows:** each day's §9 Vocabulary table gets merged in here by the
day-agent that wrote it, alphabetically, with a link back to the day that taught it.
Don't redefine a term that's already here; link to it.

**Column meaning:**
- **Term** — what you'll hear in an interview
- **Plain definition** — one sentence, no jargon
- **Why an FDE cares** — the reason it comes up in a customer conversation

---

## Terms that span the whole course

These belong to no single day, so they live here from the start.

| Term | Plain definition | Why an FDE cares |
|---|---|---|
| **FDE (Forward Deployed Engineer)** | An engineer who works inside a customer's operation, finds where time and money leak, and builds the software that fixes it — then feeds what they learned back into the product. | It's the job you're interviewing for. The role is half consultant, half engineer, and the interview tests both halves. |
| **Applied AI Engineer** | The same role under a different name, common at Anthropic and other labs. | Job titles for this role are unstandardised — also FDSE, Deployment Strategist, Customer-Facing AI Engineer. Search all of them. |
| **Echo / Delta** | Palantir's internal names for the two halves of a deployment team: *Delta* wrote production code, *Echo* owned the customer domain and strategy. | Palantir invented this role. Knowing the vocabulary signals you've read the actual history, not a recruiter blog. |
| **Deployment** | Everything between "the model can do this in a demo" and "the customer's staff rely on it daily." | The entire premise of the FDE role: every company can buy the same frontier intelligence, so the advantage moves to deployment. |
| **Last mile** | The gap between a general capability and one specific customer's messy reality. | It's where FDEs live. Nobody gets paid for the first 90%. |
| **Vertical slice** | One thin, complete path through a system — end to end, however narrow — rather than one layer built out fully. | It's how you scope a pilot that proves something in week two instead of week twelve. |
| **Golden dataset** | A small set of real cases with hand-written correct answers, used to measure whether the system is improving. | Taught properly on [Day 17](day-17-golden-dataset/). Listed here because it recurs from Day 16 onward. |

---

## A–Z

*Populated as each day is written. Days 1–30 append their §9 tables here.*

| Term | Plain definition | Why an FDE cares |
|---|---|---|
| **Agent** | A system where the model directs its own process and tool use, deciding at run time how to accomplish the task. | Deciding *where* this is warranted is the judgment call the role is hired for. · [Day 1](day-01-agent-loop/) |
| **Agent loop** | The repeating cycle: assemble the prompt, call the model, parse it, act, feed the result back. | You'll be asked to draw it. Which stations are yours is where every control lives. · [Day 1](day-01-agent-loop/) |
| **Agentic system** | Anthropic's umbrella term for anything orchestrating a model with tools and data — workflows and agents both. | Lets you stop arguing about the word "agent" and describe the system instead. · [Day 1](day-01-agent-loop/) |
| **API** | The published doorway one program uses to ask another for something over the network. | Every cost, latency and failure figure you'll quote is measured per API call. · [Day 1](day-01-agent-loop/) |
| **Augmented LLM** | Anthropic's name for the basic building block: a model enhanced with retrieval, tools and memory. | All five workflow patterns are made of this one block, which stops you over-designing. · [Day 1](day-01-agent-loop/) |
| **Benchmark** | A fixed set of tasks with known right answers, run by everyone so methods compare on the same footing. | Vendor claims are benchmark claims; knowing what one measures is how you read a pitch deck. · [Day 1](day-01-agent-loop/) |
| **Chain-of-thought prompting** | Having the model write its reasoning step by step before answering, with no actions and no access to the world. | The baseline ReAct is measured against — the other half of every benchmark number you might quote. · [Day 1](day-01-agent-loop/) |
| **Context window** | The fixed amount of text a model can consider in one pass. | The second ceiling on a loop, alongside the step cap — the lower one wins. Day 4 owns it properly, including what happens to accuracy before you reach the limit. · [Day 1](day-01-agent-loop/) |
| **Function** | A named block of your code that takes inputs and returns a result. | What actually runs when "the agent does something": your code, your credentials, your consequences. · [Day 1](day-01-agent-loop/) |
| **Ground truth** | The real result returned by the environment at each step, as opposed to the model's belief about what happened. | The difference between a feedback loop and a machine narrating a plausible story. · [Day 1](day-01-agent-loop/) |
| **Hallucination** | A model stating something fluent, specific and false — an invented citation, figure or event. | What a customer means by "can I trust it?" Grounding is the defence, and it costs reasoning flexibility. · [Day 1](day-01-agent-loop/) |
| **Inference** | One round trip to the model: send a prompt, get generated text back. The model keeps no state between calls. | The unit you're billed for; a ten-step run is ten calls, each prompt longer than the last. · [Day 1](day-01-agent-loop/) |
| **LLM (large language model)** | A very large statistical model of text that, given a block of text, predicts what text comes next. | Everyone buys it identically, so the model itself is never your differentiator. · [Day 1](day-01-agent-loop/) |
| **Max-step cap** | A hard limit on how many times the loop may run, enforced by your code regardless of what the model wants. | Bounds cost, latency and blast radius — not quality. Be ready to justify the number. · [Day 1](day-01-agent-loop/) |
| **Prompt** | The complete text sent on one request: instructions, available actions, and the history so far. | No hidden channel: if it behaved oddly the answer is in the prompt, so you must be able to reconstruct it. · [Day 1](day-01-agent-loop/) |
| **Reasoning trace** | Text the model writes to itself before acting, changing nothing in the world. ReAct added it to the action space. | Why you can read a transcript and see what the agent thought it was doing. · [Day 1](day-01-agent-loop/) |
| **Stopping condition** | Any rule that ends the loop: the model declaring completion, the cap firing, or an external interrupt. | Treating "ran out of steps" as success is a common silent failure. · [Day 1](day-01-agent-loop/) |
| **Temperature** | The parameter controlling how much randomness the model uses when choosing each next token. Zero is the least random setting available. | Even at zero, output is not reproducible — which reshapes how you test and what you promise. · [Day 1](day-01-agent-loop/) |
| **Token** | The unit text is chopped into before a model reads it — roughly 4 characters or 0.75 words of English. Priced separately as **input** (what you send) and **output** (what the model writes), output costing several times more. | Cost, latency and how much the model can see are all denominated in tokens. · [Day 1](day-01-agent-loop/) |
| **Tool** | One named operation you make available to the model, e.g. look up an invoice. Called an *action* in this day's prose. | The model's entire vocabulary for affecting anything. Day 2 is about designing them. · [Day 1](day-01-agent-loop/) |
| **Transcript** | The running list of a single run: the goal, what the model said each pass, what each action returned. | The agent's memory, and your only record of what it thought it was doing. · [Day 1](day-01-agent-loop/) |
| **Workflow** | A system where the model and its tools are orchestrated through predefined code paths — you chose the sequence at build time. | The right answer more often than the customer expects; recommending it is what makes you credible rather than a vendor. · [Day 1](day-01-agent-loop/) |
