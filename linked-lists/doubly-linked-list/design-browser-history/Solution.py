# represents a node in the doubly linked list which also represents a web page in the browser history

class ListNode:
    def __init__(self, url, prev=None, next=None):

        self.url = url
        self.prev = prev
        self.next = next

"""
    conceptually this is what a web page looks like as a node in a doubly linked list

    page
    ↓
    [ prev: None | url: "google.com" | next: None ]
"""

class BrowserHistory:

    """
        creates the first home page and makes self.cur point to it

        [Google]
            ^
        self.cur
    """
    
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    """
        if you're on Google and visit Youtube

        Google <- YouTube
        ^         ^
        cur     new_page
    """
    def visit(self, url: str) -> None:
        
        # creates a new page that comes after the current page
        new_page = ListNode(url, prev=self.cur)

        # this points the current page to the new page
        self.cur.next = new_page

        # this moves the current page to the new page 
        self.cur = new_page

    # it allows you to traverse backward through the linked list as long as you are not at an end of a doubly linked list
    def back(self, steps: int) -> str:

        while self.cur.prev is not None and steps > 0:
            self.cur = self.cur.prev
            steps -= 1

        return self.cur.url

    # it allows you to traverse forward through the linked list as long as you are not at an end of a doubly linked list
    def forward(self, steps: int) -> str:
        
        while self.cur.next is not None and steps > 0:
            self.cur = self.cur.next
            steps -= 1

        return self.cur.url
    
