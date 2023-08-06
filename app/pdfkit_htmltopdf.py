import pdfkit

# 定义要转换为 PDF 的页面列表
pages = [
    "https://docs.mryqr.com/build-your-own-software-skyscraper/",
    "https://docs.mryqr.com/ddd-introduction/",
    "https://docs.mryqr.com/ddd-in-plain-words/",
    "https://docs.mryqr.com/ddd-strategic-design/",
    "https://docs.mryqr.com/ddd-project-structure/",
    "https://docs.mryqr.com/ddd-request-process-flow/",
    "https://docs.mryqr.com/ddd-aggregate-root-and-repository/",
    "https://docs.mryqr.com/ddd-entity-and-value-object/",
    "https://docs.mryqr.com/ddd-application-service-and-domain-service/",
    "https://docs.mryqr.com/ddd-domain-events/",
    "https://docs.mryqr.com/ddd-cqrs/",
    "https://docs.mryqr.com/backend-is-not-crud/",
    "https://docs.mryqr.com/how-clean-can-clean-architecture-be/",
    "https://docs.mryqr.com/how-to-use-lombok-in-ddd/",
    "https://docs.mryqr.com/ddd-faq/"
]

# 配置 PDF 选项
options = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
}

# 循环遍历页面列表，并将每个页面转换为 PDF
for index, page in enumerate(pages):
    pdf_file = f'page{index+1}.pdf'  # 生成的 PDF 文件名
    pdfkit.from_url(page, pdf_file, options=options)
    print(f'{page} 转换为 {pdf_file}')

print('转换完成！')
