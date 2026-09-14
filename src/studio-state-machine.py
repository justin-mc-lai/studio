# Studio State Machine - ponytail: dict, not LangGraph dep (yet)
# When hand-written state-model.md needs enforcement, swap to LangGraph

STATES = {
    "demand": ["inbox", "routed", "doing", "done"],
    "project": ["green", "yellow", "red"]
}
TRANSITIONS = {
    ("inbox", "routed"), ("routed", "doing"), ("doing", "done"), ("doing", "inbox"),
    ("green", "yellow"), ("yellow", "red"), ("yellow", "green"), ("red", "green")
}
TERMINAL = {"done", "red"}  # no outgoing is ok

def can_transit(frm, to):
    return (frm, to) in TRANSITIONS

# ponytail: 5 lines, LangGraph would be 50 + dep. Swap when Studio trace > file.
# LangGraph version (when needed):
# from langgraph.graph import StateGraph
# g = StateGraph(dict); g.add_edge("inbox","routed") ...
