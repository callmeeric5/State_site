from typing import Optional


class HTMLNode:
    def __init__(
        self, tag=None, value=None, children=None, props: Optional[dict] = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self) -> str:
        return f"HTMLNode = ({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props: Optional[dict] = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        # if self.props is None:
        #     return  f"<{self.tag}>{self.value}</{self.tag}>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag=None,
        children: list | None = None,
        props: dict | None = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError

        if self.children is None:
            raise ValueError("need a child node")

        html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
