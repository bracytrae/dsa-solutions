# each node stores a page URL and references to the previous and next nodes

class ListNode:
    def __init__(self, url, prev=None, next=None):

        self.url = url
        self.prev = prev
        self.next = next

"""
    node in a doubly linked list

    page
    ↓
    [ prev: None | url: "google.com" | next: None ]
"""

class BrowserHistory:

    """
        initialize the list with the homepage as the current node

        [Google]
            ^
        self.current
    """

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    """
        if you're on Google and visit Youtube

        Google <- YouTube
        ^         ^
        current  new_page
    """
    def visit(self, url: str) -> None:

        # create a new node whose previous reference points to the current node
        new_page = ListNode(url, prev=self.current)

        # link the current node to the new node, discarding any forward history
        self.current.next = new_page

        # update the current node
        self.current = new_page

    # traverse backward through previous references, stopping at the head
    def back(self, steps: int) -> str:

        while self.current.prev is not None and steps > 0:
            self.current = self.current.prev
            steps -= 1

        return self.current.url

    # traverse forward through next references, stopping at the tail
    def forward(self, steps: int) -> str:

        while self.current.next is not None and steps > 0:
            self.current = self.current.next
            steps -= 1

        return self.current.url
