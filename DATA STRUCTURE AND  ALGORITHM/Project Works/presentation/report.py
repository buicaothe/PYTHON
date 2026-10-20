"""Generate the project presentation report as a self-contained HTML file.

Run:  python presentation/report.py
Output: presentation/report.html  (open in any browser)
"""

from __future__ import annotations

import json
import os

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(_PROJECT_ROOT, "presentation", "report.html")
CONFIG_PATH = os.path.join(_PROJECT_ROOT, "project_config.json")


def load_project_config(path: str = CONFIG_PATH) -> dict:
    """Read the project config JSON (group + team members).

    The config lives next to the project root so anyone who pulls the whole
    repository can build without needing environment variables or local secrets.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def team_members() -> list[str]:
    """Return the ordered list of team member full names from the config."""
    config = load_project_config()
    members = config.get("team", [])
    return [
        m.get("full_name", str(m)) if isinstance(m, dict) else str(m)
        for m in members
    ]


# ---------------------------------------------------------------------------
# Slide content
# ---------------------------------------------------------------------------

SLIDES: list[dict[str, str]] = [
    {
        "title": "Implementation of Essential Data Structures & Algorithms in Python",
        "subtitle": "DSA Project — Trees, Hash Tables, Sorting, Searching & More",
        "body": """
        <p><strong>Presented by:</strong> DSA Project Group</p>
        <p><strong>Team members:</strong> __TEAM_MEMBERS__</p>
        <p><strong>Language:</strong> Python 3 (standard library only)</p>
        <p>A comprehensive, from-scratch implementation of fundamental data structures and algorithms, demonstrated through real-world scenarios.</p>
        """,
        "kind": "title",
    },
    {
        "title": "Project Overview & Objectives",
        "body": """
        <ul>
          <li>Implement core data structures: arrays, linked lists, stacks, queues, trees (binary, BST, balanced AVL), and hash tables.</li>
          <li>Implement core algorithms: bubble/insertion/merge sort, linear/binary search, in-order/pre-order/post-order traversal.</li>
          <li>Analyze time &amp; space complexity of every algorithm.</li>
          <li>Validate with test cases covering scenarios and edge cases.</li>
          <li>Compare sorting and traversal performance across input sizes and types.</li>
          <li>Explore hash functions and collision-resolution techniques.</li>
        </ul>
        <p><em>All structures demonstrated through scenario-based programs.</em></p>
        """,
        "kind": "content",
    },
    {
        "title": "Data Structures Implemented",
        "body": """
        <table>
          <tr><th>Structure</th><th>Key Operations</th><th>Complexity Highlight</th></tr>
          <tr><td>DynamicArray</td><td>append, insert, delete, get, set</td><td>append amortized O(1)</td></tr>
          <tr><td>SinglyLinkedList</td><td>insert_head, append, insert_at, delete, search, reverse</td><td>head/tail O(1); indexed O(n)</td></tr>
          <tr><td>StackArray / StackLinked</td><td>push, pop, peek</td><td>O(1)</td></tr>
          <tr><td>QueueLinked</td><td>enqueue, dequeue, peek</td><td>O(1)</td></tr>
          <tr><td>BinaryTree</td><td>level-order insert, height, size</td><td>insert O(n)</td></tr>
          <tr><td>BinarySearchTree</td><td>insert, search, delete, min, max</td><td>O(h); O(log n) balanced</td></tr>
          <tr><td>AVLTree</td><td>insert, search, delete, is_balanced</td><td>O(log n) guaranteed</td></tr>
          <tr><td>ChainingHashTable</td><td>put, get, remove</td><td>O(1) amortized average</td></tr>
          <tr><td>OpenAddressingHashTable</td><td>put, get, remove</td><td>O(1) amortized average</td></tr>
        </table>
        """,
        "kind": "content",
    },
    {
        "title": "Algorithms Implemented",
        "body": """
        <h3>Sorting</h3>
        <ul>
          <li><strong>Bubble Sort</strong> — O(n²), stable, early-exit on sorted input.</li>
          <li><strong>Insertion Sort</strong> — O(n²), stable, few swaps on nearly-sorted data.</li>
          <li><strong>Merge Sort</strong> — O(n log n) all cases, stable.</li>
        </ul>
        <h3>Searching</h3>
        <ul>
          <li><strong>Linear Search</strong> — O(n), works on any list.</li>
          <li><strong>Binary Search</strong> — O(log n), iterative and recursive variants (requires sorted input).</li>
        </ul>
        <h3>Tree Traversals</h3>
        <ul>
          <li>In-order, Pre-order, Post-order — recursive and explicit-stack iterative.</li>
          <li>Level-order (breadth-first) using the project's own QueueLinked.</li>
        </ul>
        <p>All sorting/searching functions accept an optional <code>OpStats</code> counter for comparisons and swaps.</p>
        """,
        "kind": "content",
    },
    {
        "title": "Hashing: Functions & Collision Resolution",
        "body": """
        <h3>Hash functions (from scratch)</h3>
        <ul>
          <li><strong>division_hash</strong> — key % table_size (integer keys).</li>
          <li><strong>polynomial_hash</strong> — Horner's method, base 31 (string keys).</li>
          <li><strong>djb2_hash</strong> — classic djb2 (string keys).</li>
        </ul>
        <h3>Collision resolution</h3>
        <ul>
          <li><strong>Separate chaining</strong> — plain-list buckets, grow-only resizing at load factor 0.75.</li>
          <li><strong>Open addressing</strong> — linear and quadratic (triangular) probing, tombstone deletions.</li>
        </ul>
        <p>Both tables track collision count and resize count, and are demonstrated against integer IDs and string names.</p>
        """,
        "kind": "content",
    },
    {
        "title": "Scenarios: Using Structures in Practice",
        "body": """
        <table>
          <tr><th>Scenario</th><th>Structure</th><th>Real-world framing</th></tr>
          <tr><td>dynamic_array_grades</td><td>DynamicArray</td><td>student grade book</td></tr>
          <tr><td>linked_list_playlist</td><td>SinglyLinkedList</td><td>music playlist</td></tr>
          <tr><td>stack_undo_redo</td><td>StackArray</td><td>text-editor undo/redo + bracket matching</td></tr>
          <tr><td>queue_scheduling</td><td>QueueLinked</td><td>FIFO print-job scheduler</td></tr>
          <tr><td>binary_tree_expr</td><td>BinaryTree</td><td>arithmetic expression tree evaluation</td></tr>
          <tr><td>bst_student_records</td><td>BinarySearchTree</td><td>student record lookup by ID</td></tr>
          <tr><td>avl_sorted_ids</td><td>AVLTree vs BST</td><td>sorted-input height: AVL ~4 vs BST 19</td></tr>
          <tr><td>hash_contacts</td><td>both hash tables</td><td>contact directory, word frequency, collision demo</td></tr>
          <tr><td>searching_inventory</td><td>linear + binary search</td><td>product inventory lookup</td></tr>
          <tr><td>sorting_students</td><td>all three sorts</td><td>student grade sorting with OpStats</td></tr>
        </table>
        <p>Run all with: <code>python main.py</code> or any scenario directly.</p>
        """,
        "kind": "content",
    },
    {
        "title": "Key Finding: Balanced Trees Matter",
        "body": """
        <p>Inserting IDs 1&ndash;20 in sorted order:</p>
        <ul>
          <li><strong>BST height: 19</strong> &mdash; degenerates into a linked list. Search becomes O(n).</li>
          <li><strong>AVL height: 4</strong> &mdash; self-balancing keeps search O(log n).</li>
        </ul>
        <div style="font-family: monospace; font-size: 13px; line-height: 1.4;">
          BST (sorted input):<br>
          1<br>
          <span style="color:#888;">└──</span> 2<br>
          <span style="color:#888;">   └──</span> 3<br>
          <span style="color:#888;">      ...</span><br>
          <span style="color:#888;">         └──</span> 20   (height 19)<br><br>
          AVL (same input):<br>
          balanced tree, height 4
        </div>
        <p><strong>Lesson:</strong> Always prefer a balanced tree (AVL) when input order cannot be controlled.</p>
        """,
        "kind": "content",
    },
    {
        "title": "Performance: Sorting Algorithms Compared",
        "body": """
        <p>Wall-clock time across input sizes and distributions (random, sorted, reverse, duplicates).</p>
        <ul>
          <li><strong>Merge sort</strong> &mdash; consistently fastest for medium/large inputs (O(n log n)), unaffected by distribution.</li>
          <li><strong>Insertion sort</strong> &mdash; competitive on tiny or nearly-sorted inputs; O(n²) otherwise.</li>
          <li><strong>Bubble sort</strong> &mdash; simplest but slowest in practice; O(n²) with more swaps than insertion sort.</li>
        </ul>
        <p><strong>Recommendation:</strong> Use merge sort for general-purpose sorting; insertion sort only for tiny/nearly-sorted data.</p>
        """,
        "kind": "content",
    },
    {
        "title": "Performance: Tree Traversals",
        "body": """
        <p>Recursive vs explicit-stack iterative traversals (in-order, pre-order, post-order).</p>
        <ul>
          <li>Both produce identical sequences; both run in O(n) time.</li>
          <li>Recursive: O(h) call-stack space. Iterative: O(h) explicit-stack space.</li>
          <li>On balanced trees h = O(log n); on skewed BSTs h = O(n), so recursion depth can become a practical limit.</li>
        </ul>
        <p><strong>Recommendation:</strong> Choose recursive for clarity; iterative when stack depth is a concern.</p>
        """,
        "kind": "content",
    },
    {
        "title": "Testing & Validation",
        "body": """
        <ul>
          <li>Unit tests for every structure and algorithm (<code>tests/test_*.py</code>).</li>
          <li>Edge cases: empty/single-element containers, duplicates, boundary inserts/deletes, pop/peek/get on empty (raises), missing keys, out-of-range indexes.</li>
          <li>Correctness invariants: sorting matches <code>sorted()</code>, recursive == iterative traversals, AVL stays balanced, hash-table resize preserves data.</li>
          <li>Sorting stability and input immutability verified.</li>
          <li><code>python tests/run_tests.py</code> generates <code>TEST_VALIDATION_REPORT.md</code> with pass/fail summary.</li>
        </ul>
        """,
        "kind": "content",
    },
    {
        "title": "Challenges Faced",
        "body": """
        <ul>
          <li><strong>No built-in containers:</strong> Could not use <code>dict</code>/<code>set</code> in hash tables or <code>list.sort</code> in sorting &mdash; everything built from nodes, buckets, and slots.</li>
          <li><strong>Plain-list discipline:</strong> Restricted raw <code>[None] * capacity</code> lists to backing storage only; every other structure uses its own primitives.</li>
          <li><strong>AVL rebalancing without parent pointers:</strong> Used recursive return values to propagate new subtree roots and apply rotations on the unwind.</li>
          <li><strong>Open-addressing deletions:</strong> Needed tombstone sentinels so removing a key never breaks a later probe sequence.</li>
          <li><strong>Quadratic probing coverage:</strong> Plain <code>i^2</code> probing visits only ~half the slots of a power-of-two table; switched to triangular numbers for full coverage.</li>
        </ul>
        """,
        "kind": "content",
    },
    {
        "title": "Lessons Learned",
        "body": """
        <ul>
          <li><strong>Balance is not optional:</strong> an unstructured BST degrades to O(n) on sorted input; a balanced tree guarantees O(log n).</li>
          <li><strong>Algorithm choice depends on input:</strong> insertion sort beats merge sort only on tiny/nearly-sorted data; merge sort wins generally.</li>
          <li><strong>Hash-table tuning matters:</strong> load factor, hash-function quality, and collision strategy all affect real-world performance.</li>
          <li><strong>Recursive vs iterative:</strong> same asymptotic result, but iterative avoids stack-depth limits on skewed trees.</li>
          <li><strong>Document complexity alongside code:</strong> Time/Space docstrings on every method make the analysis self-documenting.</li>
        </ul>
        """,
        "kind": "content",
    },
    {
        "title": "Project Deliverables",
        "body": """
        <table>
          <tr><th>#</th><th>Deliverable</th><th>Location</th><th>Status</th></tr>
          <tr><td>1</td><td>Python code: all data structures &amp; algorithms</td><td><code>src/dsa/</code>, <code>scenarios/</code></td><td>✅ Complete</td></tr>
          <tr><td>2</td><td>Documentation: design, functionality, usage examples</td><td><code>README.md</code>, <code>docs/DESIGN.md</code>, docstrings</td><td>✅ Complete</td></tr>
          <tr><td>3</td><td>Test cases &amp; validation report</td><td><code>tests/</code>, <code>TEST_VALIDATION_REPORT.md</code></td><td>✅ Complete</td></tr>
          <tr><td>4</td><td>Performance analysis report</td><td><code>performance/</code>, <code>PERFORMANCE_ANALYSIS_REPORT.md</code></td><td>✅ Complete</td></tr>
          <tr><td>5</td><td>Presentation slides</td><td><code>presentation/report.py</code> (+ <code>report.html</code>)</td><td>✅ Complete</td></tr>
        </table>
        """,
        "kind": "content",
    },
    {
        "title": "How to Run Everything",
        "body": """
        <table>
          <tr><th>Goal</th><th>Command</th></tr>
          <tr><td>Run all scenarios</td><td><code>python main.py</code></td></tr>
          <tr><td>Run one scenario</td><td><code>python main.py --scenario avl_sorted_ids</code></td></tr>
          <tr><td>Run tests + validation report</td><td><code>python tests/run_tests.py</code></td></tr>
          <tr><td>Run performance analysis</td><td><code>python performance/analysis.py</code></td></tr>
          <tr><td>Generate slides</td><td><code>python presentation/report.py</code></td></tr>
        </table>
        <p><strong>Requirements:</strong> Python 3.9+, standard library only.</p>
        """,
        "kind": "content",
    },
    {
        "title": "Thank You / Questions",
        "body": """
        <p><strong>Implementation of Essential Data Structures and Algorithms in Python</strong></p>
        <p>All code: <code>src/dsa/</code> &bull; Scenarios: <code>scenarios/</code> &bull; Tests: <code>tests/</code> &bull; Analysis: <code>performance/</code> &bull; Slides: <code>presentation/</code></p>
        <p>Standard library only &bull; From-scratch implementations &bull; Scenario-driven demonstrations</p>
        """,
        "kind": "content",
    },
]


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

CSS = """
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0; padding: 0; background: #f4f6f8; color: #1a1a1a;
}
.slide {
  width: 100vw; height: 100vh;
  padding: 40px 60px; background: #ffffff; border-bottom: 1px solid #e2e4e7;
  overflow-y: auto;
}
.slide h1 {
  font-size: 34px; margin: 0 0 6px 0; color: #0f62fe;
}
.slide h2 { font-size: 24px; margin: 16px 0 10px 0; color: #1a1a1a; }
.slide h3 { font-size: 21px; margin: 14px 0 8px 0; color: #0f62fe; }
.slide p { font-size: 18px; line-height: 1.6; margin: 8px 0; }
.slide ul, .slide ol { font-size: 18px; line-height: 1.7; margin: 8px 0 8px 22px; }
.slide li { font-size: 18px; margin: 4px 0; }
.slide table {
  border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 15px;
}
.slide th, .slide td {
  border: 1px solid #c9cdcf; padding: 6px 8px; text-align: left;
}
.slide th { background: #eef2f5; color: #0f62fe; }
.slide .subtitle { font-size: 22px; color: #5c6064; margin-bottom: 24px; }
.slide .kind-title { min-height: 70vh; display: flex; flex-direction: column; justify-content: center; }
.nav {
  position: fixed; bottom: 16px; left: 50%; transform: translateX(-50%);
  display: flex; gap: 8px; z-index: 10;
}
.nav button {
  background: #0f62fe; color: #fff; border: none; border-radius: 6px;
  padding: 6px 14px; font-size: 14px; cursor: pointer;
}
.nav button:hover { background: #0b53c8; }
.nav button.active { background: #17a2b8; }
.code { background: #f2f4f7; border: 1px solid #e2e4e7; border-radius: 6px;
  padding: 10px 14px; font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 15px; white-space: pre-wrap; margin: 8px 0; }
"""

JS = """
let current = 0;
const total = __TOTAL__;
function show(n) {
  current = (n + total) % total;
  document.querySelectorAll('.slide').forEach((s, i) => {
    s.style.display = i === current ? 'block' : 'none';
  });
  document.querySelectorAll('.nav button').forEach((b, i) => {
    b.className = i === current ? 'active' : '';
  });
}
document.addEventListener('DOMContentLoaded', () => {
  show(0);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ') show(current + 1);
    if (e.key === 'ArrowLeft') show(current - 1);
  });
});
"""


def slide_html(slide: dict, index: int, total: int) -> str:
    kind = slide.get("kind", "content")
    title = slide["title"]
    subtitle = slide.get("subtitle", "")
    body = slide["body"]
    body_class = "kind-title" if kind == "title" else ""
    return f"""
<section id="slide-{index}" class="slide {body_class}" style="display:{'block' if index == 0 else 'none'}">
  {'<h2 class="subtitle">' + subtitle + '</h2>' if subtitle else ''}
  <h1>{title}</h1>
  {body}
</section>
"""


def build() -> str:
    members = ", ".join(team_members())
    slides = [
        {**slide, "body": slide["body"].replace("__TEAM_MEMBERS__", members)}
        for slide in SLIDES
    ]
    total = len(slides)
    sections = "\n".join(slide_html(s, i, total) for i, s in enumerate(slides))
    nav = "\n".join(f'<button onclick="show({i})">{i + 1}</button>' for i in range(total))
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DSA Project Presentation</title>
<style>{CSS}</style>
</head>
<body>
{sections}
<div class="nav">{nav}</div>
<script>{JS.replace("__TOTAL__", str(total))}</script>
</body>
</html>
"""
    return html


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    html = build()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Presentation written to {OUTPUT_PATH} ({len(SLIDES)} slides)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
