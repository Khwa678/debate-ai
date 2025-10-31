# dagviz.py
from graphviz import Digraph

def build_dag(path="debate_dag"):
    g = Digraph("DebateDAG", format="svg")
    g.attr(rankdir="LR")
    nodes = [
        ("UserInput", "User Input"),
        ("Scientist", "Agent A (Scientist)"),
        ("MemoryA", "Memory Node (A)"),
        ("Philosopher", "Agent B (Philosopher)"),
        ("MemoryB", "Memory Node (B)"),
        ("Judge", "Judge Node")
    ]
    for nid, label in nodes:
        g.node(nid, label)
    g.edges([
        ("UserInput", "Scientist"),
        ("Scientist", "MemoryA"),
        ("MemoryA", "Philosopher"),
        ("Philosopher", "MemoryB"),
        ("MemoryB", "Judge")
    ])
    out = g.render(path, cleanup=True)
    print("DAG saved to", out)
    return out

if __name__ == "__main__":
    build_dag()
