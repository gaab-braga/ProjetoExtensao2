"""
Conversor Markdown -> PDF com formatacao profissional.
Usa fpdf2 (puro Python, sem dependencias nativas).
Suporta: headings, tabelas, code blocks, blockquotes, listas, negrito, italico, checkboxes.
"""
import re
from fpdf import FPDF
import os

# -- CORES -------------------------------------------------------
C_H1       = (26, 35, 126)
C_H2       = (40, 53, 147)
C_H3       = (57, 73, 171)
C_H4       = (92, 107, 192)
C_TEXT      = (30, 30, 30)
C_CODE_BG  = (38, 50, 56)
C_CODE_FG  = (238, 255, 255)
C_INLINE_BG = (236, 239, 241)
C_INLINE_FG = (198, 40, 40)
C_QUOTE_BG  = (255, 243, 224)
C_QUOTE_BAR = (255, 112, 67)
C_QUOTE_FG  = (78, 52, 46)
C_TH_BG     = (40, 53, 147)
C_TH_FG     = (255, 255, 255)
C_ROW_ALT   = (245, 245, 245)
C_BORDER    = (200, 200, 200)
C_HR        = (197, 202, 233)
C_WHITE     = (255, 255, 255)


def sanitize_text(text):
    """Converte caracteres Unicode para equivalentes latin-1 seguros."""
    reps = {
        '\u2014': '--', '\u2013': '-', '\u2018': "'", '\u2019': "'",
        '\u201c': '"', '\u201d': '"', '\u2026': '...', '\u2022': '*',
        '\u2713': '[V]', '\u2717': '[X]', '\u2610': '[ ]',
        '\u25bc': 'v', '\u25b6': '>', '\u2500': '-', '\u2502': '|',
        '\u250c': '+', '\u2510': '+', '\u2514': '+', '\u2518': '+',
        '\u251c': '+', '\u2524': '+', '\u252c': '+', '\u2534': '+',
        '\u253c': '+', '\u2550': '=', '\u2551': '|', '\u25cf': '*',
        '\u25cb': 'o', '\u25a0': '#', '\u25a1': '[ ]', '\u2588': '#',
        '\u00a0': ' ', '\u200b': '', '\u00d7': 'x',
        '\u2265': '>=', '\u2264': '<=', '\u2260': '!=',
        '\u2192': '->', '\u2190': '<-', '\u21d2': '=>',
        '\u2248': '~=', '\u221e': 'inf',
        '\u2705': '[V]', '\u274c': '[X]', '\u26a0': '[!]',
        '\u2b50': '[*]', '\u25ac': '-', '\u25b2': '^',
        '\u25c0': '<', '\u25ba': '>',
        '\u2591': '.', '\u2592': ':', '\u2593': '#',
    }
    for uni, repl in reps.items():
        text = text.replace(uni, repl)
    try:
        text = text.encode('latin-1', errors='replace').decode('latin-1')
    except:
        text = text.encode('ascii', errors='replace').decode('ascii')
    return text


class MarkdownPDF(FPDF):
    def __init__(self, title=""):
        super().__init__('P', 'mm', 'A4')
        self.doc_title = title
        self.set_auto_page_break(auto=True, margin=20)
        self.font_main = "Helvetica"
        self.font_mono = "Courier"

    def header(self):
        if self.page_no() > 1:
            self.set_font(self.font_main, 'I', 7)
            self.set_text_color(150, 150, 150)
            self.cell(0, 5, sanitize_text(self.doc_title), align='R')
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font(self.font_main, 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Pagina {self.page_no()} / {{nb}}', align='C')


def render_table(pdf, rows):
    """Renderiza uma tabela Markdown completa."""
    if len(rows) < 2:
        return

    header = [sanitize_text(c.strip()) for c in rows[0].strip('|').split('|')]
    data_rows = []
    for row in rows[2:]:
        cells = [sanitize_text(c.strip()) for c in row.strip('|').split('|')]
        if cells:
            data_rows.append(cells)

    num_cols = len(header)
    if num_cols == 0:
        return

    page_w = pdf.w - pdf.l_margin - pdf.r_margin

    # Larguras proporcionais baseadas no conteudo
    col_max = []
    for i in range(num_cols):
        mx = len(header[i]) if i < len(header) else 3
        for row in data_rows:
            if i < len(row):
                mx = max(mx, len(row[i]))
        col_max.append(max(mx, 3))

    total = sum(col_max)
    col_w = [(l / total) * page_w for l in col_max]
    for i in range(len(col_w)):
        col_w[i] = max(col_w[i], 10)
    total_w = sum(col_w)
    if total_w > page_w:
        col_w = [w * page_w / total_w for w in col_w]

    rh = 6.5

    # Verificar espaco
    if pdf.get_y() + rh * (1 + len(data_rows)) > pdf.h - 25:
        pdf.add_page()

    def print_header():
        pdf.set_font(pdf.font_main, 'B', 8)
        pdf.set_fill_color(*C_TH_BG)
        pdf.set_text_color(*C_TH_FG)
        pdf.set_draw_color(*C_TH_BG)
        for ci, h in enumerate(header):
            w = col_w[ci] if ci < len(col_w) else 15
            max_ch = max(int(w / 1.8), 4)
            txt = h[:max_ch] + '..' if len(h) > max_ch else h
            pdf.cell(w, rh, txt, border=1, fill=True)
        pdf.ln()

    print_header()

    pdf.set_font(pdf.font_main, '', 8)
    pdf.set_draw_color(*C_BORDER)
    pdf.set_text_color(*C_TEXT)

    for ri, row in enumerate(data_rows):
        if pdf.get_y() + rh > pdf.h - 22:
            pdf.add_page()
            print_header()
            pdf.set_font(pdf.font_main, '', 8)
            pdf.set_draw_color(*C_BORDER)
            pdf.set_text_color(*C_TEXT)

        if ri % 2 == 1:
            pdf.set_fill_color(*C_ROW_ALT)
        else:
            pdf.set_fill_color(*C_WHITE)

        for ci in range(num_cols):
            txt = row[ci] if ci < len(row) else ''
            w = col_w[ci] if ci < len(col_w) else 15
            max_ch = max(int(w / 1.7), 4)
            if len(txt) > max_ch and max_ch > 6:
                txt = txt[:max_ch - 2] + '..'
            pdf.cell(w, rh, txt, border=1, fill=True)
        pdf.ln()

    pdf.ln(3)


def render_code_block(pdf, lines):
    """Renderiza bloco de codigo com fundo escuro."""
    pdf.set_font(pdf.font_mono, '', 7.5)
    line_h = 4
    page_w = pdf.w - pdf.l_margin - pdf.r_margin
    block_h = len(lines) * line_h + 8

    if pdf.get_y() + min(block_h, 40) > pdf.h - 22:
        pdf.add_page()

    y_start = pdf.get_y()
    x_start = pdf.l_margin

    # Desenhar fundo (estimar altura, max 1 pagina)
    draw_h = min(block_h, pdf.h - y_start - 22)
    pdf.set_fill_color(*C_CODE_BG)
    pdf.rect(x_start, y_start, page_w, draw_h, 'F')

    pdf.set_text_color(*C_CODE_FG)
    pdf.set_xy(x_start + 4, y_start + 3)

    for line in lines:
        if pdf.get_y() + line_h > pdf.h - 22:
            pdf.add_page()
            y_new = pdf.get_y()
            remaining = lines[lines.index(line):]
            rem_h = min(len(remaining) * line_h + 6, pdf.h - y_new - 22)
            pdf.set_fill_color(*C_CODE_BG)
            pdf.rect(pdf.l_margin, y_new, page_w, rem_h, 'F')
            pdf.set_xy(pdf.l_margin + 4, y_new + 3)
            pdf.set_font(pdf.font_mono, '', 7.5)
            pdf.set_text_color(*C_CODE_FG)

        clean = sanitize_text(line)
        max_ch = int((page_w - 8) / 1.55)
        if len(clean) > max_ch:
            clean = clean[:max_ch - 3] + '...'
        pdf.cell(0, line_h, clean)
        pdf.ln(line_h)
        pdf.set_x(x_start + 4)

    pdf.ln(5)
    pdf.set_text_color(*C_TEXT)


def render_blockquote(pdf, text):
    """Renderiza blockquote com barra lateral colorida."""
    page_w = pdf.w - pdf.l_margin - pdf.r_margin

    if pdf.get_y() + 14 > pdf.h - 22:
        pdf.add_page()

    y_start = pdf.get_y()
    x_start = pdf.l_margin
    bar_w = 3
    content_x = x_start + bar_w + 3
    content_w = page_w - bar_w - 6

    clean = sanitize_text(text)
    pdf.set_font(pdf.font_main, 'I', 9)

    # Estimar altura
    char_per_line = max(int(content_w / 2.0), 20)
    est_lines = max(1, len(clean) / char_per_line + 1)
    est_h = est_lines * 5 + 8

    # Fundo + barra
    pdf.set_fill_color(*C_QUOTE_BG)
    pdf.rect(x_start, y_start, page_w, est_h, 'F')
    pdf.set_fill_color(*C_QUOTE_BAR)
    pdf.rect(x_start, y_start, bar_w, est_h, 'F')

    # Texto
    pdf.set_xy(content_x, y_start + 3)
    pdf.set_text_color(*C_QUOTE_FG)
    pdf.multi_cell(content_w, 5, clean)

    actual_h = pdf.get_y() - y_start + 3
    if actual_h > est_h:
        # Redesenhar com altura correta
        pdf.set_fill_color(*C_QUOTE_BG)
        pdf.rect(x_start, y_start, page_w, actual_h, 'F')
        pdf.set_fill_color(*C_QUOTE_BAR)
        pdf.rect(x_start, y_start, bar_w, actual_h, 'F')
        pdf.set_xy(content_x, y_start + 3)
        pdf.set_text_color(*C_QUOTE_FG)
        pdf.set_font(pdf.font_main, 'I', 9)
        pdf.multi_cell(content_w, 5, clean)

    pdf.ln(4)
    pdf.set_text_color(*C_TEXT)


def convert_md_to_pdf(md_path, pdf_path):
    """Converte arquivo Markdown para PDF."""
    print(f"  Lendo: {md_path}")

    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    title = os.path.basename(md_path).replace('.md', '')
    for line in lines:
        if line.startswith('# '):
            title = line.strip('# \n')
            break

    pdf = MarkdownPDF(title)
    pdf.alias_nb_pages()
    pdf.add_page()

    i = 0
    in_code = False
    code_lines = []
    in_table = False
    table_rows = []
    quote_buf = []

    while i < len(lines):
        raw = lines[i].rstrip('\n')
        stripped = raw.strip()

        # --- CODE BLOCK ---
        if stripped.startswith('```'):
            if in_code:
                render_code_block(pdf, code_lines)
                code_lines = []
                in_code = False
            else:
                if in_table and table_rows:
                    render_table(pdf, table_rows)
                    table_rows = []
                    in_table = False
                if quote_buf:
                    render_blockquote(pdf, ' '.join(quote_buf))
                    quote_buf = []
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(raw)
            i += 1
            continue

        # --- TABLE ---
        if '|' in stripped and stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                if quote_buf:
                    render_blockquote(pdf, ' '.join(quote_buf))
                    quote_buf = []
                in_table = True
                table_rows = []
            table_rows.append(stripped)
            i += 1
            continue
        else:
            if in_table and table_rows:
                render_table(pdf, table_rows)
                table_rows = []
                in_table = False

        # --- BLOCKQUOTE ---
        if stripped.startswith('>'):
            text = stripped.lstrip('> ').strip()
            if text:
                quote_buf.append(text)
            i += 1
            continue
        else:
            if quote_buf:
                render_blockquote(pdf, ' '.join(quote_buf))
                quote_buf = []

        # --- HR ---
        if stripped in ('---', '***', '___'):
            pdf.ln(3)
            y = pdf.get_y()
            pdf.set_draw_color(*C_HR)
            pdf.set_line_width(0.5)
            pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
            pdf.ln(5)
            i += 1
            continue

        # --- EMPTY ---
        if not stripped:
            pdf.ln(2)
            i += 1
            continue

        # --- HEADINGS ---
        if stripped.startswith('#'):
            level = len(stripped) - len(stripped.lstrip('#'))
            text = sanitize_text(stripped.lstrip('# ').strip())

            if level == 1:
                if pdf.get_y() > 50:
                    pdf.ln(6)
                pdf.set_font(pdf.font_main, 'B', 18)
                pdf.set_text_color(*C_H1)
                pdf.multi_cell(0, 9, text)
                y = pdf.get_y() + 1
                pdf.set_draw_color(*C_H1)
                pdf.set_line_width(0.8)
                pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
                pdf.ln(5)
            elif level == 2:
                if pdf.get_y() > pdf.h - 50:
                    pdf.add_page()
                pdf.ln(4)
                pdf.set_font(pdf.font_main, 'B', 14)
                pdf.set_text_color(*C_H2)
                pdf.multi_cell(0, 7, text)
                y = pdf.get_y() + 1
                pdf.set_draw_color(*C_HR)
                pdf.set_line_width(0.3)
                pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
                pdf.ln(3)
            elif level == 3:
                if pdf.get_y() > pdf.h - 40:
                    pdf.add_page()
                pdf.ln(3)
                pdf.set_font(pdf.font_main, 'B', 11)
                pdf.set_text_color(*C_H3)
                pdf.multi_cell(0, 6, text)
                pdf.ln(2)
            else:
                pdf.ln(2)
                pdf.set_font(pdf.font_main, 'B', 10)
                pdf.set_text_color(*C_H4)
                pdf.multi_cell(0, 5.5, text)
                pdf.ln(1)

            pdf.set_text_color(*C_TEXT)
            i += 1
            continue

        # --- LIST ---
        list_match = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.*)', stripped)
        if list_match:
            indent = len(list_match.group(1))
            marker = list_match.group(2)
            content = list_match.group(3)

            indent_mm = 5 + (indent // 2) * 5

            if marker in ('-', '*', '+'):
                vis = chr(149) + ' '
            else:
                vis = marker + ' '

            content = content.replace('[x]', '[V]').replace('[ ]', '[ ]')

            pdf.set_x(pdf.l_margin + indent_mm)
            pdf.set_font(pdf.font_main, '', 9.5)
            pdf.set_text_color(*C_TEXT)

            clean = sanitize_text(vis + content)
            # Strip markdown formatting
            clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean)
            clean = re.sub(r'\*([^*]+)\*', r'\1', clean)
            clean = re.sub(r'`([^`]+)`', r'[\1]', clean)

            avail_w = pdf.w - pdf.r_margin - pdf.get_x()
            pdf.multi_cell(avail_w, 5, clean)
            pdf.ln(0.5)
            i += 1
            continue

        # --- PARAGRAPH ---
        pdf.set_font(pdf.font_main, '', 10)
        pdf.set_text_color(*C_TEXT)

        clean = sanitize_text(stripped)
        clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean)
        clean = re.sub(r'\*([^*]+)\*', r'\1', clean)
        clean = re.sub(r'`([^`]+)`', r'[\1]', clean)

        pdf.multi_cell(0, 5, clean)
        pdf.ln(1)
        i += 1

    # Flush
    if in_table and table_rows:
        render_table(pdf, table_rows)
    if quote_buf:
        render_blockquote(pdf, ' '.join(quote_buf))
    if in_code and code_lines:
        render_code_block(pdf, code_lines)

    print(f"  Gerando: {pdf_path}")
    pdf.output(pdf_path)
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"  [OK] {size_kb:.0f} KB, {pdf.page_no()} paginas")


if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))

    arquivos = [
        ('BACKLOG_PROJETO.md', 'BACKLOG_PROJETO.pdf'),
        ('GUIA_TAREFAS_EQUIPE.md', 'GUIA_TAREFAS_EQUIPE.pdf'),
        ('RESUMO_TRELLO.md', 'RESUMO_TRELLO.pdf'),
    ]

    print("=" * 50)
    print("  CONVERSOR MARKDOWN -> PDF")
    print("=" * 50)

    for md_f, pdf_f in arquivos:
        md_p = os.path.join(base, md_f)
        pdf_p = os.path.join(base, pdf_f)

        if not os.path.exists(md_p):
            print(f"  [!] Nao encontrado: {md_f}")
            continue

        print(f"\n[{md_f}]")
        try:
            convert_md_to_pdf(md_p, pdf_p)
        except Exception as e:
            import traceback
            print(f"  [ERRO] {e}")
            traceback.print_exc()

    print("\n" + "=" * 50)
    print("  FINALIZADO")
    print("=" * 50)
