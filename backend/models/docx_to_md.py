from docx import Document
from docx.oxml.ns import qn

class DocxToMarkdownConverter:
    # 色スタイルを適用
    @classmethod
    def apply_color_style(cls, text: str, color) -> str:
        if color and str(color).upper() == "E97132":
            return f'<span class="orange">{text}</span>'
        return text

    # 太字スタイルを適用
    @classmethod
    def apply_bold_style(cls, text: str, is_bold: bool) -> str:
        return f'**{text}**' if is_bold else text

    # スタイルを合成（太字 → 色の順で適用）
    @classmethod
    def extract_styled_text(cls, run) -> str:
        raw_text = run.text
        bolded = cls.apply_bold_style(raw_text, run.bold)
        colored = cls.apply_color_style(bolded, run.font.color.rgb)
        return colored


    # スタイルID
    @classmethod
    def get_style_id(cls, paragraph) -> str:
        pPr = paragraph._p.find(qn('w:pPr'))
        if pPr is not None:
            pStyle = pPr.find(qn('w:pStyle'))
            if pStyle is not None:
                return pStyle.get(qn('w:val'))
        return None

    @classmethod
    def map_id_to_marker(cls, id_str: str) -> int:
        return {
            "a": 0,
            "a0": 0,
            "1": 1,
            "a1": 2,
            "20": 3,
            "3": 4
        }.get(id_str, cls._last)
    
    @classmethod
    def symbol(cls, paragraph):
        style_id = cls.get_style_id(paragraph)
        return {
            "a": 'Ⅰ',
            "a0": '1',
            "1": '(1)',
            "a1": '①',
            "20": '○',
            "3": '■'
        }.get(style_id, '')

    @classmethod
    def get_list_level(cls, paragraph) -> int:
        style_id = cls.get_style_id(paragraph)
        cls._last = style_id
        return cls.map_id_to_marker(style_id)

    @classmethod
    def convert(cls, docx_path: str, output_path: str):
        doc = Document(docx_path)
        lines = []
        cls._last = 0

        for para in doc.paragraphs:
            line = "".join(cls.extract_styled_text(run) for run in para.runs)
            indent_level = cls.get_list_level(para)
            lines.append("    " * indent_level + cls.symbol(para) + line.strip())

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

DocxToMarkdownConverter.convert('./data/Category3/example3.docx', './data/Category3/example3.md')