from tika import parser
import os

"""
tika can work with those file types: pdf, doc, docx, odf, xml
"""


def get_document_text(filepath: str) -> str:
    """
    Функция достает текст из документа. 
    Возможные типы документов для обработки: pdf, rtf, doc, docx, xml, odf

    Возвращаемая ошибка -1 означает, что передан недопустимое расширение файла.
    
    Args:
        filepath (str): путь до файла

    Returns:
        str: текст из документа
    """
    filetype = filepath[filepath.rfind('.')+1:]
    assert filetype in ['pdf', 'rtf', 'doc', 'docx', 'xml', 'odf'], -1
    
    text = parser.from_file(filepath)['content'].replace('\n', ' ')
    while '  ' in text:
        text = text.replace('  ', ' ')
    text = text.strip()
    return text


def get_document_text_dir(dirpath: str) -> list:
    """
    Функция возвращает список документов из переданной директории.

    Возвращает -1 если хотя бы один документ не соответсвует допустимому расширению.
    
    Args:
        dirpath (str): Путь до директории с файлами

    Returns:
        list: список текстов из документов
    """
    if dirpath[-1] != '/': 
        dirpath += '/'
        
    texts = []
    for file in os.listdir(dirpath):
        text = get_document_text(dirpath+file)
        if type(text) != str:
            return -1
        texts.append(text)
    
    return texts

    




