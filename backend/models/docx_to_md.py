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
        return colored.replace("\n", "")

    @classmethod
    def convert(cls, docx_path: str, output_path: str):
        doc = Document(docx_path)
        lines = []
        cls._last = 0

        for para in doc.paragraphs:
            # boldやcolorの処理
            outline = Docx_Outline.outline(para)
            text = "".join([Docx_Outline.text_indent(run) + cls.extract_styled_text(run) for run in para.runs]).strip()
            line = outline + text
            lines += [line]

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

class Docx_Outline:
    _last_level = 0
    _index = [0, 0, 0, 0]
    # ================================================================
    # スタイルID
    @classmethod
    def get_style_id(cls, paragraph) -> str:
        pPr = paragraph._p.find(qn('w:pPr'))
        if pPr is not None:
            pStyle = pPr.find(qn('w:pStyle'))
            if pStyle is not None:
                return pStyle.get(qn('w:val'))
        return None
    
    # ================================================================
    # 階層
    @classmethod
    def map_id_to_marker(cls, id_str: str) -> int:
        return {
            "a": 0,
            "a0": 1,
            "1": 2,
            "a1": 3,
            "20": 4,
            "3": 5
        }.get(id_str, cls._last_level)
    
    # ================================================================
    # インデント
    @classmethod
    def indent(cls, level) -> int:
        if level >= 0:
            return [0, 0, 1, 2, 3, 4][level]
        return cls._last_level
    
    @classmethod
    def text_indent(cls, run) -> str:
        level = cls.br_text_level(run)
        return ("\n" if level > 0 else "") + "#" * level

    @classmethod
    def br_text_level(cls, run) -> int:
        run_xml = run._element
        for child in run_xml.iter():
            if child.tag == qn('w:br'):
                return cls._last_level - 1
        return 0

    # ================================================================
    # 記号
    @classmethod
    def reset_index(cls):
        # print('aaa')
        cls._index[1] = 0
        cls._index[2] = 0
        cls._index[3] = 0

    @classmethod
    def index_count(cls, level):
        if level < 4: # 箇条書きを排する
            if cls._last_level > level: # 
                cls.reset_index()
            cls.add_index(level)
            return cls._index[level]
        return None
    
    @classmethod
    def add_index(cls, level):
        cls._index[level] += 1

    @classmethod
    def index_str(cls, level, index) -> str:
        if level == 0:
            return cls.to_roman(index)
        elif level == 1:
            return str(index)
        elif level == 2:
            return f'({index})'
        elif level == 3:
            return cls.to_circle_number(index)
        elif level == 4:
            return '○'
        elif level == 5:
            return '■'
        return ''
    
    @classmethod
    def to_roman(cls, n):
        if not (1 <= n <= 3999):
            raise ValueError("1〜3999の範囲で指定してください")

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""
        for i in range(len(val)):
            count = n // val[i]
            roman += syms[i] * count
            n -= val[i] * count
        return roman

    @classmethod
    def to_circle_number(cls, index):
        if index > 0 and index < 21:
            return [
                "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩",
                "⑪", "⑫", "⑬", "⑭", "⑮", "⑯", "⑰", "⑱", "⑲", "⑳",
            ][index]
        return '○'

    @classmethod
    def symbol(cls, level):
        index = cls.index_count(level)
        cls._last_level = level
        return cls.index_str(level, index)
    
    @classmethod
    def outline(cls, paragraph) -> str:
        level = cls.map_id_to_marker(cls.get_style_id(paragraph))
        indent_level = cls.indent(level)
        return ("#" * indent_level + cls.symbol(level))

    # @classmethod
    # def get_outline_prefix(cls, paragraph) -> str:
    #     level = cls.map_id_to_marker(cls.get_style_id(paragraph))
    #     indent_level = cls.indent(level)
    #     prefix = "    " * indent_level + cls.symbol(level)
    #     cls._last_level = level  # 状態更新
    #     return prefix

    # @classmethod
    # def split_runs_by_linebreak(cls, paragraph) -> list:
    #     lines = []
    #     current_line = ""

    #     for run in paragraph.runs:
    #         run_xml = run._element
    #         for child in run_xml.iter():
    #             if child.tag == qn('w:br'):
    #                 lines.append(current_line.strip())
    #                 current_line = ""
    #         current_line += run.text

    #     if current_line.strip():
    #         lines.append(current_line.strip())

    #     return lines

    # @classmethod
    # def outline_lines(cls, paragraph) -> list:
    #     prefix = cls.get_outline_prefix(paragraph)
    #     raw_lines = cls.split_runs_by_linebreak(paragraph)
    #     return [prefix + line for line in raw_lines]

DocxToMarkdownConverter.convert('./data/Category3/example3.docx', './data/Category3/example3.md')