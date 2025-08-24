from docx2python import docx2python

doc_result = docx2python('./data/Category3/example3.docx')
print(doc_result.text)  # 箇条書き記号が含まれる可能性あり