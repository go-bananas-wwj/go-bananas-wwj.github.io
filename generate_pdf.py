#!/usr/bin/env python3
"""Generate Chinese and English academic-style resume PDFs."""

from fpdf import FPDF

FONT_REGULAR = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
FONT_BOLD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
FONT_EN_REGULAR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_EN_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__(format='A4')
        self.set_auto_page_break(auto=True, margin=20)
        self.add_font('Noto', '', FONT_REGULAR, uni=True)
        self.add_font('Noto', 'B', FONT_BOLD, uni=True)
        self.add_font('DejaVu', '', FONT_EN_REGULAR, uni=True)
        self.add_font('DejaVu', 'B', FONT_EN_BOLD, uni=True)

    def header_line(self, text, y=None):
        if y:
            self.set_y(y)
        self.set_font('Noto', 'B', 14)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(180, 180, 180)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(2)

    def body_text(self, text, bold=False, size=10.5):
        self.set_font('Noto', 'B' if bold else '', size)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def bullet(self, text):
        self.set_font('Noto', '', 10)
        self.set_text_color(60, 60, 60)
        x = self.get_x()
        self.cell(4, 5.5, '', new_x="RIGHT", new_y="TOP")
        self.multi_cell(self.w - self.r_margin - self.get_x(), 5.5, f'• {text}')
        self.set_x(x)

    def two_col_row(self, left, right, left_bold=True, right_bold=False):
        self.set_font('Noto', 'B' if left_bold else '', 10.5)
        self.set_text_color(40, 40, 40)
        self.cell(0, 6, left, new_x="RIGHT", new_y="TOP")
        self.set_font('Noto', 'B' if right_bold else '', 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, right, align='R', new_x="LMARGIN", new_y="NEXT")


def generate_zh():
    pdf = ResumePDF()
    pdf.add_page()

    # Title
    pdf.set_font('Noto', 'B', 22)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 12, '伍炜杰', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Noto', '', 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, '博士生 · 研究遥感大模型 · 偶尔做点小东西', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Noto', '', 9.5)
    pdf.cell(0, 5, '邮箱: wuweijie25@mails.ucas.ac.cn  |  GitHub: github.com/go-bananas-wwj  |  ModelScope: modelscope.cn/profile/WeijieWu', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # Education
    pdf.header_line('教育背景')
    pdf.two_col_row('中国科学院大学', '2025.09 – 至今')
    pdf.body_text('博士，信号与信息处理 | 直博，师从李国庆教授，空天信息研究院 | 研究方向：遥感大模型、遥感智能体、地理嵌入')
    pdf.two_col_row('重庆大学（985）', '2021.09 – 2025.06')
    pdf.body_text('学士，人工智能 | 国家卓越工程师学院，明月科创实验班 | 专业排名 1/15，GPA 3.79/4.0')
    pdf.body_text('辅修金融学 | 经济与工商管理学院')
    pdf.two_col_row('重庆南开中学', '2018.09 – 2021.06')
    pdf.body_text('信息学竞赛省一')
    pdf.ln(2)

    # Experience
    pdf.header_line('工作经历')
    pdf.two_col_row('清华大学 — 研究实习生', '2024.03 – 2024.09')
    pdf.bullet('基于 Diffusion Model 的游戏设计素材自动生成研究')
    pdf.bullet('使用 ComfyUI 搭建完整工作流，利用 ControlNet 和角色骨骼模型解决图生视频中角色一致性问题')
    pdf.ln(1)

    pdf.two_col_row('重庆明月湖智能产业科创基地 / X-bot Park — 创始人', '2022.04 – 2024.07')
    pdf.bullet('创立 Cooling Technology 项目，研发穿戴式智能制冷衣')
    pdf.bullet('负责从 0 到 1 的产品闭环：机械结构设计、电路设计、嵌入式开发、样品打样、用户调研')
    pdf.bullet('项目后与重庆警察学院合作，获重庆市两江新区政府 50 万元种子轮投资，实现小规模量产并盈利')
    pdf.ln(1)

    pdf.two_col_row('宁波厨鲸有限公司 — 嵌入式研发实习生', '2023.06 – 2023.08')
    pdf.bullet('负责漱口水智能检测设备的嵌入式程序开发')
    pdf.bullet('搭建超声波模块检测系统')
    pdf.ln(2)

    # Projects
    pdf.header_line('项目经历')
    pdf.two_col_row('InstructSAM', '2024.10 – 至今')
    pdf.body_text('训练无关的指令导向遥感图像分割框架。用户通过自然语言指令即可精确分割遥感图像中的目标，无需重新训练模型。')
    pdf.bullet('技术栈: PyTorch, Vision-Language Model, SAM')
    pdf.bullet('成果: NeurIPS 2025 接收')
    pdf.ln(1)

    pdf.two_col_row('Disaster-Agent', '2025.05 – 至今')
    pdf.body_text('多智能体协同灾害应急响应平台，集成实时遥感数据流，支持灾情快速评估与决策辅助。')
    pdf.bullet('技术栈: Multi-Agent System, Remote Sensing, LLM')
    pdf.ln(1)

    pdf.two_col_row('EarthEmbeddingExplorer', '2024 – 至今')
    pdf.body_text('全球卫星影像跨模态检索可视化 Web 应用，优化地理嵌入的可视化效果与用户体验。')
    pdf.bullet('技术栈: Vue.js, Geo-Embedding, Cross-Modal Retrieval | ICLR Workshop')
    pdf.ln(1)

    pdf.two_col_row('NODA 平台数据集检索助手', '2024 – 至今')
    pdf.body_text('基于 Dify 构建的 NODA 平台智能数据检索助手，已上线运行。')
    pdf.bullet('技术栈: Dify, LLM, RAG | 链接: noda.ac.cn')
    pdf.ln(1)

    pdf.two_col_row('穿戴式制冷衣创业项目', '2023.03 – 2024.01')
    pdf.bullet('负责制冷主机的 EVT 开发（机械 + 电路部分）')
    pdf.bullet('获 50 万元种子轮投资，完成从 0 到 1 的产品闭环')
    pdf.ln(2)

    # Publications
    pdf.header_line('论文发表')
    pdf.set_font('Noto', 'B', 10)
    pdf.cell(0, 6, 'InstructSAM: A Training-Free Framework for Instruction-Oriented Remote Sensing Object Recognition', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Noto', '', 9.5)
    pdf.cell(0, 5, 'Zheng, Y.; Wu, W.; Li, Q.; et al. | Neural Information Processing Systems (NeurIPS), 2025', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Noto', 'B', 10)
    pdf.cell(0, 6, 'EarthEmbeddingExplorer: A Web Application for Cross-Modal Retrieval of Global Satellite Images', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Noto', '', 9.5)
    pdf.cell(0, 5, 'Wu, W.; et al. | ICLR Workshop', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    # Patents
    pdf.header_line('专利')
    pdf.body_text('基于靶区规划的可扩展遥感深度学习样本库建设方法（CN120612563A）')
    pdf.body_text('液冷服相关专利（多项，申请中 / 已授权）')
    pdf.ln(2)

    # Awards
    pdf.header_line('荣誉奖项')
    pdf.bullet('重庆大学优秀助教（两次：C 语言程序设计、C++程序设计），2022.11, 2023.11')
    pdf.bullet('美国大学生数学建模大赛国家级三等奖，2023.01')
    pdf.bullet('宁波 XbotPark 科创训练营最佳项目奖，2022.06 – 2023.07')
    pdf.bullet('校级优秀学生、三好学生等荣誉十余项')
    pdf.bullet('校级、创新创业工程类比赛获奖十余项')
    pdf.ln(2)

    # Skills
    pdf.header_line('技术栈')
    pdf.body_text('编程语言: Python, JavaScript, C++, MATLAB')
    pdf.body_text('深度学习: PyTorch, TensorFlow, Scikit-learn')
    pdf.body_text('智能体 / LLM: Dify, LangChain, n8n, OpenClaw, Hermes Agent, Agent RAG')
    pdf.body_text('前端 / 工程: Vue.js, React, HTML, Git, Docker, Vite, Qt')
    pdf.body_text('硬件 / 嵌入式: ARM Cortex, Altium Designer, 立创 EDA, ROS')
    pdf.body_text('设计 / 机械: SOLIDWORKS, Fusion360, ANSYS')
    pdf.body_text('语言: 中文（母语），英语（CET-6 494，可独立阅读文献）')

    pdf.output('public/resume-zh.pdf')
    print('Generated public/resume-zh.pdf')


def generate_en():
    pdf = ResumePDF()
    pdf.add_page()

    # Title
    pdf.set_font('DejaVu', 'B', 22)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 12, 'Weijie Wu (Alan)', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('DejaVu', '', 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, 'PhD Student · RS Foundation Models · Building Small Things', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('DejaVu', '', 9)
    pdf.cell(0, 5, 'Email: wuweijie25@mails.ucas.ac.cn  |  GitHub: github.com/go-bananas-wwj  |  ModelScope: modelscope.cn/profile/WeijieWu', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # Education
    pdf.header_line('Education')
    pdf.two_col_row('University of Chinese Academy of Sciences', 'Sep 2025 – Present')
    pdf.body_text("PhD, Signal and Information Processing | Direct PhD, advised by Prof. Guoqing Li | Aerospace Information Research Institute | Research: remote sensing foundation models, agents, geo-embedding")
    pdf.two_col_row('Chongqing University (Project 985)', 'Sep 2021 – Jun 2025')
    pdf.body_text("Bachelor's, Artificial Intelligence | National School of Excellence in Engineering, Mingyue Innovation Class | Rank 1/15, GPA 3.79/4.0")
    pdf.body_text('Minor, Finance | School of Economics and Business Administration')
    pdf.two_col_row('Chongqing Nankai Secondary School', 'Sep 2018 – Jun 2021')
    pdf.body_text('First Prize in Informatics Olympiad (Provincial)')
    pdf.ln(2)

    # Experience
    pdf.header_line('Experience')
    pdf.two_col_row('Tsinghua University — Research Intern', 'Mar 2024 – Sep 2024')
    pdf.bullet('Research on automated game asset generation based on Diffusion Models')
    pdf.bullet('Built complete workflow with ComfyUI, used ControlNet and character skeleton models to solve character consistency in image-to-video generation')
    pdf.ln(1)

    pdf.two_col_row('Chongqing Mingyue Lake Innovation Base / X-bot Park — Founder', 'Apr 2022 – Jul 2024')
    pdf.bullet('Founded Cooling Technology project, developed a wearable intelligent cooling suit')
    pdf.bullet('Led full 0-to-1 product cycle: mechanical design, circuit design, embedded development, prototyping, user research')
    pdf.bullet('Collaborated with Chongqing Police College, secured 500K CNY seed funding from Liangjiang New Area government, achieved small-batch production and profitability')
    pdf.ln(1)

    pdf.two_col_row('Ningbo Chujing Co., Ltd. — Embedded R&D Intern', 'Jun 2023 – Aug 2023')
    pdf.bullet('Developed embedded programs for intelligent mouthwash detection device')
    pdf.bullet('Built ultrasonic module detection system')
    pdf.ln(2)

    # Projects
    pdf.header_line('Projects')
    pdf.two_col_row('InstructSAM', 'Oct 2024 – Present')
    pdf.body_text('A training-free framework for instruction-oriented remote sensing image segmentation. Users can precisely segment targets in RS images via natural language instructions without retraining.')
    pdf.bullet('Stack: PyTorch, Vision-Language Model, SAM | NeurIPS 2025')
    pdf.ln(1)

    pdf.two_col_row('Disaster-Agent', 'May 2025 – Present')
    pdf.body_text('A multi-agent coordination platform for rapid disaster response, integrating real-time remote sensing data streams to support rapid damage assessment and decision assistance.')
    pdf.bullet('Stack: Multi-Agent System, Remote Sensing, LLM')
    pdf.ln(1)

    pdf.two_col_row('EarthEmbeddingExplorer', '2024 – Present')
    pdf.body_text('A web application for cross-modal retrieval of global satellite images, optimizing visualization effects and user experience of geo-embeddings.')
    pdf.bullet('Stack: Vue.js, Geo-Embedding, Cross-Modal Retrieval | ICLR Workshop')
    pdf.ln(1)

    pdf.two_col_row('NODA Data Retrieval Assistant', '2024 – Present')
    pdf.body_text('An intelligent data retrieval assistant for the NODA platform built on Dify, currently live in production.')
    pdf.bullet('Stack: Dify, LLM, RAG | Link: noda.ac.cn')
    pdf.ln(1)

    pdf.two_col_row('Wearable Cooling Suit Startup', 'Mar 2023 – Jan 2024')
    pdf.bullet('Led EVT development of cooling host unit (mechanical + circuit)')
    pdf.bullet('Secured 500K CNY seed funding, completed full 0-to-1 product cycle')
    pdf.ln(2)

    # Publications
    pdf.header_line('Publications')
    pdf.set_font('DejaVu', 'B', 10)
    pdf.multi_cell(0, 5.5, 'InstructSAM: A Training-Free Framework for Instruction-Oriented Remote Sensing Object Recognition')
    pdf.set_font('DejaVu', '', 9)
    pdf.cell(0, 5, 'Zheng, Y.; Wu, W.; Li, Q.; et al. | Neural Information Processing Systems (NeurIPS), 2025', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('DejaVu', 'B', 10)
    pdf.multi_cell(0, 5.5, 'EarthEmbeddingExplorer: A Web Application for Cross-Modal Retrieval of Global Satellite Images')
    pdf.set_font('DejaVu', '', 9)
    pdf.cell(0, 5, 'Wu, W.; et al. | ICLR Workshop', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    # Patents
    pdf.header_line('Patents')
    pdf.body_text('Scalable Remote Sensing Deep Learning Sample Library Construction Method Based on Target Area Planning (CN120612563A)')
    pdf.body_text('Liquid Cooling Suit Related Patents (Multiple, Applied / Granted)')
    pdf.ln(2)

    # Awards
    pdf.header_line('Awards')
    pdf.bullet('Excellent Teaching Assistant (C Programming, C++ Programming), Chongqing University, Nov 2022 & Nov 2023')
    pdf.bullet('Mathematical Contest in Modeling (MCM) National Third Prize, Jan 2023')
    pdf.bullet('XbotPark Innovation Camp Best Project Award, Jun 2022 – Jul 2023')
    pdf.bullet('Merit Student, Triple-A Student, and other honors (10+), Chongqing University')
    pdf.bullet('Innovation & Entrepreneurship Competition Awards (10+), Chongqing University')
    pdf.ln(2)

    # Skills
    pdf.header_line('Skills')
    pdf.body_text('Languages: Python, JavaScript, C++, MATLAB')
    pdf.body_text('Deep Learning: PyTorch, TensorFlow, Scikit-learn')
    pdf.body_text('Agents / LLM: Dify, LangChain, n8n, OpenClaw, Hermes Agent, Agent RAG')
    pdf.body_text('Frontend / Engineering: Vue.js, React, HTML, Git, Docker, Vite, Qt')
    pdf.body_text('Hardware / Embedded: ARM Cortex, Altium Designer, LCEDA, ROS')
    pdf.body_text('Design / Mechanical: SOLIDWORKS, Fusion360, ANSYS')
    pdf.body_text('Languages: Chinese (Native), English (CET-6 494, fluent in reading technical literature)')

    pdf.output('public/resume-en.pdf')
    print('Generated public/resume-en.pdf')


if __name__ == '__main__':
    generate_zh()
    generate_en()
