class Solution:
    """
    Key Takeaways
    -------------
    -   Split at "/"
        -   spliting "//" will result in ""
    -   ".." means to remove the last directory
    -   "." means to THIS directory
        -   essentially just remove "." from the path
    -   Skip the following directories {".", "..", ""}
    -   Join the canonical path together and append "/" to
        the front as .join doesn't add it to the first instance

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   split: O(n)
        -   iterate through split path: O(n)
        -   if _ in set: O(1)

    Space Complexity: O(n)
        -   res stack: O(n)
        -   string concatenation: O(n)
    """
    def simplifyPath(self, path: str) -> str:
        res = []
        skips = {"..", ".", ""}
        for directory in path.split("/"):
            if res and directory == "..":
                res.pop()
            elif directory not in skips:
                res.append(directory)
        return "/" + "/".join(res)


class Solution:
    """
    Key Takeaways
    -------------
    -   Same solution as above, but no set
    -   Use if elif else condition

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   split: O(n)
        -   iterate through split path: O(n)

    Space Complexity: O(n)
        -   stack: O(n)
        -   string concatenation: O(n)
    """
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split("/"):
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "" or directory == ".":
                continue
            else:
                stack.append(directory)
        return "/" + "/".join(stack)
