from pydantic_ai import Agent


class AgentTurnHandler:
    def __init__(
        self,
        *,
        agent: Agent,
        session_id: str | None = None,
        message_history: list[str] | None,
    ):
        self._agent = agent
        self._session_id = session_id
