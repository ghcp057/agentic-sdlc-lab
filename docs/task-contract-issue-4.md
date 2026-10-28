**Goal:** Add POST /payment/refund/{order_id} to refund a PAID invoice and cancel both the invoice and the order in one atomic action.
**Context:** Payment service already handles invoice payment and order transitions; OrderStateMachine allows FULFILLED -> CANCELLED and invoice refunds must respect paid-only logic.
**In scope:** Endpoint validation, invoice lookup by order ID, paid-only refund checks, invoice/order cancellation, transaction safety, and API contract.
**Out of scope:** New payment provider integrations, refund amount logic, partial refunds, or unrelated order lifecycle changes.
**Acceptance:** A paid invoice for an order is refunded via the endpoint, the invoice becomes CANCELLED, the order becomes CANCELLED, and invalid/non-paid cases return clear errors.
**Stop and ask a human if:** The order has no invoice, the invoice is not PAID, or the requested state transition is not allowed by the existing order FSM.
**Reviewer:** Maintainer or payment/order domain owner.
