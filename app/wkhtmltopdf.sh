#!/bin/bash

# 定义输入文件列表
input_files=(
"https://docs.mryqr.com/build-your-own-software-skyscraper/"
"https://docs.mryqr.com/ddd-introduction/"
"https://docs.mryqr.com/ddd-in-plain-words/"
"https://docs.mryqr.com/ddd-strategic-design/"
"https://docs.mryqr.com/ddd-project-structure/"
"https://docs.mryqr.com/ddd-request-process-flow/"
"https://docs.mryqr.com/ddd-aggregate-root-and-repository/"
"https://docs.mryqr.com/ddd-entity-and-value-object/"
"https://docs.mryqr.com/ddd-application-service-and-domain-service/"
"https://docs.mryqr.com/ddd-domain-events/"
"https://docs.mryqr.com/ddd-cqrs/"
"https://docs.mryqr.com/backend-is-not-crud/"
"https://docs.mryqr.com/how-clean-can-clean-architecture-be/"
"https://docs.mryqr.com/how-to-use-lombok-in-ddd/"
"https://docs.mryqr.com/ddd-faq/"
)

# 定义输出目录
output_dir="pdf_output"

# 创建输出目录
mkdir -p "$output_dir"
# 遍历输入文件列表
for file in "${input_files[@]}"
do
  # 提取文件名（不带扩展名）
  basename=$(basename "$file")
  filename=$(echo "$basename" | sed 's/\//-/g')
  # 构建输出文件路径
  output_file="$output_dir/$filename.pdf"

  # 使用 wkhtmltopdf 进行转换
  wkhtmltopdf "$file" "$output_file"

  # 打印转换完成的消息
  echo "转换完成: $output_file"
done