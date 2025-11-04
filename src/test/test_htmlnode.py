import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "hello world",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "Hello, world!", {"href": "https://www.google.com"})
        node3 = LeafNode(
            "p",
            "Hello, world!",
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(
            node2.to_html(), '<p href="https://www.google.com">Hello, world!</p>'
        )
        self.assertEqual(
            node3.to_html(),
            '<p href="https://www.google.com" target="_blank">Hello, world!</p>',
        )

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
