# HTMLNode class should have 4 data members in the constructor.
# tag, string representing the HTML tag name. value, a string representing the value of the HTML tag.
# children a list of HTMLNode objects representing the children of this node
# props a dictionary of key-value pairs representing the attributes of the HTML tag.
# For example a (<a> tag) might have {"href": "https://www.google.com"}
# Every data member should be optional and default to None.
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
