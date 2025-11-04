import unittest
from src.block import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_code(self):
        code_block = "```\nprint('hello')\nprint('world')\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)

    def test_quote(self):
        quote_block = "> This is a quote\n> This is another line"
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)

    def test_unordered_list(self):
        list_block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(list_block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        list_block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(list_block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Multiple words\nwith new lines"), BlockType.PARAGRAPH)


if __name__ == '__main__':
    unittest.main()