# 德国车牌自定义生成工具

这是一个用于生成符合 **DIN 74069 (2018-12-00)** 标准的车牌自定义生成工具。该工具专为德国车牌设计，并计划加入欧盟车牌的生成功能（见 [欧盟车牌生成 ToDo](https://european-union.europa.eu/principles-countries-history/symbols/european-flag_en)）。生成的车牌图片会自动保存至 **D盘根目录**。

## 功能

- **德国车牌生成**：严格按照 DIN 74069 (2018-12-00) 标准。
- **欧盟车牌生成**（即将上线）：包括欧盟标志和符号，详细参考[欧盟标志说明](https://european-union.europa.eu/principles-countries-history/symbols/european-flag_en)。

相关标准说明见 [DIN 74069 (2018-12-00) 标准说明](https://www.doc88.com/p-7846461525879.html)。

## 安装

1. **下载字体包**：为生成符合 DIN 74069 标准的车牌样式，需要下载并安装字体包（包含欧盟车牌字体）。
2. **配置保存目录**：该工具将生成的车牌图片保存至 **D盘根目录**。

## 使用方法

### 1. 现阶段使用

   - **安装必要库依赖**：使用以下命令安装所需的 Python 库：
     ```bash
     pip install pillow  # 用于图像处理
     pip install opencv-python  # 用于处理图像的进一步操作（如缩放、旋转等）
     ```
   - **运行**：在任意有python环境的IDE中打开德国车牌.py，运行。

### 2. 输入格式建议
   - **输入内容**：建议输入纯英文字符。
   - **空格建议**：为了更符合车牌格式，建议在输入的第二个字符后插入一个空格。例如：`MB 01234`。

### 3. 生成流程
   - **运行工具**：按照工具的界面提示或命令行提示输入所需内容。
   - **选择样式**：支持标准德国车牌样式，欧盟车牌样式将在后续版本中加入。
   - **保存**：生成的车牌图片自动保存至 `D:` 盘根目录。

### 4. 生成效果示例

1. 德国标准车牌样式示例：
   - 输入内容：`ZE Y2024`
   - 生成样式：`https://github.com/EddieUZ/European-license-plate-generator/blob/main/%E6%A0%B7%E4%BE%8B.png`
2. 欧盟标准车牌（待定）：
   - **功能将添加，敬请期待**

## 注意事项

- **字体包**：确保已安装字体包，否则生成效果可能不符标准。
- **D盘根目录权限**：请确保 D盘有足够的写入权限，以免生成图片时发生错误。
- **格式要求**：请尽量按建议格式输入内容，以生成合规的车牌样式。（不建议添加Ä, Ö, Ü等德语特殊字符）

## TODO

- [ ] 支持欧盟车牌生成功能（包含欧盟标志及特殊格式）
- [ ] 学习VUE3，将代码部署到前端。

---

如需了解更多信息，参考以下链接：
- **DIN 74069 (2022-10现行) 标准**：[https://www.din.de/en/getting-involved/standards-committees/naautomobil/publications/wdc-beuth:din21:358117810)
- **欧盟官方旗帜**：[https://european-union.europa.eu/principles-countries-history/symbols/european-flag_en](https://european-union.europa.eu/principles-countries-history/symbols/european-flag_en)
