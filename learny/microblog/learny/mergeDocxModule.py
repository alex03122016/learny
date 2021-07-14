

#files = ['syltest.docx', 'cloze-Test-test.docx']

def combine_word_documents(files):
    from docx import Document
    import os
    merged_document = Document()

    for index, file in enumerate(files):
        sub_doc = Document(file)

        # Don't add a page break if you've reached the last file.
        if index < len(files)-1:
           sub_doc.add_page_break()

        for element in sub_doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save(os.path.join(os.path.expanduser('~'), "merged.docx"))
    return
#combine_word_documents(files)
