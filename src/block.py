from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")
    
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(re.match(r"^- ", line) for line in lines):
        return BlockType.UNORDERED_LIST
    
    if is_ordered_list(lines):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH


def is_ordered_list(lines):
    for i, line in enumerate(lines, 1):
        if not re.match(rf"^{i}\. ", line):
            return False
    return True