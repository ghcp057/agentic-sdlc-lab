# Team design for issue 8 (order status history)

| Role | Owns paths | Tools | Stop rule |
| --- | --- | --- | --- |
| planner | docs/agent-state/ | read, search, edit (plan only) | hop_count 3; never approves its own plan |
| tester | tests/ | read, edit, search, execute | never changes an existing assertion |
| implementer (orders) | app/modules/orders/ | read, edit, search, execute | needs a file outside its path: stop and hand back |
| implementer (payment) | app/modules/payment/ | read, edit, search, execute | may call orders code, never edits it |
| human | alembic/, approvals | | |

Shared interface: OrderRepository.add_history(order_id, status) adds the row; the caller commits.